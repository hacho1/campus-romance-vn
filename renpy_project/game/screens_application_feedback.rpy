# Small, authored UI geometry only. No character or event artwork is generated.
transform application_page_fold:
    subpixel True
    xzoom 1.0
    yzoom 1.0
    rotate 0
    easeout 0.24 xzoom 0.62 yzoom 0.92 rotate -8

transform application_fold_settle:
    subpixel True
    zoom 0.94
    rotate -8
    easeout 0.22 zoom 0.86 rotate -18

transform application_plane_send:
    subpixel True
    xpos 960 ypos 438
    anchor (0.5, 0.5)
    rotate -14
    zoom 0.88
    alpha 1.0
    easeout 0.54 xpos 1320 ypos 248 rotate -28 zoom 0.54 alpha 0.0

transform application_notice_reveal:
    alpha 0.0
    easeout 0.16 alpha 1.0

transform relationship_feedback_reveal(token=0):
    subpixel True
    alpha 0.0
    xoffset -12
    easeout 0.16 alpha 1.0 xoffset 0

screen application_send_animation():
    modal True
    zorder 240
    default phase = 0
    add Solid("#f5f8fc")
    add "images/ui/application/send_path.svg" xpos 610 ypos 250 xysize (710,340)
    if phase == 0:
        add "images/ui/application/paper_open.svg" xalign 0.5 ypos 270 xysize (420,330) at (application_page_fold if _preferences.transitions else Transform())
    elif phase == 1:
        add "images/ui/application/paper_fold.svg" xalign 0.5 ypos 275 xysize (420,330) at (application_fold_settle if _preferences.transitions else Transform())
    elif phase == 2:
        if _preferences.transitions:
            add "images/ui/application/paper_plane.svg" xysize (330,230) at application_plane_send
        else:
            add "images/ui/application/paper_plane.svg" xalign 0.5 ypos 330 xysize (330,230)
    else:
        vbox:
            xalign 0.5 ypos 300 spacing 24
            at application_notice_reveal
            fixed:
                xalign 0.5 xysize (220,140)
                add "images/ui/application/paper_plane.svg" xpos 4 ypos 0 xysize (180,140)
                add "images/ui/application/sent_check.svg" xpos 158 ypos 76 xysize (52,52)
            text "전송완료" xalign 0.5 text_align 0.5 font CAMPUS_TITLE_FONT size 52 line_spacing 0 color "#293f49"
            text "참가 신청서가 전달되었습니다." xalign 0.5 text_align 0.5 font CAMPUS_BODY_FONT size 28 line_spacing 0 color "#435e6c"
    if phase < 3:
        text "신청서를 보내는 중" xalign 0.5 ypos 690 text_align 0.5 font CAMPUS_BODY_FONT size 30 line_spacing 0 color "#293f49"
    timer 0.26 action SetScreenVariable("phase", 1)
    timer 0.50 action SetScreenVariable("phase", 2)
    timer 1.08 action SetScreenVariable("phase", 3)
    timer 1.94 action Return()
    key "dismiss" action NullAction()
    key "game_menu" action NullAction()
    key "rollback" action NullAction()
    key "skip" action NullAction()

screen relationship_feedback_view():
    zorder 140
    if relationship_feedback_items and not main_menu and not renpy.get_screen("application_send_animation"):
        frame:
            id "relationship_feedback_panel"
            xpos 44 ypos 168 xsize 340
            background Frame("images/ui/controls/button.png",32,32)
            padding (22,18)
            at (relationship_feedback_reveal(relationship_feedback_serial) if _preferences.transitions else Transform())
            vbox:
                xsize 296 spacing 14
                for item in relationship_feedback_items:
                    vbox:
                        xsize 296 spacing 5
                        fixed:
                            id ("feedback_name_row_" + item["actor"])
                            xysize (296,44)
                            text item["name"] id ("feedback_name_" + item["actor"]) font CAMPUS_BODY_FONT size 27 line_spacing 0 line_leading 0 color "#293f49" bold True xalign .5 yalign .5 yoffset -2 text_align .5
                        for kind, caption in (("red","해피 호감도"), ("black","배드 호감도")):
                            if item[kind]:
                                fixed:
                                    id ("feedback_row_" + item["actor"] + "_" + kind)
                                    xysize (296,42)
                                    add heart_icon(kind, 26) xpos 0 yalign .5
                                    fixed:
                                        id ("feedback_caption_cell_" + item["actor"] + "_" + kind)
                                        xpos 34 xysize (150,42)
                                        text caption id ("feedback_caption_" + item["actor"] + "_" + kind) font CAMPUS_BODY_FONT size 23 line_spacing 0 line_leading 0 color "#435e6c" xalign .5 yalign .5 yoffset -2 text_align .5
                                    fixed:
                                        id ("feedback_value_cell_" + item["actor"] + "_" + kind)
                                        xpos 196 xysize (72,42)
                                        text ("{:+g}".format(item[kind])) id ("feedback_delta_" + item["actor"] + "_" + kind) font CAMPUS_BODY_FONT size 25 line_spacing 0 line_leading 0 bold True color (HEART_BLACK if kind == "black" else HEART_RED) xalign .5 yalign .5 yoffset -2 text_align .5
        timer 0.1 repeat True action Function(relationship_feedback_tick)
