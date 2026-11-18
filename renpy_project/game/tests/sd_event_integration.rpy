# Native Ren'Py 8.5.3 integration checks for whole-event SD illustration cuts.
# Test labels, synthetic solid-color images and registry overrides are excluded
# from builds by options.rpy's game/tests/** rule. No source JSON is changed.

init python:
    if not renpy.has_image(("roman", "smile"), exact=True):
        renpy.image("roman smile", Null(32, 32))

init python in sd_event_test:
    import copy

    EVENTS = (
        "ch01_sia_omu_argument", "ch01_drink_incident", "ch01_group_meeting", "ch01_plan_problem",
        "ch02_rival_introduction", "ch02_interview_flashback", "ch02_ski_accident", "ch02_rival_after_presentation",
        "ch03_rival_comedy", "ch03_trial_confusion", "ch03_sia_force_quit_reaction", "ch03_joint_cooperation",
    )
    OPTIONAL_EVENTS = ("ch02_whiteboard_huddle", "ch02_presentation_release", "ch03_rival_booth_open", "ch03_trial_huddle", "ch03_rest_break")
    TWO_CUT_EVENTS = ("ch01_plan_problem", "ch02_interview_flashback", "ch02_rival_after_presentation")
    VARIANTS = tuple((event_id, variant) for event_id in EVENTS
        for variant in (("01", "02") if event_id in TWO_CUT_EVENTS else ("01", "02", "03")))
    PNG = "tests/sd_assets/cut_a.png"
    WEBP = "tests/sd_assets/cut_b.webp"

    def source_registry():
        return renpy.store.read_data("sd_events")["events"]

    def restore_registry():
        # A fresh source copy also avoids mutating the dictionary held by init.
        renpy.store.SD_EVENT_REGISTRY = copy.deepcopy(source_registry())

    def missing_override(event_id, variant):
        registry = copy.deepcopy(source_registry())
        registry[event_id]["variants"][variant]["image"] = "tests/sd_assets/missing/{}_{}.webp".format(event_id, variant)
        renpy.store.SD_EVENT_REGISTRY = registry

    def fixture_override():
        registry = copy.deepcopy(source_registry())
        variants = registry["ch01_sia_omu_argument"]["variants"]
        variants["01"]["image"] = PNG
        variants["02"]["image"] = WEBP
        variants["03"]["image"] = "tests/sd_assets/cut_a.webp"
        variants["04"] = {"image":"tests/sd_assets/cut_b.png", "description":"확장자 대체 검색 검증"}
        renpy.store.SD_EVENT_REGISTRY = registry

    def screen():
        return renpy.get_screen("sd_event_view", layer="sd_events")

    def rendered_files():
        displayable = screen()
        assert displayable is not None
        found = []
        def observe(child):
            filename = getattr(child, "filename", None)
            if isinstance(filename, str):
                found.append(filename.replace("\\", "/"))
        displayable.visit_all(observe)
        return found

    def assert_cut(event_id, variant, expected_asset=None):
        s = renpy.store
        assert s.sd_event_current == event_id and s.sd_event_variant_id == variant
        assert s.story_mode == "sd_event" and list(s.story_cast) == []
        assert not s.story_effects and not s.story_chat_active
        assert s.sd_event_schema == 1
        displayed = screen()
        assert displayed is not None
        assert renpy.get_screen("sd_event_view", layer="screens") is None
        cut = displayed.scope["cut"]
        assert cut["id"] == event_id and cut["variant"] == variant
        assert cut["asset"] == expected_asset, cut
        assert cut["title"] and cut["description"] and cut["layout"] and cut["expected"]
        if expected_asset:
            assert renpy.loadable(expected_asset)
            images = [path for path in rendered_files() if path in (PNG, WEBP) or path.startswith("images/sd_events/")]
            assert images == [expected_asset], images
        assert not s.eligible_routes() and not s.persistent.endings and not s.meta_unlocked()

    def normal_snapshot():
        s = renpy.store
        return (s.story_mode, tuple(s.story_cast), dict(s.story_faces), dict(s.story_positions), dict(s.story_facing))

    def assert_normal():
        s = renpy.store
        assert s.sd_event_current is None and not s.sd_event_is_active()
        assert screen() is None
        assert s.story_mode == "normal" and list(s.story_cast) == ["roman", "sia"]
        assert s.story_faces["roman"] == "happy" and s.story_faces["sia"] == "angry"
        assert s.story_positions["roman"] == (610, 790) and s.story_positions["sia"] == (1310, 790)
        assert s.story_facing["roman"] == -1 and s.story_facing["sia"] == 1

    def placement_snapshot(transform):
        # Ren'Py 8.5.3 get_placement returns an attribute object, not a tuple.
        placement = renpy.get_placement(transform)
        return (placement.xpos, placement.ypos, placement.xanchor, placement.yanchor,
            placement.xoffset, placement.yoffset, placement.subpixel)

    def master_snapshot():
        tags = tuple(sorted(renpy.get_showing_tags(layer="master")))
        if "roman" not in tags:
            return (tags, None, None, ())
        transforms = renpy.get_at_list("roman", layer="master") or []
        return (tags, tuple(renpy.get_attributes("roman", layer="master") or ()),
            renpy.get_image_bounds("roman", layer="master"),
            tuple(placement_snapshot(transform) for transform in transforms))

    def hidden_master_snapshot():
        # Compare semantic tag/attribute/placement data, not loaded transform identities.
        return tuple((tag, tuple(attributes), tuple(placement_snapshot(transform) for transform in transforms))
            for tag, attributes, transforms in renpy.store.sd_event_hidden_master)

    def snapshot():
        s = renpy.store
        fields = ("player_name", "story_mode", "story_active", "story_stage_visible", "story_background",
            "story_chapter_number", "sd_event_current", "sd_event_variant_id", "sd_event_dissolve",
            "sd_event_previous_mode", "sd_event_schema", "team_preparation", "rival_cooperation")
        result = {name:getattr(s, name) for name in fields}
        for name in ("story_faces", "story_positions", "story_facing", "story_effects", "sd_event_previous_faces",
                "sd_event_previous_positions", "sd_event_previous_facing", "affection", "trust"):
            result[name] = dict(getattr(s, name))
        result["story_cast"] = list(s.story_cast)
        result["sd_event_previous_cast"] = list(s.sd_event_previous_cast)
        result["event_flags"] = set(s.event_flags)
        result["choice_log"] = list(s.choice_log)
        result["sd_event_hidden_master"] = hidden_master_snapshot()
        result["master_images"] = master_snapshot()
        return result

    def assert_saved():
        expected = renpy._campus_sd_event_expected
        actual = snapshot()
        differences = {key:(expected.get(key), actual.get(key)) for key in set(expected) | set(actual)
            if expected.get(key) != actual.get(key)}
        assert not differences, ("SD-event save differs (expected, actual)", differences)

    def unlock_snapshot():
        p = renpy.store.persistent
        return tuple(set(getattr(p, name)) for name in ("endings", "gallery", "profile_secrets", "chapter_completions", "choice_memories"))


testsuite sd_events:
    setup:
        python:
            import os
            assert os.environ.get("CAMPUS_SAVE_DIR"), "Set CAMPUS_SAVE_DIR to a dedicated test directory."
            assert os.path.normcase(os.path.abspath(config.savedir)) == os.path.normcase(os.path.abspath(os.environ["CAMPUS_SAVE_DIR"]))
            assert os.path.normcase(os.path.abspath(config.savedir)) != os.path.normcase(os.path.join(config.basedir, "saves"))
            assert set(SD_EVENT_REGISTRY) == set(sd_event_test.EVENTS + sd_event_test.OPTIONAL_EVENTS)
            assert sum(len(event["variants"]) for event in SD_EVENT_REGISTRY.values()) == 33 + len(sd_event_test.OPTIONAL_EVENTS)
            assert all(SD_EVENT_REGISTRY[event]["requires_art"] and set(SD_EVENT_REGISTRY[event]["variants"]) == {"01"} for event in sd_event_test.OPTIONAL_EVENTS)
            assert len(sd_event_test.VARIANTS) == 33
        $ _test.timeout = 30.0
        $ _test.transition_timeout = 0.5
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/sd-event-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        $ sd_event_test.restore_registry()
        $ renpy._campus_sd_unlocks_before = sd_event_test.unlock_snapshot()
    after testcase:
        $ sd_event_test.restore_registry()
        assert eval sd_event_test.unlock_snapshot() == renpy._campus_sd_unlocks_before
    teardown:
        $ sd_event_test.restore_registry()
        exit

    testcase every_missing_cut:
        parameter (event_id, variant) = [('ch01_sia_omu_argument', '01'), ('ch01_sia_omu_argument', '02'), ('ch01_sia_omu_argument', '03'), ('ch01_drink_incident', '01'), ('ch01_drink_incident', '02'), ('ch01_drink_incident', '03'), ('ch01_group_meeting', '01'), ('ch01_group_meeting', '02'), ('ch01_group_meeting', '03'), ('ch01_plan_problem', '01'), ('ch01_plan_problem', '02'), ('ch02_rival_introduction', '01'), ('ch02_rival_introduction', '02'), ('ch02_rival_introduction', '03'), ('ch02_interview_flashback', '01'), ('ch02_interview_flashback', '02'), ('ch02_ski_accident', '01'), ('ch02_ski_accident', '02'), ('ch02_ski_accident', '03'), ('ch02_rival_after_presentation', '01'), ('ch02_rival_after_presentation', '02'), ('ch03_rival_comedy', '01'), ('ch03_rival_comedy', '02'), ('ch03_rival_comedy', '03'), ('ch03_trial_confusion', '01'), ('ch03_trial_confusion', '02'), ('ch03_trial_confusion', '03'), ('ch03_sia_force_quit_reaction', '01'), ('ch03_sia_force_quit_reaction', '02'), ('ch03_sia_force_quit_reaction', '03'), ('ch03_joint_cooperation', '01'), ('ch03_joint_cooperation', '02'), ('ch03_joint_cooperation', '03')]
        run Start("qa_sd_event_plain")
        pause until screen "say"
        python:
            sd_event_test.missing_override(event_id, variant)
            sd_event_start(event_id, variant, transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_cut(event_id, variant)
        assert eval sd_event_test.screen().scope["cut"]["cast_text"]
        assert eval sd_event_test.screen().scope["cut"]["scene"]
        assert eval sd_event_test.screen().scope["cut"]["expected"] == "tests/sd_assets/missing/{}_{}.webp".format(event_id, variant)
        screenshot f"missing_{event_id}_{variant}.png"
        python:
            sd_event_end(transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_normal()

    testcase normal_event_variant_normal:
        run Start("qa_sd_event_plain")
        pause until screen "say"
        $ renpy._campus_sd_normal_before = sd_event_test.normal_snapshot()
        python:
            sd_event_start("ch02_rival_introduction", "01", transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_cut("ch02_rival_introduction", "01", sd_event_info()["asset"])
        python:
            sd_event_change("02", transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_cut("ch02_rival_introduction", "02", sd_event_info()["asset"])
        # Replacing the entire event while active must preserve the original
        # normal-stage return target, including expressions and saved poses.
        python:
            sd_event_start("ch03_joint_cooperation", "03", transition=0)
            renpy.restart_interaction()
        pause 0.1
        assert eval sd_event_current == "ch03_joint_cooperation" and story_cast == []
        python:
            sd_event_end(transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_normal()
        assert eval sd_event_test.normal_snapshot() == renpy._campus_sd_normal_before
        screenshot "normal_return.png"

    testcase png_webp_and_single_whole_image:
        run Start("qa_sd_event_asset_fixture")
        pause until screen "say"
        assert eval renpy.loadable(sd_event_test.PNG) and renpy.loadable(sd_event_test.WEBP)
        assert eval "roman" in renpy.get_showing_tags(layer="master")
        $ renpy._campus_sd_master_before = sd_event_test.master_snapshot()
        python:
            sd_event_test.fixture_override()
            sd_event_start("ch01_sia_omu_argument", "01", transition=0)
            renpy.restart_interaction()
        pause 0.1
        assert eval "roman" not in renpy.get_showing_tags(layer="master")
        assert eval [(tag, tuple(attributes)) for tag, attributes, transforms in sd_event_hidden_master] == [("roman", ("smile",))]
        $ sd_event_test.assert_cut("ch01_sia_omu_argument", "01", sd_event_test.PNG)
        screenshot "fixture_png.png"
        $ _preferences.transitions = 2
        python:
            sd_event_change("02", transition=0.08)
            renpy.restart_interaction()
        pause 0.2
        $ sd_event_test.assert_cut("ch01_sia_omu_argument", "02", sd_event_test.WEBP)
        screenshot "fixture_webp_after_dissolve.png"
        python:
            sd_event_change("03", transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_cut("ch01_sia_omu_argument", "03", sd_event_test.PNG)
        assert eval sd_event_info()["expected"].endswith("cut_a.webp")
        python:
            sd_event_change("04", transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_cut("ch01_sia_omu_argument", "04", sd_event_test.WEBP)
        assert eval sd_event_info()["expected"].endswith("cut_b.png")
        python:
            sd_event_end(transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_normal()
        assert eval sd_event_test.master_snapshot() == renpy._campus_sd_master_before
        assert eval sd_event_hidden_master == []
        $ _preferences.transitions = 0

    testcase save_before_during_after:
        parameter phase = ["before", "during", "after"]
        # All saved initialization runs in native statements before this say
        # checkpoint; test-local changes alone do not create Ren'Py save state.
        run Start("qa_sd_event_save_" + phase)
        pause until screen "say"
        $ renpy._campus_sd_event_expected = sd_event_test.snapshot()
        assert eval sd_event_is_active() == (phase == "during")
        screenshot f"save_{phase}_before.png"
        click "저장"
        assert screen "save"
        run FilePage("8")
        run FileSave("1", confirm=False)
        assert eval renpy.can_load("8-1")
        click "돌아가기"
        python:
            sd_event_end(transition=0)
            sd_event_start("ch03_joint_cooperation", "03", transition=0)
            renpy.store.sd_event_dissolve = 0.99
            renpy.store.sd_event_previous_cast = ["lumi"]
            renpy.store.sd_event_previous_faces = {"lumi":"sad"}
            renpy.store.sd_event_previous_positions = {"lumi":(10,10)}
            renpy.store.sd_event_previous_facing = {"lumi":1}
            renpy.store.sd_event_hidden_master = []
            affection["sia"] = 99
            trust["roman"] = 99
            renpy.store.team_preparation = 99
            event_flags.add("qa_unsaved_sd_change")
            choice_log.append("qa_unsaved_sd_change")
            renpy.restart_interaction()
        click "불러오기"
        assert screen "load"
        run FilePage("8")
        run FileLoad("1", confirm=False)
        pause until screen "say"
        $ sd_event_test.assert_saved()
        assert eval sd_event_is_active() == (phase == "during")
        if eval phase == "during":
            assert eval sd_event_current == "ch02_rival_introduction" and sd_event_variant_id == "02"
            assert eval sd_event_test.screen() is not None and story_mode == "sd_event" and story_cast == []
            assert eval "roman" not in renpy.get_showing_tags(layer="master")
        else:
            $ sd_event_test.assert_normal()
        screenshot f"save_{phase}_restored.png"
        python:
            sd_event_end(transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_normal()
        assert eval "roman" in renpy.get_showing_tags(layer="master") and renpy.get_attributes("roman", layer="master") == ("smile",)
        assert eval not eligible_routes() and not persistent.endings and not meta_unlocked()

    testcase dissolve_setting:
        run Start("qa_sd_event_plain")
        pause until screen "say"
        $ _preferences.transitions = 2
        run SetVariable("sd_event_dissolve", 0.08)
        python:
            sd_event_start("ch01_group_meeting", "01")
            renpy.restart_interaction()
        pause 0.2
        assert eval sd_event_dissolve == 0.08 and sd_event_current == "ch01_group_meeting"
        run SetVariable("sd_event_dissolve", 0.0)
        python:
            sd_event_change("02")
            renpy.restart_interaction()
        pause 0.1
        assert eval sd_event_dissolve == 0.0 and sd_event_variant_id == "02"
        # The global transition preference can suppress a nonzero cut dissolve.
        $ _preferences.transitions = 0
        run SetVariable("sd_event_dissolve", 0.7)
        python:
            sd_event_change("03")
            renpy.restart_interaction()
        pause 0.1
        assert eval sd_event_dissolve == 0.7 and sd_event_variant_id == "03"
        screenshot "dissolve_setting_disabled.png"
        python:
            sd_event_end(transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_normal()

    testcase unknown_id_variant_and_inactive_calls:
        run Start("qa_sd_event_plain")
        pause until screen "say"
        python:
            sd_event_change("99", transition=0)
            sd_event_end(transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_normal()
        python:
            sd_event_start("qa_unregistered_event", "99", transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_cut("qa_unregistered_event", "99")
        assert eval sd_event_info()["title"] == "등록 정보가 필요한 SD 이벤트"
        screenshot "unknown_event_metadata.png"
        python:
            sd_event_end(transition=0)
            sd_event_start("ch01_group_meeting", "99", transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_cut("ch01_group_meeting", "99")
        assert eval sd_event_info()["title"] == SD_EVENT_REGISTRY["ch01_group_meeting"]["title"]
        assert eval "qa_unregistered_event" not in SD_EVENT_REGISTRY and len(SD_EVENT_REGISTRY) == len(sd_event_test.EVENTS + sd_event_test.OPTIONAL_EVENTS)
        screenshot "unknown_variant_metadata.png"
        python:
            sd_event_end(transition=0)
            renpy.restart_interaction()
        pause 0.1
        $ sd_event_test.assert_normal()


# Native fixtures keep save-freeze points separate from test executor locals.
label qa_sd_event_plain:
    call qa_sd_event_normal_initialize
    jump qa_sd_event_checkpoint

label qa_sd_event_asset_fixture:
    call qa_sd_event_normal_initialize
    show roman smile at left
    jump qa_sd_event_checkpoint

label qa_sd_event_save_before:
    $ _qa_sd_event_phase = "before"
    jump qa_sd_event_save_initialize

label qa_sd_event_save_during:
    $ _qa_sd_event_phase = "during"
    jump qa_sd_event_save_initialize

label qa_sd_event_save_after:
    $ _qa_sd_event_phase = "after"
    jump qa_sd_event_save_initialize

label qa_sd_event_save_initialize:
    call qa_sd_event_normal_initialize
    show roman smile at left
    $ sd_event_dissolve = 0.31
    $ affection["sia"] = 6
    $ trust["roman"] = 4
    $ team_preparation = 2
    $ story_flag("rival_cooperation", True)
    $ choice_log.append("qa_sd_saved_checkpoint")
    if _qa_sd_event_phase != "before":
        $ sd_event_start("ch02_rival_introduction", "02", transition=0)
    if _qa_sd_event_phase == "after":
        $ sd_event_end(transition=0)
    jump qa_sd_event_checkpoint

label qa_sd_event_normal_initialize:
    $ story_begin_chapter(2, "SD 이벤트 통합 검증")
    $ player_name = "SD검증"
    $ story_scene("prep_room", mode="normal", cast=["roman", "sia"], location="SD 이벤트 검증")
    $ story_stage(faces={"roman":"happy", "sia":"angry"}, positions={"roman":(610,790), "sia":(1310,790)}, facing={"roman":-1, "sia":1})
    return

label qa_sd_event_checkpoint:
    mc "장면 전체를 한 컷으로 보여 주고, 원래 무대로 돌아갈 수 있는지 확인합니다."
    jump qa_sd_event_checkpoint
