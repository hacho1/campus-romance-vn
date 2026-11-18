# Test-only rendered typography/overflow audit. Never run against player saves.
# Run after tools/prepare_ui_qa.py --refresh; excluded from distributions.
init python in typography_qa:
    import builtins
    import copy
    import json
    import os
    from pathlib import Path
    from renpy.text.text import Text as SdkText
    from renpy.color import Color
    from renpy.display.layout import Window as SdkWindow
    from renpy.display.viewport import Viewport as SdkViewport
    from renpy.display.transform import Transform as SdkTransform

    ROOT = Path("D:/CampusRomance_VN/tests")
    RESULTS = ROOT / "typography-layout-results.json"
    LONG_NAME = "가나다라마바사아자차카타"
    LONG_REPLY = "모두가 편하게 둘러볼 수 있도록 안내 문구와 방문객의 이동 순서를 함께 정리해 볼게."
    LONG_LINE = "창가에 놓인 작은 질문 카드를 한 장씩 정리하다가, 우리는 서로의 말에 귀를 기울였다. 바쁘게 지나간 하루의 끝에서도 함께 준비한 순간은 오래 마음에 남았다."
    rows = []

    MINIMUM_TEXT = {"main_menu":9,"profiles":20,"profile_note":4,"profile_secret_notes":6,"gallery":12,"cg_view":3,"preferences":8,
        "load":16,"save":16,"help":8,"endings":12,"developer_room":6,"chapter_developer":6,"meta_test":6,
        "say":2,"choice":3,"quick_menu":6,"history":3,"input":3,"confirm":3,"sd_event_view":7,"ld_cg_view":4}

    def install_render_observer():
        # The SDK evicts Text layout caches between interactions even when the
        # renderer legitimately reuses a cached Render. Preserve metrics at the
        # moment the real screen renders each Text, rather than measuring a
        # child again in isolation with fabricated available dimensions.
        original=SdkText.render
        renpy._typography_original_text_render=original
        renpy._typography_text_metrics={}
        def observe(widget,width,height,st,at):
            rendered=original(widget,width,height,st,at)
            layout=widget.get_virtual_layout()
            if layout is not None:
                renpy._typography_text_metrics[id(widget)]={"widget":widget,
                    "size":tuple(float(v) for v in layout.size),
                    "constraint":(float(layout.width),float(layout.height))}
            return rendered
        SdkText.render=observe

    def refresh(screen_name,layer=None):
        screen=renpy.get_screen(screen_name,layer=layer) if layer else renpy.get_screen(screen_name)
        if screen is not None:
            screen.visit_all(lambda widget:renpy.redraw(widget,0))

    def ready(screen_name,layer=None):
        screen=renpy.get_screen(screen_name,layer=layer) if layer else renpy.get_screen(screen_name)
        if screen is None:
            return False
        count=[0]
        def observe(widget):
            if isinstance(widget,SdkText) and id(widget) in renpy._typography_text_metrics:
                count[0]+=1
        screen.visit_all(observe)
        return count[0]>=MINIMUM_TEXT.get(screen_name,1)

    def begin():
        expected = Path("D:/CampusRomance_VN/tests/ui_refresh_fixture/renpy_project")
        assert os.path.normcase(os.path.abspath(renpy.config.basedir)) == os.path.normcase(str(expected)), "Use the isolated QA clone."
        assert os.path.commonpath([os.path.abspath(renpy.config.savedir), str(ROOT)]) == str(ROOT)
        renpy._typography_qa_persistent = {k:copy.deepcopy(getattr(renpy.store.persistent,k)) for k in renpy.store.campus_ui_test.PERSISTENT_FIELDS}
        renpy._typography_qa_cg_registry = copy.deepcopy(renpy.store.CG_REGISTRY)
        renpy._typography_qa_sd_registry = copy.deepcopy(renpy.store.SD_EVENT_REGISTRY)
        rows[:] = []
        install_render_observer()
        refresh("main_menu")
        write_results()

    def finish():
        restore_cg_fixture()
        restore_sd_fixture()
        SdkText.render=renpy._typography_original_text_render
        for k,v in renpy._typography_qa_persistent.items():
            setattr(renpy.store.persistent,k,v)
        renpy.save_persistent()
        write_results()
        print("TYPOGRAPHY_RENDER_AUDIT",len(rows),"captures",sum(r["text_count"] for r in rows),"text layouts",sum(len(r["issues"]) for r in rows),"issues")

    def write_results():
        data = {"mode":"Metrics captured by a test-only Text.render observer during actual SDK screen rendering; never isolated synthetic re-renders",
            "virtual_canvas":[1920,1080],"captures":rows,
            "limitations":["Rotated/transformed decorative photo text is checked intrinsically; its transformed screen rectangle requires screenshot review.",
                "The audit uses native layout rectangles, not pixel-level glyph masks. Narrow metric intersections are reported with a tolerance.",
                "Intentional vertical scrolling is measured against the viewport content range; horizontal fit and per-bubble containment remain checked."]}
        RESULTS.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")

    def plain(widget):
        try:
            return str(widget.get_all_text())
        except Exception:
            return str(widget._tts_all(False))

    def numeric_limit(value):
        return float(value) if type(value) is int and value >= 1 else None

    def intersect(a,b):
        x=max(a[0],b[0]); y=max(a[1],b[1])
        right=min(a[2],b[2]); bottom=min(a[3],b[3])
        return (x,y,right,bottom) if right>x and bottom>y else None

    def hidden_phone_native_what(widget):
        # Only the native-required say.what is exempt. An open lock/list
        # page, or the actual closed arrival-gate notice, deliberately hides
        # this exact size1/alpha0/x=-2000 widget. Other off-canvas text fails.
        s=renpy.store
        if not s.story_chat_active or renpy.get_screen("say") is None:
            return False
        if renpy.get_widget("say","what") is not widget:
            return False
        lock_or_list = s.phone_is_open and s.phone_view in ("lock","list")
        closed_arrival = not s.phone_is_open and renpy.get_widget("say","phone_arrival_notice") is not None
        return ((lock_or_list or closed_arrival) and widget.style.size == 1
            and widget.get_placement()[0] == -2000 and Color(widget.style.color).alpha == 0)

    def audit(screen_name,label,layer=None):
        screen = renpy.get_screen(screen_name,layer=layer) if layer else renpy.get_screen(screen_name)
        assert screen is not None,(screen_name,label)
        issues=[]; texts=[]; unknown=[]; viewports=[]; exclusions=[]
        seen=set()
        # Traverse only the actual rendered screen. Do not call render() on a
        # child in isolation: doing so would change its wrapping constraints.
        def walk(node,x=0,y=0,exact=True,owner=None,viewport=None):
            identity=id(node)
            if identity in seen:
                return
            seen.add(identity)
            is_transform=isinstance(node,SdkTransform)
            if is_transform:
                exact=False
            if isinstance(node,SdkWindow) and hasattr(node,"window_size"):
                w,h=node.window_size
                owner=(x,y,float(w),float(h),exact)
                for axis,actual,limit in (("width",w,numeric_limit(node.style.xmaximum)),("height",h,numeric_limit(node.style.ymaximum))):
                    if limit is not None and actual>limit+2:
                        issues.append({"kind":"window_expands_past_declared_"+axis,"actual":actual,"limit":limit})
                if exact and viewport is None and (x < -2 or y < -2 or x+w>1922 or y+h>1082):
                    issues.append({"kind":"window_outside_canvas","rect":[x,y,w,h]})
            if isinstance(node,SdkViewport):
                viewport=(x,y,float(node.width),float(node.height),float(node.xadjustment.value),float(node.yadjustment.value),float(node.xadjustment.range),float(node.yadjustment.range))
                viewports.append({"rect":[x,y,node.width,node.height],"range":[node.xadjustment.range,node.yadjustment.range],"position":[node.xadjustment.value,node.yadjustment.value],"scrollable":bool(node.draggable or node.mousewheel or node.arrowkeys)})
                if node.yadjustment.range>2 and not (node.draggable or node.mousewheel or node.arrowkeys):
                    issues.append({"kind":"unreachable_vertical_viewport_content","range":node.yadjustment.range})
            if isinstance(node,SdkText):
                if hidden_phone_native_what(node):
                    exclusions.append({"widget":"say.what","reason":"Native say requirement behind phone lock/list or the verified closed arrival gate",
                        "phone_view":renpy.store.phone_view,"phone_is_open":renpy.store.phone_is_open,
                        "arrival_notice_present":renpy.get_widget("say","phone_arrival_notice") is not None,
                        "xpos":-2000,"size":1,"color_alpha":0})
                    return
                text=plain(node)
                metric=renpy._typography_text_metrics.get(id(node))
                if metric is None:
                    if text.strip():
                        issues.append({"kind":"text_has_not_been_measured_in_actual_render","text":text})
                    return
                w,h=metric["size"]
                maxw,maxh=metric["constraint"]
                record={"text":text,"rect":[round(x,2),round(y,2),w,h],"constraint":[maxw,maxh],"font":str(node.style.font),"exact_screen_geometry":exact}
                texts.append(record)
                if w>maxw+2:
                    issues.append({"kind":"text_exceeds_render_width","text":text,"actual":w,"limit":maxw})
                if viewport is None and h>maxh+2:
                    issues.append({"kind":"text_exceeds_render_height","text":text,"actual":h,"limit":maxh})
                if owner:
                    ox,oy,ow,oh,owner_exact=owner
                    # Local child offsets remain valid even if an outer
                    # transform rotates the entire window.
                    if x<ox-2 or y<oy-2 or x+w>ox+ow+2 or y+h>oy+oh+2:
                        issues.append({"kind":"text_outside_owning_window","text":text,"rect":[x-ox,y-oy,w,h],"window":[ow,oh]})
                if exact:
                    if viewport is None:
                        if x < -2 or y < -2 or x+w>1922 or y+h>1082:
                            issues.append({"kind":"text_outside_canvas","text":text,"rect":[x,y,w,h]})
                        visible=(x,y,x+w,y+h)
                    else:
                        vx,vy,vw,vh,xval,yval,xrange,yrange=viewport
                        content=(x-vx+xval,y-vy+yval,w,h)
                        if content[0]<-2 or content[0]+w>vw+xrange+2 or content[1]<-2 or content[1]+h>vh+yrange+2:
                            issues.append({"kind":"text_outside_scrollable_content","text":text,"content_rect":content,"content_size":[vw+xrange,vh+yrange]})
                        if xrange <= 2 and (content[0]<-2 or content[0]+w>vw+2):
                            issues.append({"kind":"text_clipped_horizontally_by_viewport","text":text,"content_rect":content,"viewport_width":vw})
                        visible=intersect((x,y,x+w,y+h),(vx,vy,vx+vw,vy+vh))
                    record["visible_rect"]=visible
                else:
                    unknown.append(text)
                return
            children=getattr(node,"children",None)
            offsets=getattr(node,"offsets",None)
            if not children:
                child=getattr(node,"child",None)
                children=[child] if child is not None else []
            for i,child in enumerate(children):
                if child is None:
                    continue
                if offsets is not None and i<len(offsets):
                    dx,dy=offsets[i]
                    walk(child,x+dx,y+dy,exact,owner,viewport)
                elif len(children)==1:
                    walk(child,x,y,exact and not is_transform,owner,viewport)
                else:
                    walk(child,x,y,False,owner,viewport)
        walk(screen)
        # Check only visible portions, so a scrolled-off message is never
        # treated as overlapping the phone header or reply controls.
        for i,a in enumerate(texts):
            ar=a.get("visible_rect")
            if not ar:
                continue
            for b in texts[i+1:]:
                br=b.get("visible_rect")
                if not br:
                    continue
                overlap=intersect(ar,br)
                if overlap:
                    area=(overlap[2]-overlap[0])*(overlap[3]-overlap[1])
                    smaller=min((ar[2]-ar[0])*(ar[3]-ar[1]),(br[2]-br[0])*(br[3]-br[1]))
                    if area>12 and area/max(1,smaller)>.12:
                        issues.append({"kind":"visible_text_rectangles_overlap","first":a["text"],"second":b["text"],"intersection":overlap})
        row={"screen":screen_name,"label":label,"physical_size":builtins.list(renpy.get_physical_size()),"text_count":len(texts),"viewports":viewports,"documented_exclusions":exclusions,"transformed_text_needing_visual_review":unknown,"texts":texts,"issues":issues}
        rows.append(row); write_results()
        for issue in issues[:16]:
            print("TYPOGRAPHY_LAYOUT_ISSUE",label,json.dumps(issue,ensure_ascii=False))
        print("TYPOGRAPHY_LAYOUT_CAPTURE",label,len(texts),"texts",len(issues),"issues")
        minimum=MINIMUM_TEXT.get(screen_name,1)
        if len(texts)<minimum:
            issues.append({"kind":"insufficient_rendered_text_coverage","actual":len(texts),"minimum":minimum})
            write_results()
        return len(texts)>=minimum and not issues

    def restore_cg_fixture():
        renpy.store.CG_REGISTRY=copy.deepcopy(renpy._typography_qa_cg_registry)

    def restore_sd_fixture():
        renpy.store.SD_EVENT_REGISTRY=copy.deepcopy(renpy._typography_qa_sd_registry)

    def missing_sd(event_id,variant):
        # Replace only this QA case's in-memory cut path. User-supplied SD
        # artwork and the product registry on disk are never changed.
        restore_sd_fixture()
        renpy.store.SD_EVENT_REGISTRY[event_id]["variants"][variant]["image"]=(
            "tests/sd_assets/typography_missing_sd_"+event_id+"_"+variant+".webp")
        assert renpy.store.sd_event_info(event_id,variant)["asset"] is None

    def missing_ld(cg_id):
        # Only the test's in-memory registry is overridden. Supplied artwork
        # stays untouched, and every case restores the captured real registry.
        restore_cg_fixture()
        entry=renpy.store.CG_REGISTRY[cg_id]
        entry["image"]="tests/sd_assets/typography_missing_"+cg_id+".webp"
        entry["fallback_image"]=None
        assert renpy.store.cg_asset(cg_id) is None

    def seed_phone():
        s=renpy.store
        s.phone_threads.clear()
        s.story_chat(True,title="축제 준비팀")
        s.player_name=LONG_NAME
        s.phone_record("system","새로운 대화가 시작되었습니다. 긴 안내 문장도 말풍선 바깥으로 빠져나가지 않아야 합니다.",legacy_key="typo-system")
        s.phone_record("roman",LONG_LINE,legacy_key="typo-incoming")
        s.phone_record("mc",LONG_REPLY,legacy_key="typo-outgoing")
        s.phone_threads["campus_group"]["title"]="축제 준비팀 · 함께 만드는 우리의 첫 번째 봄"
        # Enter the existing text-layout checkpoint through the public open
        # API. This is a test fixture only; production never auto-opens.
        s.phone_open_current()
        s.phone_set_view("list")
        s.phone_set_view("chat",s.phone_active_thread)

    def seed_history():
        s=renpy.store
        s._history_list=[]
        for i in range(12):
            item=renpy.character.HistoryEntry()
            item.who=LONG_NAME if i%2 else "로만"
            item.what=LONG_LINE
            s._history_list.append(item)


testsuite typography_layout:
    setup:
        $ typography_qa.begin()
        $ _test.timeout = 25.0
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _preferences.afm_enable = False
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/typography-screenshots"
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
        $ typography_qa.restore_cg_fixture()
        $ typography_qa.restore_sd_fixture()
        if screen "profile_note":
            click "접어 두기"
        if screen "profile_secret_notes":
            click id "secret_note_close" screen ("profile_secret_notes",)
        if screen "cg_view":
            click "닫기"
        if screen "confirm":
            click "취소"
        if eval main_menu:
            if not screen "main_menu":
                click "돌아가기"
        else:
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        $ typography_qa.finish()
        exit

    testcase main_window_sizes:
        parameter physical = [(1280,720),(1600,900)]
        run Function(renpy.set_physical_size,physical)
        $ typography_qa.refresh("main_menu")
        pause 0.2
        pause until eval typography_qa.ready('main_menu')
        $ renpy._typography_audit_ok = typography_qa.audit("main_menu","main_"+str(physical[0]))
        assert eval renpy._typography_audit_ok
        screenshot f"main_{physical[0]}.png"

    testcase menu_surfaces:
        parameter target = ["load","save","endings","help","developer_room","chapter_developer","meta_test"]
        if eval target == "save":
            run Start("qa_typography_normal")
            pause until screen "say"
        run ShowMenu(target)
        pause 0.15
        assert screen target
        pause until eval typography_qa.ready(target)
        $ renpy._typography_audit_ok = typography_qa.audit(target,"menu_"+target)
        assert eval renpy._typography_audit_ok
        screenshot f"menu_{target}.png"

    testcase preference_tabs:
        run ShowMenu("preferences")
        click "기본 설정"
        pause 0.1
        pause until eval typography_qa.ready('preferences')
        $ renpy._typography_audit_ok = typography_qa.audit("preferences","settings_general")
        assert eval renpy._typography_audit_ok
        screenshot "settings_general.png"
        click "사운드"
        pause 0.1
        pause until eval typography_qa.ready('preferences')
        $ renpy._typography_audit_ok = typography_qa.audit("preferences","settings_audio")
        assert eval renpy._typography_audit_ok
        screenshot "settings_audio.png"
        click "텍스트"
        pause 0.1
        pause until eval typography_qa.ready('preferences')
        $ renpy._typography_audit_ok = typography_qa.audit("preferences","settings_text")
        assert eval renpy._typography_audit_ok
        screenshot "settings_text.png"
        click "화면"
        pause 0.1
        pause until eval typography_qa.ready('preferences')
        $ renpy._typography_audit_ok = typography_qa.audit("preferences","settings_display")
        assert eval renpy._typography_audit_ok
        screenshot "settings_display.png"
        click "기타"
        pause 0.1
        pause until eval typography_qa.ready('preferences')
        $ renpy._typography_audit_ok = typography_qa.audit("preferences","settings_other")
        assert eval renpy._typography_audit_ok
        screenshot "settings_other.png"

    testcase heroine_front_back_note:
        parameter heroine = ["roman","sia","darim","omu","lumi"]
        run ShowMenu("profiles",initial=heroine)
        pause 0.15
        pause until eval typography_qa.ready('profiles')
        $ renpy._typography_audit_ok = typography_qa.audit("profiles",heroine+"_front")
        assert eval renpy._typography_audit_ok
        screenshot f"{heroine}_front.png"
        click "뒷면 보기"
        pause 0.15
        pause until eval typography_qa.ready('profiles')
        $ renpy._typography_audit_ok = typography_qa.audit("profiles",heroine+"_back")
        assert eval renpy._typography_audit_ok
        screenshot f"{heroine}_back.png"
        $ secret_note_unlock(heroine, 1, notify=False)
        $ renpy.restart_interaction()
        click id "secret_note_slot_1" screen ("profiles",)
        assert screen "profile_secret_notes"
        pause 0.15
        pause until eval typography_qa.ready("profile_secret_notes")
        $ renpy._typography_audit_ok = typography_qa.audit("profile_secret_notes",heroine+"_note")
        assert eval renpy._typography_audit_ok
        screenshot f"{heroine}_note.png"
        click id "secret_note_close" screen ("profile_secret_notes",)

    testcase gallery_tabs:
        parameter tab = ["COMMON","ROMAN","SIA","DARIM","OMU","HARIN","SPECIAL","ENDING"]
        run ShowMenu("gallery")
        click expression tab
        pause 0.1
        pause until eval typography_qa.ready('gallery')
        $ renpy._typography_audit_ok = typography_qa.audit("gallery","gallery_"+tab)
        assert eval renpy._typography_audit_ok
        screenshot f"gallery_{tab}.png"

    testcase gallery_large_view:
        $ cg_unlock("ld_08")
        run ShowMenu("gallery")
        click "ROMAN"
        click id "cg_tile_ld_08" screen ("gallery",)
        assert screen "cg_view"
        pause 0.15
        pause until eval typography_qa.ready('cg_view')
        $ renpy._typography_audit_ok = typography_qa.audit("cg_view","gallery_large_view")
        assert eval renpy._typography_audit_ok
        screenshot "gallery_large_view.png"
        click "닫기"

    testcase normal_long_name_and_paragraph:
        run Start("qa_typography_normal")
        pause until screen "say"
        assert eval player_name == typography_qa.LONG_NAME
        pause until eval typography_qa.ready('say')
        $ renpy._typography_audit_ok = typography_qa.audit("say","normal_long_name_dialogue")
        assert eval renpy._typography_audit_ok
        pause until eval typography_qa.ready('quick_menu')
        $ renpy._typography_audit_ok = typography_qa.audit("quick_menu","normal_quick_menu")
        assert eval renpy._typography_audit_ok
        screenshot "normal_long_name_dialogue.png"
        advance until screen "choice"
        pause until eval typography_qa.ready('choice')
        $ renpy._typography_audit_ok = typography_qa.audit("choice","normal_long_choices")
        assert eval renpy._typography_audit_ok
        screenshot "normal_long_choices.png"

    testcase phone_long_messages_lock_and_list:
        run Start("qa_typography_phone")
        pause until screen "say"
        pause until eval typography_qa.ready('say')
        $ renpy._typography_audit_ok = typography_qa.audit("say","phone_long_messages")
        assert eval renpy._typography_audit_ok
        pause until eval typography_qa.ready('quick_menu')
        $ renpy._typography_audit_ok = typography_qa.audit("quick_menu","phone_quick_menu")
        assert eval renpy._typography_audit_ok
        screenshot "phone_long_messages.png"
        click "잠금화면"
        pause 0.1
        pause until eval typography_qa.ready('say')
        $ renpy._typography_audit_ok = typography_qa.audit("say","phone_long_lock")
        assert eval renpy._typography_audit_ok
        screenshot "phone_long_lock.png"
        click "채팅 목록"
        pause 0.1
        pause until eval typography_qa.ready('say')
        $ renpy._typography_audit_ok = typography_qa.audit("say","phone_long_list")
        assert eval renpy._typography_audit_ok
        screenshot "phone_long_list.png"

    testcase phone_three_long_replies:
        run Start("qa_typography_phone_choice")
        pause until screen "say"
        advance until screen "choice"
        pause until eval typography_qa.ready('choice')
        $ renpy._typography_audit_ok = typography_qa.audit("choice","phone_three_long_replies")
        assert eval renpy._typography_audit_ok
        screenshot "phone_three_long_replies.png"

    testcase history_long_names_and_paragraphs:
        run Start("qa_typography_normal")
        pause until screen "say"
        $ typography_qa.seed_history()
        run ShowMenu("history")
        pause 0.15
        pause until eval typography_qa.ready('history')
        $ renpy._typography_audit_ok = typography_qa.audit("history","history_long_names")
        assert eval renpy._typography_audit_ok
        screenshot "history_long_names.png"

    testcase input_name_and_confirmation:
        run Start("qa_typography_input")
        pause until screen "input"
        pause 0.15
        pause until eval typography_qa.ready('input')
        $ renpy._typography_audit_ok = typography_qa.audit("input","input_name")
        assert eval renpy._typography_audit_ok
        screenshot "input_name.png"
        run Show("confirm",message="지금까지 읽은 이야기와 선택을 저장한 뒤, 메인 화면으로 돌아갈까요?",yes_action=NullAction(),no_action=Hide("confirm"))
        pause 0.1
        pause until eval typography_qa.ready('confirm')
        $ renpy._typography_audit_ok = typography_qa.audit("confirm","confirmation_long_message")
        assert eval renpy._typography_audit_ok
        screenshot "confirmation_long_message.png"
        click "취소"

    testcase sd_placeholder_cut:
        parameter (event_id,variant) = [('ch01_sia_omu_argument', '01'), ('ch01_sia_omu_argument', '02'), ('ch01_sia_omu_argument', '03'), ('ch01_drink_incident', '01'), ('ch01_drink_incident', '02'), ('ch01_drink_incident', '03'), ('ch01_group_meeting', '01'), ('ch01_group_meeting', '02'), ('ch01_group_meeting', '03'), ('ch01_plan_problem', '01'), ('ch01_plan_problem', '02'), ('ch02_rival_introduction', '01'), ('ch02_rival_introduction', '02'), ('ch02_rival_introduction', '03'), ('ch02_interview_flashback', '01'), ('ch02_interview_flashback', '02'), ('ch02_ski_accident', '01'), ('ch02_ski_accident', '02'), ('ch02_ski_accident', '03'), ('ch02_rival_after_presentation', '01'), ('ch02_rival_after_presentation', '02'), ('ch03_rival_comedy', '01'), ('ch03_rival_comedy', '02'), ('ch03_rival_comedy', '03'), ('ch03_trial_confusion', '01'), ('ch03_trial_confusion', '02'), ('ch03_trial_confusion', '03'), ('ch03_sia_force_quit_reaction', '01'), ('ch03_sia_force_quit_reaction', '02'), ('ch03_sia_force_quit_reaction', '03'), ('ch03_joint_cooperation', '01'), ('ch03_joint_cooperation', '02'), ('ch03_joint_cooperation', '03')]
        run Start("qa_typography_scene_hold")
        pause until screen "say"
        $ typography_qa.missing_sd(event_id,variant)
        assert eval sd_event_info(event_id,variant)["asset"] is None
        $ sd_event_start(event_id,variant,transition=0)
        $ renpy.restart_interaction()
        pause 0.1
        pause until eval typography_qa.ready('sd_event_view',layer='sd_events')
        $ renpy._typography_audit_ok = typography_qa.audit("sd_event_view","sd_"+event_id+"_"+variant,layer="sd_events")
        assert eval renpy._typography_audit_ok
        screenshot f"sd_{event_id}_{variant}.png"

    testcase ld_placeholder_cut:
        parameter cg_id = ['ld_01', 'ld_02', 'ld_03', 'ld_04', 'ld_05', 'ld_06', 'ld_07', 'ld_08', 'ld_09', 'ld_10', 'ld_11', 'ld_12']
        run Start("qa_typography_scene_hold")
        pause until screen "say"
        $ typography_qa.missing_ld(cg_id)
        assert eval cg_asset(cg_id) is None
        $ cg_start(cg_id,transition=0)
        $ renpy.restart_interaction()
        pause 0.1
        pause until eval typography_qa.ready('ld_cg_view',layer='ld_cg')
        $ renpy._typography_audit_ok = typography_qa.audit("ld_cg_view","ld_"+cg_id,layer="ld_cg")
        assert eval renpy._typography_audit_ok
        screenshot f"ld_{cg_id}.png"


label qa_typography_normal:
    $ story_begin_chapter(1,"활자와 줄바꿈 검증")
    $ player_name = typography_qa.LONG_NAME
    $ story_scene("room",mode="normal",cast=[],location="한글 줄바꿈 검증")
    mc "[typography_qa.LONG_LINE]"
    menu:
        "질문 카드와 안내 문구를 먼저 읽어 보고, 함께 준비할 수 있는 일을 차근차근 정리한다.":
            pass
        "처음 온 사람도 편하게 둘러볼 수 있도록 방문객의 이동 순서부터 친구들과 함께 점검한다.":
            pass
        "서로의 의견을 충분히 듣고 나서 역할을 나누고, 필요한 물품과 남은 시간을 다시 확인한다.":
            pass
    jump qa_typography_scene_hold

label qa_typography_phone:
    $ story_begin_chapter(1,"휴대폰 긴 문장 검증")
    $ story_scene("room",mode="normal",cast=[],location="휴대폰")
    $ typography_qa.seed_phone()
    roman "앞에서 정리한 안내 문구를 함께 살펴보면 좋겠어요. 처음 온 분들도 어렵지 않게 참여할 수 있도록, 이동하는 순서도 다시 확인해 볼까요?"
    jump qa_typography_scene_hold

label qa_typography_phone_choice:
    $ story_begin_chapter(1,"휴대폰 긴 답장 검증")
    $ story_scene("room",mode="normal",cast=[],location="휴대폰")
    $ typography_qa.seed_phone()
    sia "어떤 순서로 준비하면 좋을까?"
    menu:
        "방문객이 편하게 둘러볼 수 있도록 안내 문구와 이동하는 순서를 함께 정리해 볼게.":
            pass
        "질문 카드에 적힌 긴 문장을 먼저 읽어 보고, 처음 온 사람도 이해하기 쉽게 함께 점검하자.":
            pass
        "우리에게 남은 시간과 필요한 물품부터 살펴보고, 각자 맡을 수 있는 일을 차근차근 나눠 보자.":
            pass
    jump qa_typography_scene_hold

label qa_typography_scene_hold:
    narrator "렌더링된 글자와 패널의 경계를 확인하는 검증 위치입니다."
    jump qa_typography_scene_hold


label qa_typography_input:
    $ renpy.input("이야기 속에서 사용할 이름을 입력해 주세요.",default=typography_qa.LONG_NAME,length=12)
    jump qa_typography_scene_hold



