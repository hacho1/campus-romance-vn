# Independent regression of old SD saves inside CH02 help branches.
# No gameplay flags are advanced early just to choose an illustration.
testsuite sd_independent_legacy:
    setup:
        $ _test.timeout = 30.0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/sd-independent-legacy-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        exit
    testcase accident_branch_cut:
        parameter (saved_text, saved_actor, helped, expected) = [("일단 같이 주워주자.", "mc", False, "03"), ("나는 근처에 떨어진 카드를 주웠다.", "narrator", False, "03"), ("저기 문 앞에 있는 카드 몇 장만 집어주면 될 것 같아.", "hyeophap", False, "03"), ("저쪽에서 정리하는 것 같으니 우리 준비를 계속하자.", "mc", False, "02"), ("조금 뒤 라이벌 팀의 자료 정리가 끝났다.", "narrator", False, "02"), ("조금 뒤 라이벌 팀의 자료 정리가 끝났다.", "narrator", True, "03")]
        $ renpy._independent_sd_old_state = (saved_text, saved_actor, helped)
        run Start("qa_independent_sd_old_checkpoint")
        pause until screen "say"
        assert eval sd_event_current == "ch02_ski_accident"
        assert eval sd_event_variant_id == expected
        assert eval story_mode == "sd_event" and not story_cast and not story_effects
        assert eval renpy.get_screen("sd_event_view", layer="sd_events") is not None
        assert eval rival_helped == helped and affection["roman"] == 7 and trust["darim"] == 5

label qa_independent_sd_old_checkpoint:
    $ story_begin_chapter(2, "구버전 도움 분기 복원 검사")
    $ story_scene("corridor", mode="normal", cast=["sia", "darim"])
    $ sd_event_schema = 0
    $ story_mode = "sd"
    $ rival_helped = renpy._independent_sd_old_state[2]
    $ story_read_log = [(2, renpy._independent_sd_old_state[1], renpy._independent_sd_old_state[0])]
    $ affection["roman"] = 7
    $ trust["darim"] = 5
    $ sd_event_migrate_after_load()
    mc "불러온 장면의 컷과 진행 수치를 확인합니다."
    return
