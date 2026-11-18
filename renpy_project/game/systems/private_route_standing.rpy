# Generated private-route presentation; no authored source file is read in-game.
default private_route_standing_checkpoint = None

init 40 python:
    PRIVATE_ROUTE_STAGING = read_data("private_route_staging")
    PRIVATE_ROUTE_STAGE_ROWS = {
        filename: {row["line"]: row for row in data["rows"]}
        for filename, data in PRIVATE_ROUTE_STAGING.get("files", {}).items()
    }

    def private_route_stage_lookup(filename, line):
        basename = str(filename).replace("\\", "/").split("/")[-1]
        if basename.endswith(".rpyc"):
            basename = basename[:-1]
        return PRIVATE_ROUTE_STAGE_ROWS.get(basename, {}).get(int(line))

    def private_route_standing_refresh():
        if not getattr(store, "story_active", False) or main_menu or renpy.context()._menu:
            return
        filename, line = renpy.get_filename_line()
        row = private_route_stage_lookup(filename, line)
        if row is None:
            return
        if cg_is_active() or sd_event_is_active():
            # Never clear an active illustration or its saved stage snapshot.
            return
        if story_chat_active or phone_is_open:
            store.story_stage_visible = False
            return
        if row["status"] != "standing":
            store.story_stage_visible = False
            store.story_cast = RevertableList()
            store.private_route_standing_checkpoint = (str(filename), int(line), row["status"])
            return
        cast = [actor for actor in row["cast"] if story_asset(actor, row["faces"].get(actor, "normal"))]
        if not cast:
            store.story_stage_visible = False
            store.story_cast = RevertableList()
            return
        store.story_stage_visible = True
        faces = {actor:row["faces"].get(actor, "normal") for actor in cast}
        if tuple(story_cast) != tuple(cast):
            story_stage(cast=cast, faces=faces)
        elif any(story_faces.get(actor, "normal") != face for actor,face in faces.items()):
            story_stage(faces=faces)
        story_focus_update(story_speaker_id)
        store.private_route_standing_checkpoint = (str(filename), int(line), "standing")

    config.start_interact_callbacks.append(private_route_standing_refresh)
