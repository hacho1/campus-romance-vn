# Observations live on the engine module so FileLoad cannot roll them back.
init python in legacy_sd_test:
    def before_migration():
        s = renpy.store
        renpy._campus_legacy_before_migration = {
            "schema":s.sd_event_schema, "mode":s.story_mode, "cast":list(s.story_cast),
            "first_task_partner":s.first_task_partner, "affection":dict(s.affection), "trust":dict(s.trust),
            "last_read":s.story_read_log[-1] if s.story_read_log else None,
        }

    def observe_label(name, abnormal):
        if name == "qa_old_sd_capture_entry":
            renpy._campus_legacy_entry_visits.append(name)

testsuite legacy_sd_event:
    setup:
        $ config.after_load_callbacks.append(legacy_sd_test.before_migration)
        $ config.label_callbacks.append(legacy_sd_test.observe_label)
        $ _test.timeout = 30.0
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/sd-event-screenshots"
    before testcase:
        $ renpy._campus_legacy_before_migration = None
        $ renpy._campus_legacy_entry_visits = []
    teardown:
        $ config.after_load_callbacks.remove(legacy_sd_test.before_migration)
        $ config.label_callbacks.remove(legacy_sd_test.observe_label)
        exit
    testcase load_real_old_sd_save:
        run Function(renpy.load, "legacy_sd_mid")
        pause until screen "say"
        assert eval affection["lumi"] == 20 and trust["roman"] == 15
        assert eval first_task_partner == "lumi" and story_chapter_number == 2
        assert eval sd_event_schema == 1 and sd_event_is_active()
        assert eval sd_event_current == "ch02_rival_introduction" and sd_event_variant_id == "01"
        assert eval story_mode == "sd_event" and not story_cast and not story_effects
        assert eval renpy.get_screen("sd_event_view",layer="sd_events") is not None
        screenshot "old_sd_save_migrated.png"
        advance
        assert eval sd_event_is_active() and not story_cast

    testcase load_real_old_sd_dialogue_save:
        run Function(renpy.load, "legacy_sd_mid_dialogue")
        pause until screen "say"
        # Common _after_load calls this observation before the game's migration.
        assert eval renpy._campus_legacy_before_migration is not None
        assert eval renpy._campus_legacy_before_migration["schema"] == 0
        assert eval renpy._campus_legacy_before_migration["mode"] == "sd"
        assert eval len(renpy._campus_legacy_before_migration["cast"]) == 9
        assert eval renpy._campus_legacy_before_migration["first_task_partner"] == "lumi"
        assert eval renpy._campus_legacy_before_migration["affection"]["lumi"] == 4
        assert eval renpy._campus_legacy_before_migration["trust"]["roman"] == 3
        assert eval not renpy._campus_legacy_entry_visits
        # Preserve the actual fifth-advance dialogue checkpoint, rather than
        # replaying the capture entry and starting the new event again.
        assert eval renpy.get_screen("say").scope["what"] == "아니, 이름 말고."
        assert eval story_read_log[-1][2] == "아니, 이름 말고."
        assert eval affection["lumi"] == 20 and trust["roman"] == 15 and not choice_log
        assert eval first_task_partner == "lumi" and story_chapter_number == 2
        assert eval sd_event_schema == 1 and sd_event_is_active()
        assert eval sd_event_current == "ch02_rival_introduction" and sd_event_variant_id == "01"
        assert eval story_mode == "sd_event" and not story_cast and not story_effects
        assert eval renpy.get_screen("sd_event_view", layer="sd_events") is not None
        screenshot "old_sd_dialogue_save_migrated.png"
        advance
        assert eval renpy.get_screen("say").scope["what"] == "왜 혼자 시상식 수상 소감 하는 사람처럼 말하냐고."
        assert eval sd_event_is_active() and not story_cast
        assert eval not persistent.endings and not meta_unlocked()



# Preserve the original first-checkpoint entry label used by the real pre-SD
# capture save. This file remains excluded from product builds.
label qa_old_sd_capture_entry:
    $ story_begin_chapter(2, "구버전 SD 저장 검증")
    $ story_flag("first_task_partner", "lumi")
    $ affection["lumi"] = 4
    $ trust["roman"] = 3
    jump ch02_sc03
