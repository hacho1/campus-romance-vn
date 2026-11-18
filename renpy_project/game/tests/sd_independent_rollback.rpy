# Independent native checkpoints for SD cut rollback. Test-only, excluded from builds.
init python in sd_independent_rollback_test:
    def assert_normal():
        s = renpy.store
        assert s.sd_event_current is None
        assert s.story_mode == "normal" and list(s.story_cast) == ["roman"]
        assert s.story_faces["roman"] == "happy"
        assert s.story_positions["roman"] == (960, 790)
        assert s.story_facing["roman"] == -1.0
        assert renpy.get_screen("sd_event_view", layer="sd_events") is None

    def assert_cut(variant):
        s = renpy.store
        assert s.sd_event_current == "ch02_rival_introduction"
        assert s.sd_event_variant_id == variant
        assert s.story_mode == "sd_event" and not s.story_cast and not s.story_effects
        displayed = renpy.get_screen("sd_event_view", layer="sd_events")
        assert displayed is not None
        assert displayed.scope["cut"]["id"] == "ch02_rival_introduction"
        assert displayed.scope["cut"]["variant"] == variant
        filenames = []
        def observe(child):
            filename = getattr(child, "filename", None)
            if isinstance(filename, str):
                filenames.append(filename.replace("\\", "/"))
        displayed.visit_all(observe)
        assert not any(path.startswith("images/sd/") for path in filenames), filenames

    def say_text():
        displayed = renpy.get_screen("say")
        return str(displayed.scope["what"]) if displayed else ""


testsuite sd_independent_rollback:
    setup:
        python:
            import os
            expected = os.path.normcase(os.path.abspath("D:/CampusRomance_VN/tests/saves-independent-sd-rollback"))
            assert os.path.normcase(os.path.abspath(config.savedir)) == expected
        $ _test.timeout = 30.0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/sd-independent-rollback-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
    teardown:
        exit

    testcase native_checkpoints_round_trip:
        run Start("qa_sd_independent_rollback_checkpoints")
        advance until "일반 시작 체크포인트입니다." timeout 30
        $ sd_independent_rollback_test.assert_normal()
        advance until "첫 번째 SD 컷 체크포인트입니다." timeout 30
        $ sd_independent_rollback_test.assert_cut("01")
        advance until "두 번째 SD 컷 체크포인트입니다." timeout 30
        $ sd_independent_rollback_test.assert_cut("02")
        advance until "일반 복귀 체크포인트입니다." timeout 30
        $ sd_independent_rollback_test.assert_normal()
        screenshot "normal_before_rollback.png"

        run Rollback(force=True, checkpoints=1)
        pause 0.2
        assert eval sd_independent_rollback_test.say_text() == "두 번째 SD 컷 체크포인트입니다."
        $ sd_independent_rollback_test.assert_cut("02")
        screenshot "rollback_cut_02.png"

        run Rollback(force=True, checkpoints=1)
        pause 0.2
        assert eval sd_independent_rollback_test.say_text() == "첫 번째 SD 컷 체크포인트입니다."
        $ sd_independent_rollback_test.assert_cut("01")
        screenshot "rollback_cut_01.png"

        run Rollback(force=True, checkpoints=1)
        pause 0.2
        assert eval sd_independent_rollback_test.say_text() == "일반 시작 체크포인트입니다."
        $ sd_independent_rollback_test.assert_normal()
        screenshot "rollback_normal_start.png"

        advance until "두 번째 SD 컷 체크포인트입니다." timeout 30
        $ sd_independent_rollback_test.assert_cut("02")
        advance until "일반 복귀 체크포인트입니다." timeout 30
        $ sd_independent_rollback_test.assert_normal()
        screenshot "normal_after_replay.png"

label qa_sd_independent_rollback_checkpoints:
    $ story_begin_chapter(2, "독립 SD 롤백 검증")
    $ story_scene("prep_room", mode="normal", cast=["roman"], location="독립 SD 롤백 검증")
    $ story_stage(faces={"roman":"happy"}, positions={"roman":(960,790)}, facing={"roman":-1})
    roman "일반 시작 체크포인트입니다."
    $ sd_event_start("ch02_rival_introduction", "01", transition=0)
    ski "첫 번째 SD 컷 체크포인트입니다."
    $ sd_event_change("02", transition=0)
    sia "두 번째 SD 컷 체크포인트입니다."
    $ sd_event_end(mode="normal", cast=["roman"], transition=0)
    roman "일반 복귀 체크포인트입니다."
    jump qa_sd_independent_rollback_hold

label qa_sd_independent_rollback_hold:
    roman "롤백 검증이 끝날 때까지 대기합니다."
    jump qa_sd_independent_rollback_hold