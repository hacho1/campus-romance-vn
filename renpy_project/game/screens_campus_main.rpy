# Main title refresh: the illustration owns the middle of the screen.
# This file overrides earlier main_menu declarations without changing the spring
# dialogue, SD event, save/load, or scrapbook systems.
init offset = 900

init python:
    def campus_main_art():
        # Gallery registry is the canonical source. Retain a safe fallback while
        # importing this screen alone or before a future registry is available.
        resolver = getattr(store, "cg_asset", None)
        if resolver is not None:
            result = resolver("ld_01")
            if result:
                return result
        for suffix in (".webp", ".png"):
            path = "images/cg/ld_01_main_visual" + suffix
            if renpy.loadable(path):
                return path
        return None

    def campus_main_visit():
        # Ignore the registry's boolean return value; an on-show callback must
        # not accidentally finish the current main-menu interaction.
        unlock = getattr(store, "cg_unlock", None)
        if unlock is not None:
            unlock("ld_01")

style campus_title_logo:
    alt config.name

style campus_title_button is button:
    xsize 380
    ysize 54
    padding (16, 4)
    background None
    hover_background "images/ui/campus_main/menu_hover.svg"
    selected_background None
    selected_hover_background "images/ui/campus_main/menu_hover.svg"
    insensitive_background None
    activate_sound "audio/sfx/click.wav"

style campus_title_button_text is button_text:
    font CAMPUS_BODY_FONT
    size 29
    color "#3c596b"
    hover_color "#235c73"
    selected_color "#3c596b"
    selected_hover_color "#235c73"
    insensitive_color "#8e9ba5"
    xalign 0.5
    yalign 0.5
    text_align 0.5
    yoffset -2
    line_spacing 0

style campus_title_secondary is button:
    padding (12, 8)
    background None
    hover_background None
    selected_background None
    insensitive_background None
    activate_sound "audio/sfx/click.wav"

style campus_title_secondary_text is button_text:
    font CAMPUS_BODY_FONT
    size 23
    color "#526b7c"
    hover_color "#287388"
    selected_color "#526b7c"
    insensitive_color "#96a2ab"

screen main_menu():
    tag menu
    on "show" action Function(campus_main_visit)
    $ title_art = campus_main_art()
    add Solid("#f6fbfd")
    if title_art:
        add Transform(title_art, xysize=(1920,1080), fit="cover")
    else:
        # No final heroine artwork is synthesized. The established campus
        # background is a temporary visual until the five-heroine CG arrives.
        add Transform("bg campus", xysize=(1920,1080), fit="cover")
        add Solid("#edf7fc20")
    add "images/ui/campus_main/main_wash.svg" xysize (1920,1080)

    vbox:
        xpos 960 ypos 62 xanchor 0.5 spacing 15
        add Transform("images/ui/campus_main/title_calligraphy.png", xysize=(540, 91), fit="contain", xalign=0.5, style="campus_title_logo"):
            id "main_title"
        text "같은 봄, 조금 다른 우리" font CAMPUS_BODY_FONT size 23 line_spacing 0 color "#586b7c" xalign 0.5

    if not title_art:
        text "메인 일러스트 준비 중" xpos 960 ypos 744 xanchor 0.5 size 23 color "#586d80" outlines [(2,"#ffffffcc",0,0)]

    fixed:
        xpos 530 ypos 815 xysize (860,225)
        add "images/ui/campus_main/menu_panel.svg" xysize (860,225)
        grid 2 3:
            xalign 0.5 yalign 0.48
            xspacing 20 yspacing 10
            for caption, target in [("게임 시작",Start()), ("불러오기",ShowMenu("load")), ("갤러리",ShowMenu("gallery")), ("CC대 학생들",ShowMenu("profiles")), ("엔딩",ShowMenu("endings")), ("옵션",ShowMenu("preferences"))]:
                textbutton caption:
                    style "campus_title_button"
                    text_style "campus_title_button_text"
                    text_bold caption == "게임 시작"
                    action target

    # Preserve continuation and quitting as quiet secondary actions rather
    # than adding rows to the six requested primary menu entries.
    textbutton "이어하기":
        xpos 58 ypos 48
        style "campus_title_secondary"
        text_style "campus_title_secondary_text"
        sensitive bool(renpy.newest_slot())
        action Function(continue_action)
    textbutton "게임 종료":
        xpos 1850 ypos 48 xanchor 1.0
        style "campus_title_secondary"
        text_style "campus_title_secondary_text"
        action Quit(confirm=True)

    if CAMPUS_TEST_BUILD:
        textbutton "챕터 선택 · 테스트":
            id "main_test_chapters"
            xpos 58 ypos 1024
            style "campus_title_secondary"
            text_style "campus_title_secondary_text"
            text_size 21
            action ShowMenu("test_chapters")

    if config.developer:
        textbutton "개발실":
            xpos 1835 ypos 1024 xanchor 1.0
            style "campus_title_secondary"
            text_style "campus_title_secondary_text"
            text_size 21
            action ShowMenu("developer_room")
