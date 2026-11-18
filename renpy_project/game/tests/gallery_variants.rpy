# Native gallery regression. Run only in tests/gallery_variants_20261107;
# the suite never touches the player's real savedir or persistent collection.
init python in gallery_variants_qa:
    import copy
    import os

    def preserve():
        s = renpy.store
        renpy._gallery_variants_snapshot = {
            "cg_seen": copy.deepcopy(s.persistent.cg_seen),
            "cg_sd_seen": copy.deepcopy(s.persistent.cg_sd_seen),
            "gallery": copy.deepcopy(s.persistent.gallery),
            "registry": copy.deepcopy(s.CG_REGISTRY),
            "order": copy.deepcopy(s.CG_ORDER),
            "cg_current": s.cg_current,
        }

    def restore():
        s = renpy.store
        snap = renpy._gallery_variants_snapshot
        s.persistent.cg_seen = snap["cg_seen"]
        s.persistent.cg_sd_seen = snap["cg_sd_seen"]
        s.persistent.gallery = snap["gallery"]
        s.CG_REGISTRY = snap["registry"]
        s.CG_ORDER = snap["order"]
        s.cg_current = snap["cg_current"]
        renpy.restart_interaction()

    def only_seen(*keys):
        s = renpy.store
        s.persistent.cg_seen = set(keys)
        s.persistent.cg_sd_seen = set()
        s.persistent.gallery = set()
        renpy.restart_interaction()

    def scope():
        return renpy.get_screen("cg_view").scope

    def assert_collection_unchanged(keys):
        s = renpy.store
        assert s.persistent.cg_seen == set(keys)
        assert not s.persistent.cg_sd_seen
        assert not s.persistent.gallery
        assert s.cg_current == renpy._gallery_variants_snapshot["cg_current"]


testsuite gallery_variants:
    setup:
        python:
            import os
            expected = "D:/CampusRomance_VN/tests/gallery_variants_20261107/renpy_project"
            assert os.path.normcase(os.path.abspath(config.basedir)) == os.path.normcase(os.path.abspath(expected))
            sd_independent_isolation_test.assert_locations()
        $ _test.timeout = 30.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/gallery_variants_20261107/screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _preferences.afm_enable = False
    before testcase:
        pause until screen "main_menu"
        pause 0.1
        $ sd_independent_isolation_test.assert_locations()
        $ gallery_variants_qa.preserve()
    after testcase:
        if screen "cg_view":
            keysym "K_ESCAPE"
        if screen "gallery":
            click "돌아가기"
        pause until screen "main_menu"
        $ gallery_variants_qa.restore()
        $ sd_independent_isolation_test.assert_locations()
    teardown:
        exit

    testcase scene_groups_and_future_registry_dedup:
        python:
            for parent, cuts in (
                ("ch04_private_roman", ["ch04_private_roman", "ch04_private_roman_shy"]),
                ("ch04_private_sia", ["ch04_private_sia_tablet", "ch04_private_sia"]),
                ("ch04_private_darim", ["ch04_private_darim", "ch04_private_darim_smile"]),
            ):
                assert cg_gallery_variants(parent) == cuts
                for cut in cuts:
                    assert cg_gallery_key(cut) == parent
                tab = cg_entry(parent)["tab"]
                CG_ORDER.extend(cuts)
                assert cg_gallery_keys(tab).count(parent) == 1
                for cut in cuts:
                    if cut != parent:
                        assert cut not in cg_gallery_keys(tab)
            # The data contract works for a later chapter without a hardcoded ID.
            import copy
            CG_REGISTRY["qa_ch06_parent"] = copy.deepcopy(CG_REGISTRY["ch05_private_roman"])
            CG_REGISTRY["qa_ch06_child"] = copy.deepcopy(CG_REGISTRY["ch05_private_roman"])
            CG_REGISTRY["qa_ch06_parent"]["gallery_variants"] = ["qa_ch06_parent", "qa_ch06_child"]
            CG_ORDER.extend(["qa_ch06_parent", "qa_ch06_child"])
            gallery_variants_qa.only_seen("qa_ch06_child")
            assert cg_gallery_key("qa_ch06_child") == "qa_ch06_parent"
            assert cg_gallery_keys("ROMAN").count("qa_ch06_parent") == 1
            assert cg_unlocked_ids(cg_gallery_keys("ROMAN")) == ["qa_ch06_parent"]
            assert not cg_seen("qa_ch06_parent") and cg_gallery_seen("qa_ch06_parent")

    testcase roman_art_click_space_enter_and_scene_navigation:
        $ gallery_variants_qa.only_seen("ld_08", "ch04_private_roman", "ch04_private_roman_shy")
        click "갤러리"
        click "ROMAN"
        assert eval renpy.get_widget("gallery", "cg_tile_ch04_private_roman") is not None
        assert eval renpy.get_widget("gallery", "cg_tile_ch04_private_roman_shy") is None
        click id "cg_tile_ch04_private_roman" screen ("gallery",)
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman"
        assert eval renpy.get_widget("cg_view", "cg_view_asset") is not None
        screenshot "roman_first_cut.png"
        click id "cg_cycle_variant" screen ("cg_view",)
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman_shy"
        screenshot "roman_second_cut.png"
        keysym "K_SPACE"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman"
        keysym "K_RETURN"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman_shy"
        keysym "h"
        assert eval not gallery_variants_qa.scope()["chrome"]
        click pos (960, 450)
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman"
        keysym "K_SPACE"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman_shy"
        keysym "h"
        keysym "K_LEFT"
        assert eval gallery_variants_qa.scope()["current_cg"] == "ld_08"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ld_08"
        keysym "K_RIGHT"
        assert eval gallery_variants_qa.scope()["current_cg"] == "ch04_private_roman"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman"
        $ gallery_variants_qa.assert_collection_unchanged(("ld_08", "ch04_private_roman", "ch04_private_roman_shy"))

    testcase unviewed_expression_stays_locked:
        $ gallery_variants_qa.only_seen("ch04_private_roman")
        click "갤러리"
        click "ROMAN"
        click id "cg_tile_ch04_private_roman" screen ("gallery",)
        assert eval cg_gallery_variants("ch04_private_roman", unlocked_only=True) == ["ch04_private_roman"]
        keysym "K_SPACE"
        keysym "K_RETURN"
        click pos (960, 450)
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman"
        assert eval not cg_seen("ch04_private_roman_shy")
        $ gallery_variants_qa.assert_collection_unchanged(("ch04_private_roman",))

    testcase variant_only_legacy_collection_opens_parent_tile:
        python:
            gallery_variants_qa.only_seen()
            persistent.gallery = {"ch04_private_roman_shy"}
            renpy.restart_interaction()
        click "갤러리"
        click "ROMAN"
        assert eval not cg_seen("ch04_private_roman") and cg_gallery_seen("ch04_private_roman")
        assert eval cg_gallery_preview("ch04_private_roman") == "ch04_private_roman_shy"
        assert eval cg_unlocked_ids(cg_gallery_keys("ROMAN")) == ["ch04_private_roman"]
        click id "cg_tile_ch04_private_roman" screen ("gallery",)
        assert eval gallery_variants_qa.scope()["current_cg"] == "ch04_private_roman"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman_shy"
        keysym "K_SPACE"
        keysym "K_RETURN"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_roman_shy"
        assert eval persistent.gallery == {"ch04_private_roman_shy"} and not persistent.cg_seen
        screenshot "roman_legacy_variant_only.png"

    testcase sia_story_order_and_explicit_expression_button:
        $ gallery_variants_qa.only_seen("ch04_private_sia_tablet", "ch04_private_sia")
        click "갤러리"
        click "SIA"
        click id "cg_tile_ch04_private_sia" screen ("gallery",)
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_sia_tablet"
        click id "cg_next_variant" screen ("cg_view",)
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_sia"
        keysym "K_RETURN"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_sia_tablet"
        $ gallery_variants_qa.assert_collection_unchanged(("ch04_private_sia_tablet", "ch04_private_sia"))

    testcase darim_expression_and_singleton_arrow_navigation:
        $ gallery_variants_qa.only_seen("ld_10", "ch04_private_darim", "ch04_private_darim_smile")
        click "갤러리"
        click "DARIM"
        click id "cg_tile_ch04_private_darim" screen ("gallery",)
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_darim"
        keysym "K_SPACE"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_darim_smile"
        screenshot "darim_second_cut.png"
        click "이전 장면"
        assert eval gallery_variants_qa.scope()["current_cg"] == "ld_10"
        keysym "K_SPACE"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ld_10"
        click "다음 장면"
        assert eval gallery_variants_qa.scope()["current_cut"] == "ch04_private_darim"
        $ gallery_variants_qa.assert_collection_unchanged(("ld_10", "ch04_private_darim", "ch04_private_darim_smile"))
