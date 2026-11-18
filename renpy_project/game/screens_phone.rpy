# Clear smartphone chrome; native say/menu still own all story decisions.
init offset = 900

style phone_text is text:
    font CAMPUS_BODY_FONT

style phone_button is button:
    padding (12,7)
    background None
    hover_background phone_panel("hover")
    selected_background phone_panel("reply")

style phone_button_text is button_text:
    font CAMPUS_BODY_FONT
    size 24
    color PHONE_INK
    idle_color PHONE_INK
    hover_color PHONE_INK
    selected_idle_color PHONE_INK
    selected_hover_color PHONE_INK
    xalign .5
    yalign .5
    text_align .5

screen phone_avatar(actor, diameter=52):
    fixed:
        xysize (diameter,diameter)
        $ portrait = phone_portrait(actor)
        if portrait:
            add AlphaMask(Transform(portrait,xysize=(diameter,diameter),fit="cover"),Transform("images/ui/phone/mask.svg",xysize=(diameter,diameter))) id ("phone_avatar_photo_" + str(actor))
        elif actor in STORY_HEROES:
            # Reuse the supplied character's hobby motif; no new portrait is generated.
            add ("images/ui/phone/avatar_" + actor + ".svg") xysize (diameter,diameter)
            $ inset = max(2,int(diameter * .04))
            $ motif = Composite((diameter,diameter),(inset,inset),Transform(diary_sticker(actor),xysize=(diameter-2*inset,diameter-2*inset),fit="contain"))
            add AlphaMask(motif,Transform("images/ui/phone/mask.svg",xysize=(diameter,diameter))) id ("phone_avatar_motif_" + actor)
        else:
            $ avatar_key = "mc" if actor == "mc" else "group"
            add ("images/ui/phone/avatar_" + avatar_key + ".svg") xysize (diameter,diameter)
            $ initial = "나" if actor == "mc" else "함께"
            text initial size int(diameter * .34) color PHONE_INK xalign .5 yalign .5

screen campus_location_hud():
    button:
        id "location_badge"
        xpos 60 ypos 20 xysize (520,66) padding (20,8)
        background Frame("images/ui/controls/button.png",32,32)
        hover_background Frame("images/ui/controls/button_hover.png",32,32)
        action NullAction() keyboard_focus False
        tooltip location_name alt location_name
        text campus_ui_snippet(location_name,16) id "current_location" xmaximum 480 size 28 line_spacing 0 color "#35465e" bold True yalign 0.5 yoffset -2

screen phone_arrival_gate(current_text=None):
    button:
        xysize (1920,1080) background None action NullAction()
    # The native first line still exists, but is only readable after opening its room.
    if current_text is not None:
        text current_text id "what" xpos -2000 size 1 color "#0000" slow_cps 0
    $ title = "핸드폰에 새 메시지 도착!" if phone_notification_pending else "읽던 대화가 있어요."
    use campus_normal_say(None, title + "\n위의 휴대폰 버튼을 눌러 확인해 주세요.", alert=True)
    key "dismiss" action NullAction()
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "fast_skip" action NullAction()
    key "rollforward" action NullAction()

screen phone_message(message, native_text=None):
    $ mine = phone_message_is_mine(message)
    if message["actor"] in ("system", "system_note", "unknown", "staff"):
        frame:
            xalign .5 xmaximum 538
            background None padding (14,10)
            if native_text is not None:
                text native_text id "what" size 21 line_spacing 5 text_align .5 color PHONE_MUTED slow_cps 0
            else:
                text message["text"] size 21 line_spacing 5 text_align .5 color PHONE_MUTED
    elif mine:
        hbox:
            xalign 1.0 spacing 9
            text message["time"] size 18 color PHONE_MUTED yalign 1.0
            frame:
                xmaximum 446 background phone_panel("outgoing") padding (19,14)
                if native_text is not None:
                    text native_text id "what" size 25 line_spacing 5 color PHONE_INK slow_cps 0
                else:
                    text message["text"] size 25 line_spacing 5 color PHONE_INK
    else:
        hbox:
            spacing 11
            use phone_avatar(message["actor"],46)
            vbox:
                spacing 7
                text message["name"] size 21 color PHONE_MUTED
                hbox:
                    spacing 8
                    frame:
                        xmaximum 385 background phone_panel("incoming") padding (18,14)
                        if native_text is not None:
                            text native_text id "what" size 25 line_spacing 5 color PHONE_INK slow_cps 0
                        else:
                            text message["text"] size 25 line_spacing 5 color PHONE_INK
                    text message["time"] size 18 color PHONE_MUTED yalign 1.0

screen phone_ui(current_text=None, choices=None, browsing=False):
    style_prefix "phone"
    $ room = phone_current_room()
    $ active_page = phone_view == "chat" and phone_selected_thread == phone_active_thread and not browsing
    $ voiceover = story_speaker_id in ("narrator", None)
    if not active_page:
        key "skip" action NullAction()
        key "toggle_skip" action NullAction()
        key "fast_skip" action NullAction()
        key "rollforward" action NullAction()
    if not browsing and not active_page:
        button:
            xysize (1920,1080) background None action NullAction()
        if current_text is not None:
            text current_text id "what" xpos -2000 size 1 color "#0000" slow_cps 0
    fixed:
        id "phone_shell"
        xpos 650 ypos 18 xysize (660,1018)
        at Transform(zoom=.88)
        add "images/ui/phone/shell.svg"
        fixed:
            xpos 23 ypos 44 xysize (614,918)
            text phone_clock xpos 24 ypos 5 size 21 bold True color PHONE_INK
            text "LTE   94%" xpos 470 ypos 5 size 18 color PHONE_MUTED
            text phone_perspective_label() id "phone_perspective_name" xpos 24 ypos 31 size 18 line_spacing 0 color PHONE_MUTED
            if phone_view == "lock":
                viewport:
                    ypos 54 xysize (614,860)
                    add Transform(phone_wallpaper(),xysize=(614,860),fit="cover",alpha=.22)
                text phone_clock xalign .5 ypos 170 size 82 color PHONE_INK
                text phone_date xalign .5 ypos 306 size 26 line_spacing 0 color PHONE_MUTED
                frame:
                    xpos 20 ypos 380 xsize 574 background phone_panel() padding (25,24)
                    vbox:
                        spacing 13
                        text campus_ui_snippet(phone_current_title(),18) size 27 bold True color PHONE_INK
                        text phone_preview(phone_selected_thread) size 24 line_spacing 6 color PHONE_MUTED
                textbutton "알림 열기" id "phone_open_alert" xpos 20 ypos 620 xsize 574 ysize 76 background phone_panel("reply") hover_background phone_panel("hover") text_color PHONE_INK text_size 25 action (Function(phone_set_view,"chat",phone_selected_thread or phone_active_thread) if phone_selected_thread or phone_active_thread else Function(phone_set_view,"list"))
                textbutton "채팅 목록" xalign .5 ypos 820 text_size 23 text_color PHONE_MUTED action Function(phone_set_view,"list")
            elif phone_view == "list":
                text "메시지" xpos 24 ypos 66 size 34 bold True color PHONE_INK
                textbutton "잠금화면" xpos 470 ypos 70 text_size 20 text_color PHONE_MUTED action Function(phone_set_view,"lock")
                viewport:
                    xpos 14 ypos 142 xysize (586,704) mousewheel True draggable True
                    vbox:
                        spacing 4
                        for thread_id in phone_rooms():
                            $ thread = phone_threads[thread_id]
                            button:
                                id ("phone_room_" + thread_id)
                                xsize 582 ysize 156
                                background None hover_background phone_panel("hover")
                                padding (12,20)
                                tooltip phone_thread_display_title(thread_id)
                                alt (phone_thread_display_title(thread_id) + " · " + phone_preview(thread_id))
                                action Function(phone_set_view,"chat",thread_id)
                                hbox:
                                    spacing 14
                                    use phone_avatar(phone_room_avatar_actor(thread_id),64)
                                    vbox:
                                        spacing 9 xsize 330
                                        text campus_ui_snippet(phone_thread_display_title(thread_id),12) size 25 bold True color PHONE_INK xmaximum 330 id ("phone_room_title_" + thread_id)
                                        text phone_preview(thread_id,28) size 22 line_spacing 4 color PHONE_MUTED xmaximum 330
                                    vbox:
                                        spacing 12 xsize 72
                                        text (thread["messages"][-1]["time"] if thread["messages"] else "") size 18 color PHONE_MUTED xalign 1.0
                                        if thread["unread"]:
                                            frame:
                                                xalign 1.0 background phone_panel("outgoing") padding (9,3)
                                                text ("99+" if thread["unread"] > 99 else str(thread["unread"])) size 18 color PHONE_INK
                        if not phone_rooms():
                            text "아직 도착한 대화가 없어요." size 26 color PHONE_MUTED xalign .5 ypos 180
            else:
                textbutton "채팅 목록" xpos 7 ypos 62 xsize 125 ysize 60 text_size 20 text_color PHONE_MUTED action Function(phone_set_view,"list")
                button:
                    xpos 142 ypos 63 xysize (325,46) padding (0,0)
                    background None hover_background None action NullAction()
                    tooltip phone_current_title() alt phone_current_title()
                    text campus_ui_snippet(phone_current_title(),10) id "phone_chat_title" xmaximum 325 size 30 line_spacing 0 bold True color PHONE_INK xalign .5 yalign .5 text_align .5
                text ("학교 알림" if phone_selected_thread == "campus_notice" else "단체 대화" if phone_is_group_thread(phone_selected_thread) else "개인 대화") id "phone_chat_kind" xpos 144 ypos 112 size 19 line_spacing 0 color PHONE_MUTED
                textbutton "잠금화면" xpos 476 ypos 65 text_size 19 text_color PHONE_MUTED action Function(phone_set_view,"lock")
                add Solid("#dfe7e9") xpos 20 ypos 146 xysize (574,1)
                viewport:
                    id ("phone_messages_" + str(phone_sequence))
                    xpos 20 ypos 166 xysize (574,420 if choices else 622)
                    mousewheel True draggable True yinitial 1.0
                    vbox:
                        xsize 574 spacing 18
                        for index,message in enumerate(room["messages"]):
                            if index == 0 or message.get("day_id",message.get("date")) != room["messages"][index-1].get("day_id",room["messages"][index-1].get("date")):
                                text phone_message_date_label(message) id ("phone_date_" + str(index)) xalign .5 size 19 color PHONE_MUTED text_align .5
                            $ live = current_text if active_page and not voiceover and message.get("key") == phone_last_key else None
                            use phone_message(message,live)
                if choices:
                    viewport:
                        id "phone_choice_shell"
                        xpos 20 ypos 604 xysize (574,298)
                        mousewheel True draggable True
                        vbox:
                            xsize 574 spacing 7
                            text "어떻게 답장할까?" size 21 color PHONE_MUTED
                            for item in choices:
                                button:
                                    xsize 574 yminimum 82
                                    background phone_panel("reply") hover_background phone_panel("hover")
                                    padding (21,13) action item.action
                                    hbox:
                                        spacing 17
                                        text item.caption size 24 line_spacing 4 color PHONE_INK xsize 470 yalign .5
                                        add "images/ui/phone/send.svg" xysize (28,28) yalign .5
                elif active_page:
                    textbutton "다음 메시지" id "phone_next" xpos 20 ypos 815 xsize 574 ysize 70 background phone_panel("reply") hover_background phone_panel("hover") text_color PHONE_INK text_size 24 action Function(phone_advance)
                elif not browsing and phone_active_thread:
                    textbutton "진행 중인 대화로" xpos 20 ypos 815 xsize 574 ysize 70 background phone_panel("reply") hover_background phone_panel("hover") text_color PHONE_INK text_size 24 action Function(phone_set_view,"chat",phone_active_thread)
    $ phone_title_tip = GetTooltip()
    if phone_title_tip:
        frame:
            xpos 1365 ypos 465 xsize 440 background phone_panel() padding (24,20)
            text phone_title_tip id "phone_full_title" size 24 line_spacing 6 xmaximum 392 color PHONE_INK

screen phone_browser():
    style_prefix "phone"
    modal True zorder 180
    add Solid("#e9f0f5b8") xysize (1920,768)
    use phone_ui(browsing=True)
    textbutton "닫기" xpos 1350 ypos 90 xsize 180 ysize 68 text_size 27 text_color PHONE_INK background phone_panel() action Function(phone_archive_close)
    key "game_menu" action Function(phone_archive_close)

screen phone_voiceover_say(who, what):
    # The larger handset ends at y=914. Keep authored narration below it,
    # rather than placing the device over the ordinary y=814 dialogue window.
    window:
        id "window"
        background spring_panel("dialogue")
        xpos 60 ypos 940 xsize 1800 ysize 126
        padding (38, 12)
        text what id "what" xsize 1724 size 30 line_spacing 4 color SPRING_INK yalign .5

screen say(who, what):
    # Keep the native SayBehavior focusable; live gate callbacks own dismissal.
    modal False
    if story_chat_active:
        if phone_is_open:
            $ active_chat = phone_view == "chat" and phone_selected_thread == phone_active_thread
            $ is_notice = story_speaker_id in ("system", "staff") or (phone_active_thread in PHONE_UI["service_threads"].values() and not phone_is_group_thread(phone_active_thread) and phone_active_thread not in PHONE_UI.get("message_threads", ()))
            $ is_narration = story_speaker_id in ("narrator", None)
            if active_chat and (is_notice or is_narration):
                # Narration stays in the native bottom window, outside message history.
                use phone_ui()
                use phone_voiceover_say(who, what)
            else:
                use phone_ui(current_text=what)
                use campus_location_hud()
                if phone_view == "lock" and phone_selected_thread == phone_active_thread and phone_current_room().get("unread", 0):
                    use phone_voiceover_say(None, "알림을 열어 확인해 주세요.")
        else:
            use phone_arrival_gate(current_text=what)
    else:
        use campus_normal_say(who,what)

screen choice(items):
    modal True
    zorder 150
    if story_chat_active:
        if phone_is_open:
            use phone_ui(choices=items)
        else:
            use phone_arrival_gate()
    elif sd_event_is_active() and len(items) <= 6:
        use campus_sd_choice(items)
    else:
        use campus_normal_choice(items)

screen quick_menu():
    # Higher than the modal choice, lower than archive/confirm/game-menu screens.
    zorder 170
    $ hud_active = bool(not main_menu and not renpy.context()._menu and not renpy.get_screen("phone_browser") and not renpy.get_screen("input") and not renpy.get_screen("application_send_animation") and (renpy.get_screen("say") or renpy.get_screen("choice")))
    if hud_active:
        if story_chat_active and phone_is_open:
            vbox:
                id "quick_controls"
                style_prefix "phone"
                xpos 1365 ypos 125 spacing 16
                textbutton "휴대폰 닫기" id "phone_toolbar_close" xsize 362 ysize 64 text_size 24 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action Function(phone_close_current)
                hbox:
                    spacing 14
                    textbutton "기록" id "phone_toolbar_history" xsize 174 ysize 64 text_size 25 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action ShowMenu("history")
                    textbutton "저장" id "phone_toolbar_save" xsize 174 ysize 64 text_size 25 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action ShowMenu("save")
                hbox:
                    spacing 14
                    textbutton "불러오기" id "phone_toolbar_load" xsize 174 ysize 64 text_size 25 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action ShowMenu("load")
                    textbutton "설정" id "phone_toolbar_preferences" xsize 174 ysize 64 text_size 25 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action ShowMenu("preferences")
                hbox:
                    spacing 14
                    textbutton "자동" id "phone_toolbar_auto" xsize 174 ysize 64 text_size 25 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action Preference("auto-forward","toggle")
                    textbutton "메뉴" id "phone_toolbar_menu" xsize 174 ysize 64 text_size 25 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action MainMenu(confirm=True)
        else:
            use campus_normal_quick_menu()
            if not story_chat_active:
                textbutton "UI 숨기기" id "quick_hide_ui" style "campus_control" xpos 1700 ypos 97 xsize 160 ysize 54 text_size 22 action HideInterface() tooltip "클릭하거나 H 키로 다시 표시"
            if story_chat_active or phone_threads:
                textbutton "휴대폰" id "phone_archive_button" xpos 600 ypos 25 xsize 154 ysize 56 text_size 23 text_color PHONE_INK background phone_panel() hover_background phone_panel("hover") action Function(phone_open_archive)
                if story_chat_active and phone_notification_pending:
                    add Solid("#bd5b7c") xpos 731 ypos 30 xysize (8,8)
            if story_chat_active or renpy.get_screen("choice"):
                use campus_location_hud()
            $ hud_tooltip = GetTooltip()
            if hud_tooltip:
                frame:
                    xpos 60 ypos 96 xmaximum 700 background phone_panel() padding (18,12)
                    text hud_tooltip id "hud_full_location" xmaximum 660 size 22 line_spacing 4 color PHONE_INK

screen campus_normal_say(who, what, alert=False):
    if not alert and not renpy.get_screen("choice"):
        use campus_location_hud()
    window:
        id ("phone_arrival_notice" if alert else "window")
        background spring_panel("dialogue")
        xpos 60 ypos 814 xsize 1800 ysize 235
        padding (68, 32)
        text what id ("phone_arrival_title" if alert else "what") xpos 0 ypos 12 xsize 1650 size 34 line_spacing 8 color SPRING_INK
    if who is not None:
        frame:
            id "nameplate"
            xpos 148 ypos 771 xsize campus_nameplate_width(who) ysize 80
            background spring_panel("button_selected")
            padding (20, 8)
            text who id "who" xalign 0.5 yalign 0.5 yoffset -2 text_align 0.5 line_spacing 0 size 30 color SPRING_INK bold True
    add "images/ui/spring/flowers.svg" xpos 28 ypos 946 xysize (126,126)
    add "images/ui/spring/heart.svg" xpos 1760 ypos 980 xysize (43,43)


screen campus_normal_quick_menu():
    frame:
        id "quick_controls"
        xpos 780 ypos 20 xysize (1080,66)
        background Frame("images/ui/controls/button.png",32,32)
        padding (12,8)
        hbox:
            xalign 0.5 spacing 2
            style_prefix "small"
            textbutton "자동" id "quick_auto" xsize 112 ysize 50 padding (6,7) action Preference("auto-forward", "toggle") text_size 22
            textbutton "건너뛰기" id "quick_skip" xsize 112 ysize 50 padding (6,7) action Skip() alternate Skip(fast=True, confirm=True) text_size 22
            textbutton "기록" id "quick_history" xsize 112 ysize 50 padding (6,7) action ShowMenu("history") text_size 22
            textbutton "저장" id "quick_save" xsize 112 ysize 50 padding (6,7) action ShowMenu("save") text_size 22
            textbutton "불러오기" id "quick_load" xsize 112 ysize 50 padding (6,7) action ShowMenu("load") text_size 22
            textbutton "빠른 저장" id "quick_quicksave" xsize 112 ysize 50 padding (6,7) action QuickSave() text_size 22
            textbutton "학생증" id "quick_profiles" xsize 112 ysize 50 padding (6,7) action ShowMenu("profiles") text_size 22
            textbutton "설정" id "quick_preferences" xsize 112 ysize 50 padding (6,7) action ShowMenu("preferences") text_size 22
            textbutton "메뉴" id "quick_menu" xsize 112 ysize 50 padding (6,7) action MainMenu(confirm=True) text_size 22


screen campus_normal_choice(items):
    modal True
    add Solid("#7b75aa28")
    vbox:
        xalign 0.5 yalign 0.45 spacing 17
        for item in items:
            button:
                action item.action
                xsize 1170 yminimum 100
                background spring_panel("button")
                hover_background spring_panel("button_hover")
                padding (45, 22)
                text item.caption size 32 color SPRING_INK xmaximum 1080 xalign 0.5 yalign 0.5

