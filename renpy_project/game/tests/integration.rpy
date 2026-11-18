# Excluded from distributable builds. CAMPUS_SAVE_DIR isolates test saves on D:.
testsuite global:
    setup:
        $ _test.timeout = 12.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.skip_unseen = False
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
    before testcase:
        if eval main_menu:
            if not screen "main_menu":
                click "돌아가기"
        else:
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        pause 0.6
    teardown:
        exit

    testcase main_screen:
        assert screen "main_menu"
        screenshot "main_menu.png"
        keysym "K_F1"
        assert screen "help"
        click "돌아가기"
        assert screen "main_menu"

    testcase profiles:
        parameter person_name = ["로만", "시아", "다림", "오므", "하린"]
        click "CC대 학생들"
        click expression person_name
        screenshot f"profile_{person_name}_front.png"
        click "뒷면 보기"
        assert eval renpy.get_screen("profiles").scope["back"]
        screenshot f"profile_{person_name}_back.png"
        click "앞면 보기"
        assert eval not renpy.get_screen("profiles").scope["back"]
        click "돌아가기"
        assert screen "main_menu"

    testcase menu_navigation:
        parameter target = ["load", "preferences", "gallery", "endings", "developer_room", "meta_test"]
        run ShowMenu(target)
        assert screen target
        screenshot f"menu_{target}.png"
        click "돌아가기"
        assert screen "main_menu"

    testcase meta_sandbox:
        assert eval not meta_unlocked()
        run ShowMenu("meta_test")
        click "일반 엔딩을 본 상황 가정"
        click "가상의 대화창과 학생증 바꾸기"
        assert eval renpy.get_screen("meta_test").scope["changed"]
        assert eval not persistent.endings
        screenshot "meta_changed.png"

    testcase ending_rules:
        python:
            assert len(ENDINGS) == 15
            assert all(not e['implemented'] and e['secret_category'] is None for e in ENDINGS.values())
            for ending_id in ENDINGS:
                assert not unlock_ending(ending_id)
                assert unlock_ending(ending_id, sandbox=True)
            assert len(sandbox_endings) == 15
            assert not persistent.endings
            assert not meta_unlocked()
            assert clean_name('   ') == '나'
            assert clean_name('[이름]{태그}') == '이름태그'
            assert len(clean_name('가'*20)) == 12

    testcase chapter_paths:
        parameter path_index = [0, 1, 2, 3, 4]
        run Start("qa_legacy_ch01_entry")
        pause until screen "input"
        $ renpy.get_widget("input", "input").update_text("", True)
        type "TestUser"
        click "이 이름으로 시작"
        $ print("INPUT_RESULT", repr(player_name))
        assert eval player_name == "TestUser"
        advance until screen "choice" timeout 30
        screenshot f"choice_{path_index}.png"
        if eval path_index == 0:
            click "로만이 말을 마칠 때까지 기다린다."
        elif eval path_index == 1:
            click "시아에게 응원 담당도 손은 두 개라고 말한다."
        else:
            click "다림과 상자의 무게를 나눈다."
        advance until screen "choice" timeout 30
        if eval path_index in (0, 1):
            click "로만, 시아와 안내 문구를 쓴다."
        elif eval path_index == 3:
            click "오므와 사진 위치를 확인한다."
        else:
            click "하린과 부스 도면을 살펴본다."
        advance until screen "choice" timeout 30
        if eval path_index == 1:
            click "웃음 뒤에 조용해진 시아에게 말을 건넨다."
        elif eval path_index in (0, 3):
            click "말수가 줄어든 사람들의 의견을 먼저 묻는다."
        else:
            click "내 시간을 솔직하게 적고 일을 나눈다."
        advance until screen "choice" timeout 30
        assert eval len(choice_log) == 3
        if eval path_index == 0:
            click "로만에게 책 이야기를 묻는다."
        elif eval path_index == 1:
            click "시아와 정문 쪽으로 걷는다."
        elif eval path_index == 2:
            click "다림과 남은 물품을 옮긴다."
        elif eval path_index == 3:
            click "오므에게 오늘 사진을 보여 달라고 한다."
        else:
            click "하린과 접힌 도면을 정리한다."
        advance
        screenshot f"story_{path_index}.png"
        advance until screen "demo_complete" timeout 30
        assert eval ch01_done and len(choice_log) == 4
        assert eval not eligible_routes()
        assert eval "ch01" in persistent.chapter_completions
        assert eval "festival_note" in persistent.gallery
        assert eval secret_note_ready(HEROINE_ORDER[path_index], 1)
        assert eval not persistent.endings and not meta_unlocked()
        screenshot f"complete_{path_index}.png"
        click "학생증 보기"
        click expression HEROINES[HEROINE_ORDER[path_index]]["name"]
        click "뒷면 보기"
        assert eval renpy.get_screen("profiles").scope["back"]
        click id "secret_note_slot_1" screen ("profiles",)
        assert screen "profile_secret_notes"
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_body") is not None
        screenshot f"secret_{path_index}.png"
        click id "secret_note_close" screen ("profile_secret_notes",)
        click "돌아가기"
        click "메인 메뉴로"
        assert screen "main_menu"

    testcase save_load_buttons:
        run Start("qa_checkpoint")
        pause until screen "say"
        click "저장"
        assert screen "save"
        run FilePage("5")
        click pos (350, 420)
        if screen "confirm":
            click "확인"
        assert eval renpy.can_load("5-1")
        screenshot "save_slots.png"
        click "돌아가기"
        $ affection['roman'] = 95
        click "불러오기"
        run FilePage("5")
        click pos (350, 420)
        if screen "confirm":
            click "확인"
        assert eval affection['roman'] == 7 and trust['roman'] == 4 and player_name == "저장검증"
        run MainMenu(confirm=False)
        click "이어하기"
        assert eval not main_menu
        click "기록"
        assert screen "history"
        screenshot "history.png"
        click "돌아가기"
        click "자동"
        assert eval _preferences.afm_enable
        click "자동"
        assert eval not _preferences.afm_enable

    testcase route_preview:
        parameter heroine = ["roman", "sia", "darim", "omu", "lumi"]
        run Start("qa_legacy_ch01_entry")
        pause until screen "input"
        keysym "K_RETURN"
        run Jump("route_" + heroine)
        advance until "이 개별 루트는 제작 중입니다."
        assert eval not persistent.endings
        screenshot f"route_{heroine}_unfinished.png"

label qa_checkpoint:
    scene bg campus
    $ player_name = "저장검증"
    $ affection['roman'] = 7
    $ trust['roman'] = 4
    mc "이 대사에서 저장한 이름과 관계 수치를 불러옵니다."
    "저장 검증을 위한 별도 장면입니다."
    jump qa_checkpoint

label qa_legacy_ch01_entry:
    $ story_active = False
    $ player_name = clean_name(renpy.input("캠퍼스에서 불릴 이름을 적어 주세요.", default="하루", length=12))
    jump ch01
