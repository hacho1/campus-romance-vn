# Keep whole-scene SD faces and gestures visible while choosing a reply.
init offset = 900

screen campus_sd_choice(items):
    modal True
    add Solid("#7b75aa28")
    # A menu prompt shares the dialogue window at the bottom of the screen.
    $ dialogue_visible = renpy.get_widget("say", "window") is not None
    $ first_row_y = 116 if dialogue_visible else 780
    $ two_columns = len(items) > 3
    $ button_width = 840 if two_columns else (1170 if dialogue_visible else 1640)
    for index, item in enumerate(items):
        $ row = index // 2 if two_columns else index
        $ button_x = (100 + (index % 2) * 880) if two_columns else (1920 - button_width) // 2
        if two_columns and len(items) % 2 and index == len(items) - 1:
            $ button_x = 540
        button:
            id ("sd_choice_" + str(index))
            action item.action
            xpos button_x ypos (first_row_y + row * 94)
            xsize button_width ysize 80
            background spring_panel("button")
            hover_background spring_panel("button_hover")
            padding (32, 12)
            text item.caption:
                size 32 color SPRING_INK
                xmaximum (button_width - 64)
                xalign 0.5 yalign 0.5 text_align 0.5
                line_spacing 0
