# An extra scrapbook page; the heroine binder keeps its own layout and state.
screen met_people(initial="roman"):
    tag menu
    default people_page = 0
    $ people_page_count = met_people_page_count()
    $ people_page_keys = MET_PEOPLE_ORDER[people_page * MET_PEOPLE_PAGE_SIZE:(people_page + 1) * MET_PEOPLE_PAGE_SIZE]
    $ people_card_start = (1920 - (len(people_page_keys) * 820 + max(0, len(people_page_keys) - 1) * 48)) // 2

    add "bg campus"
    add Solid("#ebe7fb66")
    frame:
        xpos 38 ypos 52 xysize (620,98)
        background spring_panel("paper")
        padding (28,14)
        text "CC대 학생들 / 만난 사람들!" id "met_people_students_heading" font CAMPUS_TITLE_FONT size 32 line_spacing 0 color SPRING_INK yalign 0.5 yoffset -3

    hbox:
        xpos 1280 ypos 60 spacing 20
        textbutton "우리의 페이지":
            id "met_people_profiles"
            style "campus_control"
            xysize (240,76) padding (14,8)
            text_size 27 text_xalign 0.5 text_yalign 0.5 text_align 0.5
            text_idle_color SPRING_INK text_hover_color "#71426e"
            text_selected_idle_color SPRING_INK text_selected_hover_color "#71426e"
            selected False
            action ShowMenu("profiles", initial=initial)
        textbutton "만난 사람들!":
            id "met_people_selected"
            style "campus_control"
            xysize (240,76) padding (14,8)
            text_size 27 text_xalign 0.5 text_yalign 0.5 text_align 0.5
            text_idle_color SPRING_INK text_hover_color "#71426e"
            text_selected_idle_color SPRING_INK text_selected_hover_color "#71426e"
            selected True
            action NullAction()
    imagebutton:
        id "met_people_close"
        idle "images/ui/spring/close.svg" xpos 1810 ypos 38 xysize (65,65)
        action Return() alt "돌아가기"

    add "images/ui/spring/book.svg" xpos 116 ypos 216 xysize (42,42)
    text "축제를 준비하며 만난 얼굴들" xpos 174 ypos 210 font CAMPUS_TITLE_FONT size 35 color SPRING_INK

    for card_index, actor in enumerate(people_page_keys):
        $ person = MET_PEOPLE[actor]
        $ portrait = met_person_portrait(actor)
        $ accent = STORY_CAST.get(actor, {}).get("color", "#8b82ad")
        fixed:
            id ("met_person_card_" + actor)
            xpos (people_card_start + card_index * 868) ypos 295 xysize (820,660)
            add Solid("#514e7b20") xpos 5 ypos 8 xysize (820,660)
            add spring_panel("paper") xysize (820,660)
            add Solid("#fffdfb") xpos 28 ypos 52 xysize (456,552)
            add Solid(person.get("paper", "#f2eef7")) xpos 40 ypos 64 xysize (432,528)
            # The exact photo window contains the entire supplied composition.
            viewport:
                id ("met_person_portrait_" + actor)
                xpos 40 ypos 64 xysize (432,528)
                draggable False mousewheel False
                fixed:
                    xysize (432,528)
                    if portrait:
                        add Transform(portrait, xysize=(432,528), fit="contain") id ("met_person_image_" + actor) align (0.5,0.5)
                    else:
                        add "images/ui/spring/book.svg" xpos 180 ypos 205 xysize (72,72)
                        text "사진 준비 중" id ("met_person_missing_" + actor) font CAMPUS_BODY_FONT size 26 color SPRING_MUTED xalign 0.5 ypos 305
            add "images/ui/spring/tape.svg" xpos 172 ypos 36 xysize (168,32)
            text person["name"] id ("met_person_name_" + actor) xpos 506 ypos 108 font CAMPUS_TITLE_FONT size 50 line_spacing 0 color SPRING_INK
            text (person["department"] + " · " + str(person["year"]) + "학년") id ("met_person_department_" + actor) xpos 508 ypos 190 xmaximum 284 font CAMPUS_BODY_FONT size 24 line_spacing 0 color SPRING_MUTED
            add Solid(accent) xpos 508 ypos 252 xysize (48,3)
            vbox:
                xpos 508 ypos 286 xsize 284 spacing 24
                text person["intro"] id ("met_person_intro_" + actor) xmaximum 284 font CAMPUS_BODY_FONT size 27 line_spacing 8 color SPRING_INK
                if person.get("quote"):
                    text ("“" + person["quote"] + "”") id ("met_person_quote_" + actor) xmaximum 284 font CAMPUS_BODY_FONT size 24 line_spacing 6 color SPRING_MUTED

    if people_page_count > 1:
        hbox:
            xalign 0.5 ypos 995 spacing 18
            textbutton "이전" id "met_people_prev" style "campus_control" xysize (94,64) padding (12,6) text_size 24 text_xalign 0.5 text_yalign 0.5 text_align 0.5 action [SetScreenVariable("people_page", (people_page - 1) % people_page_count), With(Dissolve(0.16))]
            text (str(people_page + 1) + " / " + str(people_page_count)) id "met_people_page" xsize 130 size 26 color SPRING_INK text_align 0.5 yalign 0.5
            textbutton "다음" id "met_people_next" style "campus_control" xysize (94,64) padding (12,6) text_size 24 text_xalign 0.5 text_yalign 0.5 text_align 0.5 action [SetScreenVariable("people_page", (people_page + 1) % people_page_count), With(Dissolve(0.16))]
        key "K_LEFT" action SetScreenVariable("people_page", (people_page - 1) % people_page_count)
        key "K_RIGHT" action SetScreenVariable("people_page", (people_page + 1) % people_page_count)

    key "game_menu" action Return()
