# Native test fixture. Execute only from tests/omu_cg_20261107, with isolated saves.
init python in omu_cg_qa:
    import os

    def capture_dissolve():
        if renpy.store.cg_current != "ch04_private_omu_smile":
            return
        transition = renpy.game.interface.instantiated_transition.get("ld_cg")
        if isinstance(transition, renpy.display.transition.Dissolve):
            renpy._omu_cg_dissolve = transition.time

    if os.path.normcase(os.path.abspath(renpy.config.basedir)) == os.path.normcase(
            os.path.abspath("D:/CampusRomance_VN/tests/omu_cg_20261107/renpy_project")):
        renpy.config.periodic_callbacks.append(capture_dissolve)

    def assert_rewards(branch):
        s = renpy.store
        assert s.affection["omu"] == (10 if branch == "b" else 0)
        assert s.trust["omu"] == (10 if branch == "a" else 0)
        assert s.ch04_omu_exhibition_idea == (branch == "c")
        for other in s.HEROINE_ORDER:
            if other != "omu":
                assert s.affection[other] == 0 and s.trust[other] == 0
        for choice in ("a", "b", "c"):
            assert s.choice_log.count("ch04_sc06_omu_" + choice) == (1 if choice == branch else 0)


testsuite omu_cg:
    setup:
        python:
            import os
            expected = "D:/CampusRomance_VN/tests/omu_cg_20261107/renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(expected))
            sd_independent_isolation_test.assert_locations()
        $ _test.timeout = 90.0
        $ _test.transition_timeout = 0.60
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/omu_cg_20261107/screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 2
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
        pause 0.1
        $ sd_independent_isolation_test.assert_locations()
        $ persistent.cg_seen = set()
        $ persistent.cg_sd_seen = set()
        $ persistent.gallery = set()
        $ persistent.profile_secrets = set()
        $ renpy._omu_cg_dissolve = None
    teardown:
        exit

    testcase all_menu_branches_switch_before_first_reply:
        parameter (branch, answer, first_reply) = [
            ("a", "완성된 모습만큼 과정도 중요하겠네요.", "어. 내가 하고 싶었던 말이 그거다."),
            ("b", "사진을 좋아하시는 이유를 조금 알 것 같아요.", "……그라나?"),
            ("c", "그럼 두 사진 다 넣을 방법을 찾아볼까요?", "오, 그거 괜찮네.")]
        run Start("qa_omu_private_cg")
        advance until eval _last_say_what == "오므는 노트북으로 사진을 정리하고 있었다." timeout 80
        assert eval not cg_is_active() and story_cast == ["omu"]
        advance until eval _last_say_what == "네. 제가 너무 쉽게 말한 것 같아서요." timeout 80
        assert eval not cg_is_active() and story_cast == ["omu"]
        advance until eval _last_say_what == "뭐, 그럴 수도 있지." timeout 80
        assert eval cg_current == "ch04_private_omu" and cg_asset(cg_current) == "images/cg/ch04_private_omu.png"
        assert eval renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
        advance until screen "choice" timeout 80
        assert eval cg_current == "ch04_private_omu"
        assert eval cg_gallery_variants("ch04_private_omu", unlocked_only=True) == ["ch04_private_omu"]
        assert eval not cg_seen("ch04_private_omu_smile")
        if eval branch == "a":
            screenshot "omu_first_at_menu.png"
        click expression answer
        assert eval _last_say_what == first_reply
        pause 0.4
        assert eval cg_current == "ch04_private_omu_smile" and cg_asset(cg_current) == CG_REGISTRY[cg_current]["image"]
        assert eval renpy._omu_cg_dissolve == 0.38
        assert eval renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
        assert eval cg_gallery_variants("ch04_private_omu", unlocked_only=True) == ["ch04_private_omu", "ch04_private_omu_smile"]
        if eval branch == "a":
            screenshot "omu_smile_first_reply.png"
        if eval branch == "b":
            run FileSave("omu-expression", page="17", confirm=False)
            assert eval renpy.can_load("17-omu-expression")
            advance until eval _last_say_what == "우리는 사진을 다시 정리했다." timeout 80
            $ omu_cg_qa.assert_rewards(branch)
            run FileLoad("omu-expression", page="17", confirm=False)
            pause until eval _last_say_what == first_reply timeout 80
            assert eval cg_current == "ch04_private_omu_smile" and renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
            assert eval affection["omu"] == 0 and trust["omu"] == 0 and not choice_log
            screenshot "omu_smile_after_load.png"
        advance until eval _last_say_what == "우리는 사진을 다시 정리했다." timeout 80
        assert eval cg_current == "ch04_private_omu_smile"
        $ omu_cg_qa.assert_rewards(branch)
        advance until eval _last_say_what == "그런데 아까보다 조금 기분이 좋아 보였다." timeout 80
        assert eval cg_current == "ch04_private_omu_smile"
        advance until eval _last_say_what == "각자의 작업을 마치고 다시 동아리실에 모였다." timeout 80
        assert eval not cg_is_active() and renpy.get_screen("ld_cg_view", layer="ld_cg") is None
        assert eval ch04_personal_promise["omu"] and secret_note_ready("omu", 2)
        $ omu_cg_qa.assert_rewards(branch)

    testcase gallery_one_tile_and_seen_expression_gate:
        $ _preferences.transitions = 0
        $ persistent.cg_seen = {"ch04_private_omu"}
        click "갤러리"
        click "OMU"
        assert eval cg_gallery_keys("OMU").count("ch04_private_omu") == 1 and "ch04_private_omu_smile" not in cg_gallery_keys("OMU")
        assert eval renpy.get_widget("gallery", "cg_tile_ch04_private_omu") is not None and renpy.get_widget("gallery", "cg_tile_ch04_private_omu_smile") is None
        click id "cg_tile_ch04_private_omu" screen ("gallery",)
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_omu"
        keysym "K_SPACE"
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_omu" and not cg_seen("ch04_private_omu_smile")
        click "닫기"
        $ cg_unlock("ch04_private_omu_smile")
        $ renpy.restart_interaction()
        click id "cg_tile_ch04_private_omu" screen ("gallery",)
        click id "cg_cycle_variant" screen ("cg_view",)
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ch04_private_omu" and renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_omu_smile"
        screenshot "omu_gallery_second_expression.png"
        keysym "K_SPACE"
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_omu"
        assert eval persistent.cg_seen == {"ch04_private_omu", "ch04_private_omu_smile"} and not cg_is_active()
        click "닫기"
        click "돌아가기"
        assert screen "main_menu"

label qa_omu_private_cg:
    $ story_begin_chapter(4, "오므 개인 LD 검증")
    $ ch04_partner = "omu"
    jump ch04_sc06
