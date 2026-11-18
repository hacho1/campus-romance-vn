# Existing spring UI stays intact; these screens add reusable story staging.
transform story_motion_idle(token=0):
    zoom 1.0
    rotate 0
    xoffset 0
    yoffset 0

transform story_motion_jump(token=0):
    subpixel True
    zoom 1.0
    yoffset 0
    easeout 0.12 yoffset -22
    easein 0.14 yoffset 0

transform story_motion_surprise(token=0):
    zoom 1.0
    easeout 0.10 zoom 1.10
    easein 0.14 zoom 1.0

transform story_motion_shake(token=0):
    xoffset 0
    linear 0.05 xoffset -9
    linear 0.05 xoffset 9
    linear 0.05 xoffset -6
    linear 0.05 xoffset 0

transform story_motion_tilt(token=0):
    rotate 0
    easeout 0.14 rotate -6
    easein 0.14 rotate 0

transform story_motion_shrink(token=0):
    zoom 1.0
    easeout 0.20 zoom 0.72

transform story_motion_angry(token=0):
    yoffset 0
    easeout 0.10 yoffset -7
    easein 0.12 yoffset 0

transform story_motion_move(token=0, dx=0, dy=0):
    subpixel True
    xoffset dx
    yoffset dy
    easeout 0.25 xoffset 0 yoffset 0

init -7 python:
    def story_actor_motion(kind="idle", token=0, dx=0, dy=0):
        if not _preferences.transitions:
            return Transform(zoom=0.72 if kind == "shrink" else 1.0)
        if kind == "move":
            return story_motion_move(token,dx,dy)
        name = "jump" if kind == "group" else kind
        if name not in ("jump", "surprise", "shake", "tilt", "shrink", "angry"):
            name = "idle"
        return globals()["story_motion_" + name](token)


screen story_stage_view():
    zorder -10
    if not main_menu and not renpy.context()._menu and story_standing_available():
        add Solid("#eef4f529")
        for entry in story_render_entries():
            $ actor = entry["actor"]
            $ actor_data = STORY_CAST[actor]
            $ face = entry["face"]
            $ art = story_asset(actor,face)
            $ actor_x, actor_y = entry["position"]
            $ icon = None if entry["outgoing"] else story_icon_for(actor)
            fixed:
                id ("standing_actor_" + actor)
                pos (int(actor_x),int(actor_y))
                anchor (0.5,1.0)
                xysize (530,780)
                at Transform(function=partial(story_actor_motion_transform,actor))
                fixed:
                    id ("standing_visual_" + actor)
                    xysize (530,780)
                    at Transform(function=partial(story_focus_transform,actor))
                    if art and art.startswith(LD_STANDING_ROOT):
                        # Keep the head below the HUD and the legs behind the dialogue.
                        add Transform(art, xysize=(STORY_STANDING_WIDTH, STORY_STANDING_WIDTH*3//2), fit="contain", xzoom=entry["facing"], xalign=0.5, ypos=182, yanchor=0.0) id ("standing_art_" + actor)
                    elif art:
                        add Transform(art,xysize=(530,780),fit="contain",xzoom=entry["facing"]) xalign 0.5 yalign 1.0
                    else:
                        frame:
                            xalign 0.5 yalign 1.0 xysize (330,510)
                            background spring_panel("paper")
                            padding (20,22)
                            vbox:
                                xalign 0.5 yalign 0.5 spacing 30
                                add Solid(actor_data["color"]) xysize (190,6) xalign 0.5
                                text actor_data["name"] size 43 line_spacing 0 bold True xalign 0.5 color SPRING_INK
                                text STORY_FACE_GLYPHS[face] size 58 line_spacing 0 xalign 0.5 color SPRING_INK
                                text STORY_FACE_LABELS[face] size 27 line_spacing 0 xalign 0.5 color "#65698d"
                                text "일러스트 준비 중" size 23 line_spacing 0 xalign 0.5 color "#65698d"
                if icon and icon[0] == "heart":
                    add "images/ui/stage_effects/heart.svg":
                        id ("standing_icon_" + actor)
                        pos (420,286) anchor (0.5,0.5)
                        xysize (48,48)
                        at (Transform(function=partial(story_heart_motion_transform, icon), subpixel=True) if _preferences.transitions else Transform())
                elif icon:
                    add ("images/ui/stage_effects/" + icon[0] + ".svg") id ("standing_icon_" + actor) xpos 382 ypos 162 xysize (64,64)
        if story_exiting or story_reaction_icons:
            timer 0.05 repeat True action Function(story_motion_tick)


transform story_insert_arrival():
    on show:
        alpha 0.0
        yoffset 16
        easeout .18 alpha 1.0 yoffset 0

screen campus_recruitment_notice(show_postscript=False):
    zorder 10
    if not _windows_hidden and not main_menu and not renpy.context()._menu:
        $ art = "images/props/campus_recruitment_notice.webp"
        fixed:
            id "campus_recruitment_notice_sheet"
            xpos 1074 ypos 190 xanchor 0.5 xysize (626,478)
            at (story_insert_arrival() if _preferences.transitions else Transform())
            add Solid("#3342542b") xpos 7 ypos 9 xysize (626,478)
            if renpy.loadable(art):
                add art id "campus_recruitment_notice_art" xysize (626,478)
                add Solid("#f8e7ec") xalign 0.5 ypos 24 xysize (278,73)
            else:
                add Solid("#fffaf2") xysize (626,478)
                add Solid("#e8dbf0") xysize (626,7)
                add "images/ui/spring/tape.svg" xpos 448 ypos 24 xysize (136,22)
            text "축제 연합 프로젝트" xalign 0.5 ypos 45 font CAMPUS_BODY_FONT size 26 bold True line_spacing 0 color "#635078"
            text "추가 팀원 모집!" xalign 0.5 ypos 99 font CAMPUS_TITLE_FONT size 60 line_spacing 0 color "#34415b"
            add Solid("#e5dbe8") xpos 44 ypos 187 xysize (538,2)
            text "전공 무관! 경험 무관!\n새로운 사람 환영!" xpos 44 ypos 212 xmaximum 538 font CAMPUS_BODY_FONT size 29 line_spacing 5 color "#34415b"
            text "함께 대학 축제를 만들어 갈 분을 찾습니다!" xpos 44 ypos 319 xmaximum 538 font CAMPUS_BODY_FONT size 27 line_spacing 0 color "#34415b"
            if show_postscript:
                add Solid("#f1e8f3") xpos 34 ypos 394 xysize (558,53)
                text "※ 정상적인 소통이 가능한 분을 찾습니다." id "campus_recruitment_notice_postscript" xpos 46 ypos 403 xmaximum 534 font CAMPUS_BODY_FONT size 24 line_spacing 0 color "#554465"

screen campus_space_notice():
    zorder 10
    if not _windows_hidden and not main_menu and not renpy.context()._menu:
        frame:
            id "campus_space_notice_sheet"
            xalign 0.5 ypos 204 xysize (700,340)
            background spring_panel("paper")
            padding (52,38)
            at (story_insert_arrival() if _preferences.transitions else Transform())
            vbox:
                spacing 19
                text "축제 운영위원회" font CAMPUS_BODY_FONT size 24 color SPRING_MUTED
                text "부스 공간 배정 변경" font CAMPUS_TITLE_FONT size 42 color SPRING_INK
                add Solid("#dcd5eb") xysize (580,2)
                text "신청 구역의 사용 가능 공간이 줄었습니다.\n상세 도면은 추후 공지합니다." font CAMPUS_BODY_FONT size 28 line_spacing 12 color SPRING_INK

screen story_prop_insert(prop):
    zorder 10
    if prop == "rival_samples" and not _windows_hidden and not main_menu and not renpy.context()._menu:
        $ art = "images/props/rival_samples.webp"
        frame:
            id "story_prop_rival_samples"
            xalign 0.5 ypos 255 xysize (748,397)
            background spring_panel("paper")
            padding (26,26)
            at (story_insert_arrival() if _preferences.transitions else Transform())
            if renpy.loadable(art):
                add Transform(art, xysize=(696,345), fit="contain") align (0.5,0.5) alt "디저트 부스 시제품. 포장 쿠키와 질문 카드."
            else:
                vbox:
                    align (0.5,0.5)
                    spacing 22
                    text "디저트 부스 시제품" font CAMPUS_TITLE_FONT size 44 color SPRING_INK xalign 0.5
                    text "개별 포장 쿠키 · 손바닥 크기 질문 카드" font CAMPUS_BODY_FONT size 28 color SPRING_MUTED xalign 0.5

screen chapters_complete():
    tag menu
    modal True
    $ latest_chapter = max(3, min(7, story_chapter_number))
    $ next_story_title = {3: "장난이었는데, 왜 신경 쓰이지?", 4: "축제까지 앞으로 일주일", 5: "오늘만큼은, 조금 특별하게", 6: "우리 사이, 그 이상의 시작", 7: "선택한 사람과의 다음 이야기"}[latest_chapter]
    use page_shell("함께 보낸 날들, 그리고 다음 약속")
    vbox:
        xpos 150 ypos 240 xsize 1600 spacing 28
        if selected_route == "sia" and sia_s02_complete:
            text "시아의 다음 이야기가 도착했습니다" style "title_text" size 59
            text "S03부터 계속 읽을 수 있습니다." size 34
            text "현재 이름과 선택 기록을 유지한 채 이어집니다." size 30 color "#865989"
        elif selected_route == "omu" and not omu_o01_complete:
            text "오므의 이야기가 도착했습니다" style "title_text" size 59
            text "O01부터 계속 읽을 수 있습니다." size 34
            text "현재 이름과 선택 기록을 유지한 채 이어집니다." size 30 color "#865989"
        elif selected_route == "darim" and not darim_d01_complete:
            text "다림의 이야기가 도착했습니다" style "title_text" size 59
            text "D01부터 계속 읽을 수 있습니다." size 34
            text "현재 이름과 선택 기록을 유지한 채 이어집니다." size 30 color "#865989"
        elif selected_route == "lumi" and not harin_h01_complete:
            text "하린의 이야기가 도착했습니다" style "title_text" size 59
            text "H01부터 계속 읽을 수 있습니다." size 34
            text "현재 이름과 선택 기록을 유지한 채 이어집니다." size 30 color "#865989"
        else:
            text ("CH{:02d}까지 플레이 완료".format(latest_chapter)) style "title_text" size 59
            text "함께 준비하던 사람들이, 조금은 특별해졌습니다." size 34
            text ("다음 이야기 · " + next_story_title) size 32 color "#865989"
            if latest_chapter == 7:
                text "다섯 사람의 개별 루트와 해피·배드·시크릿 이야기를 플레이할 수 있습니다." style "caption_text"
        hbox:
            spacing 25
            if selected_route == "sia" and sia_s02_complete:
                textbutton "시아 S03 이어서" action Jump("sia_s03")
                textbutton "기록 저장" action ShowMenu("save")
            elif selected_route == "omu" and not omu_o01_complete:
                textbutton "오므 O01 이어서" id "omu_pending_continue" action Jump("omu_o01")
                textbutton "기록 저장" action ShowMenu("save")
            elif selected_route == "darim" and not darim_d01_complete:
                textbutton "다림 D01 이어서" id "darim_pending_continue" action Jump("darim_d01")
                textbutton "기록 저장" action ShowMenu("save")
            elif selected_route == "lumi" and not harin_h01_complete:
                textbutton "하린 H01 이어서" id "harin_pending_continue" action Jump("harin_h01")
                textbutton "기록 저장" action ShowMenu("save")
            if latest_chapter < 7:
                textbutton ("CH{:02d} 이어서 시작".format(latest_chapter + 1)) action Jump("chapter{:02d}".format(latest_chapter + 1))
            textbutton "학생증 보기" action ShowMenu("profiles")
            textbutton "갤러리 보기" action ShowMenu("gallery")
            textbutton "메인 메뉴로" action MainMenu(confirm=False)

screen chapter_developer():
    tag menu
    use page_shell("챕터 연출 점검")
    if config.developer:
        vbox:
            xpos 130 ypos 220 spacing 20
            text "공통 루트" size 34
            for number, title in [(1,"이 조합으로 축제가 가능해?"),(2,"우리 옆 부스가 수상하다"),(3,"시범 운영부터 사고라고?"),(4,"장난이었는데, 왜 신경 쓰이지?"),(5,"축제까지 앞으로 일주일"),(6,"오늘만큼은, 조금 특별하게"),(7,"우리 사이, 그 이상의 시작")]:
                textbutton ("CH0" + str(number) + " · " + title) xsize 800 action Start("chapter0" + str(number))
            textbutton "SD 이벤트 컷" xsize 800 action Start("story_sd_preview")
            textbutton "휴대폰 UI 미리보기" xsize 800 action Start("phone_ui_preview")
        vbox:
            xpos 1040 ypos 220 spacing 20
            text "개별 이벤트 · CH03" size 34
            for actor in STORY_HEROES:
                textbutton STORY_CAST[actor]["name"] xsize 600 action Start("debug_ch03_"+actor)
            textbutton "일반 스탠딩 · 모션 시연" xsize 600 action Start("standing_motion_preview")
        vbox:
            xpos 140 ypos 855 spacing 5
            text ("작업 상대 · " + str(first_task_partner)) size 24
            text ("CH02 상대 · " + str(ch02_partner)) size 24
            text ("CH03 상대 · " + str(ch03_partner)) size 24
            text ("협력 · " + str(rival_cooperation)) size 24
            text ("특별한 순간 · " + str(sum(special_moment.values()))) size 24
    else:
        text "이 화면은 현재 사용할 수 없습니다." xpos 200 ypos 300 size 32

# Actual debug screens guard their contents, even if called directly.
screen developer_room():
    tag menu
    if config.developer:
        use _developer_room_body()
        textbutton "공통 루트 · 챕터와 SD 연출" xpos 115 ypos 875 action ShowMenu("chapter_developer")
    else:
        use page_shell("화면 안내")
        text "이 화면은 현재 사용할 수 없습니다." xpos 200 ypos 300 size 32

screen meta_test():
    tag menu
    default simulation = False
    default changed = False
    if config.developer:
        use _meta_test_body(simulation, changed)
    else:
        use page_shell("화면 안내")
        text "이 화면은 현재 사용할 수 없습니다." xpos 200 ypos 300 size 32

# Developer-only manual controls. Presentation helpers never add story choices.
screen standing_motion_demo_controls():
    modal True
    zorder 180
    default selected = "roman"
    if config.developer:
        frame:
            xalign 0.5 ypos 36 xsize 1120
            background spring_panel("paper")
            padding (28,20)
            vbox:
                spacing 12
                text "일반 스탠딩 모션 시연" xalign 0.5 text_align 0.5 font CAMPUS_TITLE_FONT size 34 line_spacing 0
                hbox:
                    xalign 0.5 spacing 16
                    textbutton "로만 발화" action [SetScreenVariable("selected","roman"),Function(story_preview_focus,"roman")]
                    textbutton "시아 발화" action [SetScreenVariable("selected","sia"),Function(story_preview_focus,"sia")]
                    textbutton "해설 · 모두 기본" action Function(story_preview_focus,"narrator")
        frame:
            xalign 0.5 ypos 864 xsize 1780
            background spring_panel("paper")
            padding (22,16)
            vbox:
                spacing 12
                hbox:
                    xalign 0.5 spacing 12
                    textbutton "점프" action Function(story_preview_action,story_effect,"jump",selected)
                    textbutton "흔들림" action Function(story_preview_action,story_effect,"shake",selected)
                    textbutton "작은 하트" action Function(story_preview_action,story_icon,selected,"heart")
                    textbutton "느낌표" action Function(story_preview_action,story_icon,selected,"exclamation")
                    textbutton "전구" action Function(story_preview_action,story_icon,selected,"lightbulb")
                hbox:
                    xalign 0.5 spacing 12
                    textbutton "왼쪽 입장" action Function(story_preview_action,story_enter,selected,"left")
                    textbutton "오른쪽 입장" action Function(story_preview_action,story_enter,selected,"right")
                    textbutton "왼쪽 퇴장" action Function(story_preview_action,story_exit,selected,"left")
                    textbutton "오른쪽 퇴장" action Function(story_preview_action,story_exit,selected,"right")
                    textbutton "시연 끝내기" action Return()
    else:
        timer 0.01 action Return()
    key "game_menu" action Return()
