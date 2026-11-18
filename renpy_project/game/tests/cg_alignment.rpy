# Native framing regression for the five CH04 expression pairs.
# This suite only runs in its D: fixture and never changes source artwork.
init python in cg_alignment_qa:
    import json
    import os
    from pathlib import Path

    ROOT = Path("D:/CampusRomance_VN/tests/cg_alignment_20261107")
    PAIRS = (
        ("roman", "ROMAN", "ch04_private_roman", "ch04_private_roman_shy"),
        ("sia", "SIA", "ch04_private_sia_tablet", "ch04_private_sia"),
        ("darim", "DARIM", "ch04_private_darim", "ch04_private_darim_smile"),
        ("omu", "OMU", "ch04_private_omu", "ch04_private_omu_smile"),
        ("lumi", "HARIN", "ch04_private_lumi", "ch04_private_lumi_shy"),
    )
    evidence = []

    def configure_upscales():
        rows = json.loads((ROOT / "upscale_applied.json").read_text(encoding="utf-8-sig"))
        renpy._cg_alignment_upscales = {row["id"]: row for row in rows}

    def capture_dissolve():
        key = renpy.store.cg_current
        if key not in {pair[3] for pair in PAIRS}:
            return
        transition = renpy.game.interface.instantiated_transition.get("ld_cg")
        if isinstance(transition, renpy.display.transition.Dissolve):
            renpy._cg_alignment_dissolves[key] = transition.time

    if os.path.normcase(os.path.abspath(renpy.config.basedir)) == os.path.normcase(
            os.path.abspath(str(ROOT / "renpy_project"))):
        renpy.config.periodic_callbacks.append(capture_dissolve)

    def framing_nodes(widget):
        assets = []; crops = []; transforms = []; seen = set()
        def walk(node):
            if node is None or id(node) in seen:
                return
            seen.add(id(node))
            assert type(node).__name__ != "ATLTransform", "The framing tree must remain static."
            filename = getattr(node, "filename", None)
            if filename:
                assets.append(str(filename))
            kwargs = getattr(node, "kwargs", {})
            if kwargs:
                for field in ("zoom", "xzoom", "yzoom"):
                    assert kwargs.get(field, 1.0) == 1.0, (field, kwargs)
                if kwargs.get("crop") is not None:
                    crops.append((tuple(float(value) for value in kwargs["crop"]), bool(kwargs.get("crop_relative", False))))
                transforms.append({"fit": kwargs.get("fit"), "xysize": kwargs.get("xysize"),
                    "crop": kwargs.get("crop"), "crop_relative": kwargs.get("crop_relative")})
            for child in node.visit():
                walk(child)
        walk(widget)
        return sorted(set(assets)), crops, transforms

    def assert_frame(screen, widget_id, key, size=(1920, 1080), thumbnail=False, label=None, layer=None):
        s = renpy.store
        widget = renpy.get_widget(screen, widget_id, layer=layer) if layer else renpy.get_widget(screen, widget_id)
        assert widget is not None, (screen, widget_id)
        envelope = tuple(float(value) for value in widget.render_size)
        assert all(abs(actual - expected) <= 1.0 for actual, expected in zip(envelope, size)), (label, envelope, size)
        assets, crops, transforms = framing_nodes(widget)
        fresh_assets, fresh_crops, fresh_transforms = framing_nodes(s.cg_displayable(key, size=size, thumbnail=thumbnail))
        assert assets == fresh_assets and crops == fresh_crops, (label, assets, fresh_assets, crops, fresh_crops)
        assert s.cg_asset(key) in assets, (label, assets)
        source_dimensions = tuple(renpy.image_size(s.cg_asset(key)))
        upscale = getattr(renpy, "_cg_alignment_upscales", {}).get(key)
        if upscale:
            assert s.cg_asset(key) == upscale["image"], (label, s.cg_asset(key), upscale["image"])
            assert source_dimensions == tuple(upscale["size"]), (label, source_dimensions, upscale["size"])
        entry = s.cg_entry(key)
        declared = entry.get("screen_crop")
        if declared is not None:
            declared = tuple(float(value) for value in declared)
            assert len(declared) == 4 and all(0.0 <= value <= 1.0 for value in declared)
            assert declared[0] + declared[2] <= 1.000001 and declared[1] + declared[3] <= 1.000001
            assert (declared, True) in crops, (label, crops, declared)
        else:
            assert not crops, (label, crops)
        resolved_label = label or widget_id
        evidence[:] = [row for row in evidence if row["label"] != resolved_label]
        evidence.append({"label": resolved_label, "key": key, "screen": screen,
            "size": size, "rendered_envelope": envelope, "assets": assets,
            "source_dimensions": source_dimensions,
            "crops": crops, "transforms": transforms, "declared_crop": declared,
            "shared_helper_matches": True, "no_atl_or_zoom": True})
        (ROOT / "framing_evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return True

    def assert_game(key, label):
        s = renpy.store
        renpy._cg_alignment_expected_seen.add(key)
        assert s.cg_current == key
        assert s.persistent.cg_seen == renpy._cg_alignment_expected_seen
        assert not s.persistent.cg_sd_seen and not s.persistent.gallery
        return assert_frame("ld_cg_view", "ld_cg_asset", key, label=label, layer="ld_cg")

    def unlock_pairs():
        s = renpy.store
        s.persistent.cg_seen = {key for pair in PAIRS for key in pair[2:]}
        renpy.restart_interaction()

    def assert_gallery(hero, key, canonical, thumbnail=False):
        s = renpy.store
        if thumbnail:
            return assert_frame("gallery", "cg_thumb_" + canonical, key, size=(456, 256),
                thumbnail=True, label="gallery_" + hero + "_thumbnail")
        scope = renpy.get_screen("cg_view").scope
        assert scope["current_cg"] == canonical and scope["current_cut"] == key
        return assert_frame("cg_view", "cg_view_asset", key, label="gallery_" + hero + "_" + key)


testsuite cg_alignment:
    setup:
        python:
            import os
            expected = cg_alignment_qa.ROOT / "renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(str(expected)))
            sd_independent_isolation_test.assert_locations()
        $ cg_alignment_qa.configure_upscales()
        $ _test.timeout = 90.0
        $ _test.transition_timeout = 0.60
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/cg_alignment_20261107/screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
        $ _preferences.transitions = 2
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
        $ sd_independent_isolation_test.assert_locations()
        $ persistent.cg_seen = set()
        $ persistent.cg_sd_seen = set()
        $ persistent.gallery = set()
        $ renpy._cg_alignment_expected_seen = set()
        $ renpy._cg_alignment_dissolves = {}
    teardown:
        exit

    testcase five_gameplay_pairs_and_second_cut_load:
        run Start("qa_cg_alignment_pairs")
        pause until eval _last_say_what == "CG 정렬 · 로만 · 기본"
        pause 0.15
        assert eval cg_alignment_qa.assert_game("ch04_private_roman", "game_roman_first")
        assert eval not cg_seen("ch04_private_roman_shy")
        screenshot "game_roman_first.png"
        advance until eval _last_say_what == "CG 정렬 · 로만 · 표정"
        pause 0.4
        assert eval cg_alignment_qa.assert_game("ch04_private_roman_shy", "game_roman_second")
        assert eval renpy._cg_alignment_dissolves.get("ch04_private_roman_shy") == 0.38
        screenshot "game_roman_second.png"
        run FileSave("alignment-second", page="21", confirm=False)
        assert eval renpy.can_load("21-alignment-second")
        $ cg_end(transition=0)
        assert eval not cg_is_active()
        run FileLoad("alignment-second", page="21", confirm=False)
        pause until eval cg_current == "ch04_private_roman_shy" and _last_say_what == "CG 정렬 · 로만 · 표정" timeout 5
        pause 0.15
        assert eval cg_alignment_qa.assert_game("ch04_private_roman_shy", "game_roman_second_loaded")
        screenshot "game_roman_second_loaded.png"
        advance until eval _last_say_what == "CG 정렬 · 시아 · 기본"
        pause 0.15
        assert eval cg_alignment_qa.assert_game("ch04_private_sia_tablet", "game_sia_first")
        assert eval not cg_seen("ch04_private_sia")
        screenshot "game_sia_first.png"
        advance until eval _last_say_what == "CG 정렬 · 시아 · 표정"
        pause 0.4
        assert eval cg_alignment_qa.assert_game("ch04_private_sia", "game_sia_second")
        assert eval renpy._cg_alignment_dissolves.get("ch04_private_sia") == 0.38
        screenshot "game_sia_second.png"
        advance until eval _last_say_what == "CG 정렬 · 다림 · 기본"
        pause 0.15
        assert eval cg_alignment_qa.assert_game("ch04_private_darim", "game_darim_first")
        assert eval not cg_seen("ch04_private_darim_smile")
        screenshot "game_darim_first.png"
        advance until eval _last_say_what == "CG 정렬 · 다림 · 표정"
        pause 0.4
        assert eval cg_alignment_qa.assert_game("ch04_private_darim_smile", "game_darim_second")
        assert eval renpy._cg_alignment_dissolves.get("ch04_private_darim_smile") == 0.38
        screenshot "game_darim_second.png"
        advance until eval _last_say_what == "CG 정렬 · 오므 · 기본"
        pause 0.15
        assert eval cg_alignment_qa.assert_game("ch04_private_omu", "game_omu_first")
        assert eval not cg_seen("ch04_private_omu_smile")
        screenshot "game_omu_first.png"
        advance until eval _last_say_what == "CG 정렬 · 오므 · 표정"
        pause 0.4
        assert eval cg_alignment_qa.assert_game("ch04_private_omu_smile", "game_omu_second")
        assert eval renpy._cg_alignment_dissolves.get("ch04_private_omu_smile") == 0.38
        screenshot "game_omu_second.png"
        advance until eval _last_say_what == "CG 정렬 · 하린 · 기본"
        pause 0.15
        assert eval cg_alignment_qa.assert_game("ch04_private_lumi", "game_lumi_first")
        assert eval not cg_seen("ch04_private_lumi_shy")
        screenshot "game_lumi_first.png"
        advance until eval _last_say_what == "CG 정렬 · 하린 · 표정"
        pause 0.4
        assert eval cg_alignment_qa.assert_game("ch04_private_lumi_shy", "game_lumi_second")
        assert eval renpy._cg_alignment_dissolves.get("ch04_private_lumi_shy") == 0.38
        screenshot "game_lumi_second.png"
        advance until eval _last_say_what == "CG 정렬 종료"
        assert eval not cg_is_active() and renpy.get_screen("ld_cg_view", layer="ld_cg") is None
        assert eval len(persistent.cg_seen) == 10 and len(cg_unlocked_ids()) == 5

    testcase gallery_pairs_and_thumbnails_share_framing:
        $ _preferences.transitions = 0
        $ cg_alignment_qa.unlock_pairs()
        click "갤러리"
        click "ROMAN"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("roman", "ch04_private_roman", "ch04_private_roman", thumbnail=True)
        click id "cg_tile_ch04_private_roman" screen ("gallery",)
        keysym "h"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("roman", "ch04_private_roman", "ch04_private_roman")
        screenshot "gallery_roman_first.png"
        keysym "K_SPACE"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("roman", "ch04_private_roman_shy", "ch04_private_roman")
        screenshot "gallery_roman_second.png"
        keysym "h"
        click "닫기"
        click "SIA"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("sia", "ch04_private_sia_tablet", "ch04_private_sia", thumbnail=True)
        click id "cg_tile_ch04_private_sia" screen ("gallery",)
        keysym "h"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("sia", "ch04_private_sia_tablet", "ch04_private_sia")
        screenshot "gallery_sia_first.png"
        keysym "K_SPACE"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("sia", "ch04_private_sia", "ch04_private_sia")
        screenshot "gallery_sia_second.png"
        keysym "h"
        click "닫기"
        click "DARIM"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("darim", "ch04_private_darim", "ch04_private_darim", thumbnail=True)
        click id "cg_tile_ch04_private_darim" screen ("gallery",)
        keysym "h"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("darim", "ch04_private_darim", "ch04_private_darim")
        screenshot "gallery_darim_first.png"
        keysym "K_SPACE"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("darim", "ch04_private_darim_smile", "ch04_private_darim")
        screenshot "gallery_darim_second.png"
        keysym "h"
        click "닫기"
        click "OMU"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("omu", "ch04_private_omu", "ch04_private_omu", thumbnail=True)
        click id "cg_tile_ch04_private_omu" screen ("gallery",)
        keysym "h"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("omu", "ch04_private_omu", "ch04_private_omu")
        screenshot "gallery_omu_first.png"
        keysym "K_SPACE"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("omu", "ch04_private_omu_smile", "ch04_private_omu")
        screenshot "gallery_omu_second.png"
        keysym "h"
        click "닫기"
        click "HARIN"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("lumi", "ch04_private_lumi", "ch04_private_lumi", thumbnail=True)
        click id "cg_tile_ch04_private_lumi" screen ("gallery",)
        keysym "h"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("lumi", "ch04_private_lumi", "ch04_private_lumi")
        screenshot "gallery_lumi_first.png"
        keysym "K_SPACE"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("lumi", "ch04_private_lumi_shy", "ch04_private_lumi")
        screenshot "gallery_lumi_second.png"
        keysym "h"
        click "닫기"
        assert eval len(persistent.cg_seen) == 10 and not cg_is_active()
        click "돌아가기"

    testcase uncalibrated_singleton_retains_original_fit:
        run Start("qa_cg_alignment_singleton")
        pause until eval _last_say_what == "CG 정렬 · 단독 장면"
        pause 0.15
        assert eval cg_entry("ch04_evening_roman").get("screen_crop") is None
        assert eval cg_alignment_qa.assert_game("ch04_evening_roman", "singleton_gameplay")
        $ cg_end(transition=0)
        run MainMenu(confirm=False, save=False)
        pause until screen "main_menu"
        $ renpy._cg_alignment_singleton_seen = set(persistent.cg_seen)
        click "갤러리"
        click "ROMAN"
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("singleton", "ch04_evening_roman", "ch04_evening_roman", thumbnail=True)
        click id "cg_tile_ch04_evening_roman" screen ("gallery",)
        pause 0.15
        assert eval cg_alignment_qa.assert_gallery("singleton", "ch04_evening_roman", "ch04_evening_roman")
        assert eval persistent.cg_seen == renpy._cg_alignment_singleton_seen
        screenshot "gallery_singleton_unchanged.png"
        click "닫기"
        click "돌아가기"

label qa_cg_alignment_pairs:
    $ story_begin_chapter(4, "개별 CG 표정 컷 정렬 검증")
    $ story_scene("study", cast=[], light="evening", standing=False, location="CG 정렬 검증")
    $ cg_start("ch04_private_roman", transition=0)
    narrator "CG 정렬 · 로만 · 기본"
    $ cg_start("ch04_private_roman_shy", transition=0.38)
    narrator "CG 정렬 · 로만 · 표정"
    $ cg_start("ch04_private_sia_tablet", transition=0)
    narrator "CG 정렬 · 시아 · 기본"
    $ cg_start("ch04_private_sia", transition=0.38)
    narrator "CG 정렬 · 시아 · 표정"
    $ cg_start("ch04_private_darim", transition=0)
    narrator "CG 정렬 · 다림 · 기본"
    $ cg_start("ch04_private_darim_smile", transition=0.38)
    narrator "CG 정렬 · 다림 · 표정"
    $ cg_start("ch04_private_omu", transition=0)
    narrator "CG 정렬 · 오므 · 기본"
    $ cg_start("ch04_private_omu_smile", transition=0.38)
    narrator "CG 정렬 · 오므 · 표정"
    $ cg_start("ch04_private_lumi", transition=0)
    narrator "CG 정렬 · 하린 · 기본"
    $ cg_start("ch04_private_lumi_shy", transition=0.38)
    narrator "CG 정렬 · 하린 · 표정"
    $ cg_end(transition=0)
    narrator "CG 정렬 종료"
    jump qa_cg_alignment_hold

label qa_cg_alignment_singleton:
    $ story_begin_chapter(4, "단독 CG 기존 구도 검증")
    $ story_scene("campus", cast=[], light="night", standing=False, location="단독 CG 검증")
    $ cg_start("ch04_evening_roman", transition=0)
    narrator "CG 정렬 · 단독 장면"
    jump qa_cg_alignment_hold

label qa_cg_alignment_hold:
    narrator "CG 정렬 검증 종료 지점입니다."
    jump qa_cg_alignment_hold
