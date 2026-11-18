# Presentation state is saved/rolled back with the dialogue, never persistent.
default story_flashback = False
default story_memory_caption = "회상"

init -3 python:
    def story_flashback_set(active, caption="회상"):
        store.story_flashback = bool(active)
        store.story_memory_caption = str(caption or "회상")
        if _preferences.transitions:
            renpy.transition(Dissolve(0.18), layer="screens")

    def story_presentation_caption():
        owner = getattr(store, "phone_perspective", "mc")
        name = STORY_CAST.get(owner, {}).get("name", "") if owner != "mc" else ""
        if story_flashback:
            return (name + "의 시점 · " if name else "") + story_memory_caption
        return name + "의 시점" if name else ""

    def story_presentation_after_load():
        # Earlier CH02 saves predate the explicit memory flag.
        if "회상" in str(location_name or ""):
            store.story_flashback = True

    config.after_load_callbacks.append(story_presentation_after_load)

init 30 python:
    if "story_memory_overlay" not in config.overlay_screens:
        config.overlay_screens.append("story_memory_overlay")

screen story_memory_overlay():
    # Phone headers carry their own perspective label; keep them unobstructed.
    zorder 16
    if story_active and not main_menu:
        if story_flashback and not phone_is_open:
            add Solid("#e8c57829") id "memory_warm_tint" xysize (1920,1080)
        $ memory_caption = story_presentation_caption()
        if memory_caption and not phone_is_open:
            frame:
                id "story_perspective_badge"
                xpos 760 ypos 108 xysize (400,52)
                padding (14,0)
                background Solid("#fff8e8f2" if story_flashback else "#f2edf9f2")
                text memory_caption id "story_perspective_caption" font CAMPUS_BODY_FONT size 24 line_spacing 0 color "#564730" align (0.5,0.5) text_align 0.5 yoffset -2
