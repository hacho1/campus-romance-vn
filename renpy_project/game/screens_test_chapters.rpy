# The existing spring paper, fonts and profile photos carry this test menu.
screen test_chapters():
    tag menu
    default chapter_group = "common"
    default chosen_entry = "chapter01"
    default test_name = player_name
    default test_partner = "roman"

    add "bg campus"
    add Solid("#ebe7fb88")
    frame:
        xpos 38 ypos 52 xysize (620,98)
        background spring_panel("paper")
        padding (28,14)
        text "챕터 선택 · 테스트" id "test_chapters_heading" font CAMPUS_TITLE_FONT size 32 line_spacing 0 color SPRING_INK yalign .5 yoffset -3
    imagebutton:
        id "test_chapters_close"
        idle "images/ui/spring/close.svg" xpos 1810 ypos 38 xysize (65,65)
        action Return() alt "메인 메뉴로 돌아가기"

    text "읽고 싶은 장면부터" xpos 184 ypos 194 font CAMPUS_TITLE_FONT size 38 line_spacing 0 color SPRING_INK
    text "선택한 챕터부터 이어서 읽습니다. 언제든 종료 버튼으로 돌아올 수 있어요." xpos 184 ypos 253 font CAMPUS_BODY_FONT size 25 line_spacing 0 color SPRING_MUTED

    frame:
        id "test_chapters_paper"
        xpos 140 ypos 308 xysize (1640,660)
        background spring_panel("paper")
        padding (0,0)
        fixed:
            xpos 44 ypos 32 xysize (860,596)
            # Six readable tabs in two rows; keep every button inside paper.
            grid 3 2:
                xspacing 18 yspacing 10
                for group_id, group_title, first_entry in [("common", "공통 · CH01–07", "chapter01"), ("roman", "로만 · R01–06", "roman_r01"), ("sia", "시아 · S01–06", "sia_s01"), ("darim", "다림 · D01–06", "darim_d01"), ("omu", "오므 · O01–06", "omu_o01"), ("lumi", "하린 · H01–06", "harin_h01")]:
                    textbutton group_title:
                        id ("test_chapters_" + group_id + "_tab")
                        style "campus_control" xysize (264,60) padding (10,8)
                        text_size 22 text_xalign .5 text_yalign .5 text_align .5
                        selected chapter_group == group_id
                        action [SetScreenVariable("chapter_group", group_id), SetScreenVariable("chosen_entry", first_entry)]
            grid 2 4:
                xpos 0 ypos 152 xspacing 18 yspacing 14
                for entry, code, title, group in TEST_CHAPTERS:
                    if group == chapter_group:
                        button:
                            id ("test_chapter_" + entry)
                            style "campus_control" xysize (412,96) padding (18,8)
                            selected chosen_entry == entry
                            action SetScreenVariable("chosen_entry", entry)
                            vbox:
                                xalign .5 yalign .5 spacing 4
                                text ("시크릿" if code == "SECRET" else code) font CAMPUS_BODY_FONT size 21 line_spacing 0 color SPRING_MUTED xalign .5 text_align .5
                                text title font CAMPUS_BODY_FONT size 21 line_spacing 2 color SPRING_INK xmaximum 372 xalign .5 text_align .5
                for unused_cell in range(8 - len([row for row in TEST_CHAPTERS if row[3] == chapter_group])):
                    null width 412 height 96

        add Solid("#d8ccdf") xpos 940 ypos 40 xysize (1,570)
        fixed:
            xpos 988 ypos 32 xysize (600,596)
            text "읽기 설정" font CAMPUS_TITLE_FONT size 34 line_spacing 0 color SPRING_INK
            text "주인공 이름" xpos 0 ypos 76 font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_INK
            frame:
                id "test_chapter_name_field"
                xpos 0 ypos 112 xysize (554,66)
                background spring_panel("paper_cream") padding (22,8)
                input:
                    id "test_chapter_name"
                    value ScreenVariableInputValue("test_name")
                    length 12
                    font CAMPUS_BODY_FONT size 27 color SPRING_INK
                    yalign .5 xsize 510
            text "이전 개인 이벤트의 상대" xpos 0 ypos 210 font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_INK
            text "앞선 챕터의 개인 이벤트와 축제 상대에 반영합니다." xpos 0 ypos 250 font CAMPUS_BODY_FONT size 20 line_spacing 0 color SPRING_MUTED xmaximum 554
            hbox:
                xpos 0 ypos 298 spacing 12
                for actor in HEROINE_ORDER:
                    button:
                        id ("test_partner_" + actor)
                        style "campus_control" xysize (100,108) padding (6,6)
                        selected test_partner == actor
                        action SetScreenVariable("test_partner", actor)
                        vbox:
                            xalign .5 yalign .5 spacing 5
                            add Transform(diary_photo(actor), xysize=(48,61), fit="cover") xalign .5
                            text HEROINES[actor]["name"] font CAMPUS_BODY_FONT size 22 line_spacing 0 color SPRING_INK xalign .5 text_align .5
            text ("선택한 챕터 · " + (HEROINES[story_id(chosen_entry.split("_")[0])]["name"] + " 시크릿" if chosen_entry.endswith("_secret") else test_chapter_code(chosen_entry))) id "test_chapter_selection" xpos 0 ypos 436 font CAMPUS_BODY_FONT size 22 line_spacing 0 color SPRING_MUTED
            textbutton "여기서부터 읽기":
                id "test_chapter_launch"
                style "campus_control"
                xpos 102 ypos 484 xysize (350,76) padding (16,8)
                text_size 28 text_xalign .5 text_yalign .5 text_align .5
                sensitive CAMPUS_TEST_BUILD
                action Function(test_chapter_launch, chosen_entry, test_name, test_partner)

    text "선택·호감도는 테스트 안에서 이어지며, 실제 저장·수집 기록에는 반영되지 않습니다." id "test_chapters_isolation_note" xpos 184 ypos 1002 font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_INK
    key "game_menu" action Return()

screen test_chapter_overlay():
    zorder 145
    if test_story_mode and _in_replay:
        frame:
            id "test_chapter_badge"
            xpos 60 ypos 112 xysize (418,56)
            background spring_panel("paper_cream") padding (12,6)
            hbox:
                spacing 12 yalign .5
                text ("테스트 · " + test_chapter_code(test_chapter_current or test_chapter_entry)) id "test_chapter_badge_text" xsize 242 font CAMPUS_BODY_FONT size 22 line_spacing 0 color SPRING_INK yalign .5 text_align .5
                textbutton "종료":
                    id "test_chapter_exit"
                    style "campus_control" xysize (124,44) padding (8,4)
                    text_size 21 text_xalign .5 text_yalign .5 text_align .5
                    action EndReplay(False)
