# Phone narration uses the same native bottom window as ordinary narration.
# Run only in the isolated phone_narration_20261107 fixture.
init python in phone_narration_qa:
    import json
    from pathlib import Path
    from renpy.color import Color
    from renpy.text.text import Text as SdkText
    from renpy.display.layout import Window as SdkWindow

    ROOT = Path("D:/CampusRomance_VN/tests/phone_narration_20261107")
    layouts = []

    def messages():
        return [message for room in renpy.store.phone_threads.values() for message in room["messages"]]

    def assert_history(count):
        history = messages()
        assert len(history) == count
        assert len({message["key"] for message in history}) == count
        assert not any(message["actor"] == "narrator" for message in history)
        return True

    def visible_count(line):
        screen = renpy.get_screen("say")
        found = []; seen = set()
        def walk(node):
            if node is None or id(node) in seen:
                return
            seen.add(id(node))
            if isinstance(node, SdkText):
                if Color(node.style.color).alpha > 0 and str(node.get_all_text()) == line:
                    found.append(node)
            for child in node.visit():
                walk(child)
        walk(screen)
        return len(found)

    def owner_rect(widget_id):
        target = renpy.get_widget("say", widget_id)
        assert target is not None, widget_id
        found = []; seen = set()
        def walk(node, x=0, y=0, owner=None):
            if node is None or id(node) in seen:
                return
            seen.add(id(node))
            size = getattr(node, "window_size", None)
            if isinstance(node, SdkWindow) and size is not None:
                owner = (float(x), float(y), float(size[0]), float(size[1]))
            if node is target:
                assert owner is not None, widget_id
                found.append(owner)
                return
            children = getattr(node, "children", None)
            if not children:
                child = getattr(node, "child", None)
                children = [child] if child is not None else []
            offsets = getattr(node, "offsets", None)
            for index, child in enumerate(children):
                dx, dy = offsets[index] if offsets is not None and index < len(offsets) else (0, 0)
                walk(child, x + dx, y + dy, owner)
        walk(renpy.get_screen("say"))
        assert len(found) == 1, (widget_id, found)
        return found[0]

    def assert_bottom(line, label):
        assert renpy.get_widget("say", "phone_shell") is not None
        assert renpy.store.story_speaker_id == "narrator"
        assert str(renpy.get_widget("say", "what").get_all_text()) == line
        assert visible_count(line) == 1, (label, visible_count(line))
        window = owner_rect("window")
        text_owner = owner_rect("what")
        assert window == (60.0, 814.0, 1800.0, 235.0), (label, window)
        assert text_owner == window, (label, text_owner)
        assert not any(message["text"] == line for message in messages())
        layouts.append({"label": label, "line": line, "window": window,
            "what_owner": text_owner, "visible_instances": visible_count(line), "chat_message_count": len(messages())})
        (ROOT / "layout_evidence.json").write_text(json.dumps(layouts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return True

    def assert_bubble(line, actor):
        s = renpy.store
        assert renpy.get_widget("say", "phone_shell") is not None
        assert renpy.get_widget("say", "window") is None
        assert s.phone_threads[s.phone_active_thread]["messages"][-1]["text"] == line
        assert s.phone_threads[s.phone_active_thread]["messages"][-1]["actor"] == actor
        assert visible_count(line) == 1
        return True

    def assert_reply_state():
        s = renpy.store
        assert s.affection["roman"] == 10 and s.trust["roman"] == 5
        assert s.choice_log == ["qa_phone_narration_reply"]
        assert len(s.phone_threads["campus_group"]["messages"]) == 2
        assert len(s.phone_threads["private_roman"]["messages"]) == 3
        assert s.phone_sequence == 5
        assert_history(5)
        return True


testsuite phone_narration:
    setup:
        python:
            import os
            expected = "D:/CampusRomance_VN/tests/phone_narration_20261107/renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(expected))
            sd_independent_isolation_test.assert_locations()
        $ _test.timeout = 90.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/phone_narration_20261107/screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
        $ sd_independent_isolation_test.assert_locations()
    teardown:
        exit

    testcase authored_ch01_thought_bottom_and_load:
        run Start("qa_phone_narration_ch01")
        advance until eval story_chat_active and phone_active_thread == "campus_group" timeout 60
        assert eval not phone_is_open and phone_notification_pending and not phone_allow_dismiss()
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_view == "lock" and not phone_allow_dismiss()
        click "알림 열기"
        assert eval phone_is_open and phone_view == "chat" and phone_allow_dismiss()
        assert eval renpy.get_widget("say", "window") is not None
        advance until eval _last_say_what == "정말 이상한 사람들이다." timeout 60
        pause 0.15
        assert eval phone_narration_qa.assert_bottom("정말 이상한 사람들이다.", "authored_ch01_thought")
        assert eval phone_narration_qa.assert_history(24) and phone_sequence == 24
        assert eval phone_threads["campus_group"]["messages"][-1]["text"] == "아니 그 기억은 좀 지워줘!!!"
        screenshot "ch01_phone_thought_bottom.png"
        run FileSave("phone-thought", page="20", confirm=False)
        assert eval renpy.can_load("20-phone-thought")
        click id "phone_next" screen ("say",)
        pause until eval _last_say_what == "하지만 이상하게도 낯설지는 않았다."
        run FileLoad("phone-thought", page="20", confirm=False)
        pause until eval _last_say_what == "정말 이상한 사람들이다." timeout 5
        pause 0.15
        assert eval phone_narration_qa.assert_bottom("정말 이상한 사람들이다.", "authored_ch01_after_load")
        assert eval phone_narration_qa.assert_history(24) and phone_sequence == 24
        screenshot "ch01_phone_thought_after_load.png"
        advance until eval phone_active_thread == "private_roman" timeout 15
        pause 0.15
        assert eval phone_is_open and phone_view == "chat" and not phone_notification_pending
        assert eval phone_narration_qa.assert_bubble("앗,,, 늦은 시간에 연락드려서 괜찮을까요……?", "roman")
        assert eval phone_narration_qa.assert_history(25) and len(phone_threads["private_roman"]["messages"]) == 1

    testcase group_private_reply_and_lock_list_gates:
        run Start("qa_phone_narration_fixture")
        pause until screen "say"
        assert eval phone_narration_qa.assert_history(1) and not phone_allow_dismiss()
        keysym "K_SPACE"
        assert eval _last_say_what == "자료를 확인해 주실래요?" and not phone_is_open
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_view == "lock" and not phone_allow_dismiss()
        click "알림 열기"
        pause 0.15
        assert eval phone_narration_qa.assert_bubble("자료를 확인해 주실래요?", "roman")
        click id "phone_next" screen ("say",)
        pause until eval _last_say_what == "손끝이 조금 떨렸다."
        pause 0.15
        assert eval phone_narration_qa.assert_bottom("손끝이 조금 떨렸다.", "fixture_group_narration")
        assert eval phone_narration_qa.assert_history(1)
        click "잠금화면"
        assert eval phone_view == "lock" and not phone_allow_dismiss() and not phone_afm_allow()
        assert eval renpy.get_widget("say", "window") is None and phone_narration_qa.visible_count("손끝이 조금 떨렸다.") == 0
        keysym "K_SPACE"
        assert eval _last_say_what == "손끝이 조금 떨렸다." and phone_narration_qa.assert_history(1)
        click "채팅 목록"
        assert eval phone_view == "list" and not phone_allow_dismiss() and not phone_afm_allow()
        assert eval renpy.get_widget("say", "window") is None and phone_narration_qa.visible_count("손끝이 조금 떨렸다.") == 0
        keysym "K_SPACE"
        assert eval _last_say_what == "손끝이 조금 떨렸다." and phone_narration_qa.assert_history(1)
        click id "phone_room_campus_group" screen ("say",)
        pause 0.15
        assert eval phone_narration_qa.assert_bottom("손끝이 조금 떨렸다.", "fixture_return_from_list")
        click id "phone_next" screen ("say",)
        pause until eval _last_say_what == "확인했어요. 같이 준비해요."
        pause 0.15
        assert eval phone_narration_qa.assert_bubble("확인했어요. 같이 준비해요.", "mc")
        assert eval phone_narration_qa.assert_history(2)
        screenshot "phone_outgoing_stays_in_phone.png"
        click id "phone_next" screen ("say",)
        pause until eval phone_active_thread == "private_roman"
        pause 0.15
        assert eval phone_is_open and not phone_notification_pending and phone_narration_qa.assert_history(3)
        assert eval phone_narration_qa.assert_bubble("이건 따로 드리는 메시지예요.", "roman")
        click id "phone_next" screen ("say",)
        pause until eval _last_say_what == "이번 답장은 조금 신중하게 고르고 싶었다."
        pause 0.15
        assert eval phone_narration_qa.assert_bottom("이번 답장은 조금 신중하게 고르고 싶었다.", "fixture_private_narration")
        screenshot "private_phone_narration_bottom.png"
        click id "phone_next" screen ("say",)
        pause until screen "choice"
        assert eval renpy.get_widget("choice", "phone_choice_shell") is not None
        click "천천히 같이 확인할게요."
        pause until screen "say"
        pause 0.15
        assert eval phone_narration_qa.assert_bubble("천천히 같이 확인할게요.", "mc")
        assert eval affection["roman"] == 10 and trust["roman"] == 5 and choice_log == ["qa_phone_narration_reply"]
        click id "phone_next" screen ("say",)
        pause until eval _last_say_what == "고마워요."
        click id "phone_next" screen ("say",)
        pause until eval _last_say_what == "작게 웃으며 휴대전화를 내려다봤다."
        pause 0.15
        assert eval phone_narration_qa.assert_bottom("작게 웃으며 휴대전화를 내려다봤다.", "fixture_after_reply")
        assert eval phone_narration_qa.assert_reply_state()
        run FileSave("phone-reply", page="20", confirm=False)
        $ story_apply("qa_phone_narration_temporary", affection={"roman": 5})
        run FileLoad("phone-reply", page="20", confirm=False)
        pause until eval _last_say_what == "작게 웃으며 휴대전화를 내려다봤다." timeout 5
        pause 0.15
        assert eval phone_narration_qa.assert_bottom("작게 웃으며 휴대전화를 내려다봤다.", "fixture_after_reply_load")
        assert eval phone_narration_qa.assert_reply_state()
        click id "phone_next" screen ("say",)
        pause until eval _last_say_what == "휴대폰 대화가 끝났다."
        assert eval not story_chat_active and renpy.get_widget("say", "phone_shell") is None
        assert eval renpy.get_widget("say", "window") is not None and phone_narration_qa.assert_reply_state()

label qa_phone_narration_ch01:
    $ story_begin_chapter(1, "휴대폰 독백 위치 검증")
    $ first_task_partner = "roman"
    jump ch01_sc09

label qa_phone_narration_fixture:
    $ story_begin_chapter(1, "단체·개인 독백과 답장 검증")
    $ story_scene("room", cast=[], light="night", location="주인공 방 · 밤")
    $ story_chat(True, title="축제 준비팀")
    roman "자료를 확인해 주실래요?"
    narrator "손끝이 조금 떨렸다."
    mc "확인했어요. 같이 준비해요."
    $ story_chat(True, title="로만 · 개인 메시지")
    roman "이건 따로 드리는 메시지예요."
    narrator "이번 답장은 조금 신중하게 고르고 싶었다."
    menu:
        "천천히 같이 확인할게요.":
            $ story_apply("qa_phone_narration_reply", affection={"roman": 2}, trust={"roman": 1})
            mc "천천히 같이 확인할게요."
        "내일 다시 이야기해요.":
            mc "내일 다시 이야기해요."
    roman "고마워요."
    narrator "작게 웃으며 휴대전화를 내려다봤다."
    $ story_chat(False)
    narrator "휴대폰 대화가 끝났다."
    jump qa_phone_narration_hold

label qa_phone_narration_hold:
    narrator "검증 종료 지점입니다."
    jump qa_phone_narration_hold
