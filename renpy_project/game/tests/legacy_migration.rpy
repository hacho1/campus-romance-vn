testsuite legacy_migration:
    setup:
        $ _test.timeout = 50.0
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/legacy-migration-screenshots"
    teardown:
        exit
    testcase genuine_v010_slot:
        run Function(renpy.load, "legacy_ch01_mid")
        pause until screen "choice"
        assert eval choice_log == ['c1_wait']
        assert eval affection['roman'] == 10 and trust['roman'] == 10
        assert eval chapter_save_schema == 2
        assert eval first_task_partner is None and not story_active
        click "로만, 시아와 안내 문구를 쓴다."
        advance until screen "choice" timeout 40
        assert eval choice_log == ['c1_wait','c2_script']
        click "내 시간을 솔직하게 적고 일을 나눈다."
        advance until screen "choice" timeout 40
        click "시아와 정문 쪽으로 걷는다."
        advance until screen "demo_complete" timeout 40
        screenshot "legacy_complete.png"
        click "다음 챕터로"
        advance until screen "choice" timeout 80
        assert eval story_chapter_number == 2
        assert eval chapter01_complete and first_task_partner == 'sia'
        assert eval 'walk_sia' in event_flags and 'c1_wait' in choice_log
        screenshot "legacy_to_official_ch02.png"
