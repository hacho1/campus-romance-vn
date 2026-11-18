# The user's supplied spring scrapbook board is the visual authority.
# All panels and icons are original editable assets; no heroine art is generated.
init 999 python:
    SPRING_INK = "#414579"
    SPRING_MUTED = "#65698d"
    def spring_panel(kind="paper"):
        if kind in ("button", "button_hover", "button_selected"):
            # Balanced interactive surface: the visible shape and the layout
            # rectangle share the same centre, including at short heights.
            return Frame("images/ui/controls/" + kind + ".png", 32, 32)
        return Frame("images/ui/spring/" + kind + ".png", 40, 40)
    def ui_box(fill="#ffffff", border=None):
        return spring_panel("button_hover" if fill in ("#bb447e", "#ffe0f0") else "paper")
    style.default.color = SPRING_INK
    style.button.background = spring_panel("button")
    style.button.hover_background = spring_panel("button_hover")
    style.button.selected_background = spring_panel("button_selected")
    style.button.insensitive_background = spring_panel("button")
    style.button.padding = (28, 15)
    style.button_text.color = SPRING_INK
    style.button_text.hover_color = "#7e4f87"
    style.button_text.selected_color = "#874b81"
    style.button_text.selected_idle_color = SPRING_INK
    style.button_text.selected_hover_color = "#7e4f87"
    style.button_text.insensitive_color = "#9699b3"
    # Ren'Py's textbutton style has its own inherited state colours.
    # Keep selected labels legible on the pale pink paper.
    style.textbutton_text.color = SPRING_INK
    style.textbutton_text.hover_color = "#7e4f87"
    style.textbutton_text.selected_color = SPRING_INK
    style.textbutton_text.selected_idle_color = SPRING_INK
    style.textbutton_text.selected_hover_color = "#7e4f87"
    style.textbutton_text.insensitive_color = "#9699b3"
    style.frame.background = spring_panel("paper")
    style.title_text.font = CAMPUS_NOTE_FONT
    style.title_text.color = SPRING_INK
    style.caption_text.color = SPRING_MUTED
    style.action_button.background = spring_panel("button_selected")
    style.action_button.hover_background = spring_panel("button_hover")
    style.action_button_text.font = CAMPUS_BODY_FONT
    style.action_button_text.color = SPRING_INK
    style.action_button_text.hover_color = "#7e4f87"
    style.action_button_text.selected_color = SPRING_INK
    style.small_button.background = None
    style.small_button.hover_background = spring_panel("button_hover")
    style.small_button.selected_background = None
    style.small_button_text.color = SPRING_INK
    style.small_button_text.hover_color = "#9a5c93"
    style.small_button_text.selected_color = "#9a5c93"
    style.bar.left_bar = Solid("#9893cf")
    style.bar.right_bar = Solid("#e8e2f2")
    style.bar.thumb = Solid("#8a86c2")
    style.bar.ysize = 14
    # Rail and knob share one 40px canvas, centred at y=20. The native Bar
    # blits its thumb at y=0, so a taller thumb cannot centre in a 14px rail.
    style.slider.left_bar = Frame("images/ui/controls/slider_active.png", 20,0,0,0)
    style.slider.right_bar = Frame("images/ui/controls/slider_inactive.png", 0,0,20,0)
    style.slider.thumb = "images/ui/controls/slider_thumb.png"
    style.slider.thumb_shadow = None
    style.slider.thumb_offset = 20
    style.slider.left_gutter = 20
    style.slider.right_gutter = 20
    style.slider.ysize = 40
    style.scrollbar.base_bar = Solid("#ebe5f2")
    style.scrollbar.thumb = Solid("#aaa3d4")

screen spring_icon(name, size=42):
    add ("images/ui/spring/" + name + ".svg") xysize (size, size)

screen main_menu():
    tag menu
    add "bg campus"
    add Solid("#ece8ff16")
    fixed:
        xysize (940, 370)
        at Transform(pos=(625, 365), anchor=(0.5, 0.5), rotate=-6, rotate_pad=False)
        add spring_panel("paper") xysize (940, 370)
        text "우리 사이," xpos 100 ypos 20 font CAMPUS_NOTE_FONT size 135 color "#6662a3"
        text "그 이상" xpos 270 ypos 143 font CAMPUS_NOTE_FONT size 143 color "#7771af"
        add "images/ui/spring/heart.svg" xpos 670 ypos 180 xysize (115, 115)
        text "같은 봄, 조금 다른 우리" xpos 320 ypos 300 font CAMPUS_NOTE_FONT size 37 color "#9390bc"
    fixed:
        xysize (300, 280)
        at Transform(pos=(270, 840), anchor=(0.5, 0.5), rotate=9, rotate_pad=False)
        add Solid("#fffdfb") xysize (300, 280)
        add Transform("bg campus", xysize=(264, 206)) xpos 18 ypos 18
        text "첫 번째 봄" xpos 38 ypos 229 font CAMPUS_NOTE_FONT size 35 color "#6d689f"
        add "images/ui/spring/clip.svg" xpos 180 ypos -36 xysize (58, 75)
    frame:
        xpos 1300 ypos 83 xsize 495 ysize 920
        background spring_panel("paper_cream")
        padding (35, 40)
        vbox:
            spacing 7
            for caption, icon, action in [("게임 시작","play",Start()),("이어하기","continue",Function(continue_action)),("불러오기","load",ShowMenu("load")),("학생증","profile",ShowMenu("profiles")),("갤러리","gallery",ShowMenu("gallery")),("엔딩 목록","ending",ShowMenu("endings")),("환경설정","settings",ShowMenu("preferences")),("게임 종료","quit",Quit(confirm=True))]:
                button:
                    xsize 420 ysize 92
                    background None
                    hover_background spring_panel("button_hover")
                    sensitive (bool(renpy.newest_slot()) if caption == "이어하기" else True)
                    action action
                    has hbox
                    spacing 27
                    use spring_icon(icon, 40)
                    text caption size 32 color "#484a83" yalign 0.5
    add "images/ui/spring/flowers.svg" xpos 1690 ypos 886 xysize (180, 180)
    text "우리 사이, 그 이상 · CH01~03 데모" xpos 540 ypos 1005 size 23 color "#545787" outlines [(2,"#ffffffaa",0,0)]
    if config.developer:
        textbutton "개발실" xpos 1718 ypos 1020 style "small_button" text_size 22 action ShowMenu("developer_room")
    key "K_F1" action ShowMenu("help")

screen page_shell(title):
    add "bg campus"
    add Solid("#e9e5fa8c")
    add spring_panel("paper") xpos 55 ypos 150 xysize (1810, 840)
    frame:
        id "page_header"
        xpos 70 ypos 35 xysize (1300,100)
        background Frame("images/ui/controls/button.png",32,32) padding (45,0)
        text title id "page_title" font CAMPUS_TITLE_FONT size 48 line_spacing 0 color SPRING_INK yalign 0.5 yoffset -4
    textbutton "돌아가기" id "page_back" style "campus_control" xpos 1625 ypos 50 xsize 215 ysize 70 padding (20,8) text_size 25 action Return()
    add "images/ui/spring/flowers.svg" xpos 1733 ypos 906 xysize (160,160)
    key "game_menu" action Return()

screen say(who, what):
    text location_name xpos 78 ypos 40 size 24 color "#545787" outlines [(2,"#ffffffee",0,0)]
    window:
        id "window"
        background spring_panel("dialogue")
        xpos 60 ypos 814 xsize 1800 ysize 235
        padding (68, 44)
        text what id "what" xpos 0 ypos 17 xsize 1650 size 34 line_spacing 12 color SPRING_INK
    if who is not None:
        frame:
            xpos 148 ypos 771 xsize 305 ysize 80
            background spring_panel("button_selected")
            padding (20, 8)
            text who id "who" xalign 0.5 yalign 0.5 size 30 color SPRING_INK bold True
    add "images/ui/spring/flowers.svg" xpos 28 ypos 946 xysize (126,126)
    add "images/ui/spring/heart.svg" xpos 1760 ypos 980 xysize (43,43)

screen quick_menu():
    zorder 100
    if not main_menu and renpy.get_screen("say"):
        frame:
            xpos 830 ypos 20
            background spring_panel("paper")
            padding (14, 8)
            hbox:
                spacing 1
                style_prefix "small"
                textbutton "자동" action Preference("auto-forward", "toggle") text_size 23
                textbutton "건너뛰기" action Skip() alternate Skip(fast=True, confirm=True) text_size 23
                textbutton "기록" action ShowMenu("history") text_size 23
                textbutton "저장" action ShowMenu("save") text_size 23
                textbutton "불러오기" action ShowMenu("load") text_size 23
                textbutton "빠른 저장" action QuickSave() text_size 23
                textbutton "학생증" action ShowMenu("profiles") text_size 23
                textbutton "설정" action ShowMenu("preferences") text_size 23
                textbutton "메뉴" action MainMenu(confirm=True) text_size 23

screen choice(items):
    modal True
    add Solid("#7b75aa28")
    vbox:
        xalign 0.5 yalign 0.45 spacing 17
        for item in items:
            button:
                action item.action
                xsize 1170 ysize 100
                background spring_panel("button")
                hover_background spring_panel("button_hover")
                padding (45, 22)
                text item.caption size 32 color SPRING_INK xalign 0.5 yalign 0.5

screen input(prompt):
    modal True
    add "bg campus"
    add Solid("#e8e5f755")
    frame:
        xalign 0.5 yalign 0.48 xsize 1120
        background spring_panel("paper")
        padding (70, 48)
        vbox:
            spacing 26
            if application_input_active:
                text "축제 프로젝트 참가 신청서" font CAMPUS_TITLE_FONT size 40 line_spacing 0 color SPRING_INK
            text prompt id "name_prompt" xmaximum 980 size 28 line_spacing 0 color SPRING_INK
            frame:
                xsize 980 ysize 112 padding (24,12)
                background Solid("#f2f1f7")
                input id "input" size 46 font CAMPUS_BODY_FONT color "#3e4869" xsize 932 yalign 0.5
            text "한글·영문·숫자 12자 이내 · Enter로 확인" size 22 line_spacing 0 color "#606580"
            textbutton ("신청하기" if application_input_active else "이 이름으로 시작"):
                id "name_submit" style "action_button" xsize 360 ysize 76 padding (24,10)
                text_size 27 text_idle_color SPRING_INK text_hover_color "#71426e"
                text_selected_idle_color SPRING_INK text_selected_hover_color "#71426e"
                action Function(submit_input)

screen confirm(message, yes_action, no_action):
    modal True
    zorder 220
    add Solid("#64608370")
    frame:
        xalign 0.5 yalign 0.5 xsize 1020
        background spring_panel("paper")
        padding (75, 60)
        vbox:
            spacing 38
            text message id "confirm_message" size 32 color SPRING_INK xmaximum 850
            hbox:
                spacing 28
                textbutton "확인" style "action_button" xsize 240 action yes_action
                textbutton "취소" xsize 240 action no_action
    key "game_menu" action no_action

screen preferences():
    tag menu
    default settings_tab = "기본 설정"
    default text_preview_count = 0
    use page_shell("환경설정")
    vbox:
        xpos 95 ypos 215 spacing 16
        for index,caption in enumerate(["기본 설정", "사운드", "텍스트", "화면", "기타"]):
            textbutton caption style "campus_control" id ("settings_nav_"+str(index)) xsize 300 ysize 84 padding (20,8) text_size 27 text_selected_idle_color SPRING_INK text_selected_hover_color "#71426e" selected settings_tab == caption action SetScreenVariable("settings_tab", caption)
    frame:
        xpos 440 ypos 205 xsize 1340 ysize 700
        background None
        padding (40, 20)
        viewport:
            id "preferences_content_viewport"
            xysize (1260,660) mousewheel True draggable True
            vbox:
                xsize 1220 spacing 28
                if settings_tab in ("기본 설정", "사운드"):
                    text "배경음악" size 30 color SPRING_INK
                    bar value Preference("music volume") xsize 1130 id "settings_slider_music"
                    text "효과음" size 30 color SPRING_INK
                    bar value Preference("sound volume") xsize 1130 id "settings_slider_sound"
                    textbutton "효과음 들어보기" id "settings_control_preview" style "campus_control" xsize 320 ysize 66 padding (20,8) text_size 25 action Function(click_sound)
                if settings_tab in ("기본 설정", "텍스트"):
                    hbox:
                        spacing 24
                        text "텍스트 속도" size 30 color SPRING_INK
                        text ("즉시 표시" if _preferences.text_cps == 0 else "{}자/초".format(round(_preferences.text_cps))) id "settings_text_speed_value" size 24 color SPRING_MUTED yalign .5
                    bar value Preference("text speed") xsize 1130 id "settings_slider_text"
                    if settings_tab == "텍스트":
                        hbox:
                            spacing 14
                            for caption, speed in [("느리게", 20), ("보통", 38), ("빠르게", 65), ("즉시", 0)]:
                                textbutton caption style "campus_control" id ("settings_text_speed_" + str(speed)) xsize 180 ysize 58 text_size 24 selected _preferences.text_cps == speed action Preference("text speed", speed)
                        hbox:
                            spacing 20
                            textbutton "속도 미리보기" id "settings_play_text_preview" style "campus_control" xsize 230 ysize 58 text_size 23 action SetScreenVariable("text_preview_count", text_preview_count + 1)
                            if text_preview_count:
                                text "오늘도 캠퍼스에 봄바람이 불어요." id ("settings_text_preview_" + str(text_preview_count)) size 24 color SPRING_INK yalign .5 slow True slow_cps _preferences.text_cps
                    text "자동 진행 대기 시간" size 30 color SPRING_INK
                    bar value Preference("auto-forward time") xsize 1130 id "settings_slider_auto"
                if settings_tab == "텍스트":
                    textbutton "읽지 않은 대사도 건너뛰기" id "settings_skip_unread" style "campus_control" xsize 530 ysize 66 padding (20,8) text_size 25 action Preference("skip", "toggle")
                    textbutton "선택지 이후 계속 건너뛰기" id "settings_after_choices" style "campus_control" xsize 530 ysize 66 padding (20,8) text_size 25 action Preference("after choices", "toggle")
                if settings_tab == "화면":
                    text "화면 모드" font CAMPUS_TITLE_FONT size 38 line_spacing 0
                    textbutton "창 모드" id "settings_window" style "campus_control" xsize 320 ysize 66 padding (20,8) text_size 25 action Preference("display", "window")
                    textbutton "전체 화면" id "settings_fullscreen" style "campus_control" xsize 320 ysize 66 padding (20,8) text_size 25 action Preference("display", "fullscreen")
                    textbutton "화면 전환 효과" id "settings_transitions" style "campus_control" xsize 320 ysize 66 padding (20,8) text_size 25 action Preference("transitions", "toggle")
                if settings_tab == "기타":
                    textbutton "조작 방법" id "settings_help" style "campus_control" xsize 320 ysize 66 padding (20,8) text_size 25 action ShowMenu("help")
                    textbutton ("비밀 메모 알림 · " + ("켜짐" if persistent.secret_note_notifications else "꺼짐")) id "settings_secret_note_notices" style "campus_control" xsize 390 ysize 66 padding (20,8) text_size 25 action [ToggleField(persistent, "secret_note_notifications"), Function(renpy.save_persistent)]
                    if not main_menu:
                        textbutton "주인공 이름 변경" action Call("rename_player")
                    if config.developer:
                        textbutton "개발실 · 분기와 메타 테스트" action ShowMenu("developer_room")
                    text "이 데모에는 음성 대사가 포함되어 있지 않습니다." size 27 color SPRING_MUTED
    text "기본값은 이미 읽은 대사만 건너뜁니다." xpos 500 ypos 924 size 25 color SPRING_MUTED

screen endings():
    tag menu
    use page_shell("엔딩 목록")
    add "images/ui/spring/notebook.svg" xpos 230 ypos 180 xysize (1450, 790)
    text "이야기의 마지막 페이지" xpos 875 ypos 220 font CAMPUS_NOTE_FONT size 48 color SPRING_INK
    # Headers and cells share column origins; text's intrinsic width must not
    # shift the locks away from the ending category they identify.
    for column, label in enumerate(["해피", "배드", "시크릿"]):
        fixed:
            xpos (620 + column * 340) ypos 325 xysize (220, 60)
            text label size 27 color SPRING_INK xalign 0.5
    for row, key in enumerate(HEROINE_ORDER):
        text HEROINES[key]["name"] xpos 340 ypos (415 + row * 90) size 32 color SPRING_INK
        for column, kind in enumerate(["happy", "bad", "secret"]):
            $ eid = key + "_" + kind
            fixed:
                xpos (620 + column * 340) ypos (415 + row * 90) xysize (220, 65)
                if eid in persistent.endings:
                    add "images/ui/spring/heart.svg" xalign 0.5 xysize (45,45)
                else:
                    add "images/ui/spring/lock.svg" xalign 0.5 xysize (42,42)
                    text "???" xalign 0.5 ypos 39 size 20 color SPRING_MUTED
    text "15개의 자리 · 첫 데모에는 완성된 엔딩이 없습니다." xpos 500 ypos 920 size 25 color SPRING_MUTED

screen gallery():
    tag menu
    default gallery_tab = "이벤트 CG"
    use page_shell("갤러리")
    vbox:
        xpos 95 ypos 215 spacing 16
        for caption in ["이벤트 CG", "스탠딩", "배경", "배경음악"]:
            textbutton caption xsize 300 ysize 84 text_selected_idle_color SPRING_INK text_selected_hover_color SPRING_INK selected gallery_tab == caption action SetScreenVariable("gallery_tab", caption)
    if gallery_tab == "이벤트 CG":
        grid 3 2:
            xpos 460 ypos 225 spacing 25
            for index in range(6):
                button:
                    xysize (410, 285)
                    background spring_panel("paper")
                    action (Show("cg_view", cg="festival_note") if index == 0 and "festival_note" in persistent.gallery else NullAction())
                    vbox:
                        spacing 6
                        if index == 0 and "festival_note" in persistent.gallery:
                            add cg_asset("festival_note") xysize (350, 195)
                            text "첫 회의의 메모" size 24 color SPRING_INK xalign 0.5
                        else:
                            add "images/ui/spring/lock.svg" xysize (100,100) xalign 0.5
                            text "???" size 27 color SPRING_MUTED xalign 0.5
        text "CH01을 마치면 첫 회의의 메모가 열립니다. 이벤트 CG 원화는 준비 중입니다." xpos 485 ypos 890 size 24 color SPRING_MUTED
    elif gallery_tab == "배경":
        add "bg campus" xpos 480 ypos 230 xysize (1240, 698)
        text "하온대학교의 봄" xpos 520 ypos 930 font CAMPUS_NOTE_FONT size 39 color SPRING_INK
    elif gallery_tab == "배경음악":
        vbox:
            xpos 510 ypos 280 spacing 35
            text "첫 번째 봄" font CAMPUS_NOTE_FONT size 64 color SPRING_INK
            textbutton "메인 테마 듣기" action Function(play_bgm, "main") xsize 430
            text "나머지 테마는 다음 이야기와 함께 준비됩니다." size 29 color SPRING_MUTED
    else:
        text "다섯 사람의 모습은 아직 준비 중이에요.\n사진과 스탠딩은 추후 교체할 수 있습니다." xpos 540 ypos 440 size 35 color SPRING_MUTED
