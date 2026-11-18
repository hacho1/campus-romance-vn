# Explicitly enabled for this test release. Set False for a production build.
define CAMPUS_TEST_BUILD = True
default test_story_mode = False
default test_chapter_entry = None
default test_chapter_current = None
default test_chapter_started = False

init -5 python:
    import copy

    TEST_CHAPTERS = (
        ("chapter01", "CH01", "이 조합으로 축제가 가능해?", "common"),
        ("chapter02", "CH02", "우리 옆 부스가 수상하다", "common"),
        ("chapter03", "CH03", "시범 운영부터 사고라고?", "common"),
        ("chapter04", "CH04", "장난이었는데, 왜 신경 쓰이지?", "common"),
        ("chapter05", "CH05", "축제까지 앞으로 일주일", "common"),
        ("chapter06", "CH06", "드디어 축제다!", "common"),
        ("chapter07", "CH07", "우리 사이, 그 이상의 시작", "common"),
        ("roman_r01", "R01", "책갈피에 남겨둔 약속", "roman"),
        ("roman_r02", "R02", "조금씩, 가까워지는 거리", "roman"),
        ("roman_r03", "R03", "말하지 않아도 알 거라고 생각했어요", "roman"),
        ("roman_r04", "R04", "지우지 못한 문장", "roman"),
        ("roman_r05", "R05", "우리만의 마지막 페이지", "roman"),
        ("roman_r06", "R06", "말하지 못한 문장의 끝", "roman"),
        ("roman_secret", "SECRET", "선물은 저인데… 먼저 좀 풀어주세요", "roman"),
        ("sia_s01", "S01", "내 웹툰의 첫 번째 독자", "sia"),
        ("sia_s02", "S02", "너랑 있으면 이상하게 재밌어", "sia"),
        ("sia_s03", "S03", "이건 장난이 아니야", "sia"),
        ("sia_s04", "S04", "저장되지 않은 마음", "sia"),
        ("sia_s05", "S05", "마지막 컷은 아직이야", "sia"),
        ("sia_s06", "S06", "장난 아니거든?", "sia"),
        ("sia_secret", "SECRET", "위에서 내려다보지 마!", "sia"),
        ("darim_d01", "D01", "선배도 쉬는 날이 있나요?", "darim"),
        ("darim_d02", "D02", "가끔은 기대도 괜찮아요", "darim"),
        ("darim_d03", "D03", "오늘은 제가 먼저 말할게요", "darim"),
        ("darim_d04", "D04", "걱정이라는 이름으로", "darim"),
        ("darim_d05", "D05", "제가 선택할 수 있게 해주세요", "darim"),
        ("darim_d06", "D06", "당신의 손을 잡는 이유", "darim"),
        ("darim_secret", "SECRET", "이번에는 제가 놀릴게요", "darim"),
        ("omu_o01", "O01", "사진 찍으러 갈래?", "omu"),
        ("omu_o02", "O02", "사진에는 안 찍히는 것", "omu"),
        ("omu_o03", "O03", "이번엔 네 옆에 있을게", "omu"),
        ("omu_o04", "O04", "흔들린 초점", "omu"),
        ("omu_o05", "O05", "남기고 싶은 순간", "omu"),
        ("omu_o06", "O06", "셔터를 누르지 않은 날", "omu"),
        ("omu_secret", "SECRET", "오늘 하루만 메이드", "omu"),
        ("harin_h01", "H01", "설계도에 없는 하루", "lumi"),
        ("harin_h02", "H02", "완벽하지 않아도 괜찮아요", "lumi"),
        ("harin_h03", "H03", "당신에게 보여주고 싶은 나", "lumi"),
        ("harin_h04", "H04", "내가 좋아했던 모습", "lumi"),
        ("harin_h05", "H05", "당신이 원하는 사람이 아니라", "lumi"),
        ("harin_h06", "H06", "우리가 함께 그린 미래", "lumi"),
        ("harin_secret", "SECRET", "오늘만큼은 고양이랍니다♡", "lumi"),
    )
    TEST_CHAPTER_LABELS = frozenset(entry[0] for entry in TEST_CHAPTERS)

    def campus_test_collections_preview():
        # Read-only collection previews. Turning the test build off restores
        # earned locks; no persistent collection or ending is fabricated.
        return bool(getattr(store, "CAMPUS_TEST_BUILD", False))

    def test_chapter_code(label):
        return next((entry[1] for entry in TEST_CHAPTERS if entry[0] == label), "테스트")

    def test_chapter_scope(label, name, partner):
        if label not in TEST_CHAPTER_LABELS:
            raise ValueError("테스트할 수 없는 챕터입니다.")
        partner = story_id(partner)
        if partner not in HEROINE_ORDER:
            partner = HEROINE_ORDER[0]
        # A separate Persistent instance is scoped into the replay store only.
        # Never replace/reset renpy.game.persistent or the player's collections.
        snapshot = renpy.persistent.Persistent()
        for key, value in persistent.__dict__.items():
            if not key.startswith("_"):
                setattr(snapshot, key, copy.deepcopy(value))
        if label == "roman_secret":
            snapshot.endings = set(snapshot.endings or ()) | {"roman_happy"}
        elif label == "sia_secret":
            snapshot.endings = set(snapshot.endings or ()) | {"sia_happy"}
        elif label == "omu_secret":
            snapshot.endings = set(snapshot.endings or ()) | {"omu_happy"}
        elif label == "darim_secret":
            snapshot.endings = set(snapshot.endings or ()) | {"darim_happy"}
        if label == "harin_secret":
            snapshot.endings = set(snapshot.endings or ()) | {"lumi_happy"}
        scope = {
            "test_story_mode": True,
            "test_chapter_entry": label,
            "test_chapter_current": label,
            "test_chapter_started": False,
            "persistent": snapshot,
            "player_name": clean_name(name),
            "first_task_partner": partner,
            "ch02_partner": partner,
            "ch03_partner": partner,
            "ch04_partner": partner,
            "ch06_festival_partner": partner,
            "selected_route": "roman" if label.startswith("roman_") else "sia" if label.startswith("sia_") else "darim" if label.startswith("darim_") else "omu" if label.startswith("omu_") else "lumi" if label.startswith("harin_") else None,
        }
        return scope

    def test_chapter_launch(label, name, partner):
        if not CAMPUS_TEST_BUILD or label not in TEST_CHAPTER_LABELS:
            return
        scope = test_chapter_scope(label, name, partner)
        previous_no_seen = config.no_replay_seen
        try:
            config.no_replay_seen = True
            # Official replay resets/defaults stores, applies scope, then
            # restores the original StoreBackup in its own finally block.
            renpy.call_replay(label, scope)
        finally:
            config.no_replay_seen = previous_no_seen

    def test_chapter_can_continue(entry, label):
        """Follow the authored story within this one isolated replay store."""
        initial = next((row for row in TEST_CHAPTERS if row[0] == entry), None)
        target = next((row for row in TEST_CHAPTERS if row[0] == label), None)
        if not initial or not target:
            return False
        if entry == label:
            return True
        # After-stories remain explicit entries; do not auto-open a secret after
        # a happy ending or continue into a different character's story.
        if initial[1] == "SECRET" or target[1] == "SECRET":
            return False
        if initial[3] == target[3]:
            return True
        # Common chapters already dispatch to the heroine chosen in CH07.
        return (initial[3] == "common"
                and target[3] == story_id(getattr(store, "selected_route", None)))

    def test_scene_boundaries(name, abnormal):
        if (not getattr(store, "test_story_mode", False)
                or not getattr(store, "_in_replay", False)
                or not getattr(store, "test_chapter_entry", None)):
            return
        # An unimplemented route has no next episode to read. Return to the
        # test menu instead of opening the normal play completion screen.
        if name == "chapters_demo_end" and getattr(store, "test_chapter_started", False):
            renpy.end_replay()
        if name not in TEST_CHAPTER_LABELS:
            return
        if name == test_chapter_entry:
            store.test_chapter_started = True
            store.test_chapter_current = name
        elif getattr(store, "test_chapter_started", False):
            if test_chapter_can_continue(test_chapter_entry, name):
                # Do not launch another replay here: its fresh defaults would
                # lose the choices, hearts and messages from the previous part.
                store.test_chapter_current = name
            else:
                renpy.end_replay()

    config.label_callbacks.append(test_scene_boundaries)
    config.overlay_screens.append("test_chapter_overlay")
