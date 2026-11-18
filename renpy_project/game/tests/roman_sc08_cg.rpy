# Native CH04 SC08-A CG regression. Run only in the isolated fixture below.
init python in roman_sc08_cg_qa:
    import os

    def capture_dissolve():
        if renpy.store.cg_current != "ch04_evening_roman":
            return
        transition = renpy.game.interface.instantiated_transition.get("ld_cg")
        if isinstance(transition, renpy.display.transition.Dissolve):
            renpy._roman_sc08_cg_dissolve = transition.time

    if os.path.normcase(os.path.abspath(renpy.config.basedir)) == os.path.normcase(
            os.path.abspath("D:/CampusRomance_VN/tests/roman_sc08_cg_20261107/renpy_project")):
        renpy.config.periodic_callbacks.append(capture_dissolve)

    def assert_no_rewards_added():
        s = renpy.store
        assert not s.choice_log
        for hero in s.HEROINE_ORDER:
            assert s.affection[hero] == 0 and s.trust[hero] == 0


testsuite roman_sc08_cg:
    setup:
        python:
            import os
            expected = "D:/CampusRomance_VN/tests/roman_sc08_cg_20261107/renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(expected))
            sd_independent_isolation_test.assert_locations()
        $ _test.timeout = 90.0
        $ _test.transition_timeout = 0.60
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/roman_sc08_cg_20261107/screenshots"
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
        $ renpy._roman_sc08_cg_dissolve = None
    teardown:
        exit

    testcase standing_then_cg_save_load_and_shared_exit:
        run Start("qa_roman_sc08_private_cg")
        advance until eval _last_say_what == "[player_name] 씨……!" timeout 80
        assert eval not cg_is_active() and story_cast == ["roman"] and story_stage_visible
        assert eval not cg_seen("ch04_evening_roman") and renpy.get_screen("ld_cg_view", layer="ld_cg") is None
        screenshot "roman_calling_standing.png"
        advance until eval _last_say_what == "로만 씨? 아직 안 가셨어요?" timeout 80
        pause 0.4
        assert eval cg_current == "ch04_evening_roman" and cg_asset(cg_current) == "images/cg/ch04_evening_roman.png"
        assert eval renpy._roman_sc08_cg_dissolve == 0.38
        assert eval renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
        assert eval cg_seen("ch04_evening_roman") and not cg_seen("ch04_private_roman")
        screenshot "roman_sc08_cg_next_mc_line.png"
        run FileSave("roman-sc08", page="19", confirm=False)
        assert eval renpy.can_load("19-roman-sc08")
        advance until eval _last_say_what == "기다려달라는 말이 이상하게 따뜻했다." timeout 80
        assert eval cg_current == "ch04_evening_roman"
        run FileLoad("roman-sc08", page="19", confirm=False)
        pause until eval _last_say_what == "로만 씨? 아직 안 가셨어요?" timeout 80
        assert eval cg_current == "ch04_evening_roman" and renpy.get_widget("ld_cg_view", "ld_cg_asset", layer="ld_cg") is not None
        screenshot "roman_sc08_cg_after_load.png"
        advance until eval _last_say_what == "기다려달라는 말이 이상하게 따뜻했다." timeout 80
        assert eval cg_current == "ch04_evening_roman"
        advance until eval _last_say_what == "돌아가는 길이 조금 짧게 느껴졌다." timeout 80
        assert eval not cg_is_active() and renpy.get_screen("ld_cg_view", layer="ld_cg") is None
        assert eval story_stage_visible and story_mode in ("normal", "emotion")
        screenshot "roman_sc08_shared_exit.png"
        advance until eval _last_say_what == "방으로 돌아왔을 때는 이미 밤이 깊었다." timeout 80
        assert eval not cg_is_active() and renpy.get_screen("ld_cg_view", layer="ld_cg") is None
        assert eval story_background == "room" and story_light == "night" and not story_stage_visible
        assert eval ch04_evening_event == "roman"
        $ roman_sc08_cg_qa.assert_no_rewards_added()

    testcase gallery_own_scene_independent_of_sc06_expressions:
        $ _preferences.transitions = 0
        $ persistent.cg_seen = {"ch04_private_roman", "ch04_private_roman_shy"}
        click "갤러리"
        click "ROMAN"
        assert eval cg_gallery_key("ch04_evening_roman") == "ch04_evening_roman" and cg_gallery_variants("ch04_evening_roman") == ["ch04_evening_roman"]
        assert eval cg_gallery_keys("ROMAN").count("ch04_evening_roman") == 1 and cg_gallery_keys("ROMAN").count("ch04_private_roman") == 1
        assert eval "ch04_evening_roman" not in cg_gallery_variants("ch04_private_roman")
        assert eval not cg_gallery_seen("ch04_evening_roman") and "ch04_evening_roman" not in cg_unlocked_ids(cg_gallery_keys("ROMAN"))
        assert eval renpy.get_widget("gallery", "cg_tile_ch04_evening_roman") is not None and renpy.get_widget("gallery", "cg_thumb_ch04_evening_roman") is None
        $ cg_unlock("ch04_evening_roman")
        $ renpy.restart_interaction()
        assert eval renpy.get_widget("gallery", "cg_thumb_ch04_evening_roman") is not None
        click id "cg_tile_ch04_evening_roman" screen ("gallery",)
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ch04_evening_roman" and renpy.get_screen("cg_view").scope["current_cut"] == "ch04_evening_roman"
        assert eval renpy.get_widget("cg_view", "cg_view_asset") is not None and renpy.get_widget("cg_view", "cg_next_variant") is None
        screenshot "roman_sc08_gallery.png"
        keysym "K_SPACE"
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_evening_roman"
        keysym "K_LEFT"
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ch04_private_roman" and renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_roman"
        keysym "K_SPACE"
        assert eval renpy.get_screen("cg_view").scope["current_cut"] == "ch04_private_roman_shy"
        keysym "K_RIGHT"
        assert eval renpy.get_screen("cg_view").scope["current_cg"] == "ch04_evening_roman" and renpy.get_screen("cg_view").scope["current_cut"] == "ch04_evening_roman"
        assert eval persistent.cg_seen == {"ch04_private_roman", "ch04_private_roman_shy", "ch04_evening_roman"} and not cg_is_active()
        click "닫기"
        click "돌아가기"
        assert screen "main_menu"

label qa_roman_sc08_private_cg:
    $ story_begin_chapter(4, "로만 SC08-A LD 검증")
    $ ch04_partner = "roman"
    jump ch04_sc08
