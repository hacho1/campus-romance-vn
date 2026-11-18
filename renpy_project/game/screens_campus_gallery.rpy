# Quiet photo-album presentation for LD CGs. This intentionally replaces the
# previous demonstration gallery while preserving its collected memo.
init offset = 900

style campus_cg_tab_button is button:
    background None
    hover_background Solid("#e7f1f6")
    selected_background Solid("#dcecf3")
    insensitive_background None
    padding (12, 8)
style campus_cg_tab_button_text is button_text:
    font CAMPUS_BODY_FONT
    size 23
    line_spacing 0
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#47546a"
    hover_color "#354d67"
    selected_color "#354d67"
    selected_idle_color "#354d67"
    selected_hover_color "#354d67"
style campus_cg_tile_button is button:
    background Frame("images/ui/diary_polish/album_card.svg",16,16)
    hover_background Frame("images/ui/diary_polish/album_card_hover.svg",16,16)
    insensitive_background Frame("images/ui/diary_polish/album_card_locked.svg",16,16)
    padding (12, 12)
style campus_cg_chrome_button is button:
    background Solid("#ffffffed")
    hover_background Solid("#deedf4")
    insensitive_background Solid("#ffffff80")
    padding (22, 10)
style campus_cg_chrome_button_text is button_text:
    size 25
    line_spacing 0
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#394b63"
    hover_color "#344f6a"
    selected_color "#394b63"
    insensitive_color "#98a5b2"

screen gallery():
    tag menu
    modal True
    zorder 160
    default gallery_tab = "COMMON"
    default gallery_page = 0
    $ active_tab = gallery_tab if gallery_tab in CG_TABS else "COMMON"
    $ keys = cg_gallery_keys(active_tab)
    $ page_count = max(1, (len(keys) + 5) // 6)
    $ page = min(max(0, gallery_page), page_count - 1)
    $ unlocked_keys = cg_unlocked_ids(keys)
    add Solid("#edf1f4")
    add "images/ui/diary_polish/album_page.svg" xpos 90 ypos 192 xysize (1740,792)
    text "갤러리" id "gallery_album_title" xpos 115 ypos 55 font CAMPUS_TITLE_FONT size 54 line_spacing 0 color CG_INK
    text "우리의 사진첩" xpos 1310 ypos 100 font CAMPUS_NOTE_FONT size 24 line_spacing 0 color CG_INK
    add diary_sticker("common") xpos 1810 ypos 145 xysize (90,90)
    text ("TEST · 전체 일러스트 열람" if campus_test_collections_preview() else "함께한 순간을 다시 펼쳐보세요.") xpos 125 ypos 143 size 23 line_spacing 0 color CG_MUTED
    textbutton "돌아가기" style "campus_cg_chrome_button" xpos 1620 ypos 65 xsize 185 ysize 64 action Return()
    add Solid("#dce5ea") xpos 120 ypos 192 xysize (1680, 1)
    hbox:
        xalign 0.5 ypos 210 spacing 14
        for tab in CG_TABS:
            textbutton tab style "campus_cg_tab_button" xsize 180 ysize 58 selected active_tab == tab action [SetScreenVariable("gallery_tab", tab), SetScreenVariable("gallery_page", 0)]
    grid 3 2:
        xpos 210 ypos 290 spacing 30
        for offset in range(6):
            $ index = page * 6 + offset
            if index < len(keys):
                $ key = keys[index]
                $ entry = cg_entry(key)
                $ collected = cg_gallery_seen(key)
                $ art = cg_asset(cg_gallery_preview(key)) if collected else None
                button:
                    id ("cg_tile_" + key.replace("/", "_"))
                    style "campus_cg_tile_button"
                    xysize (480, 330)
                    sensitive collected
                    tooltip (entry["title"] if collected else None)
                    alt (entry["title"] + " · " + entry["chapter"] + " · " + entry["scene"] + (" · 일러스트 준비 중" if not art else "") if collected else "미수집 장면")
                    action Show("cg_view", cg=key, collection=tuple(unlocked_keys))
                    fixed:
                        xysize (456, 306)
                        if collected:
                            if art:
                                add cg_displayable(cg_gallery_preview(key), size=(456, 256), thumbnail=True) id ("cg_thumb_" + key.replace("/", "_"))
                            else:
                                add Solid(entry.get("color", "#eaf0f5")) xysize (456, 256)
                                vbox:
                                    xpos 28 ypos 72 xsize 400 spacing 15
                                    text "일러스트 준비 중" size 28 color CG_INK text_align 0.5 xalign 0.5
                                    text entry["chapter"] size 22 color CG_MUTED text_align 0.5 xalign 0.5
                            text campus_ui_snippet(entry["title"],20) id ("cg_title_" + key.replace("/", "_")) xpos 8 ypos 267 xmaximum 440 size 21 line_spacing 0 color CG_INK
                        else:
                            add Solid("#e9eef2") xysize (456, 256)
                            add "images/ui/spring/lock.svg" xpos 204 ypos 83 xysize (48, 57)
                            text "아직 만나지 못한 장면" xpos 30 ypos 165 xsize 396 text_align 0.5 size 25 color "#79899b"
                            text "미수집" xpos 8 ypos 267 size 22 line_spacing 0 color "#69788a"
                        if offset in (0,5):
                            add "images/ui/spring/tape.svg" xpos 142 ypos -17 xysize (155,29)
            else:
                null width 480 height 330
    hbox:
        xalign 0.5 ypos 1002 spacing 28
        textbutton "이전 페이지" style "campus_cg_chrome_button" xsize 195 ysize 57 sensitive page > 0 action SetScreenVariable("gallery_page", page - 1)
        text (str(page + 1) + " / " + str(page_count)) yalign 0.5 size 24 color CG_INK
        textbutton "다음 페이지" style "campus_cg_chrome_button" xsize 195 ysize 57 sensitive page + 1 < page_count action SetScreenVariable("gallery_page", page + 1)
    text ("열린 장면  " + str(len(unlocked_keys)) + " / " + str(len(keys))) xpos 1510 ypos 1020 size 23 color CG_MUTED
    $ gallery_tooltip = GetTooltip()
    if gallery_tooltip:
        frame:
            xpos 580 ypos 65 xsize 900 background Solid("#fffef8f5") padding (20,12)
            text gallery_tooltip id "gallery_full_title" xmaximum 860 font CAMPUS_BODY_FONT size 22 line_spacing 0 color CG_INK
    key "game_menu" action Return()

screen cg_view(cg, collection=None):
    modal True
    zorder 240
    default current_cg = cg_gallery_key(cg)
    default cut_index = 0
    default chrome = True
    default viewer_ids = cg_unlocked_ids(collection if collection is not None else [cg])
    $ entry = cg_entry(current_cg)
    $ cuts = cg_gallery_variants(current_cg, unlocked_only=True)
    $ collected = bool(entry and cuts)
    $ current_cut = cuts[cut_index % len(cuts)] if cuts else None
    $ art = cg_asset(current_cut) if collected else None
    $ can_cycle = collected and len(cuts) > 1
    $ can_navigate = collected and len(viewer_ids) > 1 and current_cg in viewer_ids
    $ scene_dissolve = With(Dissolve(CG_SETTINGS.get("transition", 0.22)))
    $ previous_scene = [SetScreenVariable("current_cg", cg_adjacent(current_cg, viewer_ids, -1)), SetScreenVariable("cut_index", 0), scene_dissolve]
    $ next_scene = [SetScreenVariable("current_cg", cg_adjacent(current_cg, viewer_ids, 1)), SetScreenVariable("cut_index", 0), scene_dissolve]
    $ next_cut = [SetScreenVariable("cut_index", (cut_index + 1) % max(1, len(cuts))), With(Dissolve(CG_SETTINGS.get("variant_transition", 0.30)))]
    add Solid("#edf3f7")
    if collected:
        if art:
            add cg_displayable(current_cut) xalign 0.5 yalign 0.5 id "cg_view_asset"
        else:
            add Solid(entry.get("color", "#eaf0f5"))
            vbox:
                xalign 0.5 yalign 0.46 xsize 1320 spacing 28
                text "일러스트 준비 중" font CAMPUS_TITLE_FONT size 52 line_spacing 0 color CG_INK text_align 0.5 xalign 0.5
                text entry["title"] size 35 color CG_INK text_align 0.5 xalign 0.5
                text entry["description"] size 28 line_spacing 5 color CG_MUTED text_align 0.5 xalign 0.5 xmaximum 1320
                if config.developer:
                    text entry["image"] size 21 color CG_MUTED text_align 0.5 xalign 0.5
    else:
        vbox:
            xalign 0.5 yalign 0.45 spacing 28
            add "images/ui/spring/lock.svg" xysize (80,95) xalign 0.5
            text "이 장면은 아직 열리지 않았어요." size 34 color CG_INK xalign 0.5
    if can_cycle:
        # Behind the controls, so closing/navigating never also changes a cut.
        # Remains available when H hides the viewing controls.
        button:
            id "cg_cycle_variant"
            xysize (1920, 1080)
            padding (0, 0)
            background None
            hover_background None
            alt "다음 표정 보기"
            action next_cut
    if chrome:
        textbutton "닫기" style "campus_cg_chrome_button" xpos 1705 ypos 38 xsize 150 ysize 62 action Hide("cg_view")
        if can_cycle:
            textbutton ("표정  " + str(cut_index % len(cuts) + 1) + " / " + str(len(cuts)) + "  ·  바꾸기"):
                id "cg_next_variant"
                style "campus_cg_chrome_button"
                xpos 1400 ypos 38 xsize 280 ysize 62
                action next_cut
        if collected:
            frame:
                xpos 0 ypos 954 xsize 1920 ysize 126
                background Solid("#ffffffed")
                padding (110, 18)
                # Reserve a separate column for metadata; it must not sit under navigation.
                viewport:
                    id "cg_metadata_viewport"
                    xysize (1180,90) mousewheel True draggable True
                    vbox:
                        xsize 1180 spacing 4
                        text entry["title"] id "cg_view_title" xsize 1180 size 30 color CG_INK
                        text (entry["chapter"] + "  /  " + entry["scene"]) id "cg_view_metadata" xsize 1180 size 22 color CG_MUTED
            textbutton "이전 장면" style "campus_cg_chrome_button" xpos 1370 ypos 981 xsize 185 ysize 58 sensitive can_navigate action previous_scene
            textbutton "다음 장면" style "campus_cg_chrome_button" xpos 1585 ypos 981 xsize 185 ysize 58 sensitive can_navigate action next_scene
            text ("클릭 · Space · Enter 표정 바꾸기   /   ← → 장면 이동   ·   H 안내 숨기기" if can_cycle else "← → 장면 이동   ·   H 안내 숨기기") xpos 110 ypos 900 size 21 color CG_INK outlines [(2,"#ffffffdd",0,0)]
    key "K_SPACE" action If(can_cycle, next_cut, NullAction())
    key "K_RETURN" action If(can_cycle, next_cut, NullAction())
    key "K_LEFT" action If(can_navigate, previous_scene, NullAction())
    key "K_RIGHT" action If(can_navigate, next_scene, NullAction())
    key "h" action ToggleScreenVariable("chrome")
    key "game_menu" action Hide("cg_view")

# Script-facing LD presentation; native say/name/history controls remain above.
screen ld_cg_view():
    zorder 0
    if cg_is_active() and not main_menu:
        $ entry = cg_entry(cg_current)
        $ art = cg_asset(cg_current)
        add Solid("#edf3f7")
        if art:
            add cg_displayable(cg_current) xalign 0.5 yalign 0.5 id "ld_cg_asset"
        else:
            frame:
                xpos 160 ypos 142 xsize 1600 ysize 586
                background cg_panel("#fffefc", "#dce7eb")
                padding (65,42)
                vbox:
                    spacing 23
                    text ("LD 장면  /  " + (entry["chapter"] if entry else "")) size 24 color CG_MUTED
                    text (entry["title"] if entry else "기억에 남을 순간") font CAMPUS_TITLE_FONT size 48 line_spacing 0 color CG_INK
                    text "일러스트 준비 중" size 28 color CG_MUTED
                    text (entry["description"] if entry else "이 장면의 일러스트를 준비하고 있습니다.") xmaximum 1450 size 30 line_spacing 5 color CG_INK
                    if config.developer and entry:
                        text entry["image"] size 22 color CG_MUTED
