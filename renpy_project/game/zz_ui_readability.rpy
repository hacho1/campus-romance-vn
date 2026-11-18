# Final active-state contrast on light paper, after the spring style init.
init 999 python:
    # Leading belongs to paragraphs, not one-line control labels. Inherited
    # 12px leading was moving the visible ink below the centre of every pill.
    style.text.line_spacing = 0
    for _ui_text_style in (style.button_text, style.textbutton_text,
            style.action_button_text, style.small_button_text,
            style.phone_button_text, style.campus_title_button_text,
            style.campus_title_secondary_text, style.campus_cg_tab_button_text,
            style.campus_cg_chrome_button_text):
        _ui_text_style.font = CAMPUS_BODY_FONT
        _ui_text_style.line_spacing = 0
        _ui_text_style.line_leading = 0
        _ui_text_style.xalign = 0.5
        _ui_text_style.xoffset = 2
        _ui_text_style.yalign = 0.5
        # Centre the visible Hangul ink as well as its font metric rectangle.
        _ui_text_style.yoffset = -2
        _ui_text_style.text_align = 0.5
        _ui_text_style.color = "#414579"
        _ui_text_style.idle_color = "#414579"
        _ui_text_style.hover_color = "#71426e"
        _ui_text_style.selected_color = "#414579"
        _ui_text_style.selected_idle_color = "#414579"
        _ui_text_style.selected_hover_color = "#71426e"
        _ui_text_style.insensitive_color = "#76758b"
        _ui_text_style.selected_insensitive_color = "#76758b"
