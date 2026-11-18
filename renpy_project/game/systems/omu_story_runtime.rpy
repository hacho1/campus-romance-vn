# Supplied Omu manuscripts: text-first, with no standing sprites.
define omu_club_manager = Character("동아리 담당", callback=story_speaking("omu_club_manager"))
define omu_exhibition_manager = Character("전시 담당자", callback=story_speaking("omu_exhibition_manager"))
define omu_phone_voice = Character("전화 속 목소리", callback=story_speaking("narrator"))

init -3 python:
    # Phone sender metadata only; this role has no new portrait or standing.
    STORY_CAST["omu_club_manager"] = {"name":"동아리 담당", "color":"#728b91", "folder":"standings"}
    STORY_CAST["omu_exhibition_manager"] = {"name":"전시 담당자", "color":"#728b91", "folder":"standings"}

    def omu_begin_episode(code, title):
        story_begin_chapter(300 + int(str(code)[1:]), title)
        store.chapter = "오므 {} · {}".format(code, title)
        store.selected_route = "omu"
        store.route_name = ROUTES["omu"]["title"]
        store.story_stage_visible = False
        store.story_cast = RevertableList()
        store.phone_is_open = False
        event_flags.add("omu_route_entered")
        phone_perspective_set("mc")
        secret_note_unlock("omu", 1)

    def omu_draft_scene(description):
        text = str(description or "캠퍼스")
        if not story_chat_active:
            store.phone_is_open = False
        light = "night" if any(word in text for word in ("밤", "야간", "어두운")) else (
            "evening" if any(word in text for word in ("저녁", "노을", "해질")) else "day")
        if "오므의 방" in text:
            story_scene("room", light=light, location=text, standing=False)
        elif any(word in text for word in ("영화관", "상영관", "오므의 집", "현관")):
            # Existing interior stand-ins; dedicated artwork remains CONTI.
            story_scene("cafe", light=light, location=text, standing=False)
        elif "사진 동아리" in text:
            story_scene("clubroom307", light=light, location=text, standing=False)
        elif any(word in text for word in ("병원", "장례")):
            story_scene("corridor", light=light, location=text, standing=False)
        else:
            story_draft_scene(text, standing=False)
        store.story_stage_visible = False
        store.story_cast = RevertableList()

    def omu_complete_episode(code):
        label = "omu_" + str(code).lower()
        story_flag(label + "_complete", True)
        persistent.chapter_completions.add(label)
        persistent.choice_memories.update(choice_log)
        if code == "O02":
            secret_note_unlock("omu", 2)
        renpy.save_persistent()

    def omu_secret_allowed():
        return "omu_happy" in persistent.endings

    def omu_begin_secret():
        story_begin_chapter(399, "오늘 하루만 메이드")
        store.chapter = "오므 시크릿 · 오늘 하루만 메이드"
        store.selected_route = "omu"
        store.route_name = ROUTES["omu"]["title"]
        store.story_stage_visible = False
        store.story_cast = RevertableList()
        store.phone_is_open = False
        phone_perspective_set("mc")

    def omu_secret_cg(active=True):
        if not active:
            cg_end(transition=0.3, restore=False)
            store.story_stage_visible = False
            store.story_cast = RevertableList()
            return True
        if not omu_secret_allowed():
            return False
        return cg_start("ending/omu_secret", transition=0.35, story_ending=True)

    def omu_record_ending(kind):
        if kind not in ("happy", "bad", "secret"):
            raise ValueError("알 수 없는 오므 엔딩: " + str(kind))
        if kind == "secret" and not omu_secret_allowed():
            return False
        eid = "omu_" + kind
        story_flag("omu_route_complete", True)
        if kind == "secret":
            story_flag("omu_secret_after_complete", True)
            persistent.chapter_completions.add("omu_secret")
        else:
            omu_complete_episode("O06")
            story_flag("omu_" + kind + "_end_complete", True)
            if kind == "happy":
                story_flag("omu_secret_after_unlockable", True)
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

label omu_ending_happy_complete:
    $ omu_record_ending("happy")
    call ending_result_dialogue("omu_happy")
    if _in_replay:
        return
    call screen endings
    return

label omu_ending_bad_complete:
    $ omu_record_ending("bad")
    call ending_result_dialogue("omu_bad")
    if _in_replay:
        return
    call screen endings
    return

label omu_secret_complete:
    $ omu_record_ending("secret")
    if _in_replay:
        return
    call screen endings
    return
