default player_name = "나"
default affection = {key: 0 for key in HEROINE_ORDER}
default trust = {key: 0 for key in HEROINE_ORDER}
default relationship_scale_version = 0
default event_flags = set()
default choice_log = []
default chapter = "CH01 · 어쩌다 축제 준비팀"
default location_name = "하온대학교 · 중앙광장"
default ch01_done = False
default sandbox_endings = set()
default meta_line = ""
default persistent.schema_version = 1
default persistent.endings = set()
default persistent.gallery = set()
default persistent.profile_secrets = set()
default persistent.chapter_completions = set()
default persistent.choice_memories = set()

init -20 python:
    import json
    def read_data(name):
        with renpy.file("data/" + name + ".json") as stream:
            return json.load(stream)
    HEROINES = read_data("heroines")
    HEROINE_ORDER = ["roman", "sia", "darim", "omu", "lumi"]
    CHOICES = read_data("choices")
    ENDINGS = read_data("endings")
    AUDIO_TRACKS = read_data("audio")
    ROUTES = read_data("routes")
    RELATIONSHIP_POINT_UNIT = 5
    STORY_RESUME_SLOT = "auto-resume"
    SCHOOL_NAME = "하온대학교"
    GAME_TITLE = "우리 사이, 그 이상"

    def clean_name(value):
        value = value or ""
        value = "".join(c for c in value.strip() if c.isalnum() or c in " _-·")[:12]
        return value or "나"

    def submit_input():
        widget = renpy.get_widget("input", "input")
        if widget is not None:
            renpy.end_interaction(widget.content)

    def relationship_migrate_save():
        # Keep both compatibility dictionaries verbatim. Only reviewed choices
        # initialize the new gauges; old trust totals never become happy points.
        heart_migrate_save()
        store.relationship_scale_version = 1

    def relationship_check_interaction():
        if heart_schema_version < HEART_SCHEMA and not main_menu and not renpy.context()._menu:
            relationship_migrate_save()

    # A loaded save can replay script statements before its first interaction.
    # Convert the restored scores there so the replay cannot overwrite them.
    config.start_callbacks.append(relationship_migrate_save)
    config.start_interact_callbacks.append(relationship_check_interaction)

    def relationship_apply(affection_delta=None, trust_delta=None, counters=None, hearts=None, choice_id=None):
        relationship_migrate_save()
        return heart_apply_choice(affection_delta, trust_delta, counters, hearts, choice_id=choice_id)

    def relationship_write_save_summary(metadata):
        scores = [{key: stat.get(key, 0) for key in HEROINE_ORDER}
                  for stat in (affection, trust)]
        route_flags = [flag for flag in event_flags if flag.endswith("_route_entered")]
        metadata["campus_relationship"] = scores[0], scores[1], route_flags

    config.save_json_callbacks.append(relationship_write_save_summary)

    def relationship_profile_values():
        slot = renpy.newest_slot() if main_menu else None
        if not slot:
            return affection, trust, event_flags
        # Continue opens this same slot. Older saves gain the summary the next
        # time they are saved, after their original scores are loaded normally.
        return (renpy.slot_json(slot) or {}).get("campus_relationship", ({}, {}, ()))

    def apply_choice(choice_id):
        # All relationship mutations are declarative. Ren'Py rolls these back together.
        if choice_id in heart_awarded_choices and choice_id in choice_log:
            return
        effect = CHOICES[choice_id]
        feedback_changes = relationship_apply(hearts=effect.get("hearts"), choice_id=choice_id)
        event_flags.update(effect.get("flags", []))
        choice_log.append(choice_id)
        relationship_feedback_publish(choice_id, feedback_changes)

    def complete_chapter():
        relationship_migrate_save()
        persistent.chapter_completions.add("ch01")
        persistent.choice_memories.update(choice_log)
        persistent.gallery.add("festival_note")
        # Older CH01 saves reach this label after their solo walk.
        for flag in event_flags:
            if flag.startswith("walk_"):
                secret_note_unlock(flag[5:], 1)
        renpy.save_persistent()

    def eligible_routes():
        return list(HEROINE_ORDER)

    def unlock_ending(ending_id, sandbox=False):
        if ending_id not in ENDINGS:
            raise ValueError("알 수 없는 엔딩 ID: " + ending_id)
        if sandbox:
            sandbox_endings.add(ending_id)
            return True
        if not ENDINGS[ending_id]["implemented"]:
            return False
        required = ENDINGS[ending_id].get("conditions", {}).get("required_ending")
        if required and required not in persistent.endings:
            return False
        # Establish legacy NOTE03 admissions before a newly earned ending is
        # added, including direct developer-context route entry.
        secret_note_gate_migrate()
        first_clear = ending_id not in persistent.endings
        persistent.endings.add(ending_id)
        renpy.save_persistent()
        if first_clear:
            secret_note_ending_notice(ending_id)
        return True

    def meta_unlocked():
        return any(e in ENDINGS and ENDINGS[e]["kind"] in ("happy", "bad")
            for e in persistent.endings)

    def play_bgm(track, fade=0.8):
        entry = AUDIO_TRACKS[track]
        path = next((p for p in entry["files"] if renpy.loadable(p)), None)
        if path:
            renpy.music.play(path, channel="music", loop=True, fadeout=fade, fadein=fade, if_changed=True)
        else:
            renpy.music.stop(channel="music", fadeout=fade)

    def click_sound():
        if renpy.loadable("audio/sfx/click.wav"):
            renpy.sound.play("audio/sfx/click.wav")

    def continue_action():
        slot = renpy.newest_slot()
        if slot:
            renpy.load(slot)

    def profile_photo(key):
        path = "images/heroines/{}/profile.png".format(key)
        return path if renpy.loadable(path) else "images/ui/photo_placeholder_v2.svg"

    def cg_asset(key):
        path = "images/cg/{}.png".format(key)
        return path if renpy.loadable(path) else "images/ui/festival_note.svg"

label before_main_menu:
    $ secret_note_import_completed()
    $ play_bgm("main")
    return

label after_load:
    $ player_name = clean_name(player_name)
    $ story_migrate_save()
    if story_chapter_number > 0 or ch01_done:
        $ _quit_slot = STORY_RESUME_SLOT
    $ sd_event_migrate_after_load()
    $ phone_migrate_after_load()
    $ renpy.session["secret_note_import_on_interact"] = True
    return
