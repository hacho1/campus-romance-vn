# Native Ren'Py 8.5.3 coverage for the official CH01 -> CH02 -> CH03 route.
# Build exclusion is inherited from options.rpy's game/tests/** rule.
# Run with a dedicated CAMPUS_SAVE_DIR; never use a player's save directory.

init python:
    if not renpy.has_image(("roman", "smile"), exact=True):
        renpy.image("roman smile", Null(32, 32))

init python in chapter_test:
    import os

    HEROES = ("roman", "sia", "darim", "omu", "lumi")
    ALL_CAST = HEROES + ("ski", "hyeophap", "hess", "bambam")
    MOTIVATIONS = ("새로운 사람도 좀 만나보고 싶고.", "대학생활에 추억 하나쯤은 있어야지.", "재미있는 일이 생길지도 모르잖아.")
    FIRST_REPLIES = ("그럼 감상료는 얼마 주는데요?", "원래 다들 이런 분위기예요?", "그래서 모임 장소는 어디예요?")
    BOOK_REPLIES = ("책 좋아하시나 봐요?", "많이 놀랐죠? 괜찮아요?", "그 책 재미있어요?")
    FIRST_PARTNERS = (
        "로만: 전시 문구부터 같이 찾아볼까요?", "시아: 웹툰 콘티 만드는 거 도와드릴게요.",
        "다림: 일정표 정리부터 해요.", "오므: 사진 찍으러 같이 가도 돼요?", "하린: 부스 배치도 만드는 거 같이 볼까요?",
    )
    FIRST_PRIVATE = {
        "roman": ("재미있게 웃었던 날.", "조용하고 편안했던 날.", "평소와 달랐던 날."),
        "sia": ("웃긴 장면을 먼저 넣어요.", "참여 방법을 쉽게 알려줘요.", "둘 다 할 수 있지 않아요?"),
        "darim": ("공격적으로 플레이하는 편이에요.", "안전하게 운영하는 편이에요.", "그때그때 달라요."),
        "omu": ("사진에는 찍는 사람의 취향이 보이는 것 같아요.", "전 그냥 잘 나온 사진이 좋던데요.", "저도 사진 좀 배워볼까요?"),
        "lumi": ("동선을 조금 더 단순하게 만들어요.", "사진 공간을 더 넓히면 좋겠어요.", "앉아서 쉴 공간도 있으면 좋겠는데요."),
    }
    RIVAL_REPLIES = ("그 자신감이면 부스도 혼자 만들겠네요.", "서로 열심히 준비해 봐요.", "어떤 부스를 준비하고 있어요?")
    DAY_REPLIES = ("정신없는 하루", "평범하고 편안한 하루", "무언가 기대되는 하루")
    SECOND_PARTNERS = (
        "로만과 질문 카드를 만든다.", "시아와 안내 만화를 수정한다.", "다림과 운영 계획을 정리한다.",
        "오므와 전시용 사진을 찍는다.", "하린과 부스 모형을 만든다.",
    )
    SECOND_PRIVATE = {
        "roman": ("생각보다 재미있는 사람들을 만난 날.", "조금씩 새로운 걸 배우는 날.", "아직 어떻게 끝날지 모르는 날."),
        "sia": ("강아지는 남기고 내용을 단순화해요.", "사람이 직접 설명하는 방식으로 바꿔요.", "설명은 간단하게, 마지막에 개그를 넣어요."),
        "darim": ("제가 안내문 점검을 맡을게요.", "작업별 마감일을 같이 확인해요.", "다른 팀원들 의견도 먼저 들어보죠."),
        "omu": ("같이 치워요.", "관리하시는 분께 알려드려요.", "저런 사람들은 왜 그러는 걸까요?"),
        "lumi": ("관람객이 움직이기 편한 게 우선이죠.", "전시물이 잘 보이는 것도 중요하지 않을까요?", "잠깐 쉴 수 있는 공간은 없어요?"),
    }
    HELP_REPLIES = ("일단 같이 주워요.", "필요한 게 있는지 물어보자.", "저쪽에서 정리하는 것 같으니 우리 준비를 계속해요.")
    PITCH_REPLIES = ("팀원들의 예시 작품을 먼저 전시하겠습니다.", "참여 절차를 더 간단하게 만들겠습니다.", "방문객이 쉽게 이해할 안내물을 강화하겠습니다.")
    TRIAL_REPLIES = ("로만과 전시 안내문을 확인한다.", "하린과 방문객 동선을 확인한다.", "다림과 팀원별 역할을 확인한다.")
    POLICY_REPLIES = ("기록하지 않고 관람만 해도 되게 해요.", "공개 여부와 철회 방법을 확실히 안내해요.", "글 대신 간단한 스티커 참여도 가능하게 해요.")
    THIRD_PARTNERS = (
        "로만과 질문 카드 수정하기", "시아와 안내 만화 완성하기", "다림과 운영 자료 정리하기",
        "오므와 현장 사진 확인하기", "하린과 부스 배치 수정하기",
    )
    THIRD_PRIVATE = {
        "roman": ("저도 로만 씨랑 이야기하는 거 좋아해요.", "그럼 다음에 또 도서관에 올까요?", "그럼 질문 하나만 더 만들어볼까요?"),
        "sia": ("그림 그릴 때 시아 씨 모습이 좀 멋있었어요.", "다음 작품도 같이 고민해볼까요?", "강아지 우주 대모험은 꼭 완성해 주세요."),
        "darim": ("선배랑 있으면 편해요.", "다음에는 제가 먼저 커피 살게요.", "게임은 제가 이길 것 같은데요?"),
        "omu": ("오므 씨랑 같이 찍으러 다니니까 재미있어요.", "사진 구도 좀 더 알려 주세요.", "이 사진은 전시에 꼭 넣어요."),
        "lumi": ("당황했어요?", "다음에도 같이 작업해요.", "이번엔 제가 놀린 것 같네요."),
    }
    COOP_REPLIES = ("하린·협합과 동선을 수정한다.", "다림·밤밤·헤스와 방문객을 안내한다.", "시아·오므·로만과 안내 표지를 만든다.")
    FIRST_FLAGS = ("roman_library_visit", "sia_concept_event", "darim_game_event", "omu_photo_event", "lumi_design_event")
    SECOND_FLAGS = ("roman_question_event", "sia_webtoon_revision", "darim_schedule_event", "omu_campus_photo_event", "lumi_model_event")
    THIRD_FLAGS = ("roman_playful_event", "sia_webtoon_promise", "darim_game_rival", "omu_representative_photo", "lumi_reverse_prank")
    EVENING_MESSAGES = {
        "roman": "앗,,, 다음에 같이 읽고 싶은 책이 생겼어요. 나중에 보여드릴게요……!",
        "sia": "야 오늘 해준 말 기억한다? ㅋㅋ 다음 작품도 기대해라",
        "darim": "오늘 같이 이야기해서 좋았어요. 게임 약속도 잊지 마세요. 후후.",
        "omu": "아까 말한 사진 정리했다. 다음에 보면 보여줄게.",
        "lumi": "오늘은 조금 예상 밖이었네요. 그래도 재미있었어. 좋은 밤 보내요.",
    }
    FIRST_MESSAGES = {
        "roman": "오늘 같이 책 찾아주셔서 감사했어요.", "sia": "야ㅋㅋ 오늘 그 콘티 다시 봤는데",
        "darim": "오늘 일정표 정리 도와주셔서 감사했어요.", "omu": "야 오늘 사진 정리했는데",
        "lumi": "오늘 같이 봤던 부스 배치도 수정해 봤어요.",
    }
    # Hand-calculated relation totals, in HEROES order. These are not derived
    # from runtime effects, so accidental reward changes are observable.
    EXPECTED_AFFECTION = ((10, 20, 0, 0, 0), (0, 10, 0, 5, 0), (0, 0, 0, 5, 0), (5, 15, 0, 5, 5), (5, 5, 0, 5, 5), (10, 0, 0, 0, 0))
    EXPECTED_TRUST = ((5, 0, 5, 0, 0), (5, 0, 10, 0, 10), (5, 0, 20, 5, 0), (5, 0, 5, 0, 0), (5, 0, 5, 0, 10), (10, 0, 15, 5, 0))

    def reset_observation():
        # Engine-owned test observation survives Start/FileLoad; it is never
        # written to the game's rollback store or any player's persistent data.
        renpy._campus_chapter_observation = {"labels": [], "invalid_casts": [], "sd_events": set(), "sd_variants": set(), "invalid_sd_states": [], "cg_events": set(), "invalid_cg_states": []}

    def observe_label(name, abnormal):
        if renpy.is_in_test() and hasattr(renpy, "_campus_chapter_observation"):
            renpy._campus_chapter_observation["labels"].append(name)

    def observe_say(event, **kwargs):
        if event != "begin" or not renpy.is_in_test() or not renpy.store.story_active:
            return
        observation = getattr(renpy, "_campus_chapter_observation", None)
        if observation is None:
            return
        mode, cast = renpy.store.story_mode, list(renpy.store.story_cast)
        current = renpy.store.sd_event_current
        current_cg = renpy.store.cg_current
        if current is not None:
            if mode != "sd_event" or cast or renpy.store.story_effects or current_cg is not None:
                observation["invalid_sd_states"].append((current, mode, cast, dict(renpy.store.story_effects)))
            variant = renpy.store.sd_event_variant_id
            observation["sd_events"].add(current)
            observation["sd_variants"].add((current, variant))
        elif current_cg is not None:
            if not renpy.store.cg_is_active() or current_cg not in renpy.store.CG_REGISTRY or mode != "ld_cg" or cast or renpy.store.story_effects or renpy.store.story_stage_visible:
                observation["invalid_cg_states"].append((current_cg, mode, cast, dict(renpy.store.story_effects), renpy.store.story_stage_visible))
            observation["cg_events"].add(current_cg)
        elif mode not in ("normal", "emotion") or len(cast) != len(set(cast)) or not set(cast).issubset(renpy.store.STORY_CAST):
            observation["invalid_casts"].append((mode, cast))

    def assert_selected_flags(names, selected):
        for actor, name in zip(HEROES, names):
            assert getattr(renpy.store, name) == (actor == selected), (name, selected)
            assert (name in renpy.store.event_flags) == (actor == selected), ("event_flags", name, selected)

    def assert_exclusive_message(chapter_number, messages, selected):
        read = [text for number, actor, text in renpy.store.story_read_log if number == chapter_number]
        for actor, message in messages.items():
            assert read.count(message) == (1 if actor == selected else 0), (chapter_number, actor, selected, read.count(message))

    def assert_complete_path(path_index, first, second, third, common, help_reply, pitch_reply, private_reply):
        s = renpy.store
        letter, help_letter, pitch_letter = "abc"[common], "abc"[help_reply], "abc"[pitch_reply]
        expected = [
            "ch01_sc01_motivation_" + letter, "ch01_sc02_" + letter, "ch01_sc03_" + letter,
            "ch01_sc06_" + "abcde"[HEROES.index(first)], "ch01_sc07_" + first + "_" + letter,
            "ch02_sc03_" + letter, "ch02_sc05_" + letter, "ch02_sc06_" + second,
            "ch02_" + second + "_" + letter, "ch02_sc06_" + second + "_complete",
            "ch02_sc07_" + help_letter, "ch02_sc08_" + pitch_letter,
            "ch03_sc02_" + letter, "ch03_sc05_" + help_letter, "ch03_sc06_partner_" + third,
            "ch03_sc06_" + third + "_" + "abc"[private_reply], "ch03_sc07_" + pitch_letter,
        ]
        assert list(s.choice_log) == expected, (list(s.choice_log), expected)
        assert len([choice for choice in s.choice_log if not choice.endswith("_complete")]) == 16
        assert tuple(s.affection[key] for key in HEROES) == EXPECTED_AFFECTION[path_index]
        assert tuple(s.trust[key] for key in HEROES) == EXPECTED_TRUST[path_index]
        assert set(s.affection) == set(HEROES) and set(s.trust) == set(HEROES)
        assert s.first_task_partner == first and s.ch02_partner == second and s.ch03_partner == third
        assert s.chapter01_complete and s.chapter02_complete and s.chapter03_complete and s.ch01_done
        assert {"ch01", "ch02", "ch03"}.issubset(s.persistent.chapter_completions)
        assert set(s.choice_log).issubset(s.persistent.choice_memories)
        assert "festival_note" in s.persistent.gallery
        assert s.space_issue_discovered and s.rival_project_observed and s.visitor_withdrawal_occurred
        assert s.visitor_policy_established and s.rival_cooperation and s.trial_operation_complete
        assert s.rival_helped == (help_reply != 2)
        assert s.rival_attitude == ("cooperative", "respectful", "neutral")[help_reply]
        assert s.rival_project_known == (common == 2)
        assert s.pitch_strategy == ("sample", "simple", "guide")[pitch_reply]
        assert (s.team_preparation, s.exhibition_quality, s.promotion_quality) == (
            int(help_reply == 2) + int(pitch_reply == 1), int(pitch_reply == 0), int(pitch_reply == 2))
        assert s.trial_preparation == ("guide", "space", "staff")[common]
        assert s.visitor_policy_priority == ("optional", "privacy", "simple")[help_reply]
        assert s.visitor_policy == s.visitor_policy_priority
        assert s.cooperation_method == ("layout", "guide", "sign")[pitch_reply]
        assert s.ch03_evening_event == third
        assert dict(s.special_moment) == {key: key == third for key in HEROES}
        assert_selected_flags(FIRST_FLAGS, first)
        assert_selected_flags(SECOND_FLAGS, second)
        assert_selected_flags(tuple(key + "_special_moment" for key in HEROES), third)
        assert_selected_flags(THIRD_FLAGS, third if private_reply == 2 else None)
        assert s.rumi_design_event == s.lumi_design_event == (first == "lumi")
        assert s.rumi_model_event == s.lumi_model_event == (second == "lumi")
        assert s.roman_book_event == (common == 2)
        assert_exclusive_message(1, FIRST_MESSAGES, first)
        assert_exclusive_message(3, EVENING_MESSAGES, third)
        callbacks = ("처음 같이 책 이야기했던 때가 생각나요…….", "지난번에 같이 다듬었던 문장도 다시 읽어봤어요.", "전에 책 내용에 관해 물어봐 주신 것도 기억나요…….")
        read03 = [text for number, actor, text in s.story_read_log if number == 3]
        for message, present in zip(callbacks, (third == first == "roman", third == second == "roman", third == "roman" and common == 2)):
            assert read03.count(message) == int(present), (message, present)
        observation = renpy._campus_chapter_observation
        for chapter_number in (1, 2, 3):
            for scene_number in range(1, 10):
                label = "ch{:02d}_sc{:02d}".format(chapter_number, scene_number)
                assert observation["labels"].count(label) == 1, (label, observation["labels"])
            assert s.chapter_metrics[chapter_number]["displayed_lines"] > 100
            assert s.chapter_metrics[chapter_number]["displayed_characters"] > 1000
        for prefix, selected in (("ch01_sc07_", first), ("ch02_sc06_", second), ("ch03_sc06_", third)):
            private_labels = [label for label in observation["labels"] if label.startswith(prefix) and label[len(prefix):] in HEROES]
            assert private_labels == [prefix + selected], private_labels
        assert not observation["invalid_casts"], observation["invalid_casts"]
        assert not observation["invalid_sd_states"], observation["invalid_sd_states"]
        assert not observation["invalid_cg_states"], observation["invalid_cg_states"]
        assert observation["cg_events"].issubset(set(s.CG_REGISTRY)), observation["cg_events"]
        assert all(s.cg_seen(key) for key in observation["cg_events"])
        required_cg = {"ld_03", "ld_05", "ld_{:02d}".format(8 + HEROES.index(third))}
        assert required_cg.issubset(observation["cg_events"]), (required_cg, observation["cg_events"])
        assert observation["cg_events"].intersection({"ld_08","ld_09","ld_10","ld_11","ld_12"}) == {"ld_{:02d}".format(8 + HEROES.index(third))}
        assert not s.cg_is_active() and renpy.get_screen("ld_cg_view", layer="ld_cg") is None
        assert not observation["cg_events"].intersection({"ld_02", "ld_04", "ld_06", "ld_07"})
        assert {item for item in observation["sd_variants"] if item[0].startswith("ch01_")} == {
            ("ch01_sia_omu_argument", "01"), ("ch01_drink_incident", "01"), ("ch01_group_meeting", "01"),
        }
        required_later_cuts = {
            ("ch02_interview_flashback", "02"), ("ch02_ski_accident", "01"), ("ch02_rival_after_presentation", "02"),
            ("ch03_sia_force_quit_reaction", "01"), ("ch03_sia_force_quit_reaction", "02"), ("ch03_sia_force_quit_reaction", "03"),
            ("ch03_joint_cooperation", "01"), ("ch03_joint_cooperation", "02"), ("ch03_joint_cooperation", "03"),
        }
        if help_reply == 0:
            required_later_cuts.add(("ch02_ski_accident", "03"))
        optional_cuts = ("ch02_whiteboard_huddle", "ch02_presentation_release", "ch03_rival_booth_open", "ch03_trial_huddle", "ch03_rest_break")
        required_later_cuts.update((event, "01") for event in optional_cuts if s.sd_event_info(event, "01")["asset"])
        later_cuts = {item for item in observation["sd_variants"] if not item[0].startswith("ch01_")}
        assert later_cuts == required_later_cuts, (later_cuts, required_later_cuts)
        assert all(variant in s.SD_EVENT_REGISTRY[event_id]["variants"] for event_id, variant in observation["sd_variants"])
        assert s.sd_event_current is None
        assert renpy.get_screen("sd_event_view", layer="sd_events") is None
        assert not s.eligible_routes() and not s.persistent.endings and not s.meta_unlocked()
        assert s.story_active and s.story_chapter_number == 4 and not s.story_chat_active
        print("OFFICIAL_CHAPTER_PATH_OK", path_index, first, second, third, "16 decisions; 27 scenes;", len(observation["sd_events"]), "SD events", sorted(observation["sd_variants"]), dict(s.chapter_metrics))

    def transform_placements(transforms):
        result = []
        for transform in transforms:
            placement = renpy.get_placement(transform)
            result.append((placement.xpos,placement.ypos,placement.xanchor,placement.yanchor,
                placement.xoffset,placement.yoffset,placement.subpixel))
        return tuple(result)

    def cg_hidden_master_snapshot():
        return tuple((tag,tuple(attributes),transform_placements(transforms))
            for tag,attributes,transforms in renpy.store.cg_hidden_master)

    def visible_master_snapshot():
        return tuple((tag,tuple(renpy.get_attributes(tag,layer="master") or ()),
                transform_placements(renpy.get_at_list(tag,layer="master") or []))
            for tag in renpy.get_showing_tags(layer="master",sort=True) if renpy.store.story_id(tag) in renpy.store.STORY_CAST)

    def stage_snapshot():
        s = renpy.store
        fields = ("player_name", "first_task_partner", "ch02_partner", "ch03_partner", "ch03_evening_event",
            "chapter01_complete", "chapter02_complete", "chapter03_complete", "roman_book_event", "roman_question_event",
            "rival_attitude", "rival_helped", "rival_cooperation", "team_preparation", "exhibition_quality", "promotion_quality",
            "pitch_strategy", "trial_preparation", "visitor_policy", "visitor_policy_priority", "visitor_policy_established",
            "visitor_withdrawal_occurred", "cooperation_method", "trial_operation_complete", "lumi_reverse_prank",
            "story_mode", "story_background", "story_chapter_number", "story_stage_visible", "story_effect_serial",
            "sd_event_current", "sd_event_variant_id", "sd_event_dissolve", "sd_event_previous_mode", "sd_event_schema",
            "cg_current", "cg_previous_mode", "cg_previous_stage_visible", "cg_previous_chat_active")
        result = {name: getattr(s, name) for name in fields}
        result.update(affection=dict(s.affection), trust=dict(s.trust), special_moment=dict(s.special_moment),
            event_flags=set(s.event_flags), choice_log=list(s.choice_log), story_cast=list(s.story_cast),
            story_faces=dict(s.story_faces), story_effects=dict(s.story_effects),
            story_positions=dict(s.story_positions), story_facing=dict(s.story_facing),
            sd_event_previous_cast=list(s.sd_event_previous_cast), sd_event_previous_faces=dict(s.sd_event_previous_faces),
            sd_event_previous_positions=dict(s.sd_event_previous_positions), sd_event_previous_facing=dict(s.sd_event_previous_facing),
            sd_event_hidden_master=list(s.sd_event_hidden_master),
            cg_previous_cast=list(s.cg_previous_cast), cg_previous_faces=dict(s.cg_previous_faces),
            cg_previous_positions=dict(s.cg_previous_positions), cg_previous_facing=dict(s.cg_previous_facing),
            cg_hidden_master=cg_hidden_master_snapshot(), visible_master=visible_master_snapshot())
        return result

    def assert_saved_snapshot():
        expected = renpy._campus_saved_snapshot
        actual = stage_snapshot()
        differences = {key: (expected.get(key), actual.get(key))
            for key in set(expected) | set(actual) if expected.get(key) != actual.get(key)}
        assert not differences, ("Saved chapter state differs (expected, actual)", differences)


testsuite official_chapters:
    setup:
        python:
            import os
            assert os.environ.get("CAMPUS_SAVE_DIR"), "Set CAMPUS_SAVE_DIR to a dedicated test directory."
            assert os.path.normcase(os.path.abspath(config.savedir)) == os.path.normcase(os.path.abspath(os.environ["CAMPUS_SAVE_DIR"]))
            assert os.path.normcase(os.path.abspath(config.savedir)) != os.path.normcase(os.path.join(config.basedir, "saves"))
            config.label_callbacks.append(chapter_test.observe_label)
            config.all_character_callbacks.append(chapter_test.observe_say)
        $ _test.timeout = 180.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/chapter-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.skip_unseen = False
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        $ chapter_test.reset_observation()
        assert eval not persistent.endings and not meta_unlocked()
    teardown:
        python:
            if chapter_test.observe_label in config.label_callbacks:
                config.label_callbacks.remove(chapter_test.observe_label)
            if chapter_test.observe_say in config.all_character_callbacks:
                config.all_character_callbacks.remove(chapter_test.observe_say)
        exit

    testcase complete_official_paths:
        # Five mixed paths cover every private branch in every chapter. The
        # sixth repeats Roman across chapters and verifies all prior callbacks.
        parameter (path_index, first, second, third, common, help_reply, pitch_reply, private_reply) = [(0,"roman","sia","darim",0,1,2,2), (1,"sia","darim","omu",1,2,0,2), (2,"darim","omu","lumi",2,0,1,2), (3,"omu","lumi","roman",0,1,2,2), (4,"lumi","roman","sia",1,2,0,2), (5,"roman","roman","roman",2,0,1,1)]
        click "게임 시작"
        # A story message must be opened through its real controls before advance.
        advance until eval phone_notification_pending and phone_active_thread == "campus_notice" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until screen "choice" timeout 180
        assert eval story_chapter_number == 1 and len(choice_log) == 0
        click expression chapter_test.MOTIVATIONS[common]
        advance until screen "input" timeout 180
        $ renpy.get_widget("input", "input").update_text("", True)
        type "ChapterQA"
        click expression ("신청하기" if application_input_active else "이 이름으로 시작")
        advance until eval phone_notification_pending and phone_active_thread == "festival_application" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until screen "choice" timeout 180
        assert eval player_name == "ChapterQA" and len(choice_log) == 1
        click expression chapter_test.FIRST_REPLIES[common]
        advance until screen "choice" timeout 180
        click expression chapter_test.BOOK_REPLIES[common]
        advance until screen "choice" timeout 180
        click expression chapter_test.FIRST_PARTNERS[chapter_test.HEROES.index(first)]
        advance until screen "choice" timeout 180
        assert eval first_task_partner == first
        click expression chapter_test.FIRST_PRIVATE[first][common]
        # CH01 evening: group invite, private follow-up, then the committee notice.
        advance until eval phone_notification_pending and phone_active_thread == "campus_group" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until eval story_chat_active and phone_active_thread == "private_" + first timeout 180
        assert eval phone_is_open and not phone_notification_pending and phone_view == "chat" and phone_selected_thread == phone_active_thread
        advance until eval phone_notification_pending and phone_active_thread == "festival_committee" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        # CH02 morning reuses the rooms without reusing their read state.
        advance until eval story_chapter_number == 2 and phone_notification_pending and phone_active_thread == "campus_group" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until eval phone_notification_pending and phone_active_thread == "private_" + first timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until eval phone_notification_pending and phone_active_thread == "festival_committee" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until screen "choice" timeout 180
        assert eval chapter01_complete and ch01_done and story_chapter_number == 2 and len(choice_log) == 5
        assert eval "ch01" in persistent.chapter_completions
        $ chapter_test.assert_selected_flags(chapter_test.FIRST_FLAGS, first)
        click expression chapter_test.RIVAL_REPLIES[common]
        advance until screen "choice" timeout 180
        click expression chapter_test.DAY_REPLIES[common]
        advance until screen "choice" timeout 180
        click expression chapter_test.SECOND_PARTNERS[chapter_test.HEROES.index(second)]
        advance until screen "choice" timeout 180
        assert eval ch02_partner == second
        click expression chapter_test.SECOND_PRIVATE[second][common]
        advance until screen "choice" timeout 180
        $ chapter_test.assert_selected_flags(chapter_test.SECOND_FLAGS, second)
        click expression chapter_test.HELP_REPLIES[help_reply]
        advance until screen "choice" timeout 180
        click expression chapter_test.PITCH_REPLIES[pitch_reply]
        # CH02 evening and CH03 morning each deliver another round of messages.
        advance until eval phone_notification_pending and phone_active_thread == "private_" + second timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until eval phone_notification_pending and phone_active_thread == "festival_committee" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until eval story_chapter_number == 3 and phone_notification_pending and phone_active_thread == "campus_group" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until eval story_chat_active and phone_active_thread == "private_" + second timeout 180
        assert eval phone_is_open and not phone_notification_pending and phone_view == "chat" and phone_selected_thread == phone_active_thread
        advance until screen "choice" timeout 180
        assert eval chapter02_complete and story_chapter_number == 3 and len(choice_log) == 12
        assert eval "ch02" in persistent.chapter_completions
        screenshot f"chapter03_trial_choice_{path_index}.png"
        click expression chapter_test.TRIAL_REPLIES[common]
        advance until screen "choice" timeout 180
        assert eval visitor_withdrawal_occurred
        click expression chapter_test.POLICY_REPLIES[help_reply]
        advance until screen "choice" timeout 180
        assert eval visitor_policy_established and visitor_policy == ("optional", "privacy", "simple")[help_reply]
        click expression chapter_test.THIRD_PARTNERS[chapter_test.HEROES.index(third)]
        advance until screen "choice" timeout 180
        assert eval ch03_partner == third and cg_is_active() and cg_current == {"roman":"ld_08", "sia":"ld_09", "darim":"ld_10", "omu":"ld_11", "lumi":"ld_12"}[third]
        assert eval story_mode == "ld_cg" and story_cast == [] and story_effects == {} and not story_stage_visible
        assert eval sd_event_current is None and renpy.get_screen("ld_cg_view",layer="ld_cg") is not None
        screenshot f"chapter03_private_{third}_{path_index}.png"
        click expression chapter_test.THIRD_PRIVATE[third][private_reply]
        advance until screen "choice" timeout 180
        assert eval sum(special_moment.values()) == 1 and special_moment[third]
        click expression chapter_test.COOP_REPLIES[pitch_reply]
        advance until eval phone_notification_pending and phone_active_thread == "campus_group" timeout 180
        click id "phone_archive_button" screen ("quick_menu",)
        click "알림 열기"
        advance until eval story_chat_active and phone_active_thread == "private_" + third timeout 180
        assert eval phone_is_open and not phone_notification_pending and phone_view == "chat" and phone_selected_thread == phone_active_thread
        advance until eval story_chapter_number == 4 timeout 180
        $ chapter_test.assert_complete_path(path_index, first, second, third, common, help_reply, pitch_reply, private_reply)
        screenshot f"official_complete_{path_index}.png"
        click id "quick_profiles" screen ("quick_menu",)
        assert screen "profiles"
        click expression HEROINES[third]["name"]
        click "뒷면 보기"
        assert eval renpy.get_screen("profiles").scope["back"]
        click "돌아가기"
        assert screen "say"
        run MainMenu(confirm=False, save=False)
        assert screen "main_menu"

    testcase chapter_state_save_load:
        parameter stage_mode = ["normal", "emotion", "sd_event", "ld_cg"]
        # Native statements initialize the checkpoint before the say interaction.
        # This exercises Ren'Py's actual save freeze point, including new fields.
        if eval stage_mode == "ld_cg":
            $ renpy._campus_ld_fixture_starts = 0
        run Start("qa_story_save_" + stage_mode)
        pause until screen "say"
        if eval stage_mode == "ld_cg":
            # Freeze a second dialogue interaction so loading cannot pass by
            # replaying the native initializer and calling cg_start again.
            advance
            pause until screen "say"
        $ renpy._campus_saved_snapshot = chapter_test.stage_snapshot()
        assert eval first_task_partner == "lumi" and ch03_partner == "lumi" and ch03_evening_event == "lumi"
        assert eval len(story_cast) == (0 if stage_mode in ("sd_event", "ld_cg") else 3)
        if eval stage_mode == "sd_event":
            assert eval sd_event_current == "ch02_rival_introduction" and sd_event_variant_id == "02"
            assert eval story_mode == "sd_event" and story_effects == {} and sd_event_schema == 1
            assert eval renpy.get_screen("sd_event_view", layer="sd_events") is not None
        elif eval stage_mode == "ld_cg":
            assert eval cg_is_active() and cg_current == "ld_07" and cg_seen("ld_07")
            assert eval story_mode == "ld_cg" and not story_effects and not story_stage_visible and sd_event_current is None
            assert eval renpy.get_screen("ld_cg_view",layer="ld_cg") is not None
            assert eval "roman" not in renpy.get_showing_tags(layer="master")
            assert eval [(tag,tuple(attributes)) for tag,attributes,transforms in cg_hidden_master] == [("roman",("smile",))]
        else:
            assert eval sd_event_current is None and story_mode == stage_mode
            assert eval story_effects["sia"][0] == "shake"
        screenshot f"save_before_{stage_mode}.png"
        click "저장"
        assert screen "save"
        run FilePage("7")
        run FileSave("1", confirm=False)
        assert eval renpy.can_load("7-1")
        click "돌아가기"
        python:
            player_name = "변경됨"
            first_task_partner = "darim"
            ch02_partner = "omu"
            ch03_partner = "sia"
            ch03_evening_event = "sia"
            chapter01_complete = False
            chapter02_complete = False
            rival_attitude = "neutral"
            rival_cooperation = False
            team_preparation = 99
            exhibition_quality = 99
            promotion_quality = 99
            visitor_policy = "simple"
            visitor_policy_priority = "simple"
            cooperation_method = "sign"
            special_moment["lumi"] = False
            affection["lumi"] = 99
            trust["roman"] = 99
            choice_log.append("unsaved_change")
            event_flags.clear()
            if stage_mode == "ld_cg":
                cg_end(transition=0)
                renpy.store.cg_previous_mode = "emotion"
                renpy.store.cg_previous_cast = ["lumi"]
                renpy.store.cg_previous_faces = {"lumi":"sad"}
                renpy.store.cg_previous_positions = {"lumi":(10,10)}
                renpy.store.cg_previous_facing = {"lumi":1}
                renpy.store.cg_previous_stage_visible = False
                renpy.store.cg_previous_chat_active = True
                renpy.store.cg_hidden_master = []
            sd_event_end(transition=0)
            sd_event_dissolve = 0.91
            story_stage(mode="normal", cast=["sia"], faces={"lumi":"sad"},
                positions={"roman":(1500,800), "sia":(300,800)}, facing={"roman":1, "sia":-1})
            story_effect("jump", "sia")
            sd_event_start("ch03_joint_cooperation", "03", transition=0)
            renpy.restart_interaction()
        click "불러오기"
        assert screen "load"
        run FilePage("7")
        run FileLoad("1", confirm=False)
        pause until screen "say"
        $ chapter_test.assert_saved_snapshot()
        if eval stage_mode == "ld_cg":
            assert eval not story_stage_visible and story_active and chapter_save_schema == 2
        else:
            assert eval story_stage_visible and story_active and chapter_save_schema == 2
        assert eval len(story_cast) == (0 if stage_mode in ("sd_event", "ld_cg") else 3)
        assert eval story_faces["lumi"] == "happy" and sd_event_dissolve == 0.37
        if eval stage_mode == "sd_event":
            assert eval sd_event_current == "ch02_rival_introduction" and sd_event_variant_id == "02"
            assert eval story_mode == "sd_event" and story_effects == {}
            assert eval renpy.get_screen("sd_event_view", layer="sd_events") is not None
        elif eval stage_mode == "ld_cg":
            assert eval renpy._campus_ld_fixture_starts == 1
            assert eval cg_is_active() and cg_current == "ld_07" and story_mode == "ld_cg"
            assert eval not story_cast and not story_effects and not story_stage_visible and sd_event_current is None
            assert eval renpy.get_screen("ld_cg_view",layer="ld_cg") is not None
            assert eval "roman" not in renpy.get_showing_tags(layer="master")
        else:
            assert eval story_effects["sia"][0] == "shake"
            assert eval sd_event_current is None and renpy.get_screen("sd_event_view", layer="sd_events") is None
        assert eval story_positions["roman"] == (420,480) and story_positions["sia"] == (860,540)
        assert eval story_facing["roman"] == -1 and story_facing["sia"] == 1
        assert eval not eligible_routes() and not persistent.endings and not meta_unlocked()
        screenshot f"save_restored_{stage_mode}.png"
        if eval stage_mode == "sd_event":
            $ sd_event_end(transition=0)
            $ renpy.restart_interaction()
            assert eval sd_event_current is None and story_mode == "normal"
            assert eval list(story_cast) == renpy._campus_saved_snapshot["sd_event_previous_cast"]
            assert eval dict(story_faces) == renpy._campus_saved_snapshot["sd_event_previous_faces"]
            assert eval dict(story_positions) == renpy._campus_saved_snapshot["sd_event_previous_positions"]
            assert eval dict(story_facing) == renpy._campus_saved_snapshot["sd_event_previous_facing"]
            assert eval renpy.get_screen("sd_event_view", layer="sd_events") is None
            screenshot "save_event_return_normal.png"
        elif eval stage_mode == "ld_cg":
            $ cg_end(transition=0)
            $ renpy.restart_interaction()
            assert eval not cg_is_active() and story_mode == renpy._campus_saved_snapshot["cg_previous_mode"]
            assert eval list(story_cast) == renpy._campus_saved_snapshot["cg_previous_cast"]
            assert eval dict(story_faces) == renpy._campus_saved_snapshot["cg_previous_faces"]
            assert eval dict(story_positions) == renpy._campus_saved_snapshot["cg_previous_positions"]
            assert eval dict(story_facing) == renpy._campus_saved_snapshot["cg_previous_facing"]
            assert eval story_stage_visible == renpy._campus_saved_snapshot["cg_previous_stage_visible"]
            assert eval story_chat_active == renpy._campus_saved_snapshot["cg_previous_chat_active"]
            assert eval renpy.get_screen("ld_cg_view",layer="ld_cg") is None and not cg_hidden_master
            assert eval "roman" in renpy.get_showing_tags(layer="master")
            assert eval renpy.get_attributes("roman",layer="master") == ("smile",)
            assert eval chapter_test.transform_placements(renpy.get_at_list("roman",layer="master") or []) == renpy._campus_saved_snapshot["cg_hidden_master"][0][2]
            screenshot "save_ld_return_normal.png"

    testcase developer_gate_and_asset_fallback:
        run Start("chapter03")
        pause until screen "say"
        python:
            developer_before = config.developer
            config.developer = False
            try:
                # A release build cannot use this helper to jump out of context.
                assert story_debug_start("chapter01") is None
                assert story_chapter_number == 3
            finally:
                config.developer = developer_before
            missing_all_portraits = not any(path.endswith(".png") and path.startswith(("images/heroines/", "images/rivals/", "images/sd/")) for path in renpy.list_files())
            for actor in chapter_test.ALL_CAST:
                for sd in (False, True):
                    art = story_asset(actor, "confused", sd=sd)
                    assert art is None or renpy.loadable(art)
                    if sd:
                        assert art is None, "Individual SD sprite loading must remain disabled."
                    if missing_all_portraits:
                        assert art is None, (actor, sd, art)
            assert story_id("rumi") == "lumi"
        run ShowMenu("chapter_developer")
        assert screen "chapter_developer"
        screenshot "chapter_developer.png"


# Test-only native save fixtures. Excluded from shipped builds with this file.
label qa_story_save_normal:
    $ _qa_story_save_mode = "normal"
    jump qa_story_save_initialize

label qa_story_save_emotion:
    $ _qa_story_save_mode = "emotion"
    jump qa_story_save_initialize

label qa_story_save_sd_event:
    $ _qa_story_save_mode = "sd_event"
    jump qa_story_save_initialize

label qa_story_save_ld_cg:
    $ _qa_story_save_mode = "ld_cg"
    jump qa_story_save_initialize

label qa_story_save_initialize:
    python:
        story_begin_chapter(3, "챕터 저장 복원 검증")
        renpy.store.player_name = "챕터저장"
        for name, value in {"first_task_partner":"rumi", "ch02_partner":"roman", "ch03_partner":"rumi",
                "ch03_evening_event":"rumi", "chapter01_complete":True, "chapter02_complete":True,
                "roman_book_event":True, "roman_question_event":True, "rumi_design_event":True,
                "lumi_special_moment":True, "lumi_reverse_prank":True, "rival_attitude":"cooperative",
                "rival_helped":True, "rival_cooperation":True, "team_preparation":2,
                "exhibition_quality":1, "promotion_quality":3, "pitch_strategy":"guide",
                "trial_preparation":"space", "visitor_policy_priority":"privacy", "visitor_policy_established":True,
                "visitor_withdrawal_occurred":True, "cooperation_method":"layout", "trial_operation_complete":True}.items():
            story_flag(name, value)
        affection["lumi"] = 8
        trust["roman"] = 6
        choice_log.append("chapter_save_checkpoint")
        story_scene("booth", mode="normal" if _qa_story_save_mode in ("sd_event","ld_cg") else _qa_story_save_mode, cast=chapter_test.ALL_CAST, location="저장 복원 검증")
        story_stage(faces={"rumi":"smile", "ski":"surprised", "sia":"angry"},
            positions={"roman":(420,480), "sia":(860,540)}, facing={"roman":-1, "sia":1})
        story_effect("shake", "sia")
        sd_event_dissolve = 0.37
        if _qa_story_save_mode == "sd_event":
            sd_event_start("ch02_rival_introduction", "02", transition=0)
        elif _qa_story_save_mode == "ld_cg":
            renpy._campus_ld_fixture_starts += 1
            renpy.show("roman smile",at_list=[left],layer="master")
            cg_start("ld_07",transition=0)
    jump qa_story_save_checkpoint

label qa_story_save_checkpoint:
    mc "함께 준비한 이름과 관계, 무대 위치와 방향을 이 대사에서 저장합니다."
    jump qa_story_save_checkpoint

