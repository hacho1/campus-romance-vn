# Background-only time-of-day assets. Character sprites and LD/SD layers are not
# part of this resolver. Keep original daytime assets available for old saves.
init -9 python:
    STORY_LIGHTING_ALIASES = {"night_campus":"campus", "prep_room":"clubroom"}
    STORY_BACKGROUND_PREFERRED = {
        "room": "images/cg/ld_03_first_day_evening.webp",
        "clubroom307": "images/backgrounds/clubroom307.webp",
        "presentation": "images/backgrounds/presentation_pixai.webp",
        "rest_area": "images/backgrounds/rest_area.webp",
    }
    STORY_BACKGROUND_FALLBACKS = {"clubroom307":"clubroom", "rest_area":"booth"}
    STORY_LIGHTING_TINTS = {"day":"#ffffff", "evening":"#ffe5db", "night":"#8c9cb9"}
    STORY_LIGHTING_REGISTRY = {
        "room": {"day":"images/backgrounds/room_morning_pixai.webp", "night":"images/backgrounds/room_night.png"},
        "campus": {"night":"images/backgrounds/campus_night.png"},
    }

    def story_lighting_normalize(light):
        return light if light in STORY_LIGHTING_TINTS else "day"

    def story_background_info(bg, light="day"):
        light = story_lighting_normalize(light)
        key = str(bg or "campus")
        preferred = STORY_BACKGROUND_PREFERRED.get(key)
        if light == "day":
            daytime = STORY_LIGHTING_REGISTRY.get(key, {}).get("day")
            if daytime and renpy.loadable(daytime):
                preferred = daytime
        if preferred and renpy.loadable(preferred):
            return {"background":key,"resolved":key,"light":light,"path":preferred,
                "dedicated_night":key == "room" and light == "night",
                "tint":None if key == "room" else STORY_LIGHTING_TINTS[light]}
        resolved = STORY_BACKGROUND_FALLBACKS.get(key, STORY_LIGHTING_ALIASES.get(key, key))
        night_path = STORY_LIGHTING_REGISTRY.get(resolved, {}).get("night")
        if light == "night" and night_path:
            stem, extension = night_path.rsplit(".", 1)
            candidates = [night_path] + [stem + suffix for suffix in (".png", ".webp") if suffix != "." + extension.lower()]
            supplied = next((path for path in candidates if renpy.loadable(path)), None)
            if supplied:
                return {"background":key,"resolved":resolved,"light":light,"path":supplied,
                    "dedicated_night":True,"tint":None}
        # The original path order remains PNG -> story SVG -> root SVG.
        # WebP is an optional addition; missing night files remain playable.
        candidates = ["images/backgrounds/" + resolved + ".png",
            "images/backgrounds/" + resolved + ".webp",
            "images/backgrounds/story/" + resolved + ".svg",
            "images/backgrounds/" + resolved + ".svg",
            "images/backgrounds/story/corridor.svg"]
        path = next((candidate for candidate in candidates if renpy.loadable(candidate)), candidates[-1])
        return {"background":key,"resolved":resolved,"light":light,"path":path,
            "dedicated_night":False,"tint":STORY_LIGHTING_TINTS[light]}

    def story_background_display(bg, light="day"):
        """Return one background Displayable; a pre-painted night asset is not tinted twice."""
        info = story_background_info(bg, light)
        if info["tint"] is None:
            # Explicit identity prevents inherited old blue TintMatrix state
            # from being transferred when the same tag is refreshed after load.
            return Transform(info["path"], xysize=(1920,1080), matrixcolor=IdentityMatrix())
        return Transform(info["path"], xysize=(1920,1080), matrixcolor=TintMatrix(info["tint"]))

    def story_lighting_restore_after_load():
        # Old saves have the new default story_light='day'. An explicit old
        # night location/id is stronger evidence than that injected default.
        bg = getattr(store, "story_background", "campus")
        light = story_lighting_normalize(getattr(store, "story_light", "day"))
        location = str(getattr(store, "location_name", "") or "").strip()
        if bg == "clubroom" and story_chapter_number in (1, 2) and location.startswith("공동 동아리실"):
            bg = "clubroom307"
            store.story_background = bg
        if light == "day" and (bg == "night_campus" or location.endswith("밤")):
            light = "night"
        store.story_light = light
        if not getattr(store, "story_active", False) or getattr(store, "main_menu", False):
            return
        if not renpy.showing("story_background", layer="master"):
            return
        # Replace only the existing master background tag. Never call scene(),
        # story_scene(), hide actors or change LD/SD state/layers. Their full
        # illustration remains above master, with the correct night underneath.
        renpy.show("story_background", what=story_background_display(bg,light), layer="master")

    def story_lighting_will_load():
        # Keep only the pending work outside rollback-store restoration. The
        # loaded story fields themselves remain normal saved/rollback state.
        renpy.session["story_lighting_restore_on_interact"] = True

    def story_lighting_start_interact():
        # A restored say interaction can resume after the native _after_load
        # callback's store/SceneList changes have been reset. Rebuild exactly
        # once at the actual resume boundary, before its first visible frame.
        if renpy.session.pop("story_lighting_restore_on_interact", False):
            story_lighting_restore_after_load()

    if story_lighting_restore_after_load not in config.after_load_callbacks:
        config.after_load_callbacks.append(story_lighting_restore_after_load)
    if story_lighting_will_load not in config.before_load_callbacks:
        config.before_load_callbacks.append(story_lighting_will_load)
    if story_lighting_start_interact not in config.start_interact_callbacks:
        config.start_interact_callbacks.append(story_lighting_start_interact)


