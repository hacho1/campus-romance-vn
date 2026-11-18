testsuite diary_ui:
    setup:
        $ sd_independent_isolation_test.assert_locations()
        $ _test.timeout = 28.0
        $ _test.transition_timeout = 0.02
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/secret_notes_20261106/evidence"
        $ persistent.profile_discoveries = set()
        $ persistent.profile_secrets = set()
        $ persistent.endings = set()
        $ persistent.choice_memories = set()
        $ persistent.chapter_completions = set()
        $ persistent.secret_note_notifications = True
    before testcase:
        if not screen "main_menu":
            if eval main_menu:
                keysym "K_ESCAPE"
            else:
                run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
    teardown:
        exit

    testcase five_diaries:
        parameter heroine = ["roman", "sia", "darim", "omu", "lumi"]
        run ShowMenu("profiles", initial=heroine)
        assert eval renpy.get_screen("profiles").scope["selected"] == heroine
        assert eval all(renpy.get_widget("profiles", "secret_note_slot_%d" % number) is not None for number in (1, 2, 3))
        assert eval not any(secret_note_ready(heroine, number) for number in (1, 2, 3))
        click "스티커 살펴보기"
        assert screen "profile_note"
        assert eval heroine + ".sticker" in persistent.profile_discoveries
        click "접어 두기"
        click "사진 모서리 살펴보기"
        assert screen "profile_note"
        click "접어 두기"
        click id "secret_note_slot_1" screen ("profiles",)
        assert screen "profile_secret_notes"
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_locked") is not None
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_title") is None
        click id "secret_note_close" screen ("profile_secret_notes",)
        $ secret_note_unlock(heroine, 1, notify=False)
        click id "secret_note_slot_1" screen ("profiles",)
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_body").get_all_text() == SECRET_NOTE_DATA[heroine]["note01"]["text"]
        screenshot f"{heroine}_note01.png"
        click id "secret_note_close" screen ("profile_secret_notes",)
        click "뒷면 보기"
        assert eval renpy.get_screen("profiles").scope["back"]
        click "앞면 보기"
        click "다음"
        assert eval renpy.get_screen("profiles").scope["selected"] == HEROINE_ORDER[(HEROINE_ORDER.index(heroine) + 1) % 5]
        keysym "K_LEFT"
        assert eval renpy.get_screen("profiles").scope["selected"] == heroine
        click "돌아가기"

    testcase independent_ending_notes:
        $ ENDINGS["sia_happy"]["implemented"] = True
        $ ENDINGS["sia_bad"]["implemented"] = True
        $ ENDINGS["sia_secret"]["implemented"] = True
        $ ENDINGS["omu_secret"]["implemented"] = True
        $ store.affection["sia"] = 100
        $ store.trust["sia"] = 100
        $ store.event_flags.add("sia_route_entered")
        $ persistent.profile_discoveries.add("sia.note_2")
        $ store.profile_debug_unlock = True
        assert eval not secret_note_ready("sia", 2) and not secret_note_ready("sia", 3)
        $ unlock_ending("sia_secret", sandbox=True)
        assert eval secret_note_content("sia", 3, "secret") is None
        run ShowMenu("profiles", initial="sia")
        click id "secret_note_slot_3" screen ("profiles",)
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_title") is None
        assert eval all(not renpy.get_widget("profile_secret_notes", "secret_note_ending_" + kind).sensitive for kind in SECRET_ENDING_KINDS)
        click id "secret_note_close" screen ("profile_secret_notes",)
        $ unlock_ending("sia_bad")
        $ unlock_ending("sia_happy")
        assert eval secret_ending_kinds("sia") == ("happy", "bad")
        click id "secret_note_slot_3" screen ("profiles",)
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_body").get_all_text() == SECRET_NOTE_DATA["sia"]["note03"]["happy"]["text"]
        assert eval not renpy.get_widget("profile_secret_notes", "secret_note_ending_secret").sensitive
        assert eval secret_note_content("sia", 3, "secret") is None
        click id "secret_note_ending_bad" screen ("profile_secret_notes",)
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_body").get_all_text() == SECRET_NOTE_DATA["sia"]["note03"]["bad"]["text"]
        screenshot "sia_two_endings_secret_locked.png"
        click id "secret_note_close" screen ("profile_secret_notes",)
        $ unlock_ending("sia_secret")
        $ unlock_ending("omu_secret")
        assert eval secret_ending_kinds("sia") == ("happy", "bad", "secret") and not secret_note_ready("omu", 3)
        assert eval secret_note_content("omu", 3, "secret") is None
        click id "secret_note_slot_3" screen ("profiles",)
        click id "secret_note_ending_secret" screen ("profile_secret_notes",)
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_body").get_all_text() == SECRET_NOTE_DATA["sia"]["note03"]["secret"]["text"]
        click id "secret_note_close" screen ("profile_secret_notes",)
        click "돌아가기"

    testcase first_notice_only_and_toggle:
        run ShowMenu("preferences")
        click id "settings_nav_4" screen ("preferences",)
        click id "settings_secret_note_notices" screen ("preferences",)
        assert eval not persistent.secret_note_notifications
        click id "settings_secret_note_notices" screen ("preferences",)
        assert eval persistent.secret_note_notifications
        click "돌아가기"
        run Start("qa_secret_notice")
        pause until screen "say"
        $ secret_note_unlock("roman", 2)
        $ renpy.restart_interaction()
        pause until screen "secret_note_unlock_toast" timeout 6
        assert eval renpy.get_widget("secret_note_unlock_toast", "secret_note_toast_detail").get_all_text() == "로만 · 그날의 진심"
        run Hide("secret_note_unlock_toast")
        $ secret_note_unlock("roman", 2)
        assert eval not renpy.get_screen("secret_note_unlock_toast") and secret_note_ready("roman", 2)
        $ persistent.secret_note_notifications = False
        $ secret_note_unlock("darim", 2)
        assert eval not renpy.get_screen("secret_note_unlock_toast") and secret_note_ready("darim", 2)

    testcase historical_proof_and_old_slots:
        $ persistent.profile_secrets.discard(secret_note_key("lumi", 1))
        run Start("qa_secret_legacy_checkpoint")
        pause until screen "say"
        run Function(renpy.save, "notes-before")
        assert eval not secret_note_ready("lumi", 1) and not secret_note_ready("lumi", 2)
        $ secret_note_unlock("omu", 2, notify=False)
        run Function(renpy.save, "notes-after")
        run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
        run Function(renpy.load, "notes-before")
        pause until eval secret_note_ready("lumi", 2) timeout 6
        assert eval secret_note_ready("lumi", 1) and secret_note_ready("lumi", 2) and secret_note_ready("omu", 2)
        assert eval secret_note_ready("harin", 1) and secret_note_ready("rumi", 2)
        assert eval "sia_01" in persistent.profile_secrets and not secret_note_ready("sia", 2)
        run Function(renpy.load, "notes-after")
        pause until screen "say"
        assert eval secret_note_ready("lumi", 2) and secret_note_ready("omu", 2)
        run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
        click "게임 시작"
        pause until screen "say"
        assert eval story_chapter_number == 1 and secret_note_ready("lumi", 2) and secret_note_ready("omu", 2)

label qa_secret_notice:
    $ story_begin_chapter(4, "메모 검증")
    $ story_scene("room", standing=False)
    narrator "비밀 메모 알림 검증."
    return

label qa_secret_legacy_checkpoint:
    $ story_begin_chapter(4, "구버전 저장")
    $ story_scene("room", standing=False)
    $ rumi_design_event = True
    $ ch04_personal_promise["harin"] = True
    $ persistent.profile_secrets.add("sia_01")
    narrator "완료한 장면 이후의 구버전 저장."
    return
