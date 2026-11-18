init -10 python:
    gui.init(1920, 1080)
    gui.text_font = CAMPUS_BODY_FONT
    gui.name_text_font = CAMPUS_BODY_FONT
    gui.interface_text_font = CAMPUS_BODY_FONT
    gui.text_size = 34
    gui.name_text_size = 32
    gui.interface_text_size = 30
    gui.accent_color = "#477a9b"
    gui.text_color = "#242438"
    gui.interface_text_color = "#242438"
    gui.idle_color = "#35364e"
    gui.hover_color = "#bb447e"
    gui.selected_color = "#bb447e"
    gui.insensitive_color = "#79758a"
    config.overlay_screens.append("quick_menu")

    def ui_box(fill, border="#242438"):
        return Frame(Composite((64, 64),
            (0, 0), Solid(border, xysize=(64, 64)),
            (2, 2), Solid(fill, xysize=(60, 60))), 4, 4)

style default:
    font CAMPUS_BODY_FONT
    size 30
    color "#242438"
    language "korean-with-spaces"
style text:
    line_spacing 0
style button:
    background ui_box("#ffffff")
    hover_background ui_box("#bb447e")
    selected_background ui_box("#bb447e")
    insensitive_background Solid("#e9e8ee")
    padding (24, 13)
    activate_sound "audio/sfx/click.wav"
style button_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#35364e"
    yoffset -2
    line_spacing 0
    line_leading 0
    hover_color "#71426e"
    selected_color "#414579"
    selected_idle_color "#414579"
    selected_hover_color "#71426e"
    insensitive_color "#79758a"
style textbutton is button:
    # Textbutton has its own cached background; set the balanced surface here
    # as well as on button, rather than inheriting the old PNG's shadow padding.
    background Frame("images/ui/controls/button.png",32,32)
    hover_background Frame("images/ui/controls/button_hover.png",32,32)
    selected_background Frame("images/ui/controls/button_selected.png",32,32)
    selected_hover_background Frame("images/ui/controls/button_hover.png",32,32)
    insensitive_background Frame("images/ui/controls/button.png",32,32)
    padding (20,10)
style campus_control is button:
    # Explicit state surfaces prevent inherited idle PNGs from shifting the
    # visible centre while the selected surface uses the new balanced asset.
    background Frame("images/ui/controls/button.png",32,32)
    idle_background Frame("images/ui/controls/button.png",32,32)
    hover_background Frame("images/ui/controls/button_hover.png",32,32)
    selected_background Frame("images/ui/controls/button_selected.png",32,32)
    selected_idle_background Frame("images/ui/controls/button_selected.png",32,32)
    selected_hover_background Frame("images/ui/controls/button_hover.png",32,32)
    insensitive_background Frame("images/ui/controls/button.png",32,32)
    padding (20,10)
style campus_control_text is button_text:
    font CAMPUS_BODY_FONT
    size 25
    line_spacing 0
    line_leading 0
    xalign 0.5
    yalign 0.5
    text_align 0.5
    xoffset 2
    yoffset -2
    idle_color "#414579"
    hover_color "#71426e"
    selected_idle_color "#414579"
    selected_hover_color "#71426e"
style frame:
    background ui_box("#ffffff")
    padding (40, 32)
style title_text:
    font CAMPUS_TITLE_FONT
    size 64
    color "#242438"
style caption_text:
    size 24
    color "#62627a"
style small_button_text:
    size 24
    hover_color "#bb447e"
    selected_color "#bb447e"
style small_button:
    background None
    hover_background Solid("#f3e3ed")
    selected_background None
    padding (14, 10)
style menu_button:
    xsize 395
    ysize 66
    padding (24, 8)
style menu_button_text:
    size 30
style action_button:
    background ui_box("#bb447e")
    hover_background ui_box("#ffffff")
    padding (34, 18)
style action_button_text:
    color "#414579"
    idle_color "#414579"
    hover_color "#242438"
    size 30
    line_spacing 0
    yoffset -2
style bar:
    xsize 610
    ysize 22
    left_bar Solid("#bb447e")
    right_bar Solid("#e4dce7")
    thumb Solid("#242438")
    thumb_offset 8
style slider is bar
style scrollbar:
    xsize 10
    base_bar Solid("#e4dce7")
    thumb Solid("#bb447e")
style vscrollbar is scrollbar

screen file_slots(title, saving=False):
    use page_shell(title)
    hbox:
        xpos 110
        ypos 178
        spacing 15
        textbutton "자동" id "file_page_auto" style "campus_control" xsize 110 ysize 64 padding (16,8) text_size 25 action FilePage("auto")
        textbutton "빠른 저장" id "file_page_quick" style "campus_control" xsize 190 ysize 64 padding (16,8) text_size 25 action FilePage("quick")
        for p in range(1, 6):
            textbutton str(p) style "campus_control" id ("file_page_"+str(p)) xsize 64 ysize 64 padding (8,8) text_size 25 action FilePage(p)
    grid 3 2:
        xpos 110
        ypos 270
        spacing 26
        for slot in range(1, 7):
            $ slot_name = FileSaveName(slot) or ""
            $ slot_time = FileTime(slot, format="%Y.%m.%d  %H:%M", empty="빈 저장 공간")
            button:
                id ("file_slot_" + str(slot))
                xsize 545 ysize 322 padding (22, 16)
                background Solid("#ffffff")
                hover_background Solid("#f1d6e4")
                action (FileSave(slot) if saving else FileLoad(slot))
                alt ("저장 슬롯 " + str(slot) + " · " + slot_time + " · " + slot_name)
                tooltip slot_name
                fixed:
                    xysize (501,290)
                    # Preserve the screenshot ratio and reserve real space for both captions.
                    add Transform(FileScreenshot(slot), xysize=(496,196), fit="contain") xpos 2 id ("file_thumb_" + str(slot))
                    text slot_time id ("file_time_" + str(slot)) xpos 2 ypos 203 xsize 496 size 22 line_spacing 0
                    text (slot_name[:19] + "…" if len(slot_name) > 19 else slot_name) id ("file_name_" + str(slot)) xpos 2 ypos 248 xsize 496 size 22 line_spacing 0
    $ slot_tooltip = GetTooltip()
    if slot_tooltip:
        frame:
            id "file_name_tooltip"
            xpos 825 ypos 170 xsize 1000
            padding (24,14)
            text slot_tooltip id "file_name_full" xmaximum 950 size 22 line_spacing 3
    hbox:
        xpos 110
        ypos 970
        spacing 30
        textbutton "이전 페이지" id "file_prev" style "campus_control" xsize 230 ysize 64 padding (18,8) text_size 25 action FilePagePrevious()
        fixed:
            xsize 120 ysize 64
            text "[FilePageName(auto='자동 저장', quick='빠른 저장')]" id "file_page_label" size 24 line_spacing 0 text_align 0.5 xalign 0.5 yalign 0.5
        textbutton "다음 페이지" id "file_next" style "campus_control" xsize 230 ysize 64 padding (18,8) text_size 25 action FilePageNext()

screen save():
    tag menu
    use file_slots("이 순간을 저장", True)
screen load():
    tag menu
    use file_slots("이야기 불러오기")

screen history():
    tag menu
    use page_shell("지나간 대화")
    viewport:
        xpos 130
        ypos 210
        xsize 1635
        ysize 745
        mousewheel True
        draggable True
        scrollbars "vertical"
        has vbox
        spacing 28
        if not _history_list:
            text "아직 기록된 대화가 없습니다." size 30
        for h in _history_list:
            vbox:
                spacing 8
                if h.who:
                    text h.who size 27 bold True
                text h.what size 30 xmaximum 1500 substitute False

screen cg_view(cg):
    modal True
    zorder 210
    add Solid("#172d41ef")
    add cg_asset(cg) xalign 0.5 yalign 0.5 xysize (1600, 900)
    textbutton "닫기" xpos 1700 ypos 50 action Hide("cg_view") text_color "#ffffff"
    key "game_menu" action Hide("cg_view")

screen notify(message):
    zorder 200
    frame:
        xpos 75
        ypos 80
        xmaximum 1760
        text message id "notify_text" size 28 xmaximum 1660
    timer 3.0 action Hide("notify")

screen skip_indicator():
    zorder 110
    text "대사를 건너뛰는 중" xpos 1390 ypos 48 size 26 color "#242438" outlines [(2, "#ffffff", 0, 0)]

screen help():
    tag menu
    use page_shell("조작 방법")
    vbox:
        xpos 140
        ypos 230
        xsize 1640
        spacing 32
        for keys, detail in [("클릭 / Enter / Space", "다음 대사 · 선택 확인"), ("방향키 / Tab", "버튼과 선택지 사이 이동"), ("Esc / 오른쪽 클릭", "환경설정 · 돌아가기"), ("마우스 휠 위 / Page Up", "지난 대사로 되돌아가기"), ("Ctrl / Tab", "읽은 대사 건너뛰기 / 전환"), ("H / F / S", "대사창 숨기기 / 전체 화면 / 화면 저장")]:
            hbox:
                text keys xsize 620 size 32
                text detail size 30 xmaximum 980
        text "아래 빠른 메뉴에서 기록·자동 진행·저장·불러오기를 사용할 수 있습니다." size 27 xmaximum 1640 color "#62627a"

screen _developer_room_body():
    use page_shell("개발실")
    viewport:
        id "developer_routes_viewport"
        xpos 120 ypos 208 xysize (850,635)
        mousewheel True draggable True
        vbox:
            xsize 820 spacing 20
            text "개별 루트 · 진행 점검" size 40
            for key in HEROINE_ORDER:
                textbutton (HEROINES[key]["name"] + "  /  " + ROUTES[key]["title"]):
                    action Function(renpy.call_in_new_context, "route_" + key)
            textbutton "메타 연출 테스트" style "action_button" action ShowMenu("meta_test")
            text "완성된 일반 엔딩을 1개 이상 보면 메타 연출이 열립니다." style "caption_text"
            textbutton ("사진·스티커 미리보기: 켜짐" if profile_debug_unlock else "사진·스티커 미리보기: 꺼짐"):
                action ToggleVariable("profile_debug_unlock")
    viewport:
        id "developer_stats_viewport"
        xpos 1050 ypos 208 xysize (740,635)
        mousewheel True draggable True
        vbox:
            xsize 720 spacing 24
            text "현재 관계" size 40
            for key in HEROINE_ORDER:
                text (HEROINES[key]["name"] + "  ·  해피 호감도 " + str(heart_value(key, "happy")) + " / 배드 호감도 " + str(heart_value(key, "bad"))) size 27
            text "CH07 최종 선택 · 점수 제한 없음\n로만 R01~R06 · 시아 S01~S06 · 다림 D01~D06 · 오므 O01~O06 구현\n시크릿: 로만·시아·다림·오므" style "caption_text"
            textbutton "15개 엔딩 ID 검사 · 임시 기록" xsize 700 text_size 24 action [SetVariable("sandbox_endings", set(ENDINGS)), Notify("임시 해금 15개를 검사했습니다. 실제 수집 기록은 바뀌지 않습니다.")]
            text "임시 해금: [len(sandbox_endings)] / 15" size 27
            text "실제 엔딩 기록: [len(persistent.endings)] / 15" size 27

screen _meta_test_body(simulation, changed):
    use page_shell("메타 연출 · 안전한 시험 화면")
    viewport:
        id "meta_content_viewport"
        xpos 140 ypos 225 xysize (1640,730)
        mousewheel True draggable True
        vbox:
            xsize 1600 spacing 24
            text ("일반 엔딩 조건: 충족" if meta_unlocked() else "일반 엔딩 조건: 잠김") size 36
            text "담당 히로인은 미정입니다. 이 화면의 화자는 ‘테스트 화자’입니다." size 29
            textbutton "일반 엔딩을 본 상황 가정" action ToggleScreenVariable("simulation") selected simulation
            textbutton "가상의 대화창과 학생증 바꾸기":
                sensitive simulation or meta_unlocked()
                action ToggleScreenVariable("changed")
            frame:
                xsize 1580
                ysize 310
                vbox:
                    spacing 20
                    text ("학생증 · 화면 밖의 당신에게" if changed else "학생증 · " + player_name) size 35
                    text ("테스트 화자: ‘[player_name]’이라는 이름 뒤에서, 선택해 준 당신을 기다렸어요." if changed else "테스트 화자: 아직 평범한 캠퍼스의 대화입니다.") size 30 xmaximum 1470
                    text ("다른 선택의 기억: " + str(len(persistent.choice_memories)) + "개 · 완료 시점에 보관된 게임 기록만 읽습니다.") style "caption_text"
            text "이름과 ‘화면 밖의 당신’을 구분하는 허구의 연출입니다.\n운영체제·개인정보·실제 파일에는 접근하지 않습니다." size 27 color "#62627a"

screen demo_complete():
    tag menu
    modal True
    use page_shell("첫 회의, 그리고 다음 약속")
    vbox:
        xpos 160
        ypos 250
        xsize 1600
        spacing 34
        text "CH01을 마쳤습니다." style "title_text" size 60
        text "축제 준비팀에 당신의 자리가 생겼습니다.\n누군가와 조금 가까워졌다면, 학생증 뒷면을 펼쳐 보세요." size 32
        text "다음 이야기  ·  CH02 우리 옆 부스가 수상하다" size 32 color "#bb447e"
        text "이어서 CH02와 CH03을 플레이할 수 있습니다.\n이번 완료 기록은 일반 엔딩으로 계산되지 않습니다." style "caption_text"
        hbox:
            spacing 25
            textbutton "다음 챕터로" style "action_button" action Return("next_chapter")
            textbutton "학생증 보기" action ShowMenu("profiles")
            textbutton "갤러리 보기" action ShowMenu("gallery")
            textbutton "메인 메뉴로" action MainMenu(confirm=False)

