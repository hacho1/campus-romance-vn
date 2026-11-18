# Test-only save isolation. This file is excluded by options.rpy game/tests/**.
# CAMPUS_SAVE_DIR is an explicit test-run opt-in; ordinary player launches are unchanged.
python early:
    import os as _campus_isolation_os
    import renpy as _campus_isolation_renpy

    _campus_isolation_target = _campus_isolation_os.environ.get("CAMPUS_SAVE_DIR")
    if _campus_isolation_target:
        _campus_isolation_target = _campus_isolation_os.path.abspath(_campus_isolation_target)
        _campus_isolation_renpy.config.savedir = _campus_isolation_target
        _campus_save_module = _campus_isolation_renpy.savelocation
        if not hasattr(_campus_save_module, "_campus_independent_original_init"):
            _campus_save_module._campus_independent_original_init = _campus_save_module.init

        def _campus_independent_isolated_save_init(
                _original=_campus_save_module._campus_independent_original_init,
                _engine=_campus_isolation_renpy,
                _path=_campus_isolation_os.path,
                _target=_campus_isolation_target):
            # Ren'Py initializes locations twice. Both passes must be filtered
            # before persistent merging and save-token upgrades can occur.
            _engine.config.savedir = _target
            _original()
            _wanted = _path.normcase(_path.abspath(_target))
            _locations = _engine.loadsave.location
            _locations.locations = [entry for entry in _locations.locations
                if _path.normcase(_path.abspath(entry.directory)) == _wanted]
            if len(_locations.locations) != 1:
                raise RuntimeError("Test save isolation did not retain exactly one intended save location.")

        _campus_save_module.init = _campus_independent_isolated_save_init

init python in sd_independent_isolation_test:
    def assert_locations():
        import os
        target = os.path.normcase(os.path.abspath(os.environ["CAMPUS_SAVE_DIR"]))
        assert os.path.normcase(os.path.abspath(renpy.config.savedir)) == target
        location = renpy.loadsave.location
        assert location.locations
        assert location.active_locations()
        assert all(os.path.normcase(os.path.abspath(entry.directory)) == target
            for entry in location.locations)
        assert all(os.path.normcase(os.path.abspath(entry.directory)) == target
            for entry in location.active_locations())


testsuite sd_independent_save_isolation:
    setup:
        $ _test.timeout = 30.0
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
    teardown:
        exit

    testcase sentinel_writes_stay_in_test_directory:
        run Start("qa_sd_independent_save_isolation")
        pause until screen "say"
        $ sd_independent_isolation_test.assert_locations()
        $ renpy.save("independent-isolation-sentinel")
        assert eval renpy.can_load("independent-isolation-sentinel")
        $ persistent.campus_independent_isolation_sentinel = "sd-independent-isolation-20261104"
        $ renpy.save_persistent()
        $ sd_independent_isolation_test.assert_locations()
        python:
            import os
            target = os.environ["CAMPUS_SAVE_DIR"]
            assert os.path.isfile(os.path.join(target, "independent-isolation-sentinel" + renpy.savegame_suffix))
            assert os.path.isfile(os.path.join(target, "persistent"))
        assert eval persistent.campus_independent_isolation_sentinel == "sd-independent-isolation-20261104"

label qa_sd_independent_save_isolation:
    $ story_begin_chapter(2, "독립 저장 격리 검증")
    $ story_scene("prep_room", mode="normal", cast=["roman"], location="독립 저장 격리 검증")
    roman "검사용 저장 위치에만 기록하는지 확인합니다."
    jump qa_sd_independent_save_isolation