# Supplied Harin H01-H06 and secret: source memories retain harin_* names,
# while routes, characters, score keys and ending IDs retain the stable lumi ID.
# All illustration / standing directions remain production cues in route files.
define harin_student_a = Character("학생 A", callback=story_speaking("harin_student_a"))
define harin_workshop_presenter = Character("진행자", callback=story_speaking("harin_workshop_presenter"))

default harin_h06_complete = False

init -3 python:
    STORY_CAST["harin_student_a"] = {"name":"학생 A", "color":"#728b91", "folder":"standings"}
    STORY_CAST["harin_workshop_presenter"] = {"name":"진행자", "color":"#728b91", "folder":"standings"}

    def harin_begin_episode(code, title):
        story_begin_chapter(500 + int(str(code)[1:]), title)
        store.chapter = "하린 {} · {}".format(code, title)
        store.selected_route = "lumi"
        store.route_name = ROUTES["lumi"]["title"]
        store.story_stage_visible = False
        store.story_cast = RevertableList()
        store.phone_is_open = False
        event_flags.add("harin_route_entered")
        phone_perspective_set("mc")
        secret_note_unlock("lumi", 1)

    def harin_draft_scene(description):
        text = str(description or "캠퍼스")
        if not story_chat_active:
            store.phone_is_open = False
        light = "night" if any(word in text for word in ("밤", "야간", "어두운", "스탠드 조명")) else (
            "evening" if any(word in text for word in ("저녁", "노을", "해 질")) else "day")
        if "하린의 방" in text or "하린의 집" in text:
            # Existing room background stands in for the unsupplied interior.
            story_scene("room", light=light, location=text, standing=False)
        elif any(word in text for word in ("작업실", "작업대", "하린의 작품 전시")):
            story_scene("architecture", light=light, location=text, standing=False)
        elif "발표실" in text and not any(word in text for word in ("밖", "복도")):
            story_scene("presentation", light=light, location=text, standing=False)
        else:
            story_draft_scene(text, standing=False)
        store.story_stage_visible = False
        store.story_cast = RevertableList()

    def harin_complete_episode(code):
        label = "harin_" + str(code).lower()
        story_flag(label + "_complete", True)
        persistent.chapter_completions.add(label)
        persistent.choice_memories.update(choice_log)
        if code == "H02":
            secret_note_unlock("lumi", 2)
        renpy.save_persistent()

    def harin_delete_uncertain_message():
        """H05 L2437 deletes the authored sent bubble, retaining its identity."""
        if story_chapter_number != 505:
            return False
        room = phone_threads.get("private_lumi", {})
        for message in reversed(room.get("messages", ())):
            if (message.get("actor") == "lumi"
                    and message.get("text") == "제가 어떤 모습일 때 가장 좋으신지……."):
                message["text"] = "삭제된 메시지입니다."
                return True
        return False

    def harin_secret_allowed():
        return "lumi_happy" in persistent.endings

    def harin_begin_secret():
        story_begin_chapter(599, "오늘만큼은 고양이랍니다♡")
        store.chapter = "하린 시크릿 · 오늘만큼은 고양이랍니다♡"
        store.selected_route = "lumi"
        store.route_name = ROUTES["lumi"]["title"]
        store.story_stage_visible = False
        store.story_cast = RevertableList()
        store.phone_is_open = False
        phone_perspective_set("mc")

    def harin_close_route_view():
        cg_end(transition=0, restore=False)
        story_chat(False)
        phone_perspective_set("mc")
        store.story_active = False
        store.story_stage_visible = False
        store.story_cast = RevertableList()

    def harin_record_ending(kind):
        if kind not in ("happy", "bad", "secret"):
            raise ValueError("알 수 없는 하린 엔딩: " + str(kind))
        # Both ending bodies must finish their authored flag and actual policy
        # evidence before a stable ending ID can be recorded.
        if kind == "bad" and not harin_bad_completion_allowed():
            return False
        if kind == "secret" and not harin_secret_allowed():
            return False
        if kind == "happy" and not harin_happy_completion_allowed():
            return False
        eid = "lumi_" + kind
        if kind == "secret":
            story_flag("harin_secret_after_complete", True)
            persistent.chapter_completions.add("harin_secret")
        else:
            harin_complete_episode("H06")
            story_flag("harin_" + kind + "_end_complete", True)
            if kind == "happy":
                story_flag("harin_secret_after_unlockable", True)
        story_flag("harin_route_complete", True)
        persistent.choice_memories.update(choice_log)
        if not unlock_ending(eid):
            return False
        cg_unlock("ending/" + eid)
        harin_close_route_view()
        renpy.save_persistent()
        return True

label harin_ending_happy_complete:
    if not harin_record_ending("happy"):
        jump harin_relationship_review_pending
    call ending_result_dialogue("lumi_happy")
    if _in_replay:
        return
    call screen endings
    return

label harin_ending_bad_complete:
    if not harin_record_ending("bad"):
        jump harin_relationship_review_pending
    call ending_result_dialogue("lumi_bad")
    if _in_replay:
        return
    call screen endings
    return

label harin_relationship_review_pending:
    $ story_chat(False)
    narrator "이전 선택과 마지막 대화가 아직 하나의 결말로 이어지지 않았습니다. 관계 회복을 확인할 수 없어 엔딩은 해금되지 않습니다."
    $ harin_close_route_view()
    if _in_replay:
        return
    call screen endings
    return

label harin_secret_complete:
    $ harin_record_ending("secret")
    if _in_replay:
        return
    call screen endings
    return
