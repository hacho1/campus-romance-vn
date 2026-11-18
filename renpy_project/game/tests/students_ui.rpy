# Native regressions for the student binder and two-page supplied NPC portraits.
# Run only from tests/people_portraits_20261108, with isolated player data.
init python in students_ui_qa:
    import copy
    import json
    import os
    from pathlib import Path
    from renpy.text.text import Text as SdkText
    from renpy.display.viewport import Viewport as SdkViewport

    ROOT = Path("D:/CampusRomance_VN/tests/people_portraits_20261108")
    EXPECTED_PEOPLE = (
        ("ski", "스키", "제과제빵과", 3),
        ("hyeophap", "협합", "제과제빵과", 3),
        ("bambam", "밤밤", "심리학과", 2),
        ("hess", "헤스", "심리학과", 1),
    )
    layouts = []
    ink_checks = []

    def begin():
        renpy.store.typography_qa.install_render_observer()
        renpy._students_original_story_asset = None
        renpy._students_original_loadable = None

    def finish():
        restore_story_asset()
        SdkText.render = renpy._typography_original_text_render

    def refresh(screen):
        renpy.store.typography_qa.refresh(screen)

    def write():
        (ROOT / "layout_evidence.json").write_text(json.dumps(layouts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (ROOT / "button_ink_queue.json").write_text(json.dumps({"checks": ink_checks}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def queue_button(screen, widget_id, caption, screenshot):
        assert (ROOT / "screenshots" / screenshot).is_file(), screenshot
        widget, row = renpy.store.screenshot_polish_qa.button_for(caption, screen, widget_id)
        x, y, width, height = row["global_button_rect"]
        ink_checks.append({"kind": "ink_centre_pending_png", "label": caption,
            "screenshot": screenshot, "button_rect": [x, y, width, height],
            "text_metric_rect": [x + row["x"], y + row["y"], row["w"], row["h"]],
            "background_present": widget.style.background is not None})
        write()
        return True

    def assert_profile(hero, back=False):
        s = renpy.store
        scope = renpy.get_screen("profiles").scope
        assert scope["selected"] == hero and scope["back"] == back
        assert renpy.get_widget("profiles", "profile_name").get_all_text() == s.HEROINES[hero]["name"]
        expected_badge = s.HEROINES[hero]["department"] + " " + str(s.HEROINES[hero]["year"]) + "학년"
        assert renpy.get_widget("profiles", "profile_department_badge").get_all_text() == expected_badge
        assert s.campus_ui_test.contains_text("profiles", "CC대 학생들")
        assert s.campus_ui_test.contains_text("profiles", s.HEROINES[hero]["intro"] if back else s.PROFILE_PAGES[hero]["one_line"])
        if back:
            assert s.campus_ui_test.contains_text("profiles", s.HEROINES[hero]["relations"])
        for widget_id in ("secret_notes_open", "secret_note_slot_1", "secret_note_slot_2", "secret_note_slot_3",
                "profile_relationship_panel", "profile_affection_value", "profile_trust_value", "met_people_open"):
            assert renpy.get_widget("profiles", widget_id) is not None, widget_id
        return True

    def rect_for(screen_name, widget_id):
        target = renpy.get_widget(screen_name, widget_id)
        assert target is not None, widget_id
        found = []; seen = set()
        def walk(node, x=0, y=0):
            if node is None or id(node) in seen:
                return
            seen.add(id(node))
            if node is target:
                size = (node.width, node.height) if isinstance(node, SdkViewport) else getattr(node, "render_size", None)
                if size is None:
                    # Fixed's xysize is stored as the native style minimums.
                    size = (node.style.xminimum, node.style.yminimum)
                found.append((float(x), float(y), float(size[0]), float(size[1])))
                return
            children = getattr(node, "children", None)
            if not children:
                child = getattr(node, "child", None)
                children = [child] if child is not None else []
            offsets = getattr(node, "offsets", None)
            for index, child in enumerate(children):
                dx, dy = offsets[index] if offsets is not None and index < len(offsets) else (0, 0)
                walk(child, x + dx, y + dy)
        walk(renpy.get_screen(screen_name))
        assert len(found) == 1, (widget_id, found)
        return found[0]

    def inside(rect, container):
        x, y, width, height = rect
        left, top, available_width, available_height = container
        return (x >= left - 1 and y >= top - 1 and x + width <= left + available_width + 1
            and y + height <= top + available_height + 1)

    def asset_names(widget):
        names = []; seen = set()
        def walk(node):
            if node is None or id(node) in seen:
                return
            seen.add(id(node))
            filename = getattr(node, "filename", None)
            if filename:
                names.append(str(filename))
            for child in node.visit():
                walk(child)
        walk(widget)
        return names

    def assert_cards(page=0, photo_mode="dedicated"):
        s = renpy.store
        expected_order = ("ski", "hyeophap", "bambam", "hess")
        assert tuple(s.MET_PEOPLE_ORDER) == expected_order
        assert s.MET_PEOPLE_PAGE_SIZE == 2 and s.met_people_page_count() == 2
        scope = renpy.get_screen("met_people").scope
        assert scope["people_page"] == page
        visible_people = expected_order[page * 2:page * 2 + 2]
        assert tuple(scope["people_page_keys"]) == visible_people
        page_text = renpy.get_widget("met_people", "met_people_page").get_all_text()
        assert "".join(page_text.split()) == str(page + 1) + "/2"
        for actor in expected_order:
            assert (renpy.get_widget("met_people", "met_person_card_" + actor) is not None) == (actor in visible_people)
        text_rows = s.screenshot_polish_qa.text_rows(renpy.get_screen("met_people"))
        for card_index, (actor, name, department, year) in enumerate(EXPECTED_PEOPLE[page * 2:page * 2 + 2]):
            person = s.MET_PEOPLE[actor]
            assert person["name"] == name and person["department"] == department and person["year"] == year
            assert "age" not in person and "mbti" not in person
            supplied_path = "images/people/profile_" + actor + ".png"
            assert person["portrait_image"] == supplied_path
            card = rect_for("met_people", "met_person_card_" + actor)
            assert inside(card, (0, 0, 1920, 1080)), (actor, card)
            assert all(abs(actual - expected) <= 0.1 for actual, expected in
                zip(card, (116 + card_index * 868, 295, 820, 660))), (actor, card)
            text_evidence = []
            for field in ("name", "department", "intro", "quote"):
                widget_id = "met_person_" + field + "_" + actor
                widget = renpy.get_widget("met_people", widget_id)
                assert widget is not None, widget_id
                expected_text = (department + " · " + str(year) + "학년" if field == "department"
                    else "“" + person["quote"] + "”" if field == "quote" else person[field])
                assert widget.get_all_text() == expected_text
                matching = [row for row in text_rows if row["widget"] is widget]
                assert len(matching) == 1, widget_id
                row = matching[0]
                text_rect = (row["x"], row["y"], row["w"], row["h"])
                assert inside(text_rect, card), (widget_id, text_rect, card)
                text_evidence.append({"id": widget_id, "text": expected_text, "rect": text_rect})
            portrait = renpy.get_widget("met_people", "met_person_portrait_" + actor)
            image = renpy.get_widget("met_people", "met_person_image_" + actor)
            missing = renpy.get_widget("met_people", "met_person_missing_" + actor)
            assert isinstance(portrait, SdkViewport) and not portrait.draggable and not portrait.mousewheel
            portrait_rect = rect_for("met_people", "met_person_portrait_" + actor)
            assert inside(portrait_rect, card), (actor, portrait_rect, card)
            assert all(abs(actual - expected) <= 0.1 for actual, expected in
                zip(portrait_rect[2:], (432, 528))), (actor, portrait_rect)
            image_rect = None
            portrait_assets = []
            source_dimensions = None
            placeholder_rect = None
            expected_source = supplied_path
            placeholder = actor == "ski" and photo_mode == "placeholder"
            if placeholder:
                assert image is None and missing is not None
                assert missing.get_all_text() == "사진 준비 중"
                matching = [row for row in text_rows if row["widget"] is missing]
                assert len(matching) == 1
                row = matching[0]
                placeholder_rect = (row["x"], row["y"], row["w"], row["h"])
                assert inside(placeholder_rect, portrait_rect)
            else:
                assert image is not None and missing is None
                image_rect = rect_for("met_people", "met_person_image_" + actor)
                assert inside(image_rect, portrait_rect), (actor, image_rect, portrait_rect)
                portrait_assets = asset_names(image)
                if actor == "ski" and photo_mode == "standing":
                    expected_source = s.story_asset(actor, "normal")
                    assert supplied_path not in portrait_assets
                assert expected_source in portrait_assets, (actor, portrait_assets, expected_source)
                source_dimensions = tuple(renpy.image_size(expected_source))
                if expected_source == supplied_path:
                    assert source_dimensions == (1232, 1504), (actor, source_dimensions)
            label = actor + "_page" + str(page + 1) + "_" + photo_mode
            layouts[:] = [row for row in layouts if row["label"] != label]
            layouts.append({"label": label, "actor": actor, "card": card,
                "page": page, "text": text_evidence, "portrait": portrait_rect,
                "image": image_rect, "portrait_assets": portrait_assets,
                "photo_mode": photo_mode, "expected_source": expected_source,
                "source_dimensions": source_dimensions, "placeholder_text": placeholder_rect,
                "fallback": placeholder,
                "text_inside_card": True, "card_inside_canvas": True})
        write()
        return True

    def missing_ski_asset(actor, *args, **kwargs):
        return None if actor == "ski" else renpy._students_original_story_asset(actor, *args, **kwargs)

    def missing_ski_dedicated(path, *args, **kwargs):
        dedicated = renpy.store.MET_PEOPLE["ski"]["portrait_image"]
        if str(path).replace("\\", "/") == dedicated:
            return False
        return renpy._students_original_loadable(path, *args, **kwargs)

    def install_missing_asset(fully_missing=False):
        if renpy._students_original_loadable is None:
            renpy._students_original_loadable = renpy.loadable
            renpy.loadable = missing_ski_dedicated
        if fully_missing and renpy._students_original_story_asset is None:
            renpy._students_original_story_asset = renpy.store.story_asset
            renpy.store.story_asset = missing_ski_asset
        renpy.restart_interaction()

    def restore_story_asset():
        original = getattr(renpy, "_students_original_story_asset", None)
        if original is not None:
            renpy.store.story_asset = original
            renpy._students_original_story_asset = None
        original_loadable = getattr(renpy, "_students_original_loadable", None)
        if original_loadable is not None:
            renpy.loadable = original_loadable
            renpy._students_original_loadable = None
        renpy.restart_interaction()

    def snapshot_game():
        s = renpy.store
        renpy._students_game_snapshot = copy.deepcopy((s.affection, s.trust, s.event_flags, s.choice_log))

    def assert_game_unchanged():
        s = renpy.store
        assert (s.affection, s.trust, s.event_flags, s.choice_log) == renpy._students_game_snapshot
        return True


testsuite students_ui:
    setup:
        python:
            import os
            expected = students_ui_qa.ROOT / "renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(str(expected)))
            sd_independent_isolation_test.assert_locations()
        $ _test.timeout = 60.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/people_portraits_20261108/screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 0
        $ students_ui_qa.begin()
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
        $ sd_independent_isolation_test.assert_locations()
        $ persistent.profile_secrets = set()
        $ profile_debug_unlock = False
        $ students_ui_qa.refresh("main_menu")
        pause 0.15
    after testcase:
        $ students_ui_qa.restore_story_asset()
        if screen "profile_secret_notes":
            click id "secret_note_close" screen ("profile_secret_notes",)
        if not screen "main_menu":
            if eval main_menu:
                keysym "K_ESCAPE"
            else:
                run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
    teardown:
        $ students_ui_qa.finish()
        exit

    testcase two_page_portraits_pager_and_selected_heroine_return:
        click "CC대 학생들"
        click "다림"
        click id "met_people_open" screen ("profiles",)
        pause until screen "met_people"
        $ students_ui_qa.refresh("met_people")
        pause 0.15
        assert eval renpy.get_screen("met_people").scope["initial"] == "darim"
        screenshot "met_people_page_1.png"
        assert eval students_ui_qa.assert_cards(page=0)
        assert eval students_ui_qa.queue_button("met_people", "met_people_profiles", "우리의 페이지", "met_people_page_1.png")
        assert eval students_ui_qa.queue_button("met_people", "met_people_selected", "만난 사람들!", "met_people_page_1.png")
        assert eval students_ui_qa.queue_button("met_people", "met_people_prev", "이전", "met_people_page_1.png")
        assert eval students_ui_qa.queue_button("met_people", "met_people_next", "다음", "met_people_page_1.png")
        click id "met_people_next" screen ("met_people",)
        pause 0.2
        screenshot "met_people_page_2.png"
        assert eval students_ui_qa.assert_cards(page=1)
        click id "met_people_next" screen ("met_people",)
        assert eval renpy.get_screen("met_people").scope["people_page"] == 0
        click id "met_people_prev" screen ("met_people",)
        assert eval renpy.get_screen("met_people").scope["people_page"] == 1
        keysym "K_RIGHT"
        assert eval renpy.get_screen("met_people").scope["people_page"] == 0
        keysym "K_LEFT"
        assert eval renpy.get_screen("met_people").scope["people_page"] == 1
        click id "met_people_prev" screen ("met_people",)
        assert eval renpy.get_screen("met_people").scope["people_page"] == 0
        click id "met_people_profiles" screen ("met_people",)
        pause 0.15
        assert eval students_ui_qa.assert_profile("darim")
        click id "met_people_open" screen ("profiles",)
        pause until screen "met_people"
        click id "met_people_close" screen ("met_people",)
        assert screen "main_menu"

    testcase main_menu_and_all_five_original_profiles:
        assert eval campus_ui_test.main_ready()
        assert eval "히로인 설명" not in campus_ui_test.focus_items()
        screenshot "students_main_menu.png"
        click "CC대 학생들"
        pause 0.15
        assert eval students_ui_qa.assert_profile("roman")
        screenshot "heroine_roman_front.png"
        assert eval students_ui_qa.queue_button("profiles", "met_people_open", "만난 사람들!", "heroine_roman_front.png")
        click "뒷면 보기"
        pause 0.15
        assert eval students_ui_qa.assert_profile("roman", back=True)
        screenshot "heroine_roman_back.png"
        click "앞면 보기"
        click "시아"
        pause 0.15
        assert eval students_ui_qa.assert_profile("sia")
        screenshot "heroine_sia_front.png"
        click "뒷면 보기"
        pause 0.15
        assert eval students_ui_qa.assert_profile("sia", back=True)
        click "앞면 보기"
        click "다림"
        pause 0.15
        assert eval students_ui_qa.assert_profile("darim")
        screenshot "heroine_darim_front.png"
        click "뒷면 보기"
        pause 0.15
        assert eval students_ui_qa.assert_profile("darim", back=True)
        screenshot "heroine_darim_back.png"
        click "앞면 보기"
        click "오므"
        pause 0.15
        assert eval students_ui_qa.assert_profile("omu")
        screenshot "heroine_omu_front.png"
        click "뒷면 보기"
        pause 0.15
        assert eval students_ui_qa.assert_profile("omu", back=True)
        click "앞면 보기"
        click "하린"
        pause 0.15
        assert eval students_ui_qa.assert_profile("lumi")
        screenshot "heroine_lumi_front.png"
        click "뒷면 보기"
        pause 0.15
        assert eval students_ui_qa.assert_profile("lumi", back=True)
        click "앞면 보기"
        click id "secret_note_slot_1" screen ("profiles",)
        assert screen "profile_secret_notes"
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_locked") is not None
        click id "secret_note_close" screen ("profile_secret_notes",)
        $ secret_note_unlock("lumi", 1, notify=False)
        $ renpy.restart_interaction()
        click id "secret_note_slot_1" screen ("profiles",)
        assert eval renpy.get_widget("profile_secret_notes", "secret_note_body").get_all_text() == SECRET_NOTE_DATA["lumi"]["note01"]["text"]
        screenshot "heroine_existing_secret_memo.png"
        click id "secret_note_close" screen ("profile_secret_notes",)
        keysym "K_ESCAPE"
        assert screen "main_menu"

    testcase in_game_metrics_and_both_missing_photo_fallbacks:
        run Start("qa_students_ui_ingame")
        pause until eval _last_say_what == "학생 페이지를 열어 확인해 봅니다."
        $ students_ui_qa.snapshot_game()
        click "학생증"
        click "오므"
        pause 0.15
        assert eval students_ui_qa.assert_profile("omu")
        assert eval "35 / 100" in renpy.get_widget("profiles", "profile_affection_value").get_all_text()
        assert eval "60 / 100" in renpy.get_widget("profiles", "profile_trust_value").get_all_text()
        click id "met_people_open" screen ("profiles",)
        pause until screen "met_people"
        assert eval renpy.get_screen("met_people").scope["initial"] == "omu"
        $ students_ui_qa.install_missing_asset()
        $ students_ui_qa.refresh("met_people")
        pause 0.15
        screenshot "met_people_standing_fallback.png"
        assert eval students_ui_qa.assert_cards(page=0, photo_mode="standing")
        $ students_ui_qa.install_missing_asset(fully_missing=True)
        $ students_ui_qa.refresh("met_people")
        pause 0.15
        screenshot "met_people_placeholder_fallback.png"
        assert eval students_ui_qa.assert_cards(page=0, photo_mode="placeholder")
        $ students_ui_qa.restore_story_asset()
        click id "met_people_profiles" screen ("met_people",)
        pause 0.15
        assert eval students_ui_qa.assert_profile("omu")
        assert eval "35 / 100" in renpy.get_widget("profiles", "profile_affection_value").get_all_text()
        assert eval "60 / 100" in renpy.get_widget("profiles", "profile_trust_value").get_all_text()
        click id "met_people_open" screen ("profiles",)
        pause until screen "met_people"
        keysym "K_ESCAPE"
        pause until screen "say"
        assert eval _last_say_what == "학생 페이지를 열어 확인해 봅니다." and not main_menu
        assert eval renpy.get_screen("met_people") is None and renpy.get_screen("profiles") is None
        assert eval students_ui_qa.assert_game_unchanged()

label qa_students_ui_ingame:
    $ story_begin_chapter(4, "학생 페이지 검증")
    $ story_scene("clubroom307", cast=["omu"], location="학생 페이지 검증")
    $ affection["omu"] = 35
    $ trust["omu"] = 60
    narrator "학생 페이지를 열어 확인해 봅니다."
    jump qa_students_ui_hold

label qa_students_ui_hold:
    narrator "학생 페이지 검증 종료 지점입니다."
    jump qa_students_ui_hold
