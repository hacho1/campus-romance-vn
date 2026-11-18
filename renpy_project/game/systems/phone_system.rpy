# Native message UI. Phone history belongs to the current save, never a global collection.
default phone_threads = {}
default phone_active_thread = None
default phone_selected_thread = None
default phone_view = "chat"
default phone_sequence = 0
default phone_schema = 0
default phone_date = "축제 준비 · 첫날"
default phone_clock = "11:40"
default phone_last_key = None
default phone_is_open = False
default phone_notification_pending = False
default phone_gate_schema = 0
default phone_read_ready_at = 0.0
default phone_previous_skipping = None
default phone_continuation_checkpoint = None

init -5 python:
    import hashlib
    import os
    PHONE_UI = read_data("phone_ui")
    PHONE_INK = "#293f49"
    PHONE_MUTED = "#586e77"

    def phone_wallpaper():
        path = PHONE_UI.get("wallpaper", "")
        stem,extension = os.path.splitext(path)
        return next((candidate for candidate in (path,stem+".png",stem+".webp") if candidate and renpy.loadable(candidate)),"images/backgrounds/campus.png")

    def phone_panel(kind="panel"):
        return Frame("images/ui/phone/" + kind + ".png", 28,28)

    def phone_thread_id(title):
        # A heroine talking to a friend is not the player's private room with
        # that friend. Keep both histories instead of relabelling old messages.
        perspective_id = PHONE_UI.get("perspective_threads", {}).get(phone_perspective, {}).get(title)
        if perspective_id:
            return perspective_id
        group_id = PHONE_UI.get("group_threads", {}).get(title)
        if group_id:
            return group_id
        service_id = PHONE_UI["service_threads"].get(title)
        if service_id:
            return service_id
        if "루미" in title:
            return "private_lumi"
        for actor in STORY_HEROES:
            if STORY_CAST[actor]["name"] in title:
                return "private_" + actor
        return "campus_group"

    def phone_is_group_thread(thread_id):
        return (thread_id in ("campus_group", "sia_course_group")
            or thread_id in PHONE_UI.get("group_threads", {}).values())

    def phone_thread_actor(thread_id):
        actor = PHONE_UI.get("thread_actors", {}).get(thread_id)
        if actor:
            return actor
        return thread_id.replace("private_", "") if thread_id and thread_id.startswith("private_") else "group"

    def phone_is_replaying_choice(choice_id):
        # Retained phone data can outlive the script checkpoint being replayed
        # during loading. An effect already in the saved choice log is complete.
        # This flag ends before the first real interaction; normal play and
        # ordinary rollback retain their original choice-effect behaviour.
        return bool(story_chat_active and not main_menu and not renpy.context()._menu
            and renpy.session.get("phone_gate_restore_on_interact", False)
            and choice_id in choice_log)

    def phone_sync_skip_permission():
        # The SDK's Skip timer bypasses say_allow_dismiss. Suspend its native
        # permission only while the current phone line cannot yet be read.
        blocked = story_chat_active and (not phone_is_open or phone_view != "chat" or phone_selected_thread != phone_active_thread)
        if blocked:
            if phone_previous_skipping is None:
                store.phone_previous_skipping = store._skipping
            store._skipping = False
        elif phone_previous_skipping is not None:
            store._skipping = phone_previous_skipping
            store.phone_previous_skipping = None

    def phone_begin(title, keep_open=False):
        key = phone_thread_id(title)
        if (renpy.session.get("phone_gate_restore_on_interact", False)
                and phone_schema >= 1 and phone_gate_schema >= 1
                and key == phone_active_thread and key in phone_threads):
            # Loading can replay the current event's entry before its first say.
            # The saved lock/list/chat state already belongs to this same room.
            return
        store.phone_continuation_checkpoint = None
        if key not in phone_threads:
            room_title = title
            if key == "campus_group":
                room_title = "축제 준비팀"
            elif key.startswith("private_"):
                room_title = STORY_CAST[phone_thread_actor(key)]["name"]
            phone_threads[key] = RevertableDict({"title":room_title, "messages":RevertableList(), "unread":0})
        store.phone_active_thread = key
        store.phone_selected_thread = key
        store.phone_view = "chat"
        phone_timeline_ensure()
        store.phone_schema = 1
        # Adjacent rooms can share an open phone. A separate event waits until
        # the player opens its first native line from the notification.
        store.phone_is_open = keep_open
        store.phone_notification_pending = not keep_open
        store.phone_read_ready_at = 0.0
        store.phone_gate_schema = 1
        config.skipping = None
        phone_sync_skip_permission()

    def phone_open_current():
        if not phone_active_thread:
            return
        first_open = phone_notification_pending
        store.phone_is_open = True
        store.phone_notification_pending = False
        store.phone_selected_thread = phone_active_thread
        store.phone_view = "lock" if first_open else phone_view if phone_view in ("lock","list","chat") else "chat"
        if phone_view == "chat":
            # A load may replay setup before the first visible interaction.
            # Replayed navigation is not a fresh acknowledgement by the player.
            if not renpy.session.get("phone_gate_restore_on_interact", False):
                phone_threads[phone_active_thread]["unread"] = 0
            phone_reset_read_delay()
        config.skipping = None
        phone_sync_skip_permission()
        renpy.restart_interaction()

    def phone_close_current():
        store.phone_is_open = False
        config.skipping = None
        phone_sync_skip_permission()
        renpy.restart_interaction()

    def phone_record(actor, text, legacy_key=None):
        if not phone_active_thread:
            phone_begin(story_chat_title)
        filename,line = renpy.get_filename_line()
        key_prefix = "{}:{}:{}:".format(story_chapter_number, filename, line)
        key = legacy_key or key_prefix + hashlib.sha256((str(actor) + text).encode("utf-8")).hexdigest()[:16]
        replaying = legacy_key is None and renpy.session.get("phone_gate_restore_on_interact", False)
        room = phone_threads[phone_active_thread]
        if legacy_key is None and phone_pov_recap_reference(room, actor, renpy.substitute(text)):
            return
        if replaying:
            # Added staging statements move filename:line keys between builds.
            # Only the exact saved live message may be referenced while loading;
            # ordinary play and genuine repeated messages still append normally.
            saved = next((message for message in room["messages"]
                          if message.get("key") == phone_last_key), None)
            old_key = str(saved.get("key", "")) if saved else ""
            old_prefix = old_key.rsplit(":", 2)[0]
            old_file = old_prefix.split(":", 1)[1] if ":" in old_prefix else ""
            same_file = old_file.replace("\\", "/").split("/")[-1] == str(filename).replace("\\", "/").split("/")[-1]
            if (saved and old_key.startswith(str(story_chapter_number) + ":") and same_file
                    and saved.get("actor") == actor and saved.get("text") == renpy.substitute(text)):
                return
        # Loading may replay earlier authored statements while retained phone
        # history already includes them, including keys from before the rename.
        if any(message["key"] == key or
               (replaying and message["actor"] == actor and message["key"].startswith(key_prefix))
               for message in room["messages"]):
            return
        name = player_name if actor == "mc" else STORY_CAST.get(actor,{}).get("name","알림")
        store.phone_sequence += 1
        room["updated"] = phone_sequence
        room["messages"].append(RevertableDict({"actor":actor,"name":name,"text":renpy.substitute(text),"time":phone_clock,"date":phone_date,"day_id":phone_day_id,"day_index":phone_day_index,"perspective":phone_perspective,"key":key}))
        if story_id(actor) != phone_perspective and (not phone_is_open or phone_view != "chat" or phone_selected_thread != phone_active_thread):
            room["unread"] += 1
        else:
            room["unread"] = 0
        store.phone_last_key = key

    def phone_reset_read_delay():
        # Waiting on a lock screen must not consume the native line's AFM time.
        room = phone_threads.get(phone_selected_thread,{})
        text = room.get("messages", [{}])[-1].get("text", "") if room.get("messages") else ""
        delay = ((config.afm_bonus + len(text)) / max(1.0,config.afm_characters)) * _preferences.afm_time
        store.phone_read_ready_at = renpy.get_game_runtime() + max(.25,delay)

    def phone_set_view(view, thread=None):
        store.phone_view = view
        if thread is not None:
            store.phone_selected_thread = thread
        if view == "chat" and phone_selected_thread in phone_threads:
            if not renpy.session.get("phone_gate_restore_on_interact", False):
                phone_threads[phone_selected_thread]["unread"] = 0
            phone_reset_read_delay()
            config.skipping = None
        phone_sync_skip_permission()
        renpy.restart_interaction()

    def phone_advance():
        if phone_allow_dismiss():
            renpy.end_interaction(True)

    def phone_archive_close():
        if story_chat_active:
            store.phone_selected_thread = phone_active_thread
            store.phone_view = "chat"
        renpy.hide_screen("phone_browser")
        renpy.restart_interaction()

    def phone_current_room():
        return phone_threads.get(phone_selected_thread, {"title":"메시지","messages":[],"unread":0})

    def phone_rooms():
        owners = PHONE_UI.get("thread_owners", {})
        visible = PHONE_UI.get("perspective_visible_threads", {}).get(phone_perspective)
        keys = [key for key in phone_threads
            if (key not in owners or owners[key] == phone_perspective)
            and (visible is None or key in visible)]
        return sorted(keys, key=lambda key: phone_threads[key].get("updated",0), reverse=True)

    def phone_preview(key,limit=56):
        messages = phone_threads.get(key,{}).get("messages",[])
        text = messages[-1]["text"] if messages else "아직 도착한 메시지가 없어요."
        return text if len(text) <= limit else text[:limit] + "…"

    def phone_portrait(actor):
        if actor not in STORY_CAST:
            return None
        for p in ("images/heroines/profile_"+actor+".png", "images/heroines/"+actor+"/profile.png", "images/heroines/"+actor+"/profile.webp", "images/heroines/profile_"+actor+".webp"):
            if renpy.loadable(p):
                return p
        return None

    def phone_repair_ch07_greeting():
        """Repair only the SC01 -> SC02 recap emitted by version 0.4.0."""
        room = phone_threads.get("campus_group")
        if not room:
            return 0
        messages = room["messages"]

        def greeting(message, text):
            key = str(message.get("key", "")).replace("\\", "/")
            return (message.get("actor") == "sia" and message.get("text") == text
                    and key.startswith("7:") and "chapter07_official.rpy:" in key)

        removed = set()
        for index in range(len(messages) - 1):
            if not (greeting(messages[index], "야")
                    and greeting(messages[index + 1], "다들 살아 있냐?")):
                continue
            cursor = index + 2
            # A save may stop on either half of the erroneous second pair.
            while cursor < len(messages) and greeting(messages[cursor], "야"):
                removed.add(cursor)
                cursor += 1
                if cursor < len(messages) and greeting(messages[cursor], "다들 살아 있냐?"):
                    removed.add(cursor)
                    cursor += 1
        if not removed:
            return 0
        unread = max(0, min(int(room.get("unread", 0)), len(messages)))
        removed_unread = sum(index >= len(messages) - unread for index in removed)
        removed_keys = {messages[index].get("key") for index in removed}
        for index in sorted(removed, reverse=True):
            del messages[index]
        room["unread"] = unread - removed_unread
        if phone_last_key in removed_keys:
            store.phone_last_key = messages[-1].get("key") if messages else None
        return len(removed)

    def phone_migrate_after_load(force_legacy_gate=False):
        phone_timeline_migrate()
        legacy_gate = force_legacy_gate or phone_gate_schema < 1
        if renpy.session.get("phone_gate_restore_on_interact", False):
            # The loaded schema can survive native rollback reset even when the
            # other callback writes do not. Keep the FIRST schema decision.
            renpy.session.setdefault("phone_gate_legacy_loaded", legacy_gate)
        if story_chat_active and (phone_schema == 0 or not phone_active_thread):
            old = list(story_chat_messages)
            phone_begin(story_chat_title)
            for index,(name,text,actor) in enumerate(old):
                phone_record(actor,text,legacy_key="legacy:{}:{}".format(story_chapter_number,index))
        store.phone_schema = 1
        harin_name = STORY_CAST["lumi"]["name"]
        for thread_id, room in phone_threads.items():
            if thread_id == "private_lumi" and room["title"] != harin_name:
                room["title"] = harin_name
            for message in room["messages"]:
                if story_id(message.get("actor")) == "lumi" and message.get("name") != harin_name:
                    message["name"] = harin_name
        phone_repair_ch07_greeting()
        if phone_view not in ("chat","list","lock"):
            store.phone_view = "chat"
        if legacy_gate:
            # Old saves already showing a phone keep their exact reading checkpoint.
            store.phone_is_open = bool(story_chat_active)
            store.phone_notification_pending = False
        if not story_chat_active:
            store.phone_is_open = False
            store.phone_notification_pending = False
        store.phone_gate_schema = 1
        if story_chat_active and not phone_is_open:
            config.skipping = None
        phone_sync_skip_permission()

    def phone_gate_will_load():
        renpy.session["phone_gate_restore_on_interact"] = True
        renpy.session.pop("phone_gate_legacy_loaded", None)

    def phone_gate_start_interact():
        # Native loading can reset callback writes before the restored say resumes.
        # Reapply migration once at the actual first visible interaction boundary.
        if renpy.session.pop("phone_gate_restore_on_interact", False):
            phone_migrate_after_load(force_legacy_gate=renpy.session.pop("phone_gate_legacy_loaded", False))
        phone_sync_skip_permission()
        if story_chat_active and not main_menu and not renpy.context()._menu:
            # Phone navigation changes during a native say interaction. Keep
            # those exact saved values when loading, rather than the older
            # pre-say checkpoint. This SDK API leaves ordinary rollback intact.
            renpy.retain_after_load()

    if phone_gate_will_load not in config.before_load_callbacks:
        config.before_load_callbacks.append(phone_gate_will_load)
    if phone_gate_start_interact not in config.start_interact_callbacks:
        config.start_interact_callbacks.append(phone_gate_start_interact)

    def phone_open_archive():
        if story_chat_active:
            phone_open_current()
            return
        rooms = phone_rooms()
        store.phone_selected_thread = (phone_active_thread if phone_active_thread in rooms
            else rooms[0] if rooms else None)
        store.phone_view = "list"
        renpy.show_screen("phone_browser")

    # Respect the native dismissal policy while browsing another phone page.
    _phone_original_allow_dismiss = config.say_allow_dismiss
    def phone_allow_dismiss():
        if story_chat_active and (not phone_is_open or phone_view != "chat" or phone_selected_thread != phone_active_thread):
            return False
        return _phone_original_allow_dismiss() if callable(_phone_original_allow_dismiss) else _phone_original_allow_dismiss is not False
    config.say_allow_dismiss = phone_allow_dismiss

    # Auto-forward does not consult say_allow_dismiss in the SDK. Guard it too.
    _phone_original_afm_callback = config.afm_callback
    def phone_afm_allow():
        if story_chat_active and (not phone_is_open or phone_view != "chat" or phone_selected_thread != phone_active_thread):
            return False
        if story_chat_active and _preferences.afm_enable and renpy.get_game_runtime() < phone_read_ready_at:
            return False
        return _phone_original_afm_callback() if callable(_phone_original_afm_callback) else _phone_original_afm_callback is not False
    config.afm_callback = phone_afm_allow

label phone_ui_preview:
    if not config.developer:
        return
    $ story_active = True
    $ story_chat(True, title="축제 준비팀")
    $ phone_set_view("lock")
    system_note "휴대폰 UI 미리보기입니다. 본편의 사건·호감도·엔딩 기록은 바꾸지 않습니다."
    sia "다들 준비됐어? 오늘도 같이 잘해보자!"
    menu:
        "좋아. 같이 해보자!":
            mc "좋아. 같이 해보자!"
        "일단 일정부터 확인할까?":
            mc "일단 일정부터 확인할까?"
        "메시지는 확인했어.":
            mc "메시지는 확인했어."
    $ story_chat(False)
    $ story_active = False
    return
