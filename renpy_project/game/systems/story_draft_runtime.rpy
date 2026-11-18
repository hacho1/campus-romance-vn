# CH06/CH07 and Roman R01–R06 text-first production support.
# New artwork/standing directions stay in SOURCE/CONTI comments and docs.
# Existing scores, chapter labels, save directory and persistent sets are retained.
default chapter06_complete = False
default chapter07_complete = False
default common_route_complete = False
default selected_route = None
default route_locked = False
default ch07_route_candidate = None
default ch06_booth_operation_complete = False
default ch06_roman_festival_event = False
default ch06_sia_festival_event = False
default ch06_darim_festival_event = False
default ch06_omu_festival_event = False
default ch06_harin_festival_event = False
default ch06_special_memory = None
default ch06_joint_response_complete = False
default ch06_final_reflection = None
default ch06_festival_operation_finished = False
default roman_route_unlocked = False
default sia_route_unlocked = False
default darim_route_unlocked = False
default omu_route_unlocked = False
default harin_route_unlocked = False

init -4 python:
    # GPT-generated location backgrounds. Legacy keys/assets remain available.
    REFRESH_BACKGROUND_IDS = {
        "bookshop": "refresh_20261108/bookshop",
        "garden": "refresh_20261108/garden",
        "gamebooth": "refresh_20261108/gamebooth",
        "roman_room": "refresh_20261108/roman_room",
    }
    # The private room is already painted at night: prevent a second blue tint.
    STORY_LIGHTING_REGISTRY[REFRESH_BACKGROUND_IDS["roman_room"]] = {
        "night": "images/backgrounds/refresh_20261108/roman_room.png"
    }

    def story_draft_scene(description, cast=None, standing=False):
        """Resolve authored places; never automatically add a standing or CG."""
        text = str(description or "캠퍼스")
        light = "night" if any(word in text for word in ("밤", "어두운", "심야", "야간")) else (
            "evening" if any(word in text for word in ("저녁", "노을", "해질")) else "day")
        if "로만" in text and any(word in text for word in ("방", "책상")):
            bg = REFRESH_BACKGROUND_IDS["roman_room"]
            if "스탠드 조명" in text or ("책상" in text and light == "day"):
                light = "night"
        elif "서점" in text:
            bg = REFRESH_BACKGROUND_IDS["bookshop"]
        elif "게임 체험" in text:
            bg = REFRESH_BACKGROUND_IDS["gamebooth"]
        elif any(word in text for word in ("정원", "연못", "작은 공원")) and light == "evening":
            bg = REFRESH_BACKGROUND_IDS["garden"]
        elif "행사장" in text and any(word in text for word in ("낭독", "문학")) and not any(word in text for word in ("앞", "옆", "밖", "복도")):
            bg = "presentation"
        elif "주인공 방" in text:
            bg = "room"
        elif "도서관" in text or "문학" in text or "낭독" in text:
            bg = "library"
        elif "카페" in text or "식당" in text:
            bg = "cafe"
        elif "건축" in text:
            bg = "architecture"
        elif "애니메이션" in text or "작업실" in text:
            bg = "animation"
        elif "동아리" in text or "307" in text or "준비팀" in text:
            bg = "clubroom307"
        elif "복도" in text:
            bg = "corridor"
        elif any(word in text for word in ("부스", "전시", "축제", "행사장", "운영본부", "게임 체험")):
            bg = "booth"
        elif "강의" in text or "수업" in text:
            bg = "classroom"
        elif "노을" in text:
            bg = "sunset"
        else:
            bg = "campus"
        story_scene(bg, light=light, location=text, cast=cast, standing=standing)

    def story_draft_bgm(description):
        """Authored cue -> available track. No new music is fabricated."""
        text = str(description or "").strip().lower()
        if any(word in text for word in ("없음", "stop", "정적", "무음")):
            renpy.music.stop(channel="music", fadeout=0.25)
            return
        if text in AUDIO_TRACKS:
            track = text
        elif any(word in text for word in ("obsess", "dark", "uneasy", "불안", "집착", "낮고 느린 피아노", "희미한 피아노")):
            track = "dark"
        elif text in ("warm memories", "meta", "quiet reflection"):
            track = "meta"
        elif any(word in text for word in ("tension", "conflict", "confrontation", "긴장", "갈등")):
            track = "light_tension"
        elif any(word in text for word in ("comedy", "comic", "rival", "개그")):
            track = "comedy_light"
        elif any(word in text for word in ("ending", "end theme", "고조")):
            track = "chapter_ending_reprise"
        elif any(word in text for word in ("romantic", "sweet", "love", "romance")):
            track = "romantic_night" if "night" in text or "evening" in text else "romantic"
        elif any(word in text for word in ("workshop", "creative", "writing", "작업")):
            track = "warm_workshop"
        elif any(word in text for word in ("library", "book", "reading", "quiet", "piano")):
            track = "quiet_library"
        elif any(word in text for word in ("evening", "sunset", "night", "저녁")):
            track = "evening_warm"
        elif any(word in text for word in ("gentle", "soft", "walk")):
            track = "gentle_walk"
        elif any(word in text for word in ("memory", "memories", "emotional")):
            track = "emotional_warm"
        else:
            track = "campus_day"
        play_bgm(track)

    def roman_begin_episode(code, title):
        number = 199 if code == "SECRET" else 100 + int(str(code)[1:])
        story_begin_chapter(number, title)
        store.chapter = "로만 {} · {}".format(code, title)
        store.story_stage_visible = False
        store.route_name = ROUTES["roman"]["title"]
        event_flags.add("roman_route_entered")
        if code != "SECRET":
            secret_note_unlock("roman", 1)
            if getattr(store, "roman_r03_complete", False):
                secret_note_unlock("roman", 2)

    def roman_secret_illustration():
        # Only the supplied illustration is installed in this text-first release.
        if "roman_happy" not in persistent.endings:
            return False
        return cg_start("ending/roman_secret", transition=0.35)

    def roman_record_ending(kind):
        if kind not in ("happy", "bad", "secret"):
            raise ValueError("알 수 없는 로만 엔딩: " + str(kind))
        if kind == "secret" and "roman_happy" not in persistent.endings:
            return False
        eid = "roman_" + kind
        story_flag("roman_route_complete", True)
        if kind == "happy":
            story_flag("roman_happy_end_complete", True)
            story_flag("roman_secret_after_unlockable", True)
        elif kind == "bad":
            story_flag("roman_bad_end_complete", True)
        else:
            story_flag("roman_secret_after_complete", True)
        persistent.choice_memories.update(choice_log)
        unlock_ending(eid)
        cg_unlock("ending/" + eid)
        cg_end(transition=0, restore=False)
        story_chat(False)
        store.story_active = False
        store.story_stage_visible = False
        renpy.save_persistent()
        return True

label common_route_dispatch:
    $ story_chat(False)
    $ selected_route = story_id(selected_route)
    if selected_route == "roman":
        $ story_flag("roman_route_entered", True)
        jump route_roman
    if selected_route == "sia":
        $ story_flag("sia_route_entered", True)
        jump route_sia
    if selected_route == "omu":
        $ story_flag("omu_route_entered", True)
        jump route_omu
    if selected_route == "darim":
        $ story_flag("darim_route_entered", True)
        jump route_darim
    if selected_route == "lumi":
        $ story_flag("harin_route_entered", True)
        jump route_lumi
    $ route_name = ROUTES.get(selected_route, {}).get("title", "다음 이야기")
    narrator "[route_name]"
    narrator "이 인물의 개별 루트는 다음 업데이트에서 이어집니다. 공통 루트의 기록은 저장할 수 있습니다."
    jump chapters_demo_end
