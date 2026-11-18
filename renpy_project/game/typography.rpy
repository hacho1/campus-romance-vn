# Change the reading / handwritten families here, rather than editing each screen.
# Unmodified upstream TTFs and their OFL notices live together in game/fonts.
# Legacy font files stay available for old saves and optional external assets.
init -200 python:
    CAMPUS_BODY_FONT = "fonts/NotoSansKR.ttf"
    CAMPUS_NOTE_FONT = "fonts/Gaegu-Regular.ttf"
    CAMPUS_TITLE_FONT = "fonts/NotoSerifKR.ttf"

    def campus_nameplate_width(name):
        # The player may enter twelve Hangul syllables; the old 305px plate
        # only fit about eight. Keep the familiar compact plate for short names.
        plain = renpy.filter_text_tags(str(name or ""), allow=[])
        return max(305, min(560, 48 + len(plain) * 32))

    def campus_ui_snippet(value, limit):
        # Only compact metadata uses ellipsis. Story dialogue is never shortened.
        value = str(value or "")
        return value if len(value) <= limit else value[:limit - 1] + "…"

init 999 python:
    # Explicit inherited defaults also cover engine menus and future screens.
    style.default.font = CAMPUS_BODY_FONT
    style.title_text.font = CAMPUS_TITLE_FONT
    config.font_replacement_map[(CAMPUS_NOTE_FONT, True, False)] = ("fonts/Gaegu-Bold.ttf", False, False)
