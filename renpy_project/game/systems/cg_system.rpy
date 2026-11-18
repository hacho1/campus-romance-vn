# Full-frame LD illustrations and persistent gallery collections.
# Dialogues, choices and relationship changes stay in the route scripts.
default persistent.cg_seen = set()
default persistent.cg_sd_seen = set()
default cg_current = None
default cg_previous_mode = "normal"
default cg_previous_cast = []
default cg_previous_faces = {}
default cg_previous_positions = {}
default cg_previous_facing = {}
default cg_previous_stage_visible = True
default cg_previous_chat_active = False
default cg_hidden_master = []

# state.rpy's legacy cg_asset is init -20; this replaces it deliberately.
init -6 python:
    import os
    import re
    import math
    import builtins
    from renpy.revertable import RevertableDict, RevertableList

    CG_INK = "#394b63"
    CG_MUTED = "#586c7c"
    CG_PALE = "#f2f6f8"

    if "ld_cg" not in config.layers:
        config.layers.insert(config.layers.index("transient"), "ld_cg")

    def cg_normalize(key):
        key = str(key or "").strip()
        if key == "festival_note":
            return "legacy/festival_note"
        if key.startswith("sd/"):
            parts = key.split("/")
            if len(parts) == 3:
                return "sd/" + parts[1] + "/" + parts[2].zfill(2)
        match = re.fullmatch(r"ld[_-]?(\d{1,2})", key.lower())
        return "ld_{:02d}".format(int(match.group(1))) if match else key

    def _cg_collection(name):
        value = getattr(persistent, name, None)
        if not isinstance(value, set):
            value = set(value or ())
            setattr(persistent, name, value)
        return value

    def cg_entry(key):
        key = cg_normalize(key)
        if key in CG_REGISTRY:
            result = dict(CG_REGISTRY[key])
            result["id"] = key
            return result
        if key == "legacy/festival_note":
            return {"id":key, "kind":"legacy", "tab":"SPECIAL", "title":"첫 회의의 메모", "chapter":"이전 CH01", "chapter_number":1,
                "scene":"처음 함께 남긴 메모", "image":"images/cg/festival_note.png", "fallback_image":"images/ui/festival_note.svg",
                "description":"처음 함께 준비하던 날의 메모입니다.", "color":"#f3eef5", "replay_label":None}
        if key.startswith("sd/"):
            parts = key.split("/")
            if len(parts) != 3:
                return None
            event_id, variant = parts[1], parts[2].zfill(2)
            event = SD_EVENT_REGISTRY.get(event_id)
            cut = event.get("variants", {}).get(variant) if event else None
            if cut is None:
                return None
            return {"id":"sd/" + event_id + "/" + variant, "kind":"sd", "tab":"SPECIAL",
                "title":event["title"] + " · " + variant, "chapter":"CH{:02d}".format(event["chapter"]), "chapter_number":event["chapter"],
                "scene":event["scene"] + " · SD 이벤트", "image":cut["image"], "description":cut["description"],
                "color":"#eaf0f6", "replay_label":None}
        if key.startswith("ending/"):
            ending_id = key.split("/", 1)[1]
            ending = ENDINGS.get(ending_id)
            if not ending:
                return None
            return {"id":key, "kind":"ending", "tab":"ENDING", "title":ending["title"], "chapter":"개별 루트", "chapter_number":0,
                "scene":"엔딩", "image":"images/cg/endings/" + ending_id + ".webp", "ending_id":ending_id,
                "description":"이야기의 마지막에 남긴 장면입니다.", "color":"#eef0f7", "replay_label":None}
        return None

    def cg_asset(key):
        # A missing cut must never silently display an unrelated CG.
        entry = cg_entry(key)
        if not entry:
            return None
        expected = entry["image"]
        stem, extension = os.path.splitext(expected)
        candidates = [expected] + [stem + suffix for suffix in (".webp", ".png") if suffix != extension.lower()]
        if entry.get("fallback_image"):
            candidates.append(entry["fallback_image"])
        return next((path for path in candidates if renpy.loadable(path)), None)

    def cg_displayable(key, size=(1920, 1080), thumbnail=False):
        # The same source viewport is used in-story and throughout the album.
        # Relative crops compensate for expression files exported at a different
        # aspect ratio, without resizing/overwriting the original artwork.
        entry = cg_entry(key)
        art = cg_asset(key)
        if not entry or not art:
            return None
        crop = entry.get("screen_crop")
        if isinstance(crop, (builtins.list, builtins.tuple)) and len(crop) == 4:
            try:
                left, top, width, height = tuple(float(value) for value in crop)
                valid = (all(math.isfinite(value) for value in (left, top, width, height))
                    and left >= 0 and top >= 0 and width > 0 and height > 0
                    and left + width <= 1.000001 and top + height <= 1.000001)
            except (TypeError, ValueError):
                valid = False
            if valid:
                source = Transform(art, crop=(left, top, width, height), crop_relative=True)
                return Transform(source, xysize=size, fit="fill")
        return Transform(art, xysize=size, fit="contain" if thumbnail else entry.get("screen_fit", "contain"))

    def cg_seen(key):
        key = cg_normalize(key)
        entry = cg_entry(key)
        if not entry:
            return False
        if entry.get("unlock_ending") and entry["unlock_ending"] not in _cg_collection("endings"):
            return False
        if entry.get("unlock_ending") in _cg_collection("endings"):
            # Older clears can have the ending record without a separate CG ID.
            return True
        if entry["kind"] == "legacy":
            return "festival_note" in _cg_collection("gallery")
        if entry["kind"] == "ending":
            ending_id = entry["ending_id"]
            if ending_id not in _cg_collection("endings") or not ENDINGS[ending_id].get("implemented", False):
                return False
        collected = _cg_collection("cg_seen")
        if key in collected or any(cg_normalize(old) == key for old in collected):
            return True
        if entry["kind"] == "sd":
            return key in _cg_collection("cg_sd_seen")
        # Accept previously stored LD IDs without changing legacy collections.
        return any(cg_normalize(old) == key for old in _cg_collection("gallery"))

    def cg_unlock(key):
        key = cg_normalize(key)
        entry = cg_entry(key)
        if not entry or entry["kind"] == "legacy":
            return False
        if entry["kind"] == "ending":
            eid = entry["ending_id"]
            if eid not in _cg_collection("endings") or not ENDINGS[eid].get("implemented", False):
                return False
        changed = not cg_seen(key)
        _cg_collection("cg_seen").add(key)
        if entry["kind"] == "sd":
            _cg_collection("cg_sd_seen").add(key)
        # Engine shutdown and existing chapter-completion checkpoints flush
        # persistent data. Avoid a blocking disk write on every short SD cut.
        return changed

    def cg_unlock_sd(event_id, variant="01"):
        return cg_unlock("sd/" + str(event_id) + "/" + str(variant).zfill(2))

    def cg_gallery_key(key):
        # Gallery scenes group expression cuts without changing story/save IDs.
        key = cg_normalize(key)
        for scene, entry in CG_REGISTRY.items():
            if entry.get("kind") == "ld" and key in entry.get("gallery_variants", ()):
                return scene
        return key

    def cg_gallery_can_view_cut(key):
        # Test-build browsing is read-only: it must not forge earned CG/ending
        # records or affect cg_unlock's first-collection return value.
        if campus_test_collections_preview() and cg_asset(key):
            return True
        return cg_seen(key)

    def cg_gallery_variants(key, unlocked_only=False):
        scene = cg_gallery_key(key)
        entry = cg_entry(scene)
        if not entry:
            return []
        declared = entry.get("gallery_variants", [scene])
        # Keep authored cut order (Sia starts with her tablet cut). Ignore
        # unknown/mismatched entries so future data edits cannot cross tabs.
        cuts = list(dict.fromkeys(cg_normalize(cut) for cut in declared))
        if scene not in cuts:
            cuts.insert(0, scene)
        cuts = [cut for cut in cuts if cg_entry(cut)
            and cg_entry(cut)["kind"] == entry["kind"]
            and cg_entry(cut)["tab"] == entry["tab"]]
        return [cut for cut in cuts if cg_gallery_can_view_cut(cut)] if unlocked_only else cuts

    def cg_gallery_seen(key):
        return bool(cg_gallery_variants(key, unlocked_only=True))

    def cg_gallery_preview(key):
        cuts = cg_gallery_variants(key, unlocked_only=True)
        return cuts[0] if cuts else cg_gallery_key(key)

    def cg_gallery_keys(tab="COMMON"):
        if tab == "SPECIAL":
            keys = [
                "sd/" + event_id + "/" + variant
                for event_id, event in SD_EVENT_REGISTRY.items()
                for variant in event.get("gallery_variants", event["variants"])
            ]
            # Keep the previous demo's collected memo accessible.
            if cg_gallery_can_view_cut("legacy/festival_note"):
                keys.insert(0, "legacy/festival_note")
            return keys
        if tab == "ENDING":
            return ["ending/" + ending_id for ending_id in ENDINGS]
        tab = tab if tab in CG_TABS else "COMMON"
        return list(dict.fromkeys(cg_gallery_key(key) for key in CG_ORDER
            if CG_REGISTRY[key]["tab"] == tab or tab in CG_REGISTRY[key].get("gallery_tabs", ())))

    def cg_unlocked_ids(keys=None):
        keys = list(keys) if keys is not None else [key for tab in CG_TABS for key in cg_gallery_keys(tab)]
        return list(dict.fromkeys(cg_gallery_key(key) for key in keys if cg_gallery_seen(key)))

    def cg_adjacent(current, keys, direction):
        keys = cg_unlocked_ids(keys)
        if not keys:
            return cg_normalize(current)
        current = cg_gallery_key(current)
        index = keys.index(current) if current in keys else 0
        return keys[(index + direction) % len(keys)]

    def cg_is_active():
        return cg_current is not None

    def _cg_transition(value=None):
        duration = CG_SETTINGS.get("transition", 0.22) if value is None else value
        if _preferences.transitions and duration and duration > 0:
            renpy.transition(Dissolve(min(float(duration), 1.0)), layer="ld_cg")

    def cg_start(key, transition=None, story_ending=False):
        key = cg_normalize(key)
        entry = cg_entry(key)
        if not entry or entry["kind"] not in ("ld", "ending"):
            return False
        if entry.get("requires_ending") and entry["requires_ending"] not in _cg_collection("endings"):
            return False
        if entry["kind"] == "ending":
            ending = ENDINGS[entry["ending_id"]]
            # An authored after-story may show its art before its first clear.
            # Album access still requires the ending record, and the prerequisite
            # happy ending above is mandatory. This never unlocks the ending.
            first_story_view = (story_ending and ending.get("kind") == "secret"
                and entry.get("requires_ending") in _cg_collection("endings"))
            if not ending.get("implemented", False) or not (entry["ending_id"] in _cg_collection("endings") or first_story_view):
                return False
        if entry.get("requires_art") and not cg_asset(key):
            return False
        if sd_event_is_active():
            sd_event_end(transition=0)
        if not cg_is_active():
            hidden = RevertableList()
            for tag in renpy.get_showing_tags(layer="master", sort=True):
                if story_id(tag) in STORY_CAST:
                    hidden.append((tag, renpy.get_attributes(tag, layer="master") or (), renpy.get_at_list(tag, layer="master") or []))
                    renpy.hide(tag, layer="master")
            store.cg_hidden_master = hidden
            store.cg_previous_mode = story_mode if story_mode in ("normal", "emotion") else "normal"
            store.cg_previous_cast = RevertableList(story_cast)
            store.cg_previous_faces = RevertableDict(story_faces)
            store.cg_previous_positions = RevertableDict(story_positions)
            store.cg_previous_facing = RevertableDict(story_facing)
            store.cg_previous_stage_visible = story_stage_visible
            store.cg_previous_chat_active = story_chat_active
        store.cg_current = key
        store.story_mode = "ld_cg"
        store.story_cast = RevertableList()
        store.story_effects = RevertableDict()
        store.story_stage_visible = False
        store.story_chat_active = False
        cg_unlock(key)
        renpy.show_screen("ld_cg_view", _layer="ld_cg")
        _cg_transition(transition)
        return True

    def cg_end(transition=None, restore=True):
        if not cg_is_active():
            renpy.hide_screen("ld_cg_view", layer="ld_cg")
            return
        store.cg_current = None
        renpy.hide_screen("ld_cg_view", layer="ld_cg")
        store.story_mode = cg_previous_mode if restore else "normal"
        store.story_stage_visible = cg_previous_stage_visible if restore else True
        store.story_chat_active = cg_previous_chat_active if restore else False
        store.story_cast = RevertableList(cg_previous_cast) if restore else RevertableList()
        if restore:
            store.story_faces = RevertableDict(cg_previous_faces)
            store.story_positions = RevertableDict(cg_previous_positions)
            store.story_facing = RevertableDict(cg_previous_facing)
            for tag, attributes, transforms in cg_hidden_master:
                renpy.show(" ".join((tag,) + tuple(attributes)), at_list=transforms, layer="master")
        store.story_effects = RevertableDict()
        store.cg_hidden_master = RevertableList()
        _cg_transition(transition)

    def cg_restore_after_load():
        if cg_is_active():
            entry = cg_entry(cg_current)
            if entry and entry.get("requires_art") and not cg_asset(cg_current):
                cg_end(transition=0)
                return
            if sd_event_is_active():
                sd_event_end(transition=0, restore=False)
            store.story_mode = "ld_cg"
            store.story_cast = RevertableList()
            store.story_effects = RevertableDict()
            store.story_stage_visible = False
            store.story_chat_active = False
            renpy.show_screen("ld_cg_view", _layer="ld_cg")
        else:
            renpy.hide_screen("ld_cg_view", layer="ld_cg")

    config.after_load_callbacks.append(cg_restore_after_load)

    def cg_panel(fill="#ffffff", line="#dbe4e9"):
        return Frame(Composite((12,12), (0,0), Solid(line, xysize=(12,12)), (1,1), Solid(fill, xysize=(10,10))), 6,6)
