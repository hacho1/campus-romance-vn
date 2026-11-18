# Phone continuity remains independent of SD presentation.
testsuite chat_continuity:
    setup:
        $ _test.timeout = 60.0
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/chat-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
    teardown:
        exit
    testcase chat_save_load:
        run Start("qa_story_chat_checkpoint")
        advance until eval story_chat_active and len(story_chat_messages) == 3 timeout 60
        assert eval story_chat_title == "축제 준비팀"
        $ renpy._campus_chat_expected = tuple(story_chat_messages)
        screenshot "chat_group.png"
        click "저장"
        run FilePage("8")
        run FileSave("chat", confirm=False)
        assert eval renpy.can_load("8-chat")
        click "돌아가기"
        $ story_chat_messages.clear()
        $ renpy.restart_interaction()
        click "불러오기"
        run FilePage("8")
        run FileLoad("chat", confirm=False)
        pause until screen "say"
        assert eval story_chat_active and tuple(story_chat_messages) == renpy._campus_chat_expected
        screenshot "chat_restored.png"

label qa_story_chat_checkpoint:
    $ story_begin_chapter(1, "채팅 저장 검증")
    $ story_flag("first_task_partner", "sia")
    jump ch01_sc09
