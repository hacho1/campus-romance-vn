# Native HUD/phone follow-up checks; root runs only the isolated QA project.
# Product state and image choices are observed from rendered screens/actions.
default hud_followup_choice = None

init python in hud_phone_qa:
    import os
    import time
    from pathlib import Path

    def widget(screen_name,widget_id):
        result=renpy.get_widget(screen_name,widget_id)
        assert result is not None,(screen_name,widget_id)
        return result

    def rect(screen_name,widget_id):
        from renpy.display.layout import Window as SdkWindow
        target=widget(screen_name,widget_id)
        root=renpy.get_screen(screen_name)
        found=[];seen=set()
        def walk(node,x=0,y=0,owner=None):
            if node is None or id(node) in seen:return
            seen.add(id(node))
            size=getattr(node,"window_size",None)
            if isinstance(node,SdkWindow) and size is not None:
                owner=(x,y,float(size[0]),float(size[1]))
            if node is target:
                assert owner is not None,("No rendered owner",screen_name,widget_id)
                found.append(owner)
                return
            children=getattr(node,"children",None)
            if not children:
                child=getattr(node,"child",None);children=[child] if child is not None else []
            offsets=getattr(node,"offsets",None)
            for index,child in enumerate(children):
                dx,dy=offsets[index] if offsets is not None and index<len(offsets) else (0,0)
                walk(child,x+dx,y+dy,owner)
        walk(root)
        assert len(found)==1,(screen_name,widget_id,found)
        return found[0]

    def assert_hud_gaps():
        screen_name="quick_menu" if renpy.get_screen("choice") or renpy.store.story_chat_active else "say"
        location=rect(screen_name,"location_badge")
        phone=rect("quick_menu","phone_archive_button")
        controls=rect("quick_menu","quick_controls")
        assert phone[0]-(location[0]+location[2])>=16,(location,phone)
        assert controls[0]-(phone[0]+phone[2])>=16,(phone,controls)
        assert controls[0]+controls[2]<=1860,(controls,)
        print("HUD_PHONE_GAPS",location,phone,controls)
        return True

    def message_count():
        return sum(len(room["messages"]) for room in renpy.store.phone_threads.values())

    def log_gate_state(tag):
        s=renpy.store
        keys=("phone_gate_restore_on_interact","phone_gate_legacy_loaded")
        print(tag,s.phone_gate_schema,s.phone_is_open,s.phone_notification_pending,s.phone_view,s.phone_active_thread,s.phone_selected_thread,message_count(),{key:renpy.session.get(key,"<absent>") for key in keys},s._skipping,s.phone_previous_skipping)

    def log_saved_gate(slot):
        assert renpy.can_load(slot),("Save absent",slot)
        metadata=renpy.slot_json(slot)
        saved=renpy.loadsave.get_save_data(slot)
        fields=("phone_gate_schema","phone_is_open","phone_notification_pending","phone_view","phone_active_thread","phone_selected_thread","phone_previous_skipping","_skipping")
        print("HUD_SAVED_GATE",slot,metadata,{key:saved.get(key,"<default>") for key in fields},"current:")
        log_gate_state("HUD_CURRENT_AT_SAVE")
        print("HUD_SAVED_ROOM",saved.get("phone_threads",{}))
        assert metadata["_ctime"]>=renpy._hud_phone_save_started,("Stale save",metadata,renpy._hud_phone_save_started)
        return True

    def png_panel(kind):
        result=renpy.store.phone_panel(kind)
        names=[];seen=set()
        def walk(node):
            if node is None or id(node) in seen:return
            seen.add(id(node))
            filename=getattr(node,"filename",None)
            if filename:names.append(str(filename))
            for child in node.visit():walk(child)
        walk(result)
        return any(name.endswith("/"+kind+".png") for name in names)

    def photo_fixture(actor):
        return "tests/sd_assets/cut_a.png" if actor=="roman" else None

    def restore_portrait():
        original=getattr(renpy,"_hud_phone_original_portrait",None)
        if original is not None:
            renpy.store.phone_portrait=original
            renpy._hud_phone_original_portrait=None

    def start_checks():
        expected=Path("D:/CampusRomance_VN/tests/ui_refresh_fixture/renpy_project")
        assert os.path.normcase(os.path.abspath(renpy.config.basedir))==os.path.normcase(str(expected)),"QA copy only"
        assert os.environ.get("CAMPUS_SAVE_DIR"),"Separate QA save folder required"
        Path("D:/CampusRomance_VN/tests/hud-phone-screenshots").mkdir(parents=True,exist_ok=True)

screen hud_avatar_preview():
    modal True
    zorder 200
    add Solid("#f6f9fc")
    hbox:
        xpos 360 ypos 360 spacing 80
        for actor in STORY_HEROES:
            vbox:
                spacing 24 xsize 170
                use phone_avatar(actor,110)
                text STORY_CAST[actor]["name"] xalign .5 size 28
    textbutton "닫기" xpos 1600 ypos 90 action Hide("hud_avatar_preview")

testsuite hud_phone_followup:
    setup:
        $ hud_phone_qa.start_checks()
        $ _test.timeout=25.0
        $ _test.transition_timeout=.02
        $ _test.screenshot_directory="D:/CampusRomance_VN/tests/hud-phone-screenshots"
        $ _preferences.text_cps=0
        $ _preferences.afm_enable=False
        $ _preferences.transitions=0
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    after testcase:
        $ hud_phone_qa.restore_portrait()
        $ config.skipping=None
        $ _preferences.afm_enable=False
        if screen "hud_avatar_preview":
            run Hide("hud_avatar_preview")
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        exit

    testcase hud_gaps_and_choice_save_load:
        parameter mode=["normal","phone"]
        run Start("qa_hud_phone_"+mode)
        pause until screen "say"
        if eval mode=="phone":
            assert eval story_chat_active and not phone_is_open and phone_notification_pending
            click id "phone_archive_button" screen ("quick_menu",)
            assert eval phone_is_open and phone_view=="lock" and not phone_allow_dismiss()
            click "알림 열기"
            assert eval phone_view=="chat" and phone_allow_dismiss()
        else:
            pause .15
            assert eval hud_phone_qa.assert_hud_gaps()
            screenshot "normal_hud_gaps.png"
        advance until screen "choice"
        pause .15
        assert eval renpy.get_screen("quick_menu").zorder > renpy.get_screen("choice").zorder
        if eval mode=="normal":
            assert eval hud_phone_qa.assert_hud_gaps()
            screenshot "normal_choice_hud.png"
            click id "quick_save" screen ("quick_menu",)
        else:
            screenshot "phone_choice_toolbar.png"
            click id "phone_toolbar_save" screen ("quick_menu",)
        assert screen "save"
        run FilePage("13")
        run FileSave("1",confirm=False)
        click "돌아가기"
        assert screen "choice"
        if eval mode=="normal":
            click id "quick_load" screen ("quick_menu",)
        else:
            click id "phone_toolbar_load" screen ("quick_menu",)
        assert screen "load"
        run FilePage("13")
        run FileLoad("1",confirm=False)
        pause until screen "choice"
        assert eval hud_followup_choice is None and not choice_log and not persistent.endings
        click "차근차근 확인한다."
        pause until screen "say"
        assert eval hud_followup_choice=="first"

    testcase notification_waits_for_manual_open_and_survives_load:
        run Start("qa_hud_phone_phone")
        pause until screen "say"
        assert eval not phone_is_open and phone_notification_pending and phone_gate_schema==1
        assert eval renpy.get_widget("say","phone_shell") is None and not phone_allow_dismiss()
        assert eval hud_phone_qa.message_count()==1 and phone_threads["campus_group"]["unread"]==1
        $ _preferences.afm_enable=True
        $ _preferences.afm_time=.1
        $ config.skipping="fast"
        pause .5
        assert eval hud_phone_qa.message_count()==1 and not phone_is_open and not phone_afm_allow()
        $ config.skipping=None
        $ _preferences.afm_enable=False
        keysym "h"
        pause .1
        if eval _windows_hidden:
            keysym "h"
        pause .1
        assert eval not phone_is_open and hud_phone_qa.message_count()==1
        click id "quick_save" screen ("quick_menu",)
        run FilePage("13")
        $ renpy._hud_phone_save_started=hud_phone_qa.time.time()
        $ hud_phone_qa.log_gate_state("HUD_BEFORE_CLOSED_SAVE")
        run FileSave("2",confirm=False)
        assert eval hud_phone_qa.log_saved_gate("13-2")
        click "돌아가기"
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_is_open and phone_view=="lock" and not phone_allow_dismiss()
        click "알림 열기"
        assert eval phone_allow_dismiss() and hud_phone_qa.message_count()==1
        assert eval phone_threads["campus_group"]["unread"]==0
        click id "phone_toolbar_load" screen ("quick_menu",)
        run FilePage("13")
        run FileLoad("2",confirm=False)
        pause until screen "say"
        $ hud_phone_qa.log_gate_state("HUD_IMMEDIATE_CLOSED_LOAD")
        # The pre-load say can still be visible while native loading commits.
        pause until eval not phone_is_open and phone_notification_pending and hud_phone_qa.message_count()==1 timeout 1
        $ print("HUD_CLOSED_GATE_LOAD",phone_gate_schema,phone_is_open,phone_notification_pending,phone_view,hud_phone_qa.message_count())
        assert eval not phone_is_open and phone_notification_pending and hud_phone_qa.message_count()==1
        assert eval phone_threads["campus_group"]["unread"]==1
        screenshot "pending_notification_loaded.png"

    testcase close_reopen_and_png_toolbar:
        run Start("qa_hud_phone_phone")
        pause until screen "say"
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        assert eval all(hud_phone_qa.png_panel(kind) for kind in ("panel","hover","reply","incoming","outgoing"))
        click id "phone_toolbar_close" screen ("quick_menu",)
        assert eval not phone_is_open and not phone_notification_pending and not phone_allow_dismiss()
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_is_open and phone_view=="chat" and hud_phone_qa.message_count()==1
        screenshot "phone_toolbar_png.png"

    testcase matching_room_starts_fresh_auto_read_delay:
        run Start("qa_hud_phone_phone")
        pause until screen "say"
        $ _preferences.afm_enable=True
        $ _preferences.afm_time=15
        pause .3
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_view=="lock" and not phone_afm_allow()
        pause .3
        assert eval hud_phone_qa.message_count()==1
        click "채팅 목록"
        assert eval phone_view=="list" and not phone_afm_allow()
        pause .3
        assert eval hud_phone_qa.message_count()==1
        $ renpy._hud_room_open_time=renpy.get_game_runtime()
        click id "phone_room_campus_group" screen ("say",)
        assert eval phone_read_ready_at >= renpy._hud_room_open_time + .25
        assert eval hud_phone_qa.message_count()==1 and phone_allow_dismiss()
        $ _preferences.afm_enable=False

    testcase old_open_phone_schema_migrates_without_new_gate:
        run Start("qa_hud_phone_phone")
        pause until screen "say"
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        $ phone_gate_schema=0
        $ phone_is_open=False
        $ phone_notification_pending=False
        run Function(renpy.save,"hud_old_open_phone")
        run Function(renpy.load,"hud_old_open_phone")
        pause until screen "say"
        $ print("HUD_LEGACY_GATE_LOAD",phone_gate_schema,phone_is_open,phone_notification_pending,phone_view,phone_active_thread)
        assert eval phone_gate_schema==1 and phone_is_open and not phone_notification_pending
        assert eval phone_view=="chat" and phone_allow_dismiss() and hud_phone_qa.message_count()==1
        assert eval not choice_log and hud_followup_choice is None

    testcase school_notice_has_separate_room_and_manual_gate:
        run Start("qa_hud_phone_school_notice")
        pause until screen "say"
        assert eval phone_active_thread=="campus_notice" and phone_threads["campus_notice"]["title"]=="학사 알림"
        assert eval phone_clock==PHONE_UI.get("notice_time","14:20")
        assert eval phone_thread_actor("campus_notice")=="group" and not phone_is_open and phone_notification_pending
        assert eval phone_thread_id("축제 준비팀")=="campus_group" and phone_thread_id("로만")=="private_roman"
        assert eval hud_phone_qa.message_count()==1 and renpy.loadable("audio/sfx/message.wav")
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_view=="lock" and not phone_allow_dismiss()
        click "알림 열기"
        assert eval phone_view=="chat" and phone_allow_dismiss() and hud_phone_qa.message_count()==1
        assert eval phone_threads["campus_notice"]["unread"]==0
        screenshot "school_notice_opened_manually.png"

    testcase five_motif_avatars_and_photo_override:
        run Start("qa_hud_phone_normal")
        pause until screen "say"
        run Show("hud_avatar_preview")
        pause .2
        assert eval all(renpy.get_widget("hud_avatar_preview","phone_avatar_motif_"+actor) is not None for actor in STORY_HEROES)
        screenshot "five_hobby_motif_avatars.png"
        python:
            renpy._hud_phone_original_portrait=phone_portrait
            renpy.store.phone_portrait=hud_phone_qa.photo_fixture
            renpy.restart_interaction()
        pause .15
        assert eval renpy.get_widget("hud_avatar_preview","phone_avatar_photo_roman") is not None
        assert eval renpy.get_widget("hud_avatar_preview","phone_avatar_motif_roman") is None
        screenshot "supplied_photo_has_priority.png"
        click "닫기"

label qa_hud_phone_normal:
    $ story_begin_chapter(1,"HUD 검증")
    $ story_scene("campus",mode="normal",cast=[],location="하온대학교 · 축제 준비팀 동아리실과 전시 안내 게시판 앞")
    $ phone_threads=RevertableDict({"campus_group":RevertableDict({"title":"축제 준비팀","messages":RevertableList(),"unread":0,"updated":0})})
    $ hud_followup_choice=None
    mc "장소와 휴대폰, 빠른 메뉴가 겹치지 않는지 확인합니다."
    jump qa_hud_phone_menu

label qa_hud_phone_phone:
    $ story_begin_chapter(1,"휴대폰 수동 열기 검증")
    $ story_scene("room",mode="normal",cast=[],location="동아리실")
    $ phone_threads=RevertableDict()
    $ hud_followup_choice=None
    $ story_sfx("message")
    $ story_chat(True,title="축제 준비팀")
    roman "새 메시지를 직접 열어 확인해 주세요."
    jump qa_hud_phone_menu

label qa_hud_phone_menu:
    menu:
        "차근차근 확인한다.":
            $ hud_followup_choice="first"
        "조금 더 생각한다.":
            $ hud_followup_choice="second"
    jump qa_hud_phone_hold

label qa_hud_phone_hold:
    mc "선택 이후의 원래 흐름입니다."
    jump qa_hud_phone_hold

label qa_hud_phone_school_notice:
    $ story_begin_chapter(1,"첫 학사 알림 검증")
    $ story_scene("campus",mode="normal",cast=[],location="강의실")
    $ phone_threads=RevertableDict()
    $ story_sfx("message")
    $ story_chat(True,title="학사 알림")
    system_note "「오늘 예정된 강의가 모두 종료되었습니다.」"
    jump qa_hud_phone_hold
