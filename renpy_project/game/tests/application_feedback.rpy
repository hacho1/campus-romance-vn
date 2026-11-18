# Focused native regressions for the application flow and actual-delta notices.
# Excluded from builds with game/tests/**. Use a dedicated CAMPUS_SAVE_DIR.
init python in application_feedback_test:
    def commit_text(value):
        # Exercise the same Unicode commit path as the Windows IME. The test
        # framework's `type` statement only maps keyboard keysyms.
        import pygame_sdl2 as pygame
        widget = renpy.get_widget("input", "input")
        assert widget is not None
        try:
            widget.event(pygame.event.Event(pygame.TEXTINPUT, {"text":value}), 0, 0, 0.0)
        except renpy.display.core.IgnoreEvent:
            pass
        renpy.restart_interaction()

testsuite application_feedback:
    setup:
        python:
            import os
            assert os.environ.get("CAMPUS_SAVE_DIR")
            assert os.path.normcase(os.path.abspath(config.savedir)) == os.path.normcase(os.path.abspath(os.environ["CAMPUS_SAVE_DIR"]))
            assert os.path.normcase(os.path.abspath(config.savedir)) != os.path.normcase(os.path.join(config.basedir, "saves"))
        $ _test.timeout = 15.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/application-feedback-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        exit

    testcase submit_application:
        parameter method = ["button", "enter"]
        run Start("qa_application_entry")
        pause until screen "say"
        assert eval player_name == "나" and not application_input_active
        advance until screen "input" timeout 15
        assert eval application_input_active and renpy.get_widget("input", "input").content == ""
        $ application_feedback_test.commit_text("가나다라마바사아자차카타파")
        assert eval renpy.get_widget("input", "input").content == "가나다라마바사아자차카타"
        screenshot f"application_input_{method}.png"
        if eval method == "button":
            click "신청하기"
        else:
            keysym "K_RETURN"
        pause until screen "application_send_animation"
        assert eval not application_input_active
        screenshot f"application_fold_{method}.png"
        pause until eval renpy.get_screen("application_send_animation") is not None and renpy.get_screen("application_send_animation").scope["phase"] == 2 timeout 5
        screenshot f"application_plane_{method}.png"
        pause until eval renpy.get_screen("application_send_animation") is not None and renpy.get_screen("application_send_animation").scope["phase"] == 3 timeout 5
        screenshot f"application_sent_{method}.png"
        assert eval player_name == "가나다라마바사아자차카타" timeout 15
        assert eval renpy.get_screen("application_send_animation") is None
        assert screen "say"
        # The generic name editor keeps the chosen name and bypasses enrollment.
        run Call("rename_player")
        pause until screen "input"
        assert eval not application_input_active
        assert eval renpy.get_widget("input", "input").content == "가나다라마바사아자차카타"
        $ renpy.get_widget("input", "input").update_text("", True)
        $ application_feedback_test.commit_text("새이름")
        assert eval renpy.get_widget("input", "input").content == "새이름"
        keysym "K_RETURN"
        assert eval player_name == "새이름"
        assert eval renpy.get_screen("application_send_animation") is None

    testcase blank_submission:
        run Start("qa_application_entry")
        pause until screen "say"
        advance until screen "input"
        assert eval renpy.get_widget("input", "input").content == ""
        keysym "K_RETURN"
        pause until screen "application_send_animation"
        assert eval player_name == "나" and not application_input_active
        pause until eval renpy.get_screen("application_send_animation") is None timeout 15
        assert eval player_name == "나" and clean_name("   ") == "나"

    testcase modern_actual_deltas_and_expiry:
        run Start("qa_feedback_clamp_checkpoint")
        pause until screen "say"
        $ story_apply("qa_feedback_clamp", affection={"roman":8, "rumi":-4}, trust={"roman":8, "lumi":2}, values={"qa_feedback_flag":True}, counters={"team_preparation":1})
        assert eval affection["roman"] == 100 and trust["roman"] == 100 and affection["lumi"] == 0 and trust["lumi"] == 10
        assert eval choice_log == ["qa_feedback_clamp"] and "qa_feedback_flag" in event_flags and team_preparation == 1
        python:
            rows = {row["actor"]:dict(row) for row in relationship_feedback_items}
            assert set(rows) == {"roman", "lumi"}
            assert rows["roman"]["name"] == "로만" and rows["roman"]["affection"] == 1 and rows["roman"]["trust"] == 0
            assert rows["lumi"]["name"] == "하린" and rows["lumi"]["affection"] == -1 and rows["lumi"]["trust"] == 10
        assert eval relationship_feedback_choice == "qa_feedback_clamp"
        pause 0.12
        assert eval renpy.get_widget("relationship_feedback_view", "relationship_feedback_panel") is not None
        assert eval renpy.get_widget("relationship_feedback_view", "feedback_delta_roman_affection") is not None
        assert eval renpy.get_widget("relationship_feedback_view", "feedback_delta_lumi_trust") is not None
        screenshot "feedback_actual_clamped_deltas.png"
        pause 2.4
        assert eval not relationship_feedback_items and relationship_feedback_expires == 0.0
        $ story_apply("qa_feedback_full", affection={"roman":4}, trust={"roman":4})
        assert eval not relationship_feedback_items and affection["roman"] == 100 and trust["roman"] == 100
        assert eval choice_log == ["qa_feedback_clamp", "qa_feedback_full"]

    testcase legacy_actual_deltas:
        run Start("qa_feedback_clamp_checkpoint")
        pause until screen "say"
        $ apply_choice("c1_wait")
        assert eval affection["roman"] == 100 and trust["roman"] == 100
        assert eval choice_log == ["c1_wait"] and "waited_for_roman" in event_flags
        assert eval len(relationship_feedback_items) == 1 and relationship_feedback_items[0]["actor"] == "roman"
        assert eval relationship_feedback_items[0]["affection"] == 1 and relationship_feedback_items[0]["trust"] == 0
        pause 0.12
        assert eval renpy.get_widget("relationship_feedback_view", "feedback_delta_roman_affection") is not None
        screenshot "feedback_legacy_actual_delta.png"
        $ apply_choice("c1_wait")
        assert eval choice_log == ["c1_wait", "c1_wait"] and not relationship_feedback_items

    testcase chosen_old_name_and_no_replayed_notice_on_load:
        run Start("qa_feedback_saved_name")
        pause until screen "say"
        assert eval player_name == "하루" and affection["roman"] == 45 and trust["roman"] == 25
        assert eval relationship_feedback_items and relationship_feedback_serial == 1
        click "저장"
        assert screen "save"
        run FilePage("11")
        run FileSave("1", confirm=False)
        assert eval renpy.can_load("11-1")
        click "돌아가기"
        python:
            renpy.store.player_name = "변경됨"
            affection["roman"] = 99
            trust["roman"] = 99
        click "불러오기"
        assert screen "load"
        run FilePage("11")
        run FileLoad("1", confirm=False)
        pause until screen "say"
        pause until eval not relationship_feedback_items and relationship_feedback_expires == 0.0 timeout 1
        assert eval player_name == "하루" and affection["roman"] == 45 and trust["roman"] == 25
        assert eval not relationship_feedback_items and relationship_feedback_choice is None and relationship_feedback_expires == 0.0
        assert eval choice_log == ["qa_feedback_saved"] and relationship_feedback_serial == 1
        assert eval not persistent.endings and not meta_unlocked()

label qa_application_entry:
    $ story_begin_chapter(1, "신청 흐름 검증")
    $ story_scene("campus", mode="normal", cast=[])
    mc "아직 이름을 정하기 전입니다."
    call application_name_input
    $ player_name = _return
    jump qa_application_hold

label qa_application_hold:
    mc "신청 뒤의 원래 이야기로 이어집니다."
    jump qa_application_hold

label qa_feedback_clamp_checkpoint:
    $ story_begin_chapter(1, "관계 알림 검증")
    $ story_scene("campus", mode="normal", cast=["roman", "lumi"])
    $ affection["roman"] = 99
    $ trust["roman"] = 100
    $ affection["lumi"] = 1
    $ trust["lumi"] = 0
    mc "실제 수치 변화만 확인합니다."
    jump qa_feedback_hold

label qa_feedback_saved_name:
    $ story_begin_chapter(1, "기존 이름 저장 검증")
    $ story_scene("campus", mode="normal", cast=["roman"])
    $ player_name = "하루"
    $ affection["roman"] = 35
    $ trust["roman"] = 20
    $ story_apply("qa_feedback_saved", affection={"roman":2}, trust={"roman":1})
    mc "기존에 직접 고른 이름과 관계 수치를 저장합니다."
    jump qa_feedback_hold

label qa_feedback_hold:
    mc "관계 알림의 저장과 만료를 확인합니다."
    jump qa_feedback_hold
