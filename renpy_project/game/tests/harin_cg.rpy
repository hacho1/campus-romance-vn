# Native regression for the supplied CH04 Harin LD pair. Isolated fixture only.
init python in harin_cg_qa:
    import os

    def capture_dissolve():
        if renpy.store.cg_current != "ch04_private_lumi_shy":
            return
        transition = renpy.game.interface.instantiated_transition.get("ld_cg")
        if isinstance(transition, renpy.display.transition.Dissolve):
            renpy._harin_cg_dissolve = transition.time

    if os.path.normcase(os.path.abspath(renpy.config.basedir)) == os.path.normcase(
            os.path.abspath("D:/CampusRomance_VN/tests/harin_cg_20261107/renpy_project")):
        renpy.config.periodic_callbacks.append(capture_dissolve)

    def assert_rewards():
        s = renpy.store
        assert s.affection["lumi"] == 0 and s.trust["lumi"] == 10
        assert not s.ch04_harin_special_emotion
        for other in s.HEROINE_ORDER:
            if other != "lumi":
                assert s.affection[other] == 0 and s.trust[other] == 0
        assert s.choice_log == ["ch04_sc06_lumi_b"]


testsuite harin_cg:
    setup:
        python:
            import os
            expected = "D:/CampusRomance_VN/tests/harin_cg_20261107/renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(expected))
            sd_independent_isolation_test.assert_locations()
        $ _test.timeout = 90.0
        $ _test.transition_timeout = 0.60
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/harin_cg_20261107/screenshots"
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
        $ renpy._harin_cg_dissolve = None
    teardown:
        exit

    testcase exact_line_transition_save_and_scene_end:
        run Start("qa_harin_private_cg")
        advance until eval _last_say_what == "하린은 모형 앞에 앉아 있었다." timeout 80
        assert eval not cg_is_active() and story_cast == ["lumi"]
        advance until eval _last_say_what == "……아." timeout 80
        assert eval not cg_is_active() and story_cast == ["lumi"]
        advance until eval _last_say_what == "그거요?" timeout 80
        assert eval cg_current == "ch04_private_lumi" and cg_asset(cg_current) == "images/cg/ch04_private_lumi.png"
        assert eval renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
        screenshot "harin_first_cut.png"
        advance until eval _last_say_what == "하린이 나를 바라봤다." timeout 80
        assert eval cg_current == "ch04_private_lumi" and not cg_seen("ch04_private_lumi_shy")
        assert eval cg_gallery_variants("ch04_private_lumi", unlocked_only=True) == ["ch04_private_lumi"]
        screenshot "harin_before_expression_change.png"
        advance until eval _last_say_what == "……당신은 참." timeout 80
        pause 0.4
        assert eval cg_current == "ch04_private_lumi_shy" and cg_asset(cg_current) == CG_REGISTRY[cg_current]["image"]
        assert eval renpy._harin_cg_dissolve == 0.38
        assert eval renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
        assert eval cg_gallery_variants("ch04_private_lumi", unlocked_only=True) == ["ch04_private_lumi", "ch04_private_lumi_shy"]
        screenshot "harin_shy_exact_line.png"
        run FileSave("harin-expression", page="18", confirm=False)
        assert eval renpy.can_load("18-harin-expression")
        advance until screen "choice" timeout 80
        assert eval cg_current == "ch04_private_lumi_shy"
        run FileLoad("harin-expression", page="18", confirm=False)
        pause until eval _last_say_what == "……당신은 참." timeout 80
        assert eval cg_current == "ch04_private_lumi_shy" and renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
        assert eval affection["lumi"] == 0 and trust["lumi"] == 0 and not choice_log
        screenshot "harin_shy_after_load.png"
        advance until screen "choice" timeout 80
        assert eval cg_current == "ch04_private_lumi_shy"
        click "다 고치실 때까지 옆에 있을게요."
        advance until eval _last_say_what == "잠시 뒤 작은 벽을 다시 붙였다." timeout 80
        assert eval cg_current == "ch04_private_lumi_shy"
        $ harin_cg_qa.assert_rewards()
        advance until eval _last_say_what == "그런데 오늘은 그 이유를 조금 알 것 같았다." timeout 80
        assert eval cg_current == "ch04_private_lumi_shy"
        advance until eval _last_say_what == "각자의 작업을 마치고 다시 동아리실에 모였다." timeout 80
        assert eval not cg_is_active() and renpy.get_screen("ld_cg_view", layer="ld_cg") is None
        assert eval ch04_personal_promise["lumi"] and secret_note_ready("lumi", 2)
        $ harin_cg_qa.assert_rewards()

    testcase gallery_single_scene_with_two_collected_expressions:
        $ _preferences.transitions = 0
        $ persistent.cg_seen = {"ch04_private_lumi"}
        click "갤러리"
        click "HARIN"
        assert eval cg_gallery_keys("HARIN").count("ch04_private_lumi") == 1 and "ch04_private_lumi_shy" not in cg_gallery_keys("HARIN")
        assert eval renpy.get_widget("gallery", "cg_tile_ch04_private_lumi") is not None and renpy.get_widget("gallery", "cg_tile_ch04_private_lumi_shy") is None
        click id "cg_tile_ch04_private_lumi" screen ("gallery",)
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_lumi"
        keysym "K_SPACE"
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_lumi" and not cg_seen("ch04_private_lumi_shy")
        click "닫기"
        $ cg_unlock("ch04_private_lumi_shy")
        $ renpy.restart_interaction()
        click id "cg_tile_ch04_private_lumi" screen ("gallery",)
        click id "cg_cycle_variant" screen ("cg_view",)
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ch04_private_lumi" and renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_lumi_shy"
        screenshot "harin_gallery_second_expression.png"
        keysym "K_SPACE"
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_lumi"
        assert eval persistent.cg_seen == {"ch04_private_lumi", "ch04_private_lumi_shy"} and not cg_is_active()
        click "닫기"
        click "돌아가기"
        assert screen "main_menu"

label qa_harin_private_cg:
    $ story_begin_chapter(4, "하린 개인 LD 검증")
    $ ch04_partner = "lumi"
    jump ch04_sc06
