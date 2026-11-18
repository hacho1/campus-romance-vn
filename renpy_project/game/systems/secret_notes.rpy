default persistent.secret_note_notifications = True
default persistent.note03_happy_gate_schema = 0

init -14 python:
    SECRET_NOTE_DATA = read_data("secret_notes")
    SECRET_NOTE_LABELS = ("몰랐던 모습", "숨겨둔 마음", "연인에게만 보여줄 비밀")
    SECRET_ENDING_KINDS = ("happy", "bad", "secret")
    SECRET_NOTE_HINTS = (
        "아직 발견하지 못한 기록입니다.\n이 인물의 첫 개인 이벤트를 마치면 열립니다.",
        "조금 더 가까워지면 알 수 있을지도 모릅니다.\n이 인물의 핵심 개인 이벤트를 마치면 열립니다.",
        "이 인물의 해피 엔딩을 완료하면 열립니다.",
    )
    SECRET_INTRO_FLAGS = {
        "roman": ("roman_library_visit", "roman_question_event"),
        "sia": ("sia_concept_event", "sia_webtoon_revision"),
        "darim": ("darim_game_event", "darim_schedule_event"),
        "omu": ("omu_photo_event", "omu_campus_photo_event"),
        "lumi": ("lumi_design_event", "rumi_design_event", "lumi_model_event", "rumi_model_event"),
    }

    def secret_note_hero(hero):
        return "lumi" if hero in ("rumi", "harin") else hero

    def secret_note_key(hero, number):
        return "{}.note{:02d}".format(secret_note_hero(hero), number)

    def secret_note_hint(number):
        return SECRET_NOTE_HINTS[number - 1]

    def secret_note_raw_ending_kinds(hero):
        hero = secret_note_hero(hero)
        if hero not in SECRET_NOTE_DATA:
            return ()
        entries = SECRET_NOTE_DATA[hero]["note03"]
        return tuple(kind for kind in SECRET_ENDING_KINDS
                     if not entries[kind].get("pending")
                     and ENDINGS.get(hero + "_" + kind, {}).get("implemented")
                     and hero + "_" + kind in persistent.endings)

    def secret_note_gate_migrate():
        if persistent.note03_happy_gate_schema >= 1:
            return
        # Admission is union-only: retain any NOTE03 already accessible before
        # this update. New runs open NOTE03 through the happy ending only.
        for hero in HEROINE_ORDER:
            if secret_note_raw_ending_kinds(hero):
                persistent.profile_secrets.add(hero + ".note03_legacy")
        persistent.note03_happy_gate_schema = 1
        renpy.save_persistent()

    def secret_ending_kinds(hero):
        hero = secret_note_hero(hero)
        gate = (hero + "_happy" in persistent.endings
            or hero + ".note03_legacy" in persistent.profile_secrets
            or (persistent.note03_happy_gate_schema < 1 and bool(secret_note_raw_ending_kinds(hero))))
        return secret_note_raw_ending_kinds(hero) if gate else ()

    def secret_note_ready(hero, number):
        if number == 3:
            return bool(secret_ending_kinds(hero))
        return (number in (1, 2) and secret_note_hero(hero) in SECRET_NOTE_DATA
                and secret_note_key(hero, number) in persistent.profile_secrets)

    def secret_note_content(hero, number, kind=None):
        if not secret_note_ready(hero, number):
            return None
        hero = secret_note_hero(hero)
        if number == 3:
            if kind not in secret_ending_kinds(hero):
                return None
            return SECRET_NOTE_DATA[hero]["note03"][kind]
        return SECRET_NOTE_DATA[hero]["note{:02d}".format(number)]

    def secret_note_heading(hero):
        if secret_note_ready(hero, 3):
            return SECRET_NOTE_DATA[secret_note_hero(hero)]["note03"]["title"]
        return None

    def secret_note_view_ending_kinds(hero):
        if not campus_test_collections_preview():
            return secret_ending_kinds(hero)
        entries = SECRET_NOTE_DATA.get(secret_note_hero(hero), {}).get("note03", {})
        return tuple(kind for kind in SECRET_ENDING_KINDS
                     if entries.get(kind, {}).get("text"))

    def secret_note_view_ready(hero, number):
        if not campus_test_collections_preview():
            return secret_note_ready(hero, number)
        if number == 3:
            return bool(secret_note_view_ending_kinds(hero))
        if number not in (1, 2):
            return False
        return bool(SECRET_NOTE_DATA.get(secret_note_hero(hero), {})
                    .get("note{:02d}".format(number), {}).get("text"))

    def secret_note_view_content(hero, number, kind=None):
        if not campus_test_collections_preview():
            return secret_note_content(hero, number, kind)
        if not secret_note_view_ready(hero, number):
            return None
        data = SECRET_NOTE_DATA[secret_note_hero(hero)]
        if number == 3:
            return data["note03"].get(kind) if kind in secret_note_view_ending_kinds(hero) else None
        return data["note{:02d}".format(number)]

    def secret_note_view_heading(hero):
        if not campus_test_collections_preview():
            return secret_note_heading(hero)
        if secret_note_view_ready(hero, 3):
            return SECRET_NOTE_DATA[secret_note_hero(hero)]["note03"]["title"]
        return None

    def secret_note_show_notice(message, detail=None):
        if persistent.secret_note_notifications:
            renpy.show_screen("secret_note_unlock_toast", message=message, detail=detail, _transient=True)

    def secret_note_unlock(hero, number, notify=True):
        hero = secret_note_hero(hero)
        if hero not in SECRET_NOTE_DATA or number not in (1, 2) or secret_note_ready(hero, number):
            return False
        persistent.profile_secrets.add(secret_note_key(hero, number))
        renpy.save_persistent()
        if notify:
            secret_note_show_notice("새로운 비밀 메모를 발견했습니다.",
                                    HEROINES[hero]["name"] + " · " + SECRET_NOTE_LABELS[number - 1])
        return True

    def secret_note_ending_notice(ending_id):
        ending = ENDINGS[ending_id]
        hero = secret_note_hero(ending["heroine"])
        if ending["kind"] in secret_ending_kinds(hero):
            secret_note_show_notice(HEROINES[hero]["name"] + "의 새로운 엔딩 기록이 추가되었습니다.")

    def secret_note_import_completed():
        secret_note_gate_migrate()
        # No hidden trust threshold: official personal events/route completion
        # unlock notes, independently of either heart gauge. Previous unlocks
        # and discovery records are preserved by the union-only merge below.
        memories = persistent.choice_memories
        chapters = persistent.chapter_completions
        added = set()
        for hero, flags in SECRET_INTRO_FLAGS.items():
            aliases = (hero, "rumi", "harin") if hero == "lumi" else (hero,)
            event_done = any(getattr(store, flag, False) or flag in event_flags for flag in flags)
            legacy_done = ch01_done and any("walk_" + key in event_flags for key in aliases)
            ch02_done = any("ch02_sc06_" + key + "_complete" in choice_log for key in aliases)
            # The CH03 developer preview calls a subscene directly and records
            # the special moment without the actual chapter's partner choice.
            ch03_selected = any("ch03_sc06_partner_" + key in choice_log for key in aliases)
            ch03_done = ch03_selected and any(
                special_moment.get(key) or getattr(store, key + "_special_moment", False) for key in aliases)
            remembered_ch01 = "ch01" in chapters and any(
                "c4_" + key in memories or any("ch01_sc07_" + key + "_" + option in memories for option in "abc")
                for key in aliases)
            remembered_ch02 = any("ch02_sc06_" + key + "_complete" in memories for key in aliases)
            remembered_ch03 = "ch03" in chapters and any(
                "ch03_sc06_" + key + "_" + option in memories for key in aliases for option in "abc")
            remembered_intro = remembered_ch01 or remembered_ch02 or remembered_ch03
            if event_done or legacy_done or ch02_done or ch03_done or remembered_intro:
                added.add(secret_note_key(hero, 1))
            if (any(ch04_personal_promise.get(key) for key in aliases)
                    or ("ch04" in chapters and any("ch04_sc06_" + key + "_" + option in memories
                                                   for key in aliases for option in "abc"))):
                added.add(secret_note_key(hero, 2))
        if added - persistent.profile_secrets:
            persistent.profile_secrets.update(added)
            renpy.save_persistent()

    def secret_note_merge(old, new, current):
        return set(old or ()) | set(new or ())

    def secret_note_resume_import():
        # The load label may run before Ren'Py replays setup for the saved line.
        if renpy.session.pop("secret_note_import_on_interact", False):
            secret_note_import_completed()

    renpy.register_persistent("profile_secrets", secret_note_merge)
    config.start_callbacks.append(secret_note_gate_migrate)
    config.start_interact_callbacks.append(secret_note_resume_import)
