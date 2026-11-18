# Ending collection stays unchanged; this screen only aligns the record to diary rules.
init offset = 950

screen endings():
    tag menu
    use page_shell("엔딩 목록")
    add "images/ui/diary_polish/ending_ledger.svg" xpos 190 ypos 185 xysize (1540,790)
    add "images/ui/spring/tape.svg" xpos 1280 ypos 168 xysize (220,36)
    add "images/ui/spring/clip.svg" xpos 207 ypos 184 xysize (48,65)
    add diary_sticker("common") xpos 1490 ypos 220 xysize (125,125)
    text "이야기의 마지막 페이지" id "ending_diary_title" xpos 330 ypos 227 xmaximum 1050 font CAMPUS_TITLE_FONT size 36 line_spacing 0 color SPRING_INK
    fixed:
        xpos 330 ypos 300 xysize (170,50)
        text "히로인" font CAMPUS_BODY_FONT size 25 line_spacing 0 color SPRING_MUTED xalign 0.5 yalign 1.0
    for column, label in enumerate(["해피", "배드", "시크릿"]):
        fixed:
            xpos (600 + column * 320) ypos 300 xysize (250,50)
            text label id ("ending_header_" + str(column)) font CAMPUS_BODY_FONT size 25 line_spacing 0 color SPRING_INK xalign 0.5 yalign 1.0
    # Row bottoms = actual SVG rules at y420,510,600,690,780.
    for row, key in enumerate(HEROINE_ORDER):
        fixed:
            xpos 330 ypos (365 + row * 90) xysize (170,55)
            text HEROINES[key]["name"] id ("ending_name_" + key) font CAMPUS_BODY_FONT size 30 line_spacing 0 color SPRING_INK xalign 0.5 yalign 1.0
        for column, kind in enumerate(["happy", "bad", "secret"]):
            $ eid = key + "_" + kind
            fixed:
                id ("ending_cell_" + eid)
                xpos (600 + column * 320) ypos (365 + row * 90) xysize (250,55)
                hbox:
                    xalign 0.5 yalign 1.0 spacing 14
                    if eid in persistent.endings:
                        add "images/ui/spring/heart.svg" id ("ending_status_" + eid) xysize (35,36)
                        text "기록됨" font CAMPUS_BODY_FONT size 22 line_spacing 0 color SPRING_INK yalign 1.0
                    else:
                        add "images/ui/spring/lock.svg" id ("ending_status_" + eid) xysize (31,36)
                        text "???" font CAMPUS_BODY_FONT size 22 line_spacing 0 color SPRING_MUTED yalign 1.0
    fixed:
        xpos 330 ypos 800 xysize (1110,50)
        text "다섯 사람의 엔딩 기록 · 시크릿은 각 인물의 해피 엔딩 이후 열립니다." id "ending_footer" font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_MUTED yalign 1.0
    for index, actor in enumerate(("roman", "sia", "darim", "omu", "lumi")):
        fixed:
            xpos (305 + index * 267) ypos 870 xysize (252,60)
            if actor + "_happy" in persistent.endings:
                textbutton (HEROINES[actor]["name"] + " 시크릿 읽기"):
                    id ("ending_secret_replay_" + actor)
                    xysize (252,52) text_size 23
                    action Replay("harin_secret" if actor == "lumi" else actor + "_secret", scope={"player_name": player_name, "sia_s02_cat_name": sia_s02_cat_name or "고양이 인형"}, locked=False)
            else:
                text (HEROINES[actor]["name"] + " 해피 엔딩 후 열림") xmaximum 252 font CAMPUS_BODY_FONT size 20 color SPRING_MUTED xalign .5 yalign .5 text_align .5
    add "images/ui/spring/paw.svg" xpos 1540 ypos 785 xysize (70,70)
