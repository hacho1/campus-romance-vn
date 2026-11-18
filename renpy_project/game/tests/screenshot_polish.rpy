# Targeted native checks for the screenshot review fixes; excluded from builds.
# The suite reuses typography_qa's real-screen Text.render observer.
init python in screenshot_polish_qa:
    import builtins
    import copy
    import json
    from pathlib import Path
    from renpy.color import Color
    from renpy.text.text import Text as SdkText
    from renpy.display.layout import Window as SdkWindow
    from renpy.test.testfocus import find_focus

    REPORT=Path("D:/CampusRomance_VN/tests/screenshot-polish-checks.json")
    checks=[]
    LIGHT_SURFACES=("#fffafd","#ffe0f0")

    def begin():
        renpy._screenshot_polish_old_results=renpy.store.typography_qa.RESULTS
        renpy.store.typography_qa.RESULTS=Path("D:/CampusRomance_VN/tests/screenshot-polish-layout-results.json")
        renpy._screenshot_polish_preferences={key:copy.deepcopy(getattr(renpy.store._preferences,key)) for key in ("skip_unseen","skip_after_choices")}
        checks[:]=[]
        renpy._screenshot_polish_capture=None
        renpy.store.typography_qa.begin()
        write()

    def finish():
        renpy.store.typography_qa.finish()
        for key,value in renpy._screenshot_polish_preferences.items():
            setattr(renpy.store._preferences,key,value)
        renpy.store.typography_qa.RESULTS=renpy._screenshot_polish_old_results
        write()
        print("SCREENSHOT_POLISH_CHECKS",len(checks),"measurements",sum(r["passed"] is False for r in checks),"failed")

    def write():
        REPORT.write_text(json.dumps({"mode":"Native screenshots with queued text/button bounds; native assertions cover contrast and layout, not ink centring",
            "centre_verification":"PENDING tools/check_screenshot_polish_ink.py until actual PNG pixels have been analysed",
            "checks":checks,"limitations":["No font metric rectangle is accepted as proof of visible glyph centring.",
                "Centre rows have passed=null until the independent actual-PNG analysis produces screenshot-polish-ink-results.json.",
                "Enrollment and relationship feedback state changes are tested separately in application_feedback."]},
            ensure_ascii=False,indent=2),encoding="utf-8")

    def record(kind,label,passed,**evidence):
        item={"kind":kind,"label":label,"passed":None if passed is None else bool(passed),
            "screenshot":renpy._screenshot_polish_capture}
        item.update(evidence);checks.append(item);write()
        if passed is False:
            print("SCREENSHOT_POLISH_ISSUE",json.dumps(item,ensure_ascii=False))
        return bool(passed)

    def captured(name):
        # Called only AFTER the native screenshot statement writes this PNG.
        path=Path("D:/CampusRomance_VN/tests/screenshot-polish-screenshots")/name
        assert path.is_file(),("Native screenshot missing",str(path))
        renpy._screenshot_polish_capture=name

    def text_rows(root):
        rows=[];seen=set();metrics=renpy._typography_text_metrics
        def walk(widget,x=0,y=0,owner=None):
            if id(widget) in seen:return
            seen.add(id(widget))
            if isinstance(widget,SdkWindow) and hasattr(widget,"window_size"):
                owner=(widget,x,y,float(widget.window_size[0]),float(widget.window_size[1]))
            if isinstance(widget,SdkText):
                metric=metrics.get(id(widget))
                if metric:
                    rows.append({"widget":widget,"text":renpy.store.typography_qa.plain(widget),
                        "x":float(x),"y":float(y),"w":metric["size"][0],"h":metric["size"][1],"owner":owner})
                return
            children=getattr(widget,"children",None)
            if not children:
                child=getattr(widget,"child",None)
                children=[child] if child is not None else []
            offsets=getattr(widget,"offsets",None)
            for i,child in enumerate(children):
                if child is None:continue
                dx,dy=offsets[i] if offsets is not None and i<len(offsets) else (0,0)
                walk(child,x+dx,y+dy,owner)
        walk(root)
        return rows

    def text_for(screen_name,caption=None,widget_id=None):
        screen=renpy.get_screen(screen_name)
        assert screen is not None,screen_name
        target=renpy.get_widget(screen_name,widget_id) if widget_id else None
        matches=[r for r in text_rows(screen) if (r["widget"] is target if target is not None else r["text"].strip()==caption)]
        assert len(matches)==1,(screen_name,caption,widget_id,[(r["text"],r["x"],r["y"]) for r in matches])
        return matches[0]

    def button_for(caption,screen_name=None,widget_id=None):
        if widget_id is not None:
            target=renpy.get_widget(screen_name,widget_id)
            assert target is not None,("Missing control widget",screen_name,widget_id)
            if isinstance(target,SdkText):
                # Ren'Py textbutton ids may resolve to its Text rather than its
                # Button. Recover the actual enclosing Window from the screen.
                matches=[r for r in text_rows(renpy.get_screen(screen_name)) if r["widget"] is target]
                assert len(matches)==1 and matches[0]["owner"] is not None,(screen_name,widget_id)
                owner,x,y,w,h=matches[0]["owner"]
                widget=owner
                global_button=[x,y,w,h]
            else:
                widget=target
                matches=[r for r in text_rows(renpy.get_screen(screen_name)) if r["owner"] is not None and r["owner"][0] is widget]
                assert matches,(screen_name,widget_id,"No real owning Window")
                _,x,y,w,h=matches[0]["owner"];global_button=[x,y,w,h]
        else:
            focus=find_focus(caption,False)
            assert focus is not None,("No rendered focus",caption)
            widget=focus.widget
            assert hasattr(widget,"window_size"),(caption,type(widget))
            global_button=[float(focus.x),float(focus.y),float(widget.window_size[0]),float(widget.window_size[1])]
        rows=[r for r in text_rows(widget) if r["text"].strip()==caption]
        assert len(rows)==1,(caption,[r["text"] for r in rows])
        assert hasattr(widget,"window_size"),(caption,type(widget))
        row=rows[0];row["global_button_rect"]=global_button
        return widget,row

    def luminance(value):
        rgb=Color(value).rgb
        values=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in rgb]
        return .2126*values[0]+.7152*values[1]+.0722*values[2]

    def contrast(foreground,background):
        a,b=sorted((luminance(foreground),luminance(background)))
        return (b+.05)/(a+.05)

    def readable(caption,screen_name=None,widget_id=None):
        widget,row=button_for(caption,screen_name,widget_id)
        color=Color(row["widget"].style.color)
        ratios={surface:round(contrast(color,surface),3) for surface in LIGHT_SURFACES}
        return record("computed_button_contrast",caption,min(ratios.values())>=4.5 and color[3]==255,
            foreground=color.hexcode,contrast=ratios,style_prefix=str(row["widget"].style.prefix))

    def centered(caption,screen_name=None,widget_id=None):
        widget,row=button_for(caption,screen_name,widget_id)
        assert renpy._screenshot_polish_capture is not None,"Capture native PNG before queueing a centre check."
        x,y,w,h=row["global_button_rect"]
        record("ink_centre_pending_png",caption,None,button_rect=[x,y,w,h],
            text_metric_rect=[x+row["x"],y+row["y"],row["w"],row["h"]],
            foreground=Color(row["widget"].style.color).hexcode,widget_id=widget_id,
            background_present=widget.style.background is not None,
            status="requires_actual_png_pixels")
        # True means only that a real control was found and queued. No metric
        # or unexecuted raster calculation certifies visual centring here.
        return True

    def buttons(captions):
        passed=True
        for caption in captions:
            centered(caption)
            passed=readable(caption) and passed
        return passed

    def buttons_by_id(screen_name,items):
        passed=True
        for caption,widget_id in items:
            centered(caption,screen_name,widget_id)
            passed=readable(caption,screen_name,widget_id) and passed
        return passed

    def title_logo():
        widget=renpy.get_widget("main_menu","main_title")
        assert widget is not None,("Missing title widget","main_title")
        asset=getattr(getattr(widget,"child",None),"filename",None)
        size=renpy.display.render.render(widget,1920,1080,0,0).get_size()
        xpos,_,xanchor,_,_,_,_=widget.get_placement()
        alt=widget._tts(raw=True)
        return record("rendered_main_title_logo","main_title",
            asset=="images/ui/campus_main/title_calligraphy.png"
                and size[0]==540 and 90<=size[1]<=91
                and xpos==xanchor==0.5 and alt==renpy.config.name,
            asset=asset,size=size,xpos=xpos,xanchor=xanchor,alt=alt)

    def centered_in_owner(screen_name,widget_id,label=None):
        row=text_for(screen_name,widget_id=widget_id)
        assert row["owner"] is not None,(screen_name,widget_id)
        owner,x,y,w,h=row["owner"]
        assert renpy._screenshot_polish_capture is not None
        record("ink_centre_pending_png",label or widget_id,None,
            button_rect=[x,y,w,h],text_metric_rect=[row["x"],row["y"],row["w"],row["h"]],
            foreground=Color(row["widget"].style.color).hexcode,widget_id=widget_id,
            background_present=owner.style.background is not None,
            status="requires_actual_png_pixels")
        return True

    def profile_paper_helper():
        screen=renpy.get_screen("profiles")
        rows=[r for r in text_rows(screen) if r["text"].startswith("조금 더 가까워지면")]
        assert len(rows)==1,[r["text"] for r in rows]
        row=rows[0];own=row["owner"]
        inside=False
        if own is not None:
            _,x,y,w,h=own
            inside=row["x"]>=x-2 and row["y"]>=y-2 and row["x"]+row["w"]<=x+w+2 and row["y"]+row["h"]<=y+h+2
        color=Color(row["widget"].style.color)
        return record("helper_inside_own_paper","profile_unlock_hint",inside and contrast(color,"#fffafd")>=4.5,
            owner_present=own is not None,foreground=color.hexcode,text_rect=[row["x"],row["y"],row["w"],row["h"]])

    def ending_rows():
        screen=renpy.get_screen("endings")
        names=[renpy.store.HEROINES[key]["name"] for key in renpy.store.HEROINE_ORDER]
        rows=[text_for("endings",name) for name in names]
        xvalues=[r["x"] for r in rows]
        gaps=[rows[i+1]["y"]-(rows[i]["y"]+rows[i]["h"]) for i in range(len(rows)-1)]
        return record("diary_ending_row_alignment","five_heroines",max(xvalues)-min(xvalues)<=3.5 and min(gaps)>=12,
            names=names,rows=[[r["x"],r["y"],r["w"],r["h"]] for r in rows],row_gaps=gaps)

    def dialogue_labels():
        who=text_for("say",widget_id="who")
        assert who["text"]==renpy.store.typography_qa.LONG_NAME
        owned=centered_in_owner("say","who","twelve_character_nameplate")
        location=text_for("say",caption=renpy.store.location_name)
        size=location["widget"].style.size
        bold=location["widget"].style.bold
        color=Color(location["widget"].style.color)
        proper=record("readable_location_badge","current_location",size>=26 and bold and contrast(color,"#fffafd")>=4.5,
            size=size,bold=bold,foreground=color.hexcode,location=location["text"])
        return owned and proper

    def audit(screen,label):
        return renpy.store.typography_qa.audit(screen,"polish_"+label)


testsuite screenshot_polish:
    setup:
        $ screenshot_polish_qa.begin()
        $ _test.timeout = 25.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/screenshot-polish-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _preferences.afm_enable = False
    before testcase:
        if eval main_menu:
            if not screen "main_menu":
                click "돌아가기"
        else:
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        pause until eval typography_qa.ready("main_menu")
        pause 0.1
    after testcase:
        if screen "profile_note":
            click "접어 두기"
        if eval main_menu:
            if not screen "main_menu":
                click "돌아가기"
        else:
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        $ screenshot_polish_qa.finish()
        exit

    testcase main_serif_title_and_centred_actions:
        screenshot "main_actions.png"
        $ screenshot_polish_qa.captured("main_actions.png")
        $ renpy._polish_ok = screenshot_polish_qa.title_logo()
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.buttons(["게임 시작","불러오기","갤러리","CC대 학생들","엔딩","옵션"])
        assert eval renpy._polish_ok
        move "게임 시작"
        pause 0.15
        screenshot "main_serif_title_hover.png"
        $ screenshot_polish_qa.captured("main_serif_title_hover.png")
        $ renpy._polish_ok = screenshot_polish_qa.buttons(["게임 시작"])
        assert eval renpy._polish_ok

    testcase preferences_centres_and_active_states:
        parameter (tab_index,tab) = [(0,"기본 설정"),(1,"사운드"),(2,"텍스트"),(3,"화면"),(4,"기타")]
        run ShowMenu("preferences")
        click id ("settings_nav_"+str(tab_index)) screen ("preferences",)
        pause 0.15
        move id ("settings_nav_"+str(tab_index)) screen ("preferences",)
        pause 0.1
        pause until eval typography_qa.ready("preferences")
        screenshot f"preferences_{tab}_centred.png"
        $ screenshot_polish_qa.captured("preferences_"+tab+"_centred.png")
        $ renpy._polish_ok = screenshot_polish_qa.buttons_by_id("preferences",[(caption,"settings_nav_"+str(index)) for index,caption in enumerate(["기본 설정","사운드","텍스트","화면","기타"])]+[("돌아가기","page_back")])
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.audit("preferences","preferences_"+tab)
        assert eval renpy._polish_ok
        if eval tab == "텍스트":
            click id "settings_skip_unread" screen ("preferences",)
            pause 0.15
            screenshot "settings_skip_unread_selected_hover.png"
            $ screenshot_polish_qa.captured("settings_skip_unread_selected_hover.png")
            $ renpy._polish_ok = screenshot_polish_qa.buttons_by_id("preferences",[("읽지 않은 대사도 건너뛰기","settings_skip_unread")])
            assert eval renpy._polish_ok
            move id "settings_after_choices" screen ("preferences",)
            pause 0.15
            screenshot "settings_skip_unread_selected_idle.png"
            $ screenshot_polish_qa.captured("settings_skip_unread_selected_idle.png")
            $ renpy._polish_ok = screenshot_polish_qa.buttons_by_id("preferences",[("읽지 않은 대사도 건너뛰기","settings_skip_unread")])
            assert eval renpy._polish_ok
            click id "settings_skip_unread" screen ("preferences",)
            pause 0.1
            click id "settings_after_choices" screen ("preferences",)
            pause 0.15
            screenshot "settings_after_choices_selected_hover.png"
            $ screenshot_polish_qa.captured("settings_after_choices_selected_hover.png")
            $ renpy._polish_ok = screenshot_polish_qa.buttons_by_id("preferences",[("선택지 이후 계속 건너뛰기","settings_after_choices")])
            assert eval renpy._polish_ok
            click id "settings_after_choices" screen ("preferences",)
            pause 0.1

    testcase file_controls_and_return:
        parameter target = ["load","save"]
        if eval target == "save":
            run Start("qa_typography_normal")
            pause until screen "say"
        run ShowMenu(target)
        run FilePage("2")
        pause 0.15
        pause until eval typography_qa.ready(target)
        move id "file_next" screen (target,)
        pause 0.15
        screenshot f"files_{target}_centred.png"
        $ screenshot_polish_qa.captured("files_"+target+"_centred.png")
        $ renpy._polish_ok = screenshot_polish_qa.buttons_by_id(target,[("자동","file_page_auto"),("빠른 저장","file_page_quick")]+[(str(index),"file_page_"+str(index)) for index in range(1,6)]+[("이전 페이지","file_prev"),("다음 페이지","file_next"),("돌아가기","page_back")])
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.audit(target,"files_"+target)
        assert eval renpy._polish_ok

    testcase profile_controls_and_hint_paper:
        parameter heroine = ["roman","lumi"]
        run ShowMenu("profiles",initial=heroine)
        pause until eval typography_qa.ready("profiles")
        move "뒷면 보기"
        pause 0.15
        screenshot f"profile_{heroine}_front_controls.png"
        $ screenshot_polish_qa.captured("profile_"+heroine+"_front_controls.png")
        $ renpy._polish_ok = screenshot_polish_qa.buttons(["프로필","비밀 메모","일상 사진","뒷면 보기","이전","다음"])
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.centered_in_owner("profiles","profile_department_badge")
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.profile_paper_helper()
        assert eval renpy._polish_ok
        click "뒷면 보기"
        pause 0.15
        pause until eval typography_qa.ready("profiles")
        screenshot f"profile_{heroine}_back_controls.png"
        $ screenshot_polish_qa.captured("profile_"+heroine+"_back_controls.png")
        $ renpy._polish_ok = screenshot_polish_qa.buttons(["앞면 보기"])
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.audit("profiles",heroine+"_back")
        assert eval renpy._polish_ok

    testcase diary_endings_rows:
        run ShowMenu("endings")
        pause until eval typography_qa.ready("endings")
        screenshot "ending_diary_rows.png"
        $ screenshot_polish_qa.captured("ending_diary_rows.png")
        $ renpy._polish_ok = screenshot_polish_qa.ending_rows()
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.buttons(["돌아가기"])
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.audit("endings","ending_diary")
        assert eval renpy._polish_ok

    testcase long_name_location_and_quick_controls:
        run Start("qa_typography_normal")
        pause until screen "say"
        pause until eval typography_qa.ready("say")
        pause until eval typography_qa.ready("quick_menu")
        screenshot "long_name_location_quick_controls.png"
        $ screenshot_polish_qa.captured("long_name_location_quick_controls.png")
        $ renpy._polish_ok = screenshot_polish_qa.dialogue_labels()
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.buttons(["자동","건너뛰기","기록","저장","불러오기","빠른 저장","학생증","설정","메뉴"])
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.audit("say","long_name_location")
        assert eval renpy._polish_ok
        $ renpy._polish_ok = screenshot_polish_qa.audit("quick_menu","quick_controls")
        assert eval renpy._polish_ok
