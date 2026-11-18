# Real native PNG evidence for the user's rail/knob and notice alignment report.
init python in slider_feedback_qa:
    import copy
    import json
    from pathlib import Path

    REPORT = Path("D:/CampusRomance_VN/tests/slider-feedback-native-regions.json")
    rows = []

    def queue(row):
        # The native assertion reporter can evaluate its expression twice.
        key=(row["kind"],row["id"],row["screenshot"])
        rows[:]=[old for old in rows if (old["kind"],old["id"],old["screenshot"])!=key]
        rows.append(row)

    def begin():
        renpy._slider_feedback_old_results = renpy.store.typography_qa.RESULTS
        renpy.store.typography_qa.RESULTS = Path("D:/CampusRomance_VN/tests/slider-feedback-layout.json")
        renpy.store.typography_qa.begin()
        renpy._slider_feedback_saved_preferences = {key:copy.deepcopy(getattr(renpy.store._preferences,key)) for key in ("text_cps","afm_time","volumes")}
        rows[:] = []

    def finish():
        renpy.store.typography_qa.finish()
        renpy.store.typography_qa.RESULTS = renpy._slider_feedback_old_results
        for key,value in renpy._slider_feedback_saved_preferences.items():
            setattr(renpy.store._preferences,key,value)
        REPORT.write_text(json.dumps({"canvas":[1920,1080],"regions":rows,"status":"native_captures_ready_for_pixel_analysis"},ensure_ascii=False,indent=2),encoding="utf-8")

    def locate(screen_name, widget_id):
        screen=renpy.get_screen(screen_name)
        wanted=renpy.get_widget(screen_name,widget_id)
        assert screen is not None and wanted is not None,(screen_name,widget_id)
        found=[];seen=set()
        def walk(widget,x=0,y=0):
            if id(widget) in seen:return
            seen.add(id(widget))
            if widget is wanted:found.append((x,y));return
            children=getattr(widget,"children",None)
            if not children:
                child=getattr(widget,"child",None)
                children=[child] if child is not None else []
            offsets=getattr(widget,"offsets",None)
            for index,child in enumerate(children):
                if child is None:continue
                dx,dy=offsets[index] if offsets is not None and index<len(offsets) else (0,0)
                walk(child,x+dx,y+dy)
        walk(screen)
        assert len(found)==1,(screen_name,widget_id,found)
        return wanted,found[0]

    def move_sliders(fraction):
        for name in ("music","sound","text","auto"):
            bar=renpy.get_widget("preferences","settings_slider_"+name)
            bar.adjustment.change(bar.adjustment.range*fraction)
        renpy.restart_interaction()

    def rails(screenshot):
        for name in ("music","sound","text","auto"):
            bar,(x,y)=locate("preferences","settings_slider_"+name)
            fraction=bar.adjustment.value/bar.adjustment.range
            assert bar.height==40,(name,bar.height)
            assert y>=225 and y+bar.height<=885,(name,y,bar.height)
            queue({"kind":"slider","id":name,"screenshot":screenshot,"rect":[x,y,bar.width,bar.height],"fraction":fraction,"thumb_centre":[x+20+(bar.width-40)*fraction,y+20]})
        return True

    def text_cell(screen_name, text_id, cell_id, screenshot):
        target,(x,y)=locate(screen_name,cell_id)
        # xysize is screen-language sugar for equal min/max, not a readable
        # Style.xsize property in the SDK.
        width,height=target.style.xminimum,target.style.yminimum
        assert width and height,(cell_id,width,height)
        text=renpy.store.screenshot_polish_qa.text_for(screen_name,widget_id=text_id)
        queue({"kind":"notice_text","id":text_id,"screenshot":screenshot,"rect":[x,y,width,height],"text_rect":[text["x"],text["y"],text["w"],text["h"]]})
        return True

    def notice(screenshot):
        for actor in ("roman","lumi"):
            text_cell("relationship_feedback_view","feedback_name_"+actor,"feedback_name_row_"+actor,screenshot)
            for kind in ("affection","trust"):
                text_cell("relationship_feedback_view","feedback_caption_"+actor+"_"+kind,"feedback_caption_cell_"+actor+"_"+kind,screenshot)
                text_cell("relationship_feedback_view","feedback_delta_"+actor+"_"+kind,"feedback_value_cell_"+actor+"_"+kind,screenshot)
        return True

testsuite slider_feedback_followup:
    setup:
        $ slider_feedback_qa.begin()
        $ _test.timeout = 15.0
        $ _test.transition_timeout = .02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/hud-motion-screenshots"
        $ _preferences.transitions = 0
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        $ slider_feedback_qa.finish()
        exit

    testcase slider_positions:
        parameter fraction = [0.0,.5,1.0]
        run ShowMenu("preferences")
        pause until eval renpy.get_widget("preferences","settings_slider_auto") is not None
        pause .15
        $ slider_feedback_qa.move_sliders(fraction)
        pause .15
        screenshot f"sliders_{fraction}.png"
        assert eval slider_feedback_qa.rails("sliders_"+str(fraction)+".png")

    testcase centred_notice_rows:
        run Start("qa_followup_notice")
        pause until screen "say"
        pause .15
        screenshot "relationship_notice_centred.png"
        assert eval slider_feedback_qa.notice("relationship_notice_centred.png")
        assert eval affection["roman"]==10 and trust["roman"]==5 and affection["lumi"]==10 and trust["lumi"]==5
        pause 2.3
        assert eval not relationship_feedback_items

label qa_followup_notice:
    $ story_begin_chapter(1,"알림 행 정렬 검증")
    $ story_scene("room",cast=["roman","lumi"],light="night",location="주인공 방 · 밤")
    $ story_apply("qa_followup_notice",affection={"roman":2,"lumi":2},trust={"roman":1,"lumi":1})
    mc "이름과 실제 적용된 호감도·신뢰도 변화가 행 가운데에 표시됩니다."
    jump qa_followup_notice_hold

label qa_followup_notice_hold:
    mc "알림이 사라진 뒤에도 이야기는 계속됩니다."
    jump qa_followup_notice_hold
