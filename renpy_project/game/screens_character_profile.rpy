# Spring scrapbook profile: left heroine rail, open binder, three gated notes.
transform diary_sticker_hover:
    subpixel True
    zoom 1.0
    on hover:
        easeout 0.16 zoom 1.07
    on idle:
        easeout 0.16 zoom 1.0

# Word wrapping keeps each rendered line on the notebook's 48px rules.
init -8 python:
    import unicodedata

    DIARY_NOTE_PAPERS = {
        "roman": ("#fff8e8", "#d9bc89"),
        "sia": ("#fff0f7", "#dfa8c6"),
        "darim": ("#f1f6eb", "#aebfa6"),
        "omu": ("#edf4f6", "#acc3c9"),
        "lumi": ("#edf3fc", "#b3c3de"),
    }

    def diary_ruled_lines(value, units=38):
        def measure(value):
            return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1 for ch in value)
        lines = []
        for paragraph in str(value or "").split("\n"):
            current = ""
            for word in paragraph.split(" "):
                chunks, chunk = [], ""
                for character in word:
                    if chunk and measure(chunk + character) > units:
                        chunks.append(chunk)
                        chunk = character
                    else:
                        chunk += character
                chunks.append(chunk)
                for chunk_index, chunk in enumerate(chunks):
                    proposed = (current + " " + chunk) if current and chunk_index == 0 else current + chunk
                    if current and measure(proposed) > units:
                        lines.append(current)
                        current = chunk
                    else:
                        current = proposed
                    if chunk_index + 1 < len(chunks):
                        lines.append(current)
                        current = ""
            lines.append(current)
        return lines or [""]

screen profile_ruled_block(value, column_x=1003, row_y=708, width=475, rows=3, units=38, text_id="profile_intro"):
    viewport:
        id (text_id + "_viewport")
        xpos column_x ypos row_y xysize (width, rows * 48)
        mousewheel True draggable True
        vbox:
            spacing 8
            for line_index, line_value in enumerate(diary_ruled_lines(value, units)):
                fixed:
                    xysize (width,40)
                    text line_value id (text_id if line_index == 0 else text_id + "_" + str(line_index)) font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_INK yalign 0.5

screen profiles(initial="roman"):
    tag menu
    default selected = initial if initial in HEROINE_ORDER else HEROINE_ORDER[0]
    default back = False
    $ person = HEROINES[selected]
    $ page = PROFILE_PAGES[selected]
    $ page_number = HEROINE_ORDER.index(selected)
    $ previous_key = HEROINE_ORDER[(page_number - 1) % len(HEROINE_ORDER)]
    $ next_key = HEROINE_ORDER[(page_number + 1) % len(HEROINE_ORDER)]
    $ shown_red, shown_black = heart_profile_values()[:2]
    $ memo_states = [secret_note_view_ready(selected, number) for number in range(1, 4)]

    add "bg campus"
    add Solid("#ebe7fb66")
    frame:
        xpos 38 ypos 52 xsize 620 ysize 98
        background spring_panel("paper")
        padding (28, 14)
        fixed:
            xysize (564,70)
            text "CC대 학생들" id "profile_students_heading" font CAMPUS_TITLE_FONT size 32 line_spacing 0 color SPRING_INK yalign 0.5 yoffset -3 xmaximum 280
            textbutton "만난 사람들!":
                id "met_people_open"
                style "campus_control"
                xpos 314 yalign 0.5 yoffset -3 xsize 240 ysize 60 padding (14,8)
                text_size 24 text_xalign 0.5 text_yalign 0.5 text_align 0.5
                action ShowMenu("met_people", initial=selected)
    hbox:
        xpos 850 ypos 60 spacing 10
        textbutton "프로필" style "campus_control" xsize 220 ysize 76 padding (14,8) text_size 27 text_xalign 0.5 text_yalign 0.5 text_align 0.5 text_selected_color SPRING_INK selected not back action SetScreenVariable("back", False)
        textbutton "비밀 메모" id "secret_notes_open" style "campus_control" xsize 220 ysize 76 padding (14,8) text_size 27 text_xalign 0.5 text_yalign 0.5 text_align 0.5 selected False action Show("profile_secret_notes", heroine=selected)
        textbutton "일상 사진" style "campus_control" xsize 220 ysize 76 padding (14,8) text_size 27 text_xalign 0.5 text_yalign 0.5 text_align 0.5 selected False action Function(open_profile_detail, selected, "photo", profile_debug_unlock or campus_test_collections_preview())
    imagebutton:
        idle "images/ui/spring/close.svg" xpos 1810 ypos 38 xysize (65,65)
        action Return() alt "돌아가기"

    frame:
        xpos 50 ypos 235 xsize 290 ysize 705
        background spring_panel("paper")
        padding (21, 25)
        vbox:
            spacing 12
            text "히로인 목록" size 27 color SPRING_INK xalign 0.5
            for key in HEROINE_ORDER:
                button:
                    xsize 245 ysize 105
                    selected selected == key
                    action [SetScreenVariable("selected", key), SetScreenVariable("back", False), With(Dissolve(0.2))]
                    padding (12, 8)
                    hbox:
                        spacing 15
                        add Transform(diary_photo(key), xysize=(64, 82), fit="cover")
                        text HEROINES[key]["name"] size 28 color SPRING_INK yalign 0.5

    add "images/ui/spring/notebook.svg" xpos 375 ypos 200 xysize (1140,780)
    add Solid(page["paper"] + "55") xpos 950 ypos 215 xysize (548,735)
    fixed:
        xysize (447,600)
        at Transform(pos=(650,565), anchor=(0.5,0.5), rotate=-3 if selected != "lumi" else 0, rotate_pad=False)
        add Solid("#6b679c20") xpos 8 ypos 12 xysize (447,600)
        add Solid("#fffdfd") xysize (447,600)
        imagebutton:
            idle Transform(diary_photo(selected), xysize=(411,500), fit="cover")
            xpos 18 ypos 18
            action Function(open_profile_detail, selected, "photo", profile_debug_unlock or campus_test_collections_preview())
            alt "사진 모서리 살펴보기"
            tooltip "사진 뒤에 남긴 말"
        if diary_photo(selected).endswith("photo_placeholder.svg"):
            text "사진 준비 중" xalign 0.5 ypos 225 size 29 color "#696895"
            text "여기에 너의 한 장면" xalign 0.5 ypos 280 font CAMPUS_BODY_FONT size 23 color "#77709e"
        text page["photo_caption"] xpos 20 ypos 540 xmaximum 408 font CAMPUS_NOTE_FONT size 25 color SPRING_INK
        add "images/ui/spring/tape.svg" xpos 85 ypos -20 xysize (260,42)
        add "images/ui/spring/clip.svg" xpos 340 ypos -48 xysize (58,75)
    imagebutton:
        idle Transform(diary_sticker(selected), xysize=(170,170))
        xpos 760 ypos 700 xysize (170,170)
        at diary_sticker_hover
        action Function(open_profile_detail, selected, "sticker", profile_debug_unlock or campus_test_collections_preview())
        alt "스티커 살펴보기"
        tooltip "스티커 아래 작은 메모"
    add "images/ui/spring/flowers.svg" xpos 365 ypos 863 xysize (130,130)
    textbutton ("앞면 보기" if back else "뒷면 보기"):
        style "campus_control"
        xpos 630 ypos 906 xsize 235 ysize 60 padding (18,8) text_size 24
        text_xalign 0.5 text_yalign 0.5 text_align 0.5
        text_idle_color SPRING_INK text_hover_color SPRING_INK
        text_selected_idle_color SPRING_INK text_selected_hover_color SPRING_INK
        action [ToggleScreenVariable("back"), With(Dissolve(0.16))]

    fixed:
        xpos 1003 ypos 226 xysize (190,80)
        text person["name"] id "profile_name" font CAMPUS_TITLE_FONT size 54 line_spacing 0 color SPRING_INK yalign 0.5
    add "images/ui/spring/heart.svg" xpos 1160 ypos 253 xysize (32,32)
    frame:
        xpos 1210 ypos 254 xysize (270,58)
        background spring_panel("button_selected")
        padding (12,6)
        text (person["department"] + " " + str(person["year"]) + "학년") id "profile_department_badge" font CAMPUS_BODY_FONT size 21 line_spacing 0 color SPRING_INK xalign 0.5 yalign 0.5 yoffset -2 text_align 0.5
    if not back:
        # The notebook SVG rules are y=364,412,...; row bottoms share those lines.
        for row_index, label_value in enumerate([("나이",str(person["age"])+"살"),("학년",str(person["year"])+"학년"),("학과",person["department"]),("MBTI",person["mbti"])]):
            fixed:
                xpos 1003 ypos (324 + row_index * 48) xysize (475,40)
                text label_value[0] font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_MUTED yalign 0.5
                text label_value[1] xpos 145 xmaximum 330 font CAMPUS_BODY_FONT size 24 line_spacing 0 color SPRING_INK yalign 0.5
        fixed:
            xpos 1003 ypos 516 xysize (475,40)
            text "좋아하는 것" font CAMPUS_BODY_FONT size 23 line_spacing 0 color "#705674" yalign 0.5
            text person["likes"] xpos 145 xmaximum 330 font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_INK yalign 0.5
        fixed:
            xpos 1003 ypos 564 xysize (140,40)
            text "싫어하는 것" font CAMPUS_BODY_FONT size 23 line_spacing 0 color "#705674" yalign 0.5
        use profile_ruled_block(person["dislikes"], column_x=1148, row_y=564, width=330, rows=2, units=26, text_id="profile_dislikes")
        fixed:
            xpos 1003 ypos 660 xysize (475,40)
            text "한 줄 소개" font CAMPUS_BODY_FONT size 23 line_spacing 0 bold True color "#705674" yalign 0.5
        use profile_ruled_block(page.get("one_line", person["intro"]), row_y=708, rows=3, text_id="profile_intro")
    else:
        fixed:
            xpos 1003 ypos 324 xysize (475,40)
            text "함께 이어진 사이" font CAMPUS_BODY_FONT size 25 line_spacing 0 bold True color "#705674" yalign 0.5
        use profile_ruled_block(person["relations"], row_y=372, rows=3, text_id="profile_relations")
        fixed:
            xpos 1003 ypos 564 xysize (475,40)
            text "네게 남기는 한 문장" font CAMPUS_BODY_FONT size 25 line_spacing 0 bold True color "#705674" yalign 0.5
        use profile_ruled_block(person["intro"], row_y=612, rows=3, text_id="profile_quote")
        if selected == "darim":
            fixed:
                xpos 1003 ypos 804 xysize (475,40)
                text "재수 경험이 있는 대학생" font CAMPUS_BODY_FONT size 23 line_spacing 0 color SPRING_MUTED yalign 0.5

    frame:
        id "profile_relationship_panel"
        xpos 1003 ypos 866 xysize (475,78)
        background spring_panel("paper_cream")
        padding (0,0)
        fixed:
            for heart_index, kind, caption, scores in ((0,"red","해피 호감도",shown_red), (1,"black","배드 호감도",shown_black)):
                $ score = scores.get(selected)
                $ heart_color = HEART_BLACK if kind == "black" else HEART_RED
                fixed:
                    xpos (heart_index * 238) xysize (237,78)
                    add heart_icon(kind, 25) id ("profile_" + kind + "_icon") xpos 12 ypos 12
                    text caption id ("profile_" + kind + "_caption") xpos 44 ypos 14 font CAMPUS_BODY_FONT size 19 line_spacing 0 color SPRING_INK
                    text ("%s / 100" % (score if score is not None else "—")) id ("profile_" + kind + "_value") xpos 145 ypos 15 xsize 80 text_align 1.0 font CAMPUS_BODY_FONT size 18 line_spacing 0 color heart_color
                    add Solid(HEART_TRACK) id ("profile_" + kind + "_track") xpos 14 ypos 49 xysize (207,9)
                    if score:
                        add Solid(heart_color) id ("profile_" + kind + "_gauge") xpos 14 ypos 49 xysize (int(207 * heart_clamp(score) / 100),9)
            add Solid("#d8ccdf") xpos 237 ypos 12 xysize (1,48)

    for note_index, ready in enumerate(memo_states):
        $ note_number = note_index + 1
        $ note_caption = "비밀 메모 %02d" % note_number
        button:
            id ("secret_note_slot_%d" % note_number)
            xpos 1575 ypos (265 + note_index * 222) xysize (292, 181)
            background spring_panel("note")
            hover_background spring_panel("button_hover")
            action Show("profile_secret_notes", heroine=selected, initial=note_number)
            alt (note_caption + (" 열람 가능" if ready else " 잠김"))
            padding (24, 21)
            vbox:
                spacing 9
                hbox:
                    spacing 8
                    use spring_icon("heart" if ready else "lock", 27)
                    text note_caption size 25 color SPRING_INK
                text SECRET_NOTE_LABELS[note_index] font CAMPUS_TITLE_FONT size 24 color SPRING_INK
                text ("엔딩 메모 %d / 3" % len(secret_note_view_ending_kinds(selected)) if note_number == 3 and ready and campus_test_collections_preview() else "엔딩 기록 %d / 3" % len(secret_ending_kinds(selected)) if note_number == 3 and ready else "다시 읽기" if ready else "해피 엔딩 후 공개" if note_number == 3 else "미발견") size 20 color SPRING_MUTED
        add "images/ui/profile/tape.svg" xpos (1605 + (note_index%2)*95) ypos (250 + note_index*222) xysize (143,40)
    add diary_sticker("common") xpos 1700 ypos 130 xysize (140,140)
    frame:
        id "profile_unlock_hint_panel"
        xpos 1555 ypos 914 xysize (310,118)
        background spring_panel("paper_cream") padding (20,14)
        text ("TEST · 전체 열람\n비밀 메모를 확인해요." if campus_test_collections_preview() else "비밀 메모 %d / 3 수집\n장면과 결말을 기록해요." % sum(memo_states)) id "profile_unlock_hint" xmaximum 270 font CAMPUS_BODY_FONT size 22 line_spacing 6 color SPRING_INK xalign 0.5 yalign 0.5 text_align 0.5
    if heart_profile_notice():
        text heart_profile_notice() id "profile_heart_migration_notice" xpos 968 ypos 952 xsize 570 font CAMPUS_BODY_FONT size 17 line_spacing 0 color SPRING_INK text_align .5
    hbox:
        xpos 1055 ypos 994 spacing 20
        textbutton "이전" style "campus_control" xsize 94 ysize 64 padding (12,6) selected False action [SetScreenVariable("selected", previous_key), SetScreenVariable("back", False), With(Dissolve(0.2))]
        text (str(page_number+1) + " / " + str(len(HEROINE_ORDER))) xsize 130 size 26 color SPRING_INK text_align 0.5 yalign 0.5
        textbutton "다음" style "campus_control" xsize 94 ysize 64 padding (12,6) selected False action [SetScreenVariable("selected", next_key), SetScreenVariable("back", False), With(Dissolve(0.2))]
    if profile_debug_unlock:
        text "사진 · 스티커 미리보기" xpos 455 ypos 1015 size 22 color "#9a5b92"
    key "K_LEFT" action [SetScreenVariable("selected", previous_key), SetScreenVariable("back", False), With(Dissolve(0.2))]
    key "K_RIGHT" action [SetScreenVariable("selected", next_key), SetScreenVariable("back", False), With(Dissolve(0.2))]
    key "game_menu" action Return()
    $ profile_tooltip = GetTooltip()
    if profile_tooltip:
        text profile_tooltip xpos 425 ypos 151 size 22 color SPRING_INK outlines [(2,"#ffffffbb",0,0)]

screen secret_note_margin(heroine, paper, rule):
    # Authored paper marks stay outside the reading column.
    if heroine == "roman":
        add Solid(rule) xpos 928 ypos 0 xysize (49,128)
        add "images/ui/spring/book.svg" xpos 936 ypos 32 xysize (33,33)
        add "images/ui/spring/paw.svg" xpos 944 ypos 87 xysize (18,18)
    elif heroine == "sia":
        add Solid(rule) xpos 888 ypos 36 xysize (105,3)
        add Solid(rule) xpos 888 ypos 36 xysize (3,82)
        add Solid(rule) xpos 908 ypos 56 xysize (105,3)
        add Solid(rule) xpos 1010 ypos 56 xysize (3,82)
    elif heroine == "darim":
        for row in range(3):
            add Solid(rule) xpos 894 ypos (42 + row * 27) xysize (16,16)
            add Solid(paper) xpos 897 ypos (45 + row * 27) xysize (10,10)
            add Solid(rule) xpos 923 ypos (49 + row * 27) xysize (76,2)
    elif heroine == "omu":
        add Solid(rule) xpos 899 ypos 42 xysize (100,111)
        add Solid("#fffdf6") xpos 896 ypos 38 xysize (100,111)
        add Solid(paper) xpos 903 ypos 45 xysize (86,77)
        add "images/ui/spring/camera.svg" xpos 923 ypos 61 xysize (47,47)
        add Solid(rule) xpos 897 ypos 160 xysize (99,21)
        for hole in range(5):
            add Solid(paper) xpos (903 + hole * 18) ypos 164 xysize (11,5)
    else:
        for column in range(6):
            add Solid(rule) xpos (886 + column * 23) ypos 35 xysize (1,92)
        for row in range(5):
            add Solid(rule) xpos 886 ypos (35 + row * 23) xysize (116,1)
        add Solid(rule) xpos 887 ypos 112 xysize (115,3)
    add diary_sticker(heroine) xpos 881 ypos 198 xysize (124,124)

screen profile_secret_notes(heroine, initial=1):
    modal True
    zorder 250
    default number = initial
    default ending = None
    $ available_endings = secret_note_view_ending_kinds(heroine) if number == 3 else ()
    $ chosen_ending = ending if ending in available_endings else next(iter(available_endings), None)
    $ note = secret_note_view_content(heroine, number, chosen_ending)
    $ heading = secret_note_view_heading(heroine) if number == 3 and note else None
    $ paper, rule = DIARY_NOTE_PAPERS[heroine]

    add Solid("#39355180")
    frame:
        id "secret_note_panel"
        xalign 0.5 yalign 0.5 xysize (1170, 810)
        background spring_panel("button")
        padding (65, 50)
        fixed:
            xysize (1040,710)
            text (HEROINES[heroine]["name"] + " · 비밀 메모") font CAMPUS_TITLE_FONT size 42 color SPRING_INK
            hbox:
                ypos 89 spacing 16
                for index in range(1, 4):
                    $ ready = secret_note_view_ready(heroine, index)
                    button:
                        id ("secret_note_tab_%d" % index)
                        style "campus_control"
                        xysize (336,78) padding (20,12)
                        selected number == index
                        action [SetScreenVariable("number", index), SetScreenVariable("ending", None)]
                        alt ("비밀 메모 %02d %s" % (index, "열람 가능" if ready else "잠김"))
                        hbox:
                            spacing 10 yalign 0.5
                            use spring_icon("heart" if ready else "lock", 24)
                            text ("%02d  %s" % (index, SECRET_NOTE_LABELS[index - 1])) size 20 xmaximum 250 color SPRING_INK yalign 0.5
            if number == 3:
                hbox:
                    ypos 184 spacing 16
                    for kind in SECRET_ENDING_KINDS:
                        $ kind_ready = kind in available_endings
                        button:
                            id ("secret_note_ending_" + kind)
                            style "campus_control"
                            xysize (336,66) padding (20,10)
                            selected chosen_ending == kind
                            sensitive kind_ready
                            action SetScreenVariable("ending", kind)
                            alt (kind.upper() + (" 열람 가능" if kind_ready else " 잠김"))
                            hbox:
                                spacing 10 yalign 0.5
                                use spring_icon("heart" if kind_ready else "lock", 22)
                                text kind.upper() size 23 color SPRING_INK yalign 0.5
                                text ("열람 가능" if kind_ready else "미해금") size 21 color SPRING_MUTED yalign 0.5
            fixed:
                ypos (270 if number == 3 else 226) xysize (1040,346)
                add Solid(paper) xysize (1040,346)
                add Solid(rule) xysize (1040,2)
                add Solid(rule) ypos 344 xysize (1040,2)
                use secret_note_margin(heroine, paper, rule)
                if note is not None:
                    vbox:
                        xpos 36 ypos 24 xsize 822 spacing 12
                        if heading:
                            text heading id "secret_note_ending_heading" size 23 color SPRING_MUTED
                        text note["title"] id "secret_note_title" font (CAMPUS_NOTE_FONT if heroine == "roman" else CAMPUS_TITLE_FONT) size 41 color SPRING_INK xmaximum 822
                        viewport:
                            id "secret_note_viewport"
                            xysize (822, 191 if heading else 221)
                            mousewheel True draggable True arrowkeys True pagekeys True
                            text note["text"] id "secret_note_body" size 30 color SPRING_INK xsize 822 line_spacing 10
                else:
                    hbox:
                        xpos 36 yalign 0.5 spacing 15
                        use spring_icon("lock", 32)
                        text secret_note_hint(number) id "secret_note_locked" size 28 color SPRING_INK xmaximum 770 yalign 0.5
            textbutton "접어 두기" id "secret_note_close" style "campus_control" ypos 641 xalign 0.5 xysize (248,68) text_size 25 action Hide("profile_secret_notes")
    key "game_menu" action Hide("profile_secret_notes")

transform secret_note_toast_in:
    on show:
        alpha 0.0
        easeout 0.16 alpha 1.0
    on replace:
        alpha 0.0
        easeout 0.16 alpha 1.0

screen secret_note_unlock_toast(message, detail=None):
    zorder 139
    frame:
        xalign 0.968 ypos 166 xsize 505
        background spring_panel("paper_cream")
        padding (24,18)
        at (secret_note_toast_in if _preferences.transitions else Transform())
        hbox:
            spacing 13
            use spring_icon("heart", 27)
            vbox:
                xsize 414 spacing 5
                text message id "secret_note_toast_message" size 24 color SPRING_INK
                if detail:
                    text detail id "secret_note_toast_detail" size 21 color SPRING_MUTED
    timer 2.6 action Hide("secret_note_unlock_toast")

screen profile_note(heroine, note_title, note_body, note_footer):
    modal True
    zorder 250
    add Solid("#65609164")
    frame:
        id "profile_note_panel"
        xalign 0.5 yalign 0.48 xsize 1030 ymaximum 900
        background spring_panel("paper_cream")
        padding (80,65)
        vbox:
            spacing 34
            hbox:
                spacing 18
                use spring_icon("heart",46)
                text note_title id "profile_note_title" font CAMPUS_TITLE_FONT size 42 line_spacing 0 color SPRING_INK xmaximum 790
            # Long unlocked notes scroll while the footer and close button stay available.
            viewport:
                id "profile_note_body_viewport"
                xsize 860 ysize min(300, max(160, (note_body.count("\n") + 1) * 48))
                mousewheel True draggable True arrowkeys True pagekeys True
                text note_body id "profile_note_body" size 31 color SPRING_INK xsize 860 line_spacing 14
            text note_footer size 22 color SPRING_MUTED xmaximum 860
            textbutton "접어 두기" xsize 270 ysize 70 text_size 24 text_xalign 0.5 text_yalign 0.5 text_align 0.5 action Hide("profile_note")
    add "images/ui/spring/paw.svg" xpos 1295 ypos 724 xysize (90,90)
    key "game_menu" action Hide("profile_note")
