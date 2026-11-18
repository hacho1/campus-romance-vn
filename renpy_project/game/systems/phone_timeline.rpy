# Authored story time and phone ownership. These values roll back and save with
# the current playthrough; never read the operating-system clock.
default phone_day_id = "ch01_day1"
default phone_day_index = 1
default phone_timeline_episode = None
default phone_timeline_scene = None
default phone_timeline_schema = 0
default phone_perspective = "mc"

init -4 python:
    def phone_episode_id(number=None):
        number = story_chapter_number if number is None else number
        if number == 199:
            return "SECRET"
        if number == 299:
            return "SSECRET"
        if number == 399:
            return "OSECRET"
        if number == 599:
            return "HSECRET"
        if number in range(501, 507):
            return "H{:02d}".format(number - 500)
        if number == 499:
            return "DSECRET"
        if number in range(401, 407):
            return "D{:02d}".format(number - 400)
        if number in range(301, 307):
            return "O{:02d}".format(number - 300)
        if number in range(201, 207):
            return "S{:02d}".format(number - 200)
        return "R{:02d}".format(number - 100) if number >= 100 else "CH{:02d}".format(number)

    def phone_timeline_set(day_id, date, time, day_index=None, episode=None):
        """Set a script-authored date/time; previous messages remain immutable."""
        pieces = str(time).split(":")
        if len(pieces) != 2 or not all(piece.isdigit() for piece in pieces):
            raise ValueError("잘못된 대본 시각: " + str(time))
        hour, minute = int(pieces[0]), int(pieces[1])
        if not 0 <= hour <= 23 or not 0 <= minute <= 59:
            raise ValueError("잘못된 대본 시각: " + str(time))
        store.phone_day_id = str(day_id)
        store.phone_date = str(date)
        store.phone_clock = "{:02d}:{:02d}".format(hour, minute)
        if day_index is not None:
            store.phone_day_index = int(day_index)
        store.phone_timeline_episode = episode or phone_episode_id()
        store.phone_timeline_schema = 1

    def phone_timeline_cue(episode, cue):
        data = PHONE_UI.get("timeline", {}).get(str(episode), {}).get(str(cue))
        if data:
            phone_timeline_set(data["day_id"], data["date"], data["time"], data["day_index"], episode)
            return True
        return False

    def phone_timeline_enter(episode, scene):
        store.phone_timeline_scene = scene
        phone_perspective_set("mc")
        if not phone_timeline_cue(episode, scene):
            phone_timeline_ensure(episode)

    def phone_timeline_ensure(episode=None):
        episode = episode or phone_episode_id()
        if phone_timeline_schema >= 1 and phone_timeline_episode == episode:
            return
        data = PHONE_UI.get("episode_defaults", {}).get(episode)
        if data:
            phone_timeline_set(data["day_id"], data["date"], data["time"], data["day_index"], episode)
            return
        # Legacy/unregistered development labels have a visible story-light
        # fallback rather than silently reverting to chapter one's 21:14.
        clock = {"night":"21:00", "evening":"18:00"}.get(story_light, "09:00")
        phone_timeline_set("legacy_" + episode, "이야기 " + episode, clock, episode=episode)

    def phone_perspective_set(actor="mc"):
        actor = story_id(actor) if actor != "mc" else "mc"
        store.phone_perspective = actor if actor in STORY_HEROES else "mc"

    def phone_perspective_label():
        return (STORY_CAST.get(phone_perspective, {}).get("name", "") + "의 휴대폰"
                if phone_perspective != "mc" else "내 휴대폰")

    def phone_message_is_mine(message):
        return story_id(message.get("actor")) == phone_perspective

    def phone_current_title():
        return phone_thread_display_title(phone_selected_thread)

    def phone_thread_display_title(thread_id):
        if phone_perspective != "mc" and thread_id == "private_" + phone_perspective:
            return player_name
        return phone_threads.get(thread_id, {}).get("title", "메시지")

    def phone_room_avatar_actor(thread_id):
        if phone_perspective != "mc" and thread_id == "private_" + phone_perspective:
            return "mc"
        return phone_thread_actor(thread_id)

    def phone_pov_recap_reference(room, actor, text):
        # R03 SC04 rereads the two messages actually sent in SC03. This is a
        # viewpoint replay, not two additional incoming messages. No other
        # scene/day or coincidentally repeated short reply is deduplicated.
        recap = ("로만 씨, 원고 준비는 잘되고 계세요?", "마감 끝나고 시간 괜찮으시면 같이 이야기하고 싶어요.")
        if (phone_timeline_scene != "roman_r03_sc04" or phone_perspective != "roman"
                or actor != "mc" or text not in recap):
            return False
        for message in reversed(room.get("messages", [])):
            if (message.get("actor") == actor and message.get("text") == text
                    and message.get("day_id") == phone_day_id):
                store.phone_last_key = message["key"]
                return True
        return False

    def phone_message_date_label(message):
        date = message.get("date", phone_date)
        if message.get("day_id") == phone_day_id:
            return "오늘 · " + date
        previous = message.get("day_index")
        if previous is not None and previous == phone_day_index - 1:
            return "어제 · " + date
        return date

    def phone_timeline_migrate():
        # New saves retain the exact authored checkpoint. Old message timestamps
        # are historical data and are deliberately not rewritten.
        if phone_timeline_schema < 1:
            filename, line = renpy.get_filename_line()
            basename = str(filename).replace("\\", "/").split("/")[-1]
            candidates = [item for item in PHONE_UI.get("timeline_positions", {}).get(basename, []) if item["line"] <= line]
            if candidates:
                checkpoint = candidates[-1]
                phone_timeline_cue(checkpoint["episode"], checkpoint["cue"])
                phone_perspective_set(checkpoint.get("perspective", "mc"))
            else:
                phone_timeline_ensure()
        phone_perspective_set(phone_perspective)
