testsuite viewport_qa:
    setup:
        python:
            import os
            qa_root = os.path.normcase(os.path.abspath("D:/CampusRomance_VN/tests"))
            for directory in (config.basedir, config.savedir):
                assert os.path.commonpath([os.path.normcase(os.path.abspath(directory)), qa_root]) == qa_root, "Use isolated viewport test data."
        $ _test.timeout = 30.0
        $ _preferences.transitions = 0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/viewport-screenshots"
        $ persistent.profile_discoveries = set()
        $ persistent.profile_secrets = set()
    teardown:
        exit
    testcase diary_sizes:
        parameter size = [(1600, 900), (1280, 720)]
        run Function(renpy.set_physical_size, size)
        pause 0.5
        python:
            print("QA_PHYSICAL_SIZE", renpy.get_physical_size())
        run ShowMenu("profiles", initial="roman")
        screenshot f"roman_{size[0]}.png"
        click "시아"
        screenshot f"sia_{size[0]}.png"
        click "다림"
        screenshot f"darim_{size[0]}.png"
        click "오므"
        screenshot f"omu_{size[0]}.png"
        click "하린"
        screenshot f"lumi_{size[0]}.png"
        click "시아"
        $ secret_note_unlock("sia", 1, notify=False)
        $ renpy.restart_interaction()
        click id "secret_note_slot_1" screen ("profiles",)
        assert screen "profile_secret_notes"
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_body") is not None
        screenshot f"sia_note_{size[0]}.png"
        click id "secret_note_close" screen ("profile_secret_notes",)
        click "돌아가기"
