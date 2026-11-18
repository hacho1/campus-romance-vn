# Shared chapter runtime. Legacy ch01 and save data remain intact.
default first_task_partner = None
default story_offscreen_actor = None
default ch02_partner = None
default ch03_partner = None
default chapter01_complete = False
default chapter02_complete = False
default chapter03_complete = False
default chapter04_complete = False
default chapter05_complete = False
default ch04_partner = None
default ch04_conflict = None
default rival_skill_recognized = False
default ch04_personal_promise = {key: False for key in HEROINE_ORDER}
default ch04_roman_playful_event = False
default ch04_sia_special_prank = False
default ch04_darim_game_promise = False
default ch04_omu_exhibition_idea = False
default ch04_harin_special_emotion = False
default ch04_video_priority = None
default ch04_team_decision_complete = False
default ch04_submission_complete = False
default ch04_evening_event = None
default ch05_final_answer = None
default ch05_presentation_complete = False
default ch05_booth_priority = False
default ch05_invitation_seen = {key: False for key in HEROINE_ORDER}
default ch05_booth_install_complete = False
default ch05_group_photo_taken = False
default ch06_festival_partner = None
default roman_book_event = False
default roman_library_visit = False
default sia_concept_event = False
default darim_game_event = False
default omu_photo_event = False
default rumi_design_event = False
default lumi_design_event = False
default space_issue_discovered = False
default team_preparation = 0
default exhibition_quality = 0
default promotion_quality = 0
default rival_attitude = "neutral"
default rival_cooperation = False
default rival_helped = False
default rival_project_known = False
default rival_project_observed = False
default roman_question_event = False
default sia_webtoon_revision = False
default darim_schedule_event = False
default omu_campus_photo_event = False
default rumi_model_event = False
default lumi_model_event = False
default pitch_strategy = None
default visitor_policy = None
default visitor_policy_priority = None
default visitor_policy_established = False
default visitor_withdrawal_occurred = False
default trial_preparation = None
default trial_operation_complete = False
default cooperation_method = None
default ch03_evening_event = None
default special_moment = {key: False for key in HEROINE_ORDER}
default roman_special_moment = False
default sia_special_moment = False
default darim_special_moment = False
default omu_special_moment = False
default lumi_special_moment = False
default rumi_special_moment = False
default roman_playful_event = False
default sia_webtoon_promise = False
default darim_game_rival = False
default omu_representative_photo = False
default lumi_reverse_prank = False
default story_active = False
default story_stage_visible = True
default story_mode = "normal"
default story_cast = []
default story_team_speaker = None
default story_faces = {}
default story_positions = {}
default story_facing = {}
default story_effects = {}
default story_effect_serial = 0
default story_effect_times = {}
default story_effect_settled = {}
default story_exiting = {}
default story_reaction_icons = {}
default story_focus_actor = None
default story_focus_from = {}
default story_focus_started = 0.0
default story_focus_serial = 0
default story_caption = ""
default story_speaker_id = None
default story_background = "campus"
default story_light = "day"
default story_chat_active = False
default story_chat_title = "축제 준비팀"
default story_chat_messages = []
default story_chapter_number = 0
default story_chapter_started = 0.0
default story_read_log = []
default chapter_metrics = {}
default chapter_save_schema = 2

init -8 python:
    from functools import partial
    import math as _story_math
    import time as _story_clock
    from renpy.revertable import RevertableDict, RevertableList

    STORY_HEROES = ["roman", "sia", "darim", "omu", "lumi"]
    STORY_CAST = {
        "roman": {"name":"로만", "color":"#aa7591", "folder":"heroines"},
        "sia": {"name":"시아", "color":"#8a78b3", "folder":"heroines"},
        "darim": {"name":"다림", "color":"#729b8e", "folder":"heroines"},
        "omu": {"name":"오므", "color":"#ad8967", "folder":"heroines"},
        "lumi": {"name":"하린", "color":"#718faf", "folder":"heroines"},
        "ski": {"name":"스키", "color":"#b87c83", "folder":"rivals"},
        "hyeophap": {"name":"협합", "color":"#7c879e", "folder":"rivals"},
        "hess": {"name":"헤스", "color":"#87947a", "folder":"rivals"},
        "bambam": {"name":"밤밤", "color":"#aa9481", "folder":"rivals"},
        "visitor": {"name":"방문객", "color":"#78919a", "folder":"standings"},
    }
    STORY_FACE_LABELS = {
        "normal":"기본", "happy":"웃음", "angry":"뾰로통", "embarrassed":"당황",
        "surprised":"놀람", "sad":"시무룩", "smug":"장난", "confused":"갸웃", "serious":"진지",
    }
    STORY_FACE_GLYPHS = {
        "normal":"•  •", "happy":"^  ^", "angry":">  <", "embarrassed":"-  -",
        "surprised":"O  O", "sad":"T  T", "smug":"¬  ¬", "confused":"?  ?", "serious":"—  —",
    }

    def story_id(key):
        return "lumi" if key in ("rumi", "harin") else key

    def story_normalize_cast(actors):
        return list(dict.fromkeys(story_id(actor) for actor in actors if story_id(actor) in STORY_CAST))

    def story_face(face):
        aliases = {"neutral":"normal", "smile":"happy", "shy":"embarrassed",
            "playful":"smug", "deadpan":"smug", "기본":"normal", "미소":"happy", "웃음":"happy",
            "놀람":"surprised", "충격":"surprised", "당황":"embarrassed",
            "자신만만":"smug", "장난":"smug", "무표정":"normal"}
        result = aliases.get(face, face)
        return result if result in STORY_FACE_LABELS else "normal"

    def story_asset(key, expression="normal", sd=False, pose="a"):
        if sd:
            return None  # Legacy signature only; SD actor assets are inactive.
        key, expression = story_id(key), story_face(expression)
        if key not in STORY_CAST:
            return None
        art = ld_standing_path(key, expression, pose)
        if art and renpy.loadable(art):
            return art
        normal = ld_standing_path(key)
        if normal and normal != art and renpy.loadable(normal):
            return normal

        directories = [key] + (["rumi"] if key == "lumi" else [])
        root = "images/" + STORY_CAST[key]["folder"] + "/"
        aliases = {"normal":"neutral", "happy":"smile", "embarrassed":"shy", "confused":"surprised"}
        for face in [expression, aliases.get(expression, expression), "normal", "neutral"]:
            for directory in directories:
                path = root + directory + "/" + face + ".png"
                if renpy.loadable(path):
                    return path
        return None

    STORY_MOTION_DURATIONS = {"jump":0.26, "bounce":0.24, "group":0.26, "shake":0.20, "surprise":0.24,
        "tilt":0.28, "shrink":0.20, "angry":0.22, "move":0.25, "enter":0.28, "exit":0.26,
        "fade_in":0.34, "fall":0.62}
    STORY_ICON_KINDS = ("heart", "exclamation", "lightbulb")
    STORY_STANDING_WIDTH = 872
    STORY_STANDING_LINEUPS = {
        1: (960,),
        2: (640, 1280),
        3: (440, 960, 1480),
        4: (300, 740, 1180, 1620),
        5: (248, 604, 960, 1316, 1672),
        6: (170, 480, 790, 1100, 1410, 1720),
    }

    def story_standing_available():
        return story_active and story_stage_visible and story_mode in ("normal", "emotion") and not story_chat_active and not sd_event_is_active() and not cg_is_active()

    def story_shot_members(cast, reference):
        cast = list(cast)
        if len(cast) <= len(STORY_HEROES) or (len(cast) == 6 and "visitor" in cast):
            return cast
        heroine_shot = reference in STORY_HEROES
        return [actor for actor in cast if (actor in STORY_HEROES) == heroine_shot]

    def story_visible_cast():
        reference = story_team_speaker if story_team_speaker in story_cast else story_speaker_id
        if reference not in story_cast and story_cast:
            reference = story_cast[0]
        return story_shot_members(story_cast, reference)

    def story_actor_position(actor, cast=None):
        actor = story_id(actor)
        members = story_shot_members(story_cast if cast is None else cast, actor)
        slots = STORY_STANDING_LINEUPS[max(1, len(members))]
        index = members.index(actor) if actor in members else 0
        return tuple(story_positions.get(actor, (slots[index], 795)))

    def story_focus_target(actor):
        visible = story_visible_cast()
        if not story_standing_available() or len(visible) < 2:
            return (1.0,0.0)
        if story_focus_actor not in visible:
            return (1.0, -0.18 if len(visible) >= 4 else 0.0)
        if actor == story_focus_actor:
            return (1.0, 0.035)
        return (1.0,-0.18)

    def story_focus_values(actor):
        target = story_focus_target(actor)
        if not _preferences.transitions or actor not in story_cast:
            return target
        elapsed = max(0.0,_story_clock.monotonic()-story_focus_started)
        progress = min(1.0,elapsed/0.16)
        progress = 1.0-(1.0-progress)**3
        before = story_focus_from.get(actor,(1.0,0.0))
        return (1.0, before[1]+(target[1]-before[1])*progress)

    def story_focus_update(actor=None):
        actor = story_id(actor)
        visible = story_visible_cast()
        desired = actor if story_standing_available() and len(visible)>1 and actor in visible else None
        if desired == story_focus_actor:
            return False
        before = {key:story_focus_values(key) for key in story_cast}
        store.story_focus_from = RevertableDict(before)
        store.story_focus_actor = desired
        store.story_focus_started = _story_clock.monotonic()
        store.story_focus_serial += 1
        return True

    def story_focus_transform(actor, transform, st, at):
        scale, brightness = story_focus_values(actor)
        transform.zoom = scale
        transform.matrixcolor = BrightnessMatrix(brightness)
        transform.alpha = 1.0
        transform.xanchor = 0.5
        transform.yanchor = 1.0
        transform.xpos = 0.5
        transform.ypos = 1.0
        return 0.016 if _story_clock.monotonic()-story_focus_started < 0.17 else 0.1

    def story_record_motion(actor, kind, token):
        store.story_effect_times[actor] = (token,_story_clock.monotonic(),STORY_MOTION_DURATIONS.get(kind,0.0))
        store.story_effect_settled.pop(actor,None)

    def story_actor_motion_transform(actor, transform, st, at):
        outgoing = story_exiting.get(actor)
        if outgoing:
            motion = ("exit",outgoing["token"],outgoing["dx"],0)
            started, duration = outgoing["started"],0.26
        else:
            motion = story_effects.get(actor,("idle",0))
            stamp = story_effect_times.get(actor)
            started, duration = (stamp[1],stamp[2]) if stamp and stamp[0] == motion[1] else (0.0,0.0)
        kind, token = motion[0],motion[1]
        settled = not _preferences.transitions or story_effect_settled.get(actor) == token or duration <= 0
        progress = 1.0 if settled else min(1.0,max(0.0,(_story_clock.monotonic()-started)/duration))
        eased = 1.0-(1.0-progress)**3
        transform.xoffset = 0
        transform.yoffset = 0
        transform.zoom = 1.0
        transform.rotate = 0
        transform.alpha = 1.0
        if kind in ("jump","group"):
            transform.yoffset = -22*_story_math.sin(_story_math.pi*progress)
        elif kind == "bounce" and progress < 1.0:
            transform.yoffset = -12 * _story_math.sin(_story_math.pi * progress)
        elif kind == "shake":
            transform.xoffset = 9*_story_math.sin(6*_story_math.pi*progress)*(1-progress)
        elif kind == "surprise":
            transform.zoom = 1.0+0.10*_story_math.sin(_story_math.pi*progress)
        elif kind == "tilt":
            transform.rotate = -6*_story_math.sin(_story_math.pi*progress)
        elif kind == "shrink":
            transform.zoom = 1.0-0.28*eased
        elif kind == "angry":
            transform.yoffset = -7*_story_math.sin(_story_math.pi*progress)
        elif kind in ("move","enter"):
            transform.xoffset = (motion[2] if len(motion)>2 else 0)*(1-eased)
            transform.yoffset = (motion[3] if len(motion)>3 else 0)*(1-eased)
        elif kind == "fade_in":
            clock = renpy.session.get("story_standing_fade_clock")
            if not settled and clock and clock[0] == token:
                # The first draw may decode both portraits. Start on the next
                # frame, using one frame time so the pair stays in sync.
                frame_time = renpy.game.interface.frame_time
                if clock[1] is None:
                    clock[1] = frame_time
                elif clock[2] is None and frame_time > clock[1]:
                    clock[2] = frame_time
                progress = min(1.0, (frame_time - clock[2]) / duration) if clock[2] is not None else 0.0
            transform.alpha = 1.0 - (1.0 - progress) ** 2
        elif kind == "fall" and _preferences.transitions:
            direction = motion[2]
            if progress < 0.35:
                shake = _story_math.sin(progress / 0.35 * 5 * _story_math.pi)
                transform.xoffset = shake * 12
                transform.rotate = shake * 3
            else:
                fall = ((progress - 0.35) / 0.65) ** 1.6
                transform.rotate = direction * 78 * fall
                transform.xoffset = direction * 265 * fall
                transform.yoffset = 154 * fall
        elif kind == "exit":
            transform.xoffset = outgoing["dx"]*eased
            if progress >= 1.0:
                transform.alpha = 0.0
        return 0.016 if progress < 1.0 else None

    def story_render_entries():
        entries = []
        visible = story_visible_cast()
        split = len(visible) != len(story_cast)
        for actor in visible:
            entries.append({"actor":actor,"face":story_faces.get(actor,"normal"),
                "position":story_actor_position(actor),
                "facing":story_facing.get(actor,1.0),"outgoing":False})
        for actor, entry in story_exiting.items():
            available_slots = len(STORY_HEROES) + (actor == "visitor")
            if (actor not in story_cast and len(entries) < available_slots
                    and (not split or (actor in STORY_HEROES) == (visible[0] in STORY_HEROES))):
                entries.append({"actor":actor,"face":entry["face"],"position":entry["position"],
                    "facing":entry["facing"],"outgoing":True})
        return entries

    def story_visible_positions():
        # Pick up a slide at its current position when another actor joins before it settles.
        positions = {actor:story_actor_position(actor) for actor in story_cast}
        if not _preferences.transitions:
            return positions
        now = _story_clock.monotonic()
        for actor, (x, y) in positions.items():
            motion = story_effects.get(actor)
            stamp = story_effect_times.get(actor)
            if (motion and len(motion) >= 4 and stamp and motion[0] in ("move", "enter") and motion[1] == stamp[0]
                    and stamp[2] > 0 and story_effect_settled.get(actor) != stamp[0]):
                remaining = 1.0 - min(1.0, max(0.0, (now - stamp[1]) / stamp[2]))
                positions[actor] = (x + motion[2] * remaining**3, y + motion[3] * remaining**3)
        return positions

    def story_slide_cast(previous, token):
        for actor in story_cast:
            if actor in previous:
                x, y = story_actor_position(actor)
                old_x, old_y = previous[actor]
                if (old_x, old_y) != (x, y):
                    store.story_effects[actor] = ("move", token, old_x-x, old_y-y)
                    story_record_motion(actor, "move", token)

    def story_enter(actor, side="left", face=None, position=None):
        if not story_standing_available():
            return False
        actor = story_id(actor)
        if actor not in STORY_CAST:
            return False
        old_positions = story_visible_positions()
        old_positions.pop(actor, None)
        store.story_exiting.pop(actor,None)
        if actor not in story_cast:
            store.story_cast = RevertableList([actor] + list(story_cast) if side == "left" else list(story_cast) + [actor])
        if face is not None:
            store.story_faces[actor] = story_face(face)
        if position is not None:
            store.story_positions[actor] = tuple(position)
        store.story_effect_serial += 1
        token = story_effect_serial
        story_slide_cast(old_positions, token)
        target_x, _ = story_actor_position(actor)
        start_x = -460 if side == "left" else 2380
        store.story_effects[actor] = ("enter",token,start_x-target_x,0)
        story_record_motion(actor,"enter",token)
        story_focus_update(story_speaker_id)
        renpy.restart_interaction()
        return True

    def story_stage_fade_in(actors):
        if story_standing_available():
            story_stage(cast=actors)
            story_effect("fade_in", actors)
            renpy.session["story_standing_fade_clock"] = [story_effect_serial, None, None]

    def story_stage_fall(actor, side="right"):
        if story_standing_available() and actor in story_cast and _preferences.transitions:
            store.story_effect_serial += 1
            token = story_effect_serial
            store.story_effects[actor] = ("fall", token, -1 if side == "left" else 1)
            story_record_motion(actor, "fall", token)
            renpy.restart_interaction()
            renpy.pause(STORY_MOTION_DURATIONS["fall"])

    def story_exit(actor, side="right"):
        if not story_standing_available():
            return False
        actor = story_id(actor)
        if actor not in story_cast:
            return False
        positions = story_visible_positions()
        was_visible = actor in story_visible_cast()
        store.story_effect_serial += 1
        target_x = -460 if side == "left" else 2380
        entry = RevertableDict({"token":story_effect_serial,"started":_story_clock.monotonic(),
            "dx":target_x-positions[actor][0],"position":positions[actor],
            "face":story_faces.get(actor,"normal"),"facing":story_facing.get(actor,1.0)})
        store.story_cast = RevertableList(key for key in story_cast if key != actor)
        story_slide_cast(positions, story_effect_serial)
        store.story_effects.pop(actor,None)
        store.story_effect_times.pop(actor,None)
        store.story_reaction_icons.pop(actor,None)
        if _preferences.transitions and was_visible:
            store.story_exiting[actor] = entry
        else:
            store.story_exiting.pop(actor,None)
        story_focus_update(story_speaker_id)
        renpy.restart_interaction()
        return True

    def story_icon(actor, kind, duration=0.9):
        if not story_standing_available():
            return False
        actor = story_id(actor)
        if actor not in story_cast or kind not in STORY_ICON_KINDS:
            return False
        store.story_effect_serial += 1
        lifetime = max(0.2,min(float(duration),2.0))
        store.story_reaction_icons[actor] = (kind,story_effect_serial,_story_clock.monotonic()+lifetime,lifetime)
        renpy.restart_interaction()
        return True

    def story_icon_for(actor):
        icon = story_reaction_icons.get(actor)
        return icon if icon and icon[2]>_story_clock.monotonic() and actor in story_cast else None

    def story_heart_motion_transform(icon, transform, st, at):
        lifetime = icon[3] if len(icon) > 3 else 0.9
        progress = max(0.0, min(1.0, 1.0 - (icon[2] - _story_clock.monotonic()) / lifetime))
        # Follow the cue clock so dialogue redraws cannot restart the heart.
        pop = 1.0 - (1.0 - min(1.0, progress / 0.16)) ** 2
        transform.zoom = 0.82 + 0.18 * pop
        transform.yoffset = 3 - 31 * progress
        transform.alpha = (0.65 + 0.35 * pop) * min(1.0, (1.0 - progress) / 0.32)
        return 0.016 if progress < 1.0 else None

    def story_motion_tick():
        now = _story_clock.monotonic()
        for actor,entry in list(story_exiting.items()):
            if not _preferences.transitions or now-entry["started"]>=0.26:
                store.story_exiting.pop(actor,None)
        for actor,icon in list(story_reaction_icons.items()):
            if now>=icon[2] or actor not in story_cast:
                store.story_reaction_icons.pop(actor,None)

    def story_motion_restore():
        # Saved standing state is authoritative; transient travel/icons settle
        # instead of replaying. Outgoing actors were already removed from cast.
        store.story_exiting = RevertableDict()
        store.story_reaction_icons = RevertableDict()
        store.story_effect_settled = RevertableDict({actor:motion[1] for actor,motion in story_effects.items()})
        visible = story_visible_cast()
        store.story_focus_actor = story_speaker_id if story_standing_available() and len(visible)>1 and story_speaker_id in visible else None
        store.story_focus_from = RevertableDict()
        store.story_focus_started = 0.0

    def story_preview_focus(actor):
        if not config.developer:
            return
        store.story_speaker_id = story_id(actor)
        if story_speaker_id in story_cast:
            store.story_team_speaker = story_speaker_id
        story_focus_update(actor)
        renpy.restart_interaction()

    def story_preview_action(action,*args,**kwargs):
        if not config.developer:
            return
        # Function actions return non-None values from call screen. Keep the
        # helpers' success booleans from closing the manual preview controls.
        action(*args,**kwargs)
        renpy.restart_interaction()

    def story_motion_will_load():
        renpy.session["standing_motion_settle_on_interact"] = True

    def story_motion_start_interact():
        if renpy.session.pop("standing_motion_settle_on_interact",False):
            story_motion_restore()
        story_motion_tick()

    config.after_load_callbacks.append(story_motion_restore)
    config.before_load_callbacks.append(story_motion_will_load)
    config.start_interact_callbacks.append(story_motion_start_interact)

    def story_flag(name, value=True):
        if name in ("first_task_partner", "ch02_partner", "ch03_partner", "ch03_evening_event"):
            value = story_id(value)
        setattr(store, name, value)
        if isinstance(value, bool):
            if value:
                event_flags.add(name)
            else:
                event_flags.discard(name)
        if name.startswith("rumi_"):
            setattr(store, "lumi_" + name[5:], value)
            if value is True:
                event_flags.add("lumi_" + name[5:])
        if name.endswith("_special_moment"):
            key = story_id(name[:-15])
            if key in STORY_HEROES:
                special_moment[key] = bool(value)
        if name in ("visitor_policy_priority", "visitor_policy_established"):
            store.visitor_policy = getattr(store, "visitor_policy_priority", None)

    def story_apply(choice_id, affection=None, trust=None, values=None, counters=None, hearts=None):
        # A retained phone interaction can replay the already-completed script
        # after native load. Its saved reward/log must remain applied only once.
        if phone_is_replaying_choice(choice_id):
            return
        if choice_id in heart_awarded_choices and choice_id in choice_log:
            return
        feedback_changes = relationship_apply(hearts=hearts, choice_id=choice_id)
        for key, value in (values or {}).items():
            story_flag(key, value)
        for key, delta in (counters or {}).items():
            story_flag(key, getattr(store, key, 0) + delta)
        store.choice_log.append(choice_id)
        relationship_feedback_publish(choice_id, feedback_changes)

    def story_begin_chapter(number, title):
        store.story_offscreen_actor = None
        cg_end(transition=0, restore=False)
        sd_event_reset_for_chapter()
        store.story_active = True
        store.story_stage_visible = True
        store.story_chapter_number = number
        store.chapter = "CH{:02d} · {}".format(number, title)
        store.story_chapter_started = renpy.get_game_runtime()
        store.story_chat_active = False
        store.story_chat_messages = RevertableList()
        store.story_cast = RevertableList()
        store.story_team_speaker = None
        store.story_positions = RevertableDict()
        store.story_facing = RevertableDict()
        store.story_effects = RevertableDict()
        store.story_effect_times = RevertableDict()
        store.story_effect_settled = RevertableDict()
        store.story_exiting = RevertableDict()
        store.story_reaction_icons = RevertableDict()
        store.story_focus_actor = None
        store.story_focus_from = RevertableDict()
        store.story_focus_started = 0.0
        store.story_speaker_id = None
        store.story_mode = "normal"

    STORY_LOCATION_WIPE = MultipleTransition([
        False, CropMove(0.20, "wipeleft"),
        Solid("#000"), Pause(0.06),
        Solid("#000"), CropMove(0.22, "wipeleft"),
        True,
    ])

    def story_scene(bg, mode="normal", cast=None, music=None, light="day", location=None, standing=True):
        changing_place = (bg != story_background and renpy.showing("story_background", layer="master"))
        cg_end(transition=0, restore=False)
        sd_event_end(transition=0, restore=False)
        store.story_stage_visible = standing
        store.story_positions = RevertableDict()
        store.story_facing = RevertableDict()
        store.story_faces = RevertableDict()
        light = light if light in ("day","evening","night") else "day"
        store.story_background = bg
        store.story_light = light
        store.story_chat_active = False
        store.story_chat_messages = RevertableList()
        if location:
            store.location_name = location
        renpy.scene()
        renpy.show("story_background", what=story_background_display(bg,light))
        story_stage(mode=mode, cast=cast or [])
        store.story_team_speaker = story_cast[0] if story_cast else None
        if music:
            play_bgm(music)
        if _preferences.transitions and changing_place:
            renpy.transition(STORY_LOCATION_WIPE)

    def story_stage(mode=None, cast=None, faces=None, positions=None, facing=None):
        if cg_is_active():
            if mode in ("normal", "emotion"):
                cg_end(transition=0, restore=False)
            elif mode != "sd":
                return
        # Saved old SD calls are adapted to a single registered event cut.
        if mode == "sd":
            guess = sd_event_guess_legacy() or {"id":"ch01_group_meeting","variant":"01"}
            sd_event_start(guess["id"], guess["variant"])
            return
        if sd_event_is_active():
            if mode in ("normal", "emotion"):
                sd_event_end(mode=mode, transition=0, restore=False)
            else:
                return
        if mode is not None:
            if mode != story_mode:
                store.story_positions = RevertableDict()
                store.story_facing = RevertableDict()
            store.story_mode = mode
        if cast is not None:
            store.story_cast = RevertableList(story_normalize_cast(cast))
            store.story_effects = RevertableDict()
            store.story_effect_times = RevertableDict()
            store.story_effect_settled = RevertableDict()
            store.story_exiting = RevertableDict()
            store.story_reaction_icons = RevertableDict()
        for actor, face in (faces or {}).items():
            store.story_faces[story_id(actor)] = story_face(face)
        for actor, point in (positions or {}).items():
            store.story_positions[story_id(actor)] = tuple(point)
        for actor, direction in (facing or {}).items():
            store.story_facing[story_id(actor)] = -1.0 if direction < 0 else 1.0
        store.story_caption = ""
        story_focus_update(story_speaker_id)

    def story_faceoff(left, right, left_face="normal", right_face="normal"):
        left, right = story_id(left), story_id(right)
        story_stage(mode="sd", cast=[left,right], faces={left:left_face,right:right_face},
            positions={left:(610,510),right:(1310,510)}, facing={left:1,right:-1})

    def story_move(actor, x, y):
        if sd_event_is_active() or cg_is_active():
            return
        actor = story_id(actor)
        if actor not in story_cast:
            return
        old_x, old_y = story_visible_positions()[actor]
        store.story_positions[actor] = (x,y)
        store.story_effect_serial += 1
        store.story_effects[actor] = ("move",story_effect_serial,old_x-x,old_y-y)
        story_record_motion(actor,"move",story_effect_serial)
        renpy.restart_interaction()

    def story_effect(kind, target=None, caption=None):
        if sd_event_is_active() or cg_is_active():
            return
        store.story_effect_serial += 1
        targets = target if isinstance(target, (list, tuple)) else [target]
        if target is None:
            targets = story_cast
        for key in targets:
            actor = story_id(key)
            if actor in STORY_CAST:
                store.story_effects[actor] = (kind, story_effect_serial)
                story_record_motion(actor,kind,story_effect_serial)
        if caption is not None:
            store.story_caption = caption
        renpy.restart_interaction()

    def story_chat(active, title="축제 준비팀"):
        checkpoint = (story_chapter_number, story_background, story_light, location_name, len(story_read_log))
        was_reading = (story_chat_active and phone_is_open and phone_view == "chat"
                       and phone_active_thread is not None and phone_selected_thread == phone_active_thread)
        if active:
            cg_end(transition=0)
            sd_event_end(transition=0)
        elif story_chat_active:
            # A script can close one room and immediately enter another. An
            # intervening spoken line or a new scene invalidates this checkpoint.
            store.phone_continuation_checkpoint = checkpoint if was_reading else None
        store.story_chat_active = bool(active)
        store.story_chat_title = title
        store.story_chat_messages = RevertableList()
        if active:
            store.story_cast = RevertableList()
            phone_begin(title, keep_open=was_reading or checkpoint == phone_continuation_checkpoint)
            if not renpy.session.get("phone_gate_restore_on_interact", False):
                story_sfx("message")
        else:
            store.phone_active_thread = None
            phone_sync_skip_permission()

    def story_fade_out():
        cg_end(transition=0, restore=False)
        sd_event_end(transition=0, restore=False)
        store.story_stage_visible = False
        store.story_chat_active = False
        store.story_caption = ""

    def story_sfx(name):
        if name == "door":
            name = "door_open"
        paths = ["audio/sfx/" + name + extension for extension in (".ogg", ".wav", ".mp3")]
        if name == "message":
            paths.append("audio/sfx/click.wav")
        path = next((p for p in paths if renpy.loadable(p)), None)
        if path:
            renpy.sound.play(path)

    def story_speaker_callback(actor, event, **kwargs):
        if event != "begin" or not story_active:
            return
        actor = story_id(actor)
        store.story_speaker_id = actor
        text = kwargs.get("what", "")
        if text:
            store.story_read_log.append((story_chapter_number, actor, text))
        if sd_event_is_active() or cg_is_active():
            return
        # The CH02 committee notice contains authored narrator lines.
        if actor == story_offscreen_actor:
            # A voice behind a closed door does not replace the visible team.
            # Its ordinary Character name/text still belongs to this Say line.
            story_focus_update(None)
            return
        if story_chat_active and actor == "narrator" and phone_active_thread == "festival_committee":
            actor = "system"
        if story_chat_active and actor not in ("narrator", None) and text:
            name = player_name if actor == "mc" else STORY_CAST.get(actor, {}).get("name", "알림")
            store.story_chat_messages = RevertableList((list(story_chat_messages) + [(name, text, actor)])[-3:])
            phone_record(actor,text)
        elif story_standing_available() and actor in STORY_CAST and (actor != "visitor" or actor in story_cast):
            if actor not in story_cast:
                store.story_exiting.pop(actor, None)
                store.story_cast.append(actor)
            store.story_team_speaker = actor
        story_focus_update(actor)

    def story_speaking(actor):
        return partial(story_speaker_callback, actor)

    def story_complete_chapter(number):
        cg_end(transition=0, restore=False)
        story_flag("chapter{:02d}_complete".format(number), True)
        persistent.chapter_completions.add("ch{:02d}".format(number))
        persistent.choice_memories.update(choice_log)
        if number == 1:
            store.ch01_done = True
            complete_chapter()
        lines = [entry for entry in story_read_log if entry[0] == number]
        store.chapter_metrics[number] = RevertableDict({
            "engine_seconds": round(max(0, renpy.get_game_runtime() - story_chapter_started), 2),
            "displayed_lines": len(lines),
            "displayed_characters": sum(len(entry[2]) for entry in lines),
        })
        store.story_chat_active = False
        renpy.save_persistent()

    def story_migrate_save():
        # Merge collections here. Score units migrate when gameplay resumes.
        for key in STORY_HEROES:
            affection.setdefault(key, 0)
            trust.setdefault(key, 0)
            special_moment.setdefault(key, False)
        if ch01_done:
            store.chapter01_complete = True
        if first_task_partner is None and ch01_done:
            mapping = {"walk_roman":"roman", "walk_sia":"sia", "walk_darim":"darim",
                "walk_omu":"omu", "walk_lumi":"lumi"}
            detected = next((value for flag, value in mapping.items() if flag in event_flags), None)
            store.first_task_partner = detected or STORY_HEROES[0]
        for name in ("first_task_partner", "ch02_partner", "ch03_partner", "ch03_evening_event"):
            setattr(store, name, story_id(getattr(store, name, None)))
        store.chapter_save_schema = 2

    def story_debug_start(label):
        if not config.developer:
            return
        renpy.jump_out_of_context(label)

    config.always_shown_screens.append("story_stage_view")

define ski = Character("스키", callback=story_speaking("ski"))
define hyeophap = Character("협합", callback=story_speaking("hyeophap"))
define hess = Character("헤스", callback=story_speaking("hess"))
define bambam = Character("밤밤", callback=story_speaking("bambam"))
define staff = Character("운영위원", callback=story_speaking("staff"))
define visitor = Character("방문객", callback=story_speaking("visitor"))
define system_note = Character("알림", callback=story_speaking("system"))
define unknown_voice = Character("???", callback=story_speaking("unknown"))

label chapters_demo_end:
    $ sd_event_end(transition=0, restore=False)
    $ story_chat(False)
    $ story_active = False
    call screen chapters_complete
    return

# Compatibility label; its presentation is now a whole-illustration preview.
label story_sd_preview:
    if not config.developer:
        return
    $ story_begin_chapter(2, "SD 이벤트 컷 미리보기")
    $ story_scene("prep_room", mode="normal", cast=["roman"], location="SD 이벤트 컷 미리보기")
    $ sd_event_start("ch02_rival_introduction", "01")
    ski "제 준비는 언제나 완벽한 편입니다."
    $ sd_event_change("02")
    sia "그 자신감, 아직 유효해?"
    $ sd_event_change("03")
    hyeophap "작업부터 진행하죠."
    $ sd_event_end(mode="emotion", cast=["roman"])
    roman "잠깐은… 조용하게 이야기해도 괜찮을까요?"
    $ story_active = False
    return

label standing_motion_preview:
    if not config.developer:
        return
    $ story_begin_chapter(0,"일반 스탠딩 모션 시연")
    $ story_scene("clubroom",mode="normal",cast=["roman","sia"],location="개발용 일반 스탠딩 시연")
    roman "제가 말할 때는 조금 더 선명하게 보여요."
    roman "같은 사람이 계속 말해도 강조 효과를 다시 시작하지 않아요."
    sia "이번엔 내 차례. 다른 사람은 투명해지는 대신 조금 어두워져."
    narrator "해설이나 화면 밖의 목소리에서는 모두 기본 상태로 돌아옵니다."
    $ story_effect("jump","roman")
    $ story_icon("roman","exclamation")
    roman "앗,,, 조금 놀랐어요……!"
    $ story_effect("shake","sia")
    sia "잠깐, 그렇게 놀랄 일은 아니잖아!"
    $ story_icon("roman","heart")
    roman "같이 이야기해서 좋아요."
    $ story_icon("sia","lightbulb")
    sia "좋은 생각 났어."
    $ story_exit("sia","right")
    narrator "시아가 오른쪽으로 나갑니다."
    $ story_enter("lumi","right",face="happy",position=(1310,795))
    lumi "저는 오른쪽에서 들어올게요."
    $ story_exit("roman","left")
    narrator "로만이 왼쪽으로 나갑니다."
    $ story_enter("sia","left",face="happy",position=(610,795))
    sia "왼쪽 입장도 이쪽이야."
    $ story_stage(mode="normal",cast=["roman","sia"],positions={"roman":(610,795),"sia":(1310,795)})
    $ story_preview_focus("roman")
    call screen standing_motion_demo_controls
    $ story_active = False
    return
