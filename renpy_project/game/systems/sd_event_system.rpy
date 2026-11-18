# Whole-scene SD illustrations. No individual SD sprite composition.
default sd_event_current = None
default sd_event_variant_id = "01"
default sd_event_dissolve = SD_EVENT_SETTINGS.get("transition", 0.22)
default sd_event_previous_mode = "normal"
default sd_event_previous_cast = []
default sd_event_previous_faces = {}
default sd_event_previous_positions = {}
default sd_event_previous_facing = {}
default sd_event_schema = 0
default sd_event_hidden_master = []

init -7 python:
    import hashlib
    if "sd_events" not in config.layers:
        config.layers.insert(config.layers.index("transient"), "sd_events")

    def sd_event_is_active():
        return sd_event_current is not None

    def sd_event_info(event_id=None, variant=None):
        event_id = event_id or sd_event_current
        variant = str(variant or sd_event_variant_id).zfill(2)
        event = SD_EVENT_REGISTRY.get(event_id, {})
        cut = event.get("variants", {}).get(variant, {})
        expected = cut.get("image", "images/sd_events/{}_{}.webp".format(event_id, variant))
        stem, extension = os.path.splitext(expected)
        candidates = [expected] + [stem + suffix for suffix in (".webp", ".png") if suffix != extension.lower()]
        asset = next((p for p in candidates if renpy.loadable(p)), None)
        names = []
        for actor in event.get("cast", []):
            actor = story_id(actor)
            names.append(STORY_CAST.get(actor, {}).get("name", "방문객" if actor == "visitor" else actor))
        return {
            "id":event_id, "variant":variant, "asset":asset, "expected":expected,
            "title":event.get("title", "등록 정보가 필요한 SD 이벤트"),
            "chapter":event.get("chapter", story_chapter_number),
            "scene":event.get("scene", ""), "type":event.get("type", ""),
            "cast_text":" · ".join(names),
            "layout":event.get("layout", "등록 데이터에 완성된 장면의 구도를 적어 주세요."),
            "description":cut.get("description", "이 변형의 완성형 일러스트가 아직 준비되지 않았습니다."),
            "caption":cut.get("overlay_caption", ""),
        }

    def _sd_event_transition(value=None):
        duration = sd_event_dissolve if value is None else value
        if _preferences.transitions and duration and duration > 0:
            renpy.transition(Dissolve(min(float(duration), 1.0)), layer="sd_events")

    def sd_event_start(event_id, variant="01", transition=None):
        # Keep the authored standing shot when an optional illustration is pending.
        if SD_EVENT_REGISTRY.get(event_id, {}).get("requires_art") and not sd_event_info(event_id, variant)["asset"]:
            return
        cg_end(transition=0)
        if not sd_event_is_active():
            hidden = RevertableList()
            for tag in renpy.get_showing_tags(layer="master", sort=True):
                if story_id(tag) in STORY_CAST:
                    hidden.append((tag, renpy.get_attributes(tag, layer="master") or (), renpy.get_at_list(tag, layer="master") or []))
                    renpy.hide(tag, layer="master")
            store.sd_event_hidden_master = hidden
            previous = story_mode if story_mode in ("normal", "emotion") else "normal"
            store.sd_event_previous_mode = previous
            store.sd_event_previous_cast = RevertableList(story_cast)
            store.sd_event_previous_faces = RevertableDict(story_faces)
            store.sd_event_previous_positions = RevertableDict(story_positions)
            store.sd_event_previous_facing = RevertableDict(story_facing)
        store.sd_event_current = event_id
        store.sd_event_variant_id = str(variant).zfill(2)
        cg_unlock_sd(event_id, variant)
        store.sd_event_schema = 1
        store.story_mode = "sd_event"
        store.story_cast = RevertableList()
        store.story_effects = RevertableDict()
        store.story_caption = ""
        store.story_chat_active = False
        store.story_stage_visible = True
        renpy.show_screen("sd_event_view", _layer="sd_events")
        _sd_event_transition(transition)

    def sd_event_change(variant, transition=None):
        if not sd_event_is_active():
            return
        variant = str(variant).zfill(2)
        if variant == sd_event_variant_id:
            return
        store.sd_event_variant_id = variant
        cg_unlock_sd(sd_event_current, variant)
        renpy.show_screen("sd_event_view", _layer="sd_events")
        _sd_event_transition(transition)

    def sd_event_end(mode=None, cast=None, transition=None, restore=True):
        if not sd_event_is_active():
            return
        store.sd_event_current = None
        renpy.hide_screen("sd_event_view", layer="sd_events")
        store.story_mode = mode or sd_event_previous_mode
        if restore:
            store.story_cast = RevertableList(story_normalize_cast(cast if cast is not None else sd_event_previous_cast))
            store.story_faces = RevertableDict(sd_event_previous_faces)
            store.story_positions = RevertableDict(sd_event_previous_positions)
            store.story_facing = RevertableDict(sd_event_previous_facing)
            for tag, attributes, transforms in sd_event_hidden_master:
                renpy.show(" ".join((tag,) + tuple(attributes)), at_list=transforms, layer="master")
        else:
            store.story_cast = RevertableList()
        store.story_effects = RevertableDict()
        store.sd_event_hidden_master = RevertableList()
        store.sd_event_schema = 1
        _sd_event_transition(transition)

    def sd_event_reset_for_chapter():
        sd_event_end(transition=0, restore=False)
        store.sd_event_schema = 1

    def sd_event_guess_legacy():
        # The map is built from the unchanged native dialogue statement spans.
        table = read_data("sd_legacy_text_map")
        for chapter_number, actor, text in reversed(story_read_log[-40:]):
            token = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if token in table:
                return table[token]
        if story_mode == "sd":
            key = {1:"ch01_group_meeting",2:"ch02_rival_introduction",3:"ch03_rival_comedy"}.get(story_chapter_number, "ch01_group_meeting")
            return {"id":key, "variant":"01"}
        return None

    def sd_event_migrate_after_load():
        if sd_event_is_active():
            if SD_EVENT_REGISTRY.get(sd_event_current, {}).get("requires_art") and not sd_event_info()["asset"]:
                sd_event_end(transition=0)
                return
            store.story_mode = "sd_event"
            store.story_cast = RevertableList()
            renpy.show_screen("sd_event_view", _layer="sd_events")
        elif sd_event_schema == 0:
            old_mode = story_mode
            guess = sd_event_guess_legacy()
            if guess:
                variant = guess["variant"]
                if guess["id"] == "ch02_ski_accident" and variant == "03" and not rival_helped and not guess.get("help_branch", False):
                    variant = "02"
                sd_event_start(guess["id"], variant, transition=0)
            elif old_mode == "sd":
                store.story_mode = "normal"
                store.story_cast = RevertableList(story_normalize_cast(story_cast))
            store.sd_event_schema = 1
        else:
            renpy.hide_screen("sd_event_view", layer="sd_events")

screen sd_event_view():
    zorder 0
    if sd_event_is_active() and not main_menu:
        $ cut = sd_event_info()
        add Solid("#eef3f9")
        if cut["asset"]:
            # Exactly one complete cut; never crop an atlas or compose actors.
            add Transform(cut["asset"], xysize=(1920,1080), fit="contain") xalign 0.5 yalign 0.5
        else:
            frame:
                xpos 160 ypos 135 xsize 1600 ysize 600
                background spring_panel("paper_cream")
                padding (60, 38)
                viewport:
                    id "sd_placeholder_viewport"
                    xysize (1480,480) mousewheel True draggable True
                    vbox:
                        xsize 1480 spacing 10
                        text ("SD 이벤트 · CH0" + str(cut["chapter"]) + " / " + cut["scene"] + " · 컷 " + cut["variant"]) size 24 color "#65698d"
                        text cut["title"] id "sd_placeholder_title" xmaximum 1450 font CAMPUS_NOTE_FONT size 58 color SPRING_INK
                        text ("이벤트 ID · " + str(cut["id"])) size 22 color "#65698d"
                        text ("등장인물 · " + cut["cast_text"]) size 25 color SPRING_INK
                        text cut["description"] id "sd_placeholder_description" xmaximum 1450 size 28 line_spacing 4 color SPRING_INK
                        text ("구도 · " + cut["layout"]) xmaximum 1450 size 24 line_spacing 3 color "#65698d"
                        text ("필요한 이미지 · " + cut["expected"]) id "sd_placeholder_filename" xmaximum 1450 size 22 color "#65698d"
        if cut["caption"]:
            text cut["caption"] xalign 0.5 ypos 684 xmaximum 1500 font CAMPUS_NOTE_FONT size 42 color SPRING_INK outlines [(2,"#fffafd",0,0)]
