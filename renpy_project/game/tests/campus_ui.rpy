# Native UI regressions. Execute only from tools/prepare_ui_qa.py's QA project.
# This file and its native fixtures are excluded from distributable builds.
init python in campus_ui_test:
    import copy
    import os
    from renpy.display import focus as sdk_focus
    from renpy.display import tts as sdk_tts
    from renpy.test.testfocus import find_focus as sdk_find_focus

    PERSISTENT_FIELDS = ("gallery", "endings", "profile_secrets", "profile_discoveries", "chapter_completions", "choice_memories", "cg_seen", "cg_sd_seen")
    PRIMARY_MENU = ("게임 시작", "불러오기", "갤러리", "CC대 학생들", "엔딩", "옵션")

    def focus_items():
        # This is the same rendered TTS path used by SDK native click selectors.
        result = []
        visited = set()
        for focus in sdk_focus.focus_list:
            if focus.x is None or id(focus.widget) in visited:
                continue
            visited.add(id(focus.widget))
            result.append(str(focus.widget._tts_all(False)).strip())
        return result

    def text_items(screen_name):
        from renpy.text.text import Text as SdkText
        from renpy.color import Color
        screen = renpy.get_screen(screen_name)
        assert screen is not None, screen_name
        # SDK TTS can omit non-focusable children of a viewport. Inspect the
        # actual active screen's Text displayables as well; do not read profile
        # dictionaries or reconstruct the expected UI from fixture data.
        scoped = []
        visited = set()
        def collect(widget):
            if widget is None or id(widget) in visited:
                return
            visited.add(id(widget))
            if isinstance(widget, SdkText):
                color = getattr(widget.style, "color", None)
                if color is not None and Color(color).alpha == 0:
                    return
                getter = getattr(widget, "get_all_text", None)
                value = getter() if getter is not None else widget._tts_all(False)
                scoped.append(str(value))
                return
            children = widget.visit()
            for child in children:
                collect(child)
        collect(screen)
        # Preserve row order so a ruled notebook paragraph spread across
        # several Text nodes can be checked without dropping any characters.
        # Existing native TTS/focus fallbacks remain for other screen controls.
        joined = "\n".join(scoped)
        root_text = str(sdk_tts.root._tts_all(False)) if sdk_tts.root is not None else ""
        return scoped + [joined, root_text] + focus_items()

    def contains_text(screen_name, text):
        # Ruled notebook rows are separate rendered Text nodes. Native TTS
        # inserts row breaks; compare all visible characters, ignoring only
        # whitespace introduced by wrapping rather than dropping content.
        expected = "".join(str(text).split())
        return any(expected in "".join(str(item).split()) for item in text_items(screen_name))

    def main_ready():
        return renpy.get_screen("main_menu") is not None and all(sdk_find_focus(caption, False) is not None for caption in PRIMARY_MENU)

    def debug_state(stage):
        shown = {}
        for name in ("main_menu","profiles","gallery","cg_view","load","save","preferences","endings","profile_note","profile_secret_notes","phone_browser","say","choice"):
            screen = renpy.get_screen(name)
            if screen is not None:
                shown[name] = {"name":str(screen.name), "layer":screen.layer, "zorder":screen.zorder}
        print("CAMPUS_UI_STATE", stage, "main_menu",renpy.store.main_menu,"screens",shown,"focus",focus_items())

    def preserve_test_state():
        renpy._campus_ui_persistent = {name:copy.deepcopy(getattr(renpy.store.persistent, name)) for name in PERSISTENT_FIELDS}
        renpy._campus_ui_registry = copy.deepcopy(renpy.store.CG_REGISTRY)
        renpy._campus_ui_developer = renpy.config.developer

    def restore_test_state():
        for name, value in renpy._campus_ui_persistent.items():
            setattr(renpy.store.persistent, name, copy.deepcopy(value))
        renpy.store.CG_REGISTRY = copy.deepcopy(renpy._campus_ui_registry)
        renpy.config.developer = renpy._campus_ui_developer
        renpy.save_persistent()
        for name in ("cg_view", "profile_note", "profile_secret_notes", "phone_browser"):
            if renpy.has_screen(name):
                renpy.hide_screen(name)
        renpy.restart_interaction()

    def assert_main_menu():
        assert renpy.get_screen("main_menu") is not None
        texts = focus_items()
        for caption in PRIMARY_MENU:
            assert texts.count(caption) == 1, (caption, texts)
        assert "개발실" not in texts
        assert "학생증" not in texts and "엔딩 목록" not in texts and "환경설정" not in texts
        assert renpy.store.cg_seen("ld_01")

    def open_fixture_phone():
        # Only layout/content fixtures use this shortcut. Production events
        # stay closed; hud_phone_followup tests the actual player click gate.
        s=renpy.store
        s.phone_open_current()
        s.phone_set_view("list")
        s.phone_set_view("chat",s.phone_active_thread)
        assert s.phone_is_open and not s.phone_notification_pending

    def phone_snapshot():
        s = renpy.store
        fields = ("player_name", "phone_view", "phone_selected_thread", "phone_active_thread", "phone_sequence", "phone_schema", "phone_is_open", "phone_notification_pending", "phone_gate_schema", "phone_date", "phone_clock", "phone_last_key", "story_chat_active", "story_chat_title", "story_chapter_number", "team_preparation")
        result = {name:getattr(s, name) for name in fields}
        result["phone_threads"] = {key:{"title":room["title"], "unread":room["unread"], "messages":[dict(message) for message in room["messages"]]} for key, room in s.phone_threads.items()}
        result["story_chat_messages"] = [tuple(message) for message in s.story_chat_messages]
        result["affection"] = dict(s.affection)
        result["trust"] = dict(s.trust)
        result["event_flags"] = set(s.event_flags)
        result["choice_log"] = list(s.choice_log)
        return result

    def assert_phone_saved():
        expected = renpy._campus_ui_phone_saved
        actual = phone_snapshot()
        differences = {key:(expected.get(key),actual.get(key)) for key in set(expected) | set(actual) if expected.get(key) != actual.get(key)}
        assert not differences, ("Phone save differs (expected, actual)",differences)

    def assert_phone_history():
        s = renpy.store
        messages = s.phone_threads["campus_group"]["messages"]
        assert [message["actor"] for message in messages] == ["sia","roman","sia","omu","lumi"]
        assert [message["text"] for message in messages] == [
            "첫 메시지: 축제 준비 얘기하자.", "두 번째 메시지: 자료를 가져왔어요.",
            "세 번째 메시지: 다시 팀 채팅이야.", "네 번째 메시지: 사진도 챙겼다.", "다섯 번째 메시지: 모두 확인했어요."]
        assert len(s.phone_threads["private_roman"]["messages"]) == 1
        assert s.phone_threads["private_roman"]["messages"][0]["text"] == "개인 메시지: 질문 카드도 준비했어요."
        assert s.phone_sequence == 6
        assert len(s.story_chat_messages) == 3 and all(len(message) == 3 for message in s.story_chat_messages)
        assert [message[2] for message in s.story_chat_messages] == ["sia","omu","lumi"]
        assert len({message["key"] for room in s.phone_threads.values() for message in room["messages"]}) == 6


testsuite campus_ui:
    setup:
        python:
            import os
            expected = "D:/CampusRomance_VN/tests/ui_refresh_fixture/renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(expected)), "Run campus_ui only in the prepared UI QA clone."
            assert os.path.normcase(os.path.commonpath([os.path.abspath(config.savedir), os.path.abspath("D:/CampusRomance_VN/tests")])) == os.path.normcase(os.path.abspath("D:/CampusRomance_VN/tests"))
        $ _test.timeout = 30.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/campus-ui-screenshots"
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
        pause 0.1
        pause until eval campus_ui_test.main_ready()
        $ campus_ui_test.debug_state("before_testcase")
        $ campus_ui_test.preserve_test_state()
        assert eval not persistent.endings and not meta_unlocked()
    after testcase:
        $ campus_ui_test.debug_state("after_testcase_before_restore")
        if screen "cg_view":
            if eval not renpy.get_screen("cg_view").scope["chrome"]:
                keysym "h"
            click "닫기"
            assert not screen "cg_view"
        $ campus_ui_test.restore_test_state()
        # Rebuild focus after hidden modal screens before clicking the page's
        # Return button. Presence alone does not update the rendered focus list.
        pause 0.1
        if eval main_menu:
            if not screen "main_menu":
                click "돌아가기"
        else:
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        pause 0.1
        $ campus_ui_test.debug_state("after_testcase_main")
    teardown:
        exit

    testcase six_primary_buttons_release_gate:
        $ config.developer = False
        $ renpy.restart_interaction()
        assert screen "main_menu"
        pause 0.1
        screenshot "main_six_buttons_release_before_assert.png"
        $ campus_ui_test.debug_state("main_release_before_assert")
        pause until eval campus_ui_test.main_ready()
        $ campus_ui_test.assert_main_menu()
        assert not "개발실"
        screenshot "main_six_buttons_release.png"

    testcase main_primary_navigation:
        parameter (caption, target) = [("불러오기","load"),("갤러리","gallery"),("CC대 학생들","profiles"),("엔딩","endings"),("옵션","preferences")]
        click expression caption
        assert screen target
        click "돌아가기"
        assert screen "main_menu"

    testcase five_heroine_quotes_and_secret_notes:
        parameter heroine = ["roman","sia","darim","omu","lumi"]
        python:
            persistent.profile_secrets.discard(heroine + ".note01")
            renpy.store.profile_debug_unlock = False
            renpy.restart_interaction()
        pause 0.1
        $ campus_ui_test.debug_state("profile_before_open_" + heroine)
        screenshot f"profile_before_open_{heroine}.png"
        pause until eval campus_ui_test.main_ready()
        click "CC대 학생들"
        click expression HEROINES[heroine]["name"]
        assert eval renpy.get_screen("profiles").scope["selected"] == heroine
        assert eval campus_ui_test.contains_text("profiles", "CC대 학생들")
        assert eval campus_ui_test.contains_text("profiles", PROFILE_PAGES[heroine]["one_line"])
        assert eval not secret_note_ready(heroine, 1)
        click id "secret_note_slot_1" screen ("profiles",)
        assert screen "profile_secret_notes"
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_locked") is not None
        assert eval not campus_ui_test.contains_text("profile_secret_notes", SECRET_NOTE_DATA[heroine]["note01"]["title"])
        assert eval not campus_ui_test.contains_text("profile_secret_notes", SECRET_NOTE_DATA[heroine]["note01"]["text"])
        click id "secret_note_close" screen ("profile_secret_notes",)
        $ secret_note_unlock(heroine, 1, notify=False)
        $ renpy.restart_interaction()
        click id "secret_note_slot_1" screen ("profiles",)
        assert screen "profile_secret_notes"
        assert eval secret_note_ready(heroine, 1)
        assert eval campus_ui_test.contains_text("profile_secret_notes", SECRET_NOTE_DATA[heroine]["note01"]["title"])
        assert eval campus_ui_test.contains_text("profile_secret_notes", SECRET_NOTE_DATA[heroine]["note01"]["text"])
        click id "secret_note_close" screen ("profile_secret_notes",)
        click "뒷면 보기"
        assert eval renpy.get_screen("profiles").scope["back"]
        assert eval campus_ui_test.contains_text("profiles", HEROINES[heroine]["intro"])
        click "앞면 보기"
        assert eval not renpy.get_screen("profiles").scope["back"]
        screenshot f"heroine_{heroine}_quote.png"

    testcase gallery_eight_tabs_and_pagination:
        click "갤러리"
        assert screen "gallery"
        assert eval tuple(CG_TABS) == ("COMMON","ROMAN","SIA","DARIM","OMU","HARIN","SPECIAL","ENDING")
        click "SPECIAL"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "SPECIAL"
        click "다음 페이지"
        assert eval renpy.get_screen("gallery").scope["gallery_page"] == 1
        click "이전 페이지"
        assert eval renpy.get_screen("gallery").scope["gallery_page"] == 0
        click "ROMAN"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "ROMAN"
        click "SIA"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "SIA"
        click "DARIM"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "DARIM"
        click "OMU"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "OMU"
        click "HARIN"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "HARIN"
        click "ENDING"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "ENDING"
        assert eval all(not cg_seen(key) for key in cg_gallery_keys("ENDING"))
        click "COMMON"
        assert eval renpy.get_screen("gallery").scope["gallery_tab"] == "COMMON"
        screenshot "gallery_eight_tabs.png"

    testcase gallery_locked_png_webp_and_viewer_navigation:
        python:
            persistent.cg_seen = {"ld_01", "ld_02", "ld_04", "ld_06", "ld_07"}
            persistent.gallery = set()
            persistent.cg_sd_seen = set()
            CG_REGISTRY["ld_03"]["image"] = "tests/sd_assets/cut_a.webp"
            CG_REGISTRY["ld_05"]["image"] = "tests/sd_assets/cut_b.png"
            renpy.restart_interaction()
        click "갤러리"
        assert eval all(cg_seen(key) and renpy.get_widget("gallery", "cg_tile_" + key) is None for key in ("ld_02", "ld_04", "ld_06", "ld_07"))
        assert eval not cg_seen("ld_03")
        assert eval renpy.get_widget("gallery", "cg_tile_ld_03") is not None
        assert eval renpy.get_widget("gallery", "cg_thumb_ld_03") is None
        assert eval not campus_ui_test.contains_text("gallery", CG_REGISTRY["ld_03"]["title"])
        python:
            cg_unlock("ld_03")
            cg_unlock("ld_05")
            renpy.restart_interaction()
        assert eval cg_asset("ld_03") == "tests/sd_assets/cut_a.png"
        assert eval cg_asset("ld_05") == "tests/sd_assets/cut_b.webp"
        assert eval renpy.get_widget("gallery", "cg_thumb_ld_03") is not None
        click id "cg_tile_ld_03" screen ("gallery",)
        assert screen "cg_view"
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ld_03"
        assert eval renpy.get_widget("cg_view", "cg_view_asset") is not None
        assert eval campus_ui_test.contains_text("cg_view", CG_REGISTRY["ld_03"]["title"])
        assert eval campus_ui_test.contains_text("cg_view", CG_REGISTRY["ld_03"]["scene"])
        screenshot "gallery_fixture_png.png"
        click "다음 장면"
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ld_05"
        assert eval renpy.get_widget("cg_view", "cg_view_asset") is not None
        screenshot "gallery_fixture_webp.png"
        click "이전 장면"
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ld_03"
        keysym "h"
        assert eval not renpy.get_screen("cg_view").scope["chrome"]
        keysym "h"
        assert eval renpy.get_screen("cg_view").scope["chrome"]
        click "닫기"
        assert not screen "cg_view"
        assert screen "gallery"

    testcase gallery_missing_cut_metadata_and_legacy_note:
        python:
            CG_REGISTRY["ld_08"]["image"] = "tests/sd_assets/qa_missing_ld08.webp"
            cg_unlock("ld_08")
            persistent.gallery.add("festival_note")
            renpy.restart_interaction()
        click "갤러리"
        click "ROMAN"
        click id "cg_tile_ld_08" screen ("gallery",)
        assert screen "cg_view"
        assert eval cg_asset("ld_08") is None and renpy.get_widget("cg_view", "cg_view_asset") is None
        assert eval campus_ui_test.contains_text("cg_view", "일러스트 준비 중")
        assert eval campus_ui_test.contains_text("cg_view", CG_REGISTRY["ld_08"]["description"])
        assert eval campus_ui_test.contains_text("cg_view", "CH03")
        screenshot "gallery_missing_metadata.png"
        click "닫기"
        click "SPECIAL"
        assert eval cg_seen("legacy/festival_note") and "legacy/festival_note" in cg_gallery_keys("SPECIAL")
        click id "cg_tile_legacy_festival_note" screen ("gallery",)
        assert screen "cg_view"
        assert eval renpy.get_widget("cg_view", "cg_view_asset") is not None
        assert eval campus_ui_test.contains_text("cg_view", "첫 회의의 메모")
        click "닫기"
        assert not screen "cg_view"
        assert screen "gallery"

    testcase phone_lock_list_chat_and_full_history:
        run Start("qa_campus_phone_walk")
        pause until screen "say"
        assert eval phone_view == "chat" and phone_active_thread == "campus_group"
        assert eval len(phone_threads["campus_group"]["messages"]) == 1
        assert eval renpy.get_widget("say", "phone_shell") is not None
        assert eval renpy.get_widget("say", "phone_next") is not None
        assert eval campus_ui_test.contains_text("say", "단체 대화")
        assert eval renpy.get_widget("say", "window") is None and renpy.get_widget("say", "what").get_all_text() == _last_say_what
        click "잠금화면"
        assert eval phone_view == "lock"
        assert eval not phone_allow_dismiss()
        screenshot "phone_lock.png"
        click "알림 열기"
        assert eval phone_view == "chat" and phone_selected_thread == "campus_group"
        click "채팅 목록"
        assert eval phone_view == "list"
        click id "phone_room_campus_group" screen ("say",)
        assert eval phone_view == "chat"
        click "다음 메시지"
        assert eval len(phone_threads["campus_group"]["messages"]) == 2
        click "다음 메시지"
        assert eval phone_active_thread == "private_roman" and len(phone_threads["private_roman"]["messages"]) == 1
        assert eval phone_is_open and not phone_notification_pending and phone_selected_thread == phone_active_thread
        assert eval campus_ui_test.contains_text("say", "개인 대화")
        assert eval renpy.get_widget("say", "window") is None and renpy.get_widget("say", "what").get_all_text() == _last_say_what
        click "채팅 목록"
        click id "phone_room_campus_group" screen ("say",)
        assert eval phone_selected_thread == "campus_group" and phone_active_thread == "private_roman"
        assert eval not phone_allow_dismiss()
        assert not "다음 메시지"
        assert eval renpy.get_widget("say", "phone_next") is None
        screenshot "phone_other_thread.png"
        click "채팅 목록"
        click id "phone_room_private_roman" screen ("say",)
        assert eval phone_selected_thread == phone_active_thread
        click "다음 메시지"
        click "다음 메시지"
        click "다음 메시지"
        $ campus_ui_test.assert_phone_history()
        screenshot "phone_full_history.png"

    testcase phone_native_replies:
        parameter (reply, choice_id, reward) = [("좋아, 같이 준비하자.","qa_phone_reply_a","affection"),("질문 카드는 내가 확인할게.","qa_phone_reply_b","trust"),("일정부터 정리해 볼게.","qa_phone_reply_c","preparation")]
        run Start("qa_campus_phone_choice")
        advance until screen "choice" timeout 30
        assert eval phone_view == "chat" and story_chat_active
        assert eval renpy.get_widget("choice", "phone_shell") is not None
        assert eval renpy.get_widget("choice", "phone_choice_shell") is not None
        assert "좋아, 같이 준비하자."
        assert "질문 카드는 내가 확인할게."
        assert "일정부터 정리해 볼게."
        screenshot f"phone_replies_{choice_id}.png"
        click expression reply
        pause until screen "say"
        assert eval list(choice_log) == [choice_id]
        assert eval affection["sia"] == 5 * int(reward == "affection")
        assert eval trust["roman"] == 5 * int(reward == "trust")
        assert eval team_preparation == int(reward == "preparation")
        assert eval phone_threads[phone_active_thread]["messages"][-1]["actor"] == "mc"
        assert eval phone_threads[phone_active_thread]["messages"][-1]["text"] == reply
        assert eval phone_view == "chat" and phone_selected_thread == phone_active_thread

    testcase phone_save_load_views:
        parameter saved_view = ["chat","list","lock"]
        run Start("qa_campus_phone_save_" + saved_view)
        pause until screen "say"
        $ renpy._campus_ui_phone_saved = campus_ui_test.phone_snapshot()
        assert eval phone_view == saved_view and phone_schema == 1
        assert eval len(phone_threads) == 2 and phone_threads["campus_group"]["messages"][-1]["actor"] == "roman"
        click "저장"
        assert screen "save"
        run FilePage("9")
        run FileSave("1", confirm=False)
        assert eval renpy.can_load("9-1")
        click "돌아가기"
        python:
            phone_begin("시아")
            phone_record("sia", "저장하지 않은 변경", legacy_key="qa_ui_unsaved")
            phone_set_view("lock" if saved_view == "chat" else "chat", "private_sia")
            renpy.store.phone_sequence = 999
            renpy.store.phone_schema = 0
            renpy.store.phone_date = "변경된 날짜"
            renpy.store.phone_clock = "00:00"
            renpy.store.phone_last_key = "unsaved"
            renpy.store.player_name = "변경됨"
            affection["roman"] = 99
            trust["sia"] = 99
            renpy.store.team_preparation = 99
            event_flags.clear()
            story_chat_messages[:] = [("시아","저장하지 않은 대화","sia")]
            renpy.restart_interaction()
        click "불러오기"
        assert screen "load"
        run FilePage("9")
        run FileLoad("1", confirm=False)
        pause until screen "say"
        $ campus_ui_test.assert_phone_saved()
        assert eval phone_view == saved_view and phone_schema == 1
        assert eval all(len(message) == 3 for message in story_chat_messages)
        assert eval not persistent.endings and not meta_unlocked()
        screenshot f"phone_save_restored_{saved_view}.png"


label qa_campus_phone_initialize:
    $ story_begin_chapter(1, "휴대폰 UI 검증")
    $ player_name = "폰검증"
    $ story_scene("room", mode="normal", cast=[], location="휴대폰 UI 검증")
    $ story_chat(True, title="축제 준비팀")
    $ campus_ui_test.open_fixture_phone()
    return

label qa_campus_phone_walk:
    call qa_campus_phone_initialize
    sia "첫 메시지: 축제 준비 얘기하자."
    roman "두 번째 메시지: 자료를 가져왔어요."
    $ story_chat(True, title="로만")
    roman "개인 메시지: 질문 카드도 준비했어요."
    $ story_chat(True, title="축제 준비팀")
    sia "세 번째 메시지: 다시 팀 채팅이야."
    omu "네 번째 메시지: 사진도 챙겼다."
    lumi "다섯 번째 메시지: 모두 확인했어요."
    jump qa_campus_phone_hold

label qa_campus_phone_choice:
    call qa_campus_phone_initialize
    sia "어떤 일을 맡을지 답장해 줘."
    menu:
        "좋아, 같이 준비하자.":
            $ story_apply("qa_phone_reply_a", affection={"sia":1})
            mc "좋아, 같이 준비하자."
        "질문 카드는 내가 확인할게.":
            $ story_apply("qa_phone_reply_b", trust={"roman":1})
            mc "질문 카드는 내가 확인할게."
        "일정부터 정리해 볼게.":
            $ story_apply("qa_phone_reply_c", counters={"team_preparation":1})
            mc "일정부터 정리해 볼게."
    jump qa_campus_phone_hold

label qa_campus_phone_save_chat:
    $ _qa_campus_saved_view = "chat"
    jump qa_campus_phone_save_initialize
label qa_campus_phone_save_list:
    $ _qa_campus_saved_view = "list"
    jump qa_campus_phone_save_initialize
label qa_campus_phone_save_lock:
    $ _qa_campus_saved_view = "lock"
    jump qa_campus_phone_save_initialize

label qa_campus_phone_save_initialize:
    call qa_campus_phone_initialize
    $ player_name = "폰저장"
    $ phone_record("sia", "팀 채팅에 먼저 남긴 말", legacy_key="qa_ui_group_seed")
    $ story_chat(True, title="로만")
    $ campus_ui_test.open_fixture_phone()
    $ phone_record("roman", "개인 채팅에 남긴 말", legacy_key="qa_ui_private_seed")
    $ story_chat(True, title="축제 준비팀")
    $ campus_ui_test.open_fixture_phone()
    $ affection["roman"] = 7
    $ trust["sia"] = 5
    $ team_preparation = 2
    $ story_flag("qa_phone_saved_flag", True)
    $ phone_set_view(_qa_campus_saved_view, "campus_group")
    roman "이 화면의 메시지와 채팅 목록을 저장합니다."
    jump qa_campus_phone_hold

label qa_campus_phone_hold:
    narrator "휴대폰 UI 검증을 위한 대사 위치입니다."
    jump qa_campus_phone_hold
