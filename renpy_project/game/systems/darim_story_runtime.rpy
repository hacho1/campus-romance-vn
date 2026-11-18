# Supplied Darim D01-D06 and secret: the supplied secret CG is the only new art.
# Character IDs and the existing save directory are deliberately unchanged.
define darim_program_staff = Character("담당자", callback=story_speaking("darim_program_staff"))
define darim_program_presenter = Character("진행자", callback=story_speaking("darim_program_presenter"))

init -3 python:
    # Phone sender labels only. No new portraits or standing sprites are loaded.
    STORY_CAST["darim_program_staff"] = {"name":"담당자", "color":"#728b91", "folder":"standings"}
    STORY_CAST["darim_program_presenter"] = {"name":"진행자", "color":"#728b91", "folder":"standings"}

    def darim_begin_episode(code, title):
        story_begin_chapter(400 + int(str(code)[1:]), title)
        store.chapter = "다림 {} · {}".format(code, title)
        store.selected_route = "darim"
        store.route_name = ROUTES["darim"]["title"]
        store.story_stage_visible = False
        store.story_cast = RevertableList()
        store.phone_is_open = False
        event_flags.add("darim_route_entered")
        phone_perspective_set("mc")
        secret_note_unlock("darim", 1)

    def darim_draft_scene(description):
        text = str(description or "캠퍼스")
        if not story_chat_active:
            store.phone_is_open = False
        light = "night" if any(word in text for word in ("밤", "야간", "어두운")) else (
            "evening" if any(word in text for word in ("저녁", "노을", "해질")) else "day")
        if "다림의 방" in text:
            # Existing room stand-in; dedicated art is not part of this import.
            story_scene("room", light=light, location=text, standing=False)
        elif "다림의 집" in text and "집 앞" not in text:
            # Existing interior until dedicated kitchen/dining art is supplied.
            if story_chapter_number == 499 and str(phone_clock)[:2].isdigit():
                if int(str(phone_clock)[:2]) >= 19:
                    light = "night"
            story_scene("cafe", light=light, location=text, standing=False)
        elif "게임 카페" in text:
            story_scene(REFRESH_BACKGROUND_IDS["gamebooth"], light=light, location=text, standing=False)
        elif any(word in text for word in ("발표장", "발표실", "학술")) and not "앞" in text:
            story_scene("presentation", light=light, location=text, standing=False)
        else:
            story_draft_scene(text, standing=False)
        store.story_stage_visible = False
        store.story_cast = RevertableList()

    def darim_complete_episode(code):
        label = "darim_" + str(code).lower()
        story_flag(label + "_complete", True)
        persistent.chapter_completions.add(label)
        persistent.choice_memories.update(choice_log)
        if code == "D02":
            secret_note_unlock("darim", 2)
        renpy.save_persistent()

    def darim_delete_invitation_message():
        """D03's authored deletion edits one sent bubble, retaining key/time.

        Revertable message dictionaries make both deletion and rollback part of
        the current save. Re-entering this statement cannot add another message.
        """
        if story_chapter_number != 403:
            return False
        room = phone_threads.get("private_darim", {})
        for message in reversed(room.get("messages", ())):
            if (message.get("actor") == "darim"
                    and message.get("text") == "그럼 이번에는 제가 데이트……."):
                message["text"] = "삭제된 메시지입니다."
                return True
        return False

    def darim_secret_allowed():
        return "darim_happy" in persistent.endings

    def darim_begin_secret():
        story_begin_chapter(499, "이번에는 제가 놀릴게요")
        store.chapter = "다림 시크릿 · 이번에는 제가 놀릴게요"
        store.selected_route = "darim"
        store.route_name = ROUTES["darim"]["title"]
        store.story_stage_visible = False
        store.story_cast = RevertableList()
        store.phone_is_open = False
        phone_perspective_set("mc")

    def darim_secret_cg(active=True):
        if not active:
            cg_end(transition=0.3, restore=False)
            store.story_stage_visible = False
            store.story_cast = RevertableList()
            return True
        if not darim_secret_allowed():
            return False
        return cg_start("ending/darim_secret", transition=0.35, story_ending=True)

    def darim_record_ending(kind):
        if kind not in ("happy", "bad", "secret"):
            raise ValueError("알 수 없는 다림 엔딩: " + str(kind))
        if kind == "secret" and not darim_secret_allowed():
            return False
        eid = "darim_" + kind
        if kind == "secret":
            story_flag("darim_secret_after_complete", True)
            persistent.chapter_completions.add("darim_secret")
        else:
            darim_complete_episode("D06")
            story_flag("darim_" + kind + "_end_complete", True)
        story_flag("darim_route_complete", True)
        if kind == "happy":
            story_flag("darim_secret_after_unlockable", True)
        persistent.choice_memories.update(choice_log)
        if not unlock_ending(eid):
            return False
        cg_unlock("ending/" + eid)
        cg_end(transition=0, restore=False)
        story_chat(False)
        phone_perspective_set("mc")
        store.story_active = False
        store.story_stage_visible = False
        store.story_cast = RevertableList()
        renpy.save_persistent()
        return True

label darim_ending_happy_complete:
    $ darim_record_ending("happy")
    call ending_result_dialogue("darim_happy")
    if _in_replay:
        return
    call screen endings
    return

label darim_ending_bad_complete:
    $ darim_record_ending("bad")
    call ending_result_dialogue("darim_bad")
    if _in_replay:
        return
    call screen endings
    return

label darim_secret_complete:
    $ darim_record_ending("secret")
    if _in_replay:
        return
    call screen endings
    return
