# Actual chapter notifications and phone reply save/load.
testsuite official_phone_entry_followup:
    setup:
        $ _test.timeout = 30.0
        $ _test.transition_timeout = .02
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/official-phone-entry-screenshots"
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        exit

    testcase first_school_notice_is_manually_read:
        click "게임 시작"
        advance until eval story_chat_active and phone_active_thread == "campus_notice" timeout 30
        assert eval not phone_is_open and phone_notification_pending and not phone_allow_dismiss()
        assert eval phone_threads["campus_notice"]["title"] == "학사 알림"
        assert eval len(phone_threads["campus_notice"]["messages"]) == 1
        assert eval phone_threads["campus_notice"]["messages"][0]["text"] == "「오늘 예정된 강의가 모두 종료되었습니다.」"
        assert eval "핸드폰에 새 메시지 도착!" in renpy.get_widget("say", "phone_arrival_title").get_all_text()
        screenshot "first_school_notification.png"
        keysym "K_SPACE"
        assert eval not phone_is_open and phone_active_thread == "campus_notice"
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_is_open and phone_view == "lock" and not phone_allow_dismiss()
        click id "phone_toolbar_save" screen ("quick_menu",)
        assert screen "save"
        run FilePage("14")
        run FileSave("1",confirm=False)
        click "돌아가기"
        assert eval phone_is_open and phone_view == "lock"
        click "알림 열기"
        assert eval phone_view == "chat" and phone_allow_dismiss()
        assert eval phone_threads["campus_notice"]["unread"] == 0
        click id "phone_toolbar_load" screen ("quick_menu",)
        assert screen "load"
        run FilePage("14")
        run FileLoad("1",confirm=False)
        pause until screen "say"
        pause until eval phone_is_open and phone_view == "lock" timeout 1
        assert eval renpy.get_widget("say", "phone_arrival_notice") is not None and renpy.get_widget("say", "window") is None
        assert eval not phone_notification_pending and phone_threads["campus_notice"]["unread"] == 1
        assert eval len(phone_threads["campus_notice"]["messages"]) == 1
        screenshot "first_school_saved_lock_restored.png"
        click "알림 열기"
        assert eval phone_view == "chat" and phone_allow_dismiss()
        assert eval renpy.get_widget("say", "window") is not None and renpy.get_widget("say", "phone_shell") is not None
        screenshot "first_school_message_opened.png"
        click id "phone_next" screen ("say",)
        advance until screen "choice" timeout 30
        assert eval not story_chat_active and story_chapter_number == 1 and not choice_log
        assert eval player_name == "나" and all(value == 0 for value in affection.values()) and all(value == 0 for value in trust.values())
        assert eval renpy.get_widget("quick_menu","quick_controls") is not None
        screenshot "first_authored_choice_with_toolbar.png"

    testcase application_confirmation_opens_its_own_room:
        click "게임 시작"
        advance until eval story_chat_active and phone_active_thread == "campus_notice" timeout 30
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        click id "phone_next" screen ("say",)
        advance until screen "choice" timeout 30
        click "대학생활에 추억 하나쯤은 있어야지."
        advance until screen "input" timeout 30
        $ renpy.get_widget("input", "input").update_text("", True)
        type "FestivalQA"
        click "신청하기"
        advance until eval story_chat_active and phone_active_thread == "festival_application" timeout 30
        assert eval phone_notification_pending and not phone_is_open and not phone_allow_dismiss()
        assert eval phone_threads["festival_application"]["title"] == "축제 연합 프로젝트"
        assert eval phone_threads["festival_application"]["unread"] == 1
        assert eval phone_threads["festival_application"]["messages"][0]["text"] == "안녕하세요! 축제 연합 프로젝트에 지원해 주셔서 감사합니다."
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_view == "lock" and not phone_allow_dismiss()
        click "알림 열기"
        assert eval phone_view == "chat" and phone_allow_dismiss() and phone_threads["festival_application"]["unread"] == 0
        click id "phone_next" screen ("say",)
        pause until eval phone_threads["festival_application"]["messages"][-1]["text"] == "오늘 오후 2시, 학생회관 3층 공동 동아리실에서 첫 모임이 진행됩니다." timeout 4
        click id "phone_next" screen ("say",)
        pause until eval phone_threads["festival_application"]["messages"][-1]["text"] == "늦지 않게 참석해 주세요!" timeout 4
        click id "phone_next" screen ("say",)
        pause until eval not story_chat_active and _last_say_what == "……오늘?" timeout 4
        assert eval not story_chat_active and _last_say_what == "……오늘?"
        assert eval [message["text"] for message in phone_threads["festival_application"]["messages"]] == ["안녕하세요! 축제 연합 프로젝트에 지원해 주셔서 감사합니다.", "오늘 오후 2시, 학생회관 3층 공동 동아리실에서 첫 모임이 진행됩니다.", "늦지 않게 참석해 주세요!"]
        assert eval "campus_notice" in phone_threads and player_name == "FestivalQA"

    testcase committee_announcements_keep_authored_lines:
        parameter (start_label, group_first, first_line, last_line, message_count, response) = [
            ("qa_official_phone_ch01_end", True, "「축제 부스 공간 배정 관련 추가 안내」", "「자세한 내용은 내일 공지하겠습니다.」", 3, "……동일 구역 신청 팀?"),
            ("chapter02", True, "「축제 운영위원회」", "참가팀은 오전 11시까지 학생회관 안내 게시판의 세부 공지를 확인해 주시기 바랍니다.", 4, "동일 구역 신청 팀……."),
            ("qa_official_phone_ch02_end", False, "「축제 운영위원회 공지」", "「방문객의 체험 결과와 개선 사항을 제출해 주세요.」", 4, "……시범 운영?"),
        ]
        run Start(start_label)
        if eval group_first:
            advance until eval story_chat_active and phone_active_thread == "campus_group" timeout 30
            click id "phone_archive_button" screen ("quick_menu",)
            click "알림 열기"
        advance until eval story_chat_active and phone_active_thread == "festival_committee" timeout 90
        assert eval phone_notification_pending and not phone_is_open and not phone_allow_dismiss()
        assert eval phone_threads["festival_committee"]["title"] == "축제 운영위원회"
        assert eval phone_threads["festival_committee"]["unread"] == 1
        assert eval phone_threads["festival_committee"]["messages"][0]["text"] == first_line
        click id "phone_archive_button" screen ("quick_menu",)
        assert eval phone_view == "lock" and not phone_allow_dismiss()
        click "알림 열기"
        assert eval phone_view == "chat" and phone_allow_dismiss() and phone_threads["festival_committee"]["unread"] == 0
        advance until eval not story_chat_active timeout 10
        assert eval len(phone_threads["festival_committee"]["messages"]) == message_count
        assert eval phone_threads["festival_committee"]["messages"][-1]["text"] == last_line
        assert eval _last_say_what == response

    testcase phone_reply_rewards_are_not_reapplied_by_load:
        run Start("qa_official_phone_reward")
        pause until screen "say"
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        click id "phone_next" screen ("say",)
        pause until screen "choice"
        click "함께 준비할게."
        pause until screen "say"
        assert eval affection["roman"] == 10 and trust["roman"] == 5 and choice_log == ["qa_phone_reply_reward"]
        click id "phone_toolbar_save" screen ("quick_menu",)
        run FilePage("14")
        run FileSave("2",confirm=False)
        click "돌아가기"
        $ story_apply("qa_phone_temporary_change",affection={"roman":5})
        click id "phone_toolbar_load" screen ("quick_menu",)
        run FilePage("14")
        run FileLoad("2",confirm=False)
        pause until screen "say"
        pause .15
        $ print("PHONE_REPLY_RESTORED",affection["roman"],trust["roman"],list(choice_log),phone_is_open,phone_view)
        assert eval affection["roman"] == 10 and trust["roman"] == 5
        assert eval choice_log == ["qa_phone_reply_reward"]
        assert eval len(phone_threads["campus_group"]["messages"]) == 2
        assert eval phone_is_open and phone_view == "chat"

label qa_official_phone_ch01_end:
    $ story_begin_chapter(1, "프로젝트에 신청한 날")
    jump ch01_sc09

label qa_official_phone_ch02_end:
    $ story_begin_chapter(2, "우리 옆 부스가 수상하다")
    jump ch02_sc09

label qa_official_phone_reward:
    $ story_begin_chapter(1,"답장 선택 효과 저장 검증")
    $ story_scene("room",cast=[],light="night",location="주인공 방 · 밤")
    $ story_sfx("message")
    $ story_chat(True,title="축제 준비팀")
    roman "함께 준비해 주실래요?"
    menu:
        "함께 준비할게.":
            $ story_apply("qa_phone_reply_reward",affection={"roman":2},trust={"roman":1})
    roman "고마워요."
    jump qa_official_phone_reward_hold

label qa_official_phone_reward_hold:
    narrator "저장한 선택 효과가 한 번만 적용되어야 합니다."
    jump qa_official_phone_reward_hold
