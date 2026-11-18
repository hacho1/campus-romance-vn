# S01-S06 and secret text-first support; authored staging stays in CONTI.
define sia_staff = Character("직원", callback=story_speaking("narrator"))
define sia_classmate = Character("동기", callback=story_speaking("narrator"))
define sia_announcer = Character("안내 음성", callback=story_speaking("narrator"))
define sia_team_a = Character("팀원 A", callback=story_speaking("sia_team_a"))
define sia_team_b = Character("팀원 B", callback=story_speaking("sia_team_b"))
define sia_host = Character("진행자", callback=story_speaking("narrator"))
define sia_professor = Character("교수", callback=story_speaking("narrator"))
define sia_audience = Character("관객", callback=story_speaking("narrator"))

init -3 python:
    # Sender identities for the authored course-project chat. Metadata only:
    # no new standing or portrait assets are created for these speakers.
    STORY_CAST.update({
        "sia_team_a": {"name":"팀원 A", "color":"#73909b", "folder":"standings"},
        "sia_team_b": {"name":"팀원 B", "color":"#8a819c", "folder":"standings"},
    })

    def sia_begin_episode(code, title):
        if not getattr(store, "sia_s02_cat_name", None) and code not in ("S01", "S02"):
            # Direct chapter entry has no toy-name choice. Use a neutral noun,
            # without inventing a selected answer or awarding any points.
            store.sia_s02_cat_name = "고양이 인형"
        number = 200 + int(str(code)[1:])
        story_begin_chapter(number, title)
        store.chapter = "시아 {} · {}".format(code, title)
        store.selected_route = "sia"
        store.route_name = ROUTES["sia"]["title"]
        store.story_stage_visible = False
        store.phone_is_open = False
        event_flags.add("sia_route_entered")
        phone_perspective_set("mc")
        secret_note_unlock("sia", 1)

    def sia_draft_scene(description):
        # These are existing background stand-ins, not newly produced arcade or
        # photo-booth illustrations. The authored location remains in the UI.
        text = str(description or "캠퍼스")
        if not story_chat_active:
            store.phone_is_open = False
        light = "night" if any(word in text for word in ("밤", "야간")) else (
            "evening" if any(word in text for word in ("저녁", "노을")) else "day")
        if any(word in text for word in ("게임센터", "리듬 게임", "인형 뽑기")):
            story_scene(REFRESH_BACKGROUND_IDS["gamebooth"], light=light, location=text, standing=False)
        elif "포토부스" in text:
            story_scene("cafe", light=light, location=text, standing=False)
        elif "시아의 집" in text and "거실" in text:
            # Available bright interior until a dedicated summer living room is supplied.
            story_scene("cafe", light=light, location=text, standing=False)
        elif "시아의 방" in text:
            story_scene("room", light="night", location=text, standing=False)
        elif "분식집" in text:
            story_scene("cafe", light=light, location=text, standing=False)
        else:
            story_draft_scene(text)

    def sia_complete_episode(code):
        label = "sia_" + str(code).lower()
        story_flag(label + "_complete", True)
        persistent.chapter_completions.add(label)
        persistent.choice_memories.update(choice_log)
        if code == "S02":
            # A completed private date opens NOTE02; NOTE03 needs a happy ending.
            secret_note_unlock("sia", 2)
        renpy.save_persistent()

    def sia_secret_allowed():
        return "sia_happy" in persistent.endings

    def sia_begin_secret():
        if not getattr(store, "sia_s02_cat_name", None):
            store.sia_s02_cat_name = "고양이 인형"
        story_begin_chapter(299, "위에서 내려다보지 마!")
        store.chapter = "시아 시크릿 · 위에서 내려다보지 마!"
        store.selected_route = "sia"
        store.route_name = ROUTES["sia"]["title"]
        store.story_stage_visible = False
        store.phone_is_open = False
        phone_perspective_set("mc")

    def sia_secret_cg(active=True):
        if not active:
            cg_end(transition=0.3, restore=False)
            store.story_stage_visible = False
            return True
        if not sia_secret_allowed():
            return False
        # View during the first after-story without claiming its completion.
        return cg_start("ending/sia_secret", transition=0.35, story_ending=True)

    def sia_record_ending(kind):
        if kind not in ("happy", "bad", "secret"):
            raise ValueError("알 수 없는 시아 엔딩: " + str(kind))
        if kind == "secret" and not sia_secret_allowed():
            return False
        eid = "sia_" + kind
        story_flag("sia_route_complete", True)
        if kind == "secret":
            story_flag("sia_secret_after_complete", True)
            persistent.chapter_completions.add("sia_secret")
        else:
            sia_complete_episode("S06")
            story_flag("sia_" + kind + "_end_complete", True)
            if kind == "happy":
                story_flag("sia_secret_after_unlockable", True)
        persistent.choice_memories.update(choice_log)
        if not unlock_ending(eid):
            return False
        cg_unlock("ending/" + eid)
        cg_end(transition=0, restore=False)
        story_chat(False)
        phone_perspective_set("mc")
        store.story_active = False
        store.story_stage_visible = False
        renpy.save_persistent()
        return True

label sia_route_preview_end:
    $ story_chat(False)
    $ phone_perspective_set("mc")
    $ story_stage_visible = False
    narrator "시아의 이야기는 S02까지 준비되어 있습니다. 다음 이야기는 이후 업데이트에서 이어집니다. 현재 기록은 저장할 수 있습니다."
    # Retain the old label and line for 0.6 saves made at this exact statement.
    # The former completion menu also offers an explicit continuation action.
    jump sia_s03

label sia_ending_happy_complete:
    $ sia_record_ending("happy")
    call ending_result_dialogue("sia_happy")
    if _in_replay:
        return
    call screen endings
    return

label sia_ending_bad_complete:
    $ sia_record_ending("bad")
    call ending_result_dialogue("sia_bad")
    if _in_replay:
        return
    call screen endings
    return

label sia_secret_complete:
    $ sia_record_ending("secret")
    if _in_replay:
        return
    call screen endings
    return
