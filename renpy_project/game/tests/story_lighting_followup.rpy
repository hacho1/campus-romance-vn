# QA-only background checks. No artwork or product registry is edited.
init python in story_lighting_test:
    import copy
    import os

    ROOM_ART = "images/cg/ld_03_first_day_evening.webp"
    ROOM_MORNING = "images/backgrounds/room_morning_pixai.webp"

    def begin():
        expected="D:/CampusRomance_VN/tests/ui_refresh_fixture/renpy_project"
        assert os.path.normcase(os.path.abspath(renpy.config.basedir))==os.path.normcase(os.path.abspath(expected))
        renpy._lighting_registry=copy.deepcopy(renpy.store.STORY_LIGHTING_REGISTRY)
        renpy._lighting_preferred=copy.deepcopy(renpy.store.STORY_BACKGROUND_PREFERRED)
        renpy._lighting_persistent={name:copy.deepcopy(getattr(renpy.store.persistent,name)) for name in renpy.store.campus_ui_test.PERSISTENT_FIELDS}

    def restore_registry():
        renpy.store.STORY_LIGHTING_REGISTRY=copy.deepcopy(renpy._lighting_registry)
        renpy.store.STORY_BACKGROUND_PREFERRED=copy.deepcopy(renpy._lighting_preferred)

    def finish():
        restore_registry()
        for name,value in renpy._lighting_persistent.items():
            setattr(renpy.store.persistent,name,value)
        renpy.save_persistent()

    def files():
        displayable=renpy.game.context().scene_lists.get_displayable_by_tag("master","story_background")
        assert displayable is not None
        found=[]
        def observe(child):
            filename=getattr(child,"filename",None)
            if isinstance(filename,str):
                found.append(filename.replace("\\","/"))
        displayable.visit_all(observe)
        return found

    def missing_room_art(remove_preferred, remove_night_fallback):
        restore_registry()
        renpy.store.STORY_LIGHTING_REGISTRY["room"]["day"]="tests/sd_assets/qa_lighting_missing_room_day.webp"
        if remove_preferred:
            renpy.store.STORY_BACKGROUND_PREFERRED["room"]="tests/sd_assets/qa_lighting_missing_room_art.webp"
        if remove_night_fallback:
            renpy.store.STORY_LIGHTING_REGISTRY["room"]["night"]="tests/sd_assets/qa_lighting_missing_room_night.png"

    def state():
        s=renpy.store
        return {"light":s.story_light,"background":s.story_background,"cast":tuple(s.story_cast),
            "mode":s.story_mode,"affection":dict(s.affection),"trust":dict(s.trust),"choice_log":tuple(s.choice_log)}


testsuite story_lighting_followup:
    setup:
        $ story_lighting_test.begin()
        $ _test.timeout = 30.0
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _preferences.afm_enable = False
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/story-lighting-screenshots"
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        $ story_lighting_test.restore_registry()
    after testcase:
        $ story_lighting_test.restore_registry()
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
    teardown:
        $ story_lighting_test.finish()
        exit

    testcase room_uses_unretinted_art_for_each_time:
        parameter light = ["day","evening","night"]
        run Start("qa_story_lighting_room_day")
        pause until screen "say"
        $ path = story_lighting_test.ROOM_MORNING if light == "day" else story_lighting_test.ROOM_ART
        $ story_scene("room",light=light,cast=[],location="주인공 방")
        $ renpy.restart_interaction()
        pause 0.1
        assert eval story_light == light
        assert eval story_background_info("room",light)["path"] == path
        assert eval story_background_info("room",light)["tint"] is None
        assert eval story_lighting_test.files().count(path) == 1
        screenshot f"room_{light}.png"

    testcase dedicated_campus_night_asset_is_a_single_unretinted_image:
        run Start("qa_story_lighting_night_campus")
        pause until screen "say"
        assert eval story_light == "night" and story_background == "night_campus"
        assert eval renpy.loadable("images/backgrounds/campus_night.png")
        assert eval story_background_info("night_campus","night")["path"] == "images/backgrounds/campus_night.png"
        assert eval story_background_info("night_campus","night")["dedicated_night"] and story_background_info("night_campus","night")["tint"] is None
        assert eval story_lighting_test.files().count("images/backgrounds/campus_night.png") == 1
        screenshot "night_campus_night.png"

    testcase missing_room_art_uses_playable_legacy_fallbacks:
        parameter (light,remove_preferred,remove_night_fallback,path) = [("day",False,False,"images/cg/ld_03_first_day_evening.webp"),("day",True,False,"images/backgrounds/room.png"),("night",True,False,"images/backgrounds/room_night.png"),("night",True,True,"images/backgrounds/room.png")]
        run Start("qa_story_lighting_room_day")
        pause until screen "say"
        $ story_lighting_test.missing_room_art(remove_preferred,remove_night_fallback)
        $ story_scene("room",light=light,cast=[],location="주인공 방")
        $ renpy.restart_interaction()
        pause 0.1
        assert eval story_light == light
        assert eval story_background_info("room",light)["dedicated_night"] == (light == "night" and not remove_night_fallback)
        assert eval story_background_info("room",light)["path"] == path
        assert eval (story_background_info("room",light)["tint"] is None) == (path != "images/backgrounds/room.png")
        assert eval path in story_lighting_test.files()

    testcase representative_old_day_default_with_night_location_migrates_on_load:
        run Start("qa_story_lighting_legacy_night")
        pause until screen "say"
        assert eval story_light == "day" and location_name.endswith("밤")
        assert eval "images/backgrounds/room.png" in story_lighting_test.files()
        run Function(renpy.save,"qa_lighting_legacy")
        run Function(renpy.load,"qa_lighting_legacy")
        pause until screen "say"
        # Synchronize to the actual loaded interaction, not merely the say
        # screen object that is already present in the restored SceneList.
        pause until eval story_light == "night" and story_lighting_test.ROOM_ART in story_lighting_test.files() timeout 1
        assert eval story_light == "night"
        assert eval story_lighting_test.ROOM_ART in story_lighting_test.files()
        assert eval not choice_log and not persistent.endings
        assert eval "story_lighting_restore_on_interact" not in renpy.session
        screenshot "legacy_night_location_restored.png"

    testcase actual_night_save_load:
        parameter kind = ["room","night_campus"]
        run Start("qa_story_lighting_"+kind)
        pause until screen "say"
        $ renpy._lighting_expected=story_lighting_test.state()
        run Function(renpy.save,"qa_lighting_night")
        $ story_scene("room",light="day",cast=[],location="주인공 방 · 낮")
        run Function(renpy.load,"qa_lighting_night")
        pause until screen "say"
        assert eval story_lighting_test.state() == renpy._lighting_expected
        assert eval story_light == "night"
        assert eval story_background_info(story_background,story_light)["path"] in story_lighting_test.files()
        screenshot f"{kind}_save_restored.png"

    testcase day_to_night_rollback_restores_room_art_and_time:
        run Start("qa_story_lighting_rollback")
        pause until screen "say"
        assert eval story_light == "day" and location_name.endswith("낮")
        assert eval story_lighting_test.ROOM_MORNING in story_lighting_test.files()
        advance
        pause until eval story_light == "night"
        assert eval location_name.endswith("밤") and story_lighting_test.ROOM_ART in story_lighting_test.files()
        keysym "K_PAGEUP"
        pause until eval story_light == "day"
        assert eval location_name.endswith("낮") and story_lighting_test.ROOM_MORNING in story_lighting_test.files()
        screenshot "night_rollback_to_day.png"

    testcase load_background_refresh_never_replaces_active_ld_or_sd:
        parameter kind = ["ld","sd"]
        run Start("qa_story_lighting_room")
        pause until screen "say"
        if eval kind == "ld":
            $ cg_start("ld_03",transition=0)
            $ renpy.restart_interaction()
            pause 0.1
            $ story_lighting_restore_after_load()
            assert eval cg_current == "ld_03" and cg_is_active()
            assert eval renpy.get_screen("ld_cg_view",layer="ld_cg") is not None
        else:
            $ sd_event_start("ch01_sia_omu_argument","01",transition=0)
            $ renpy.restart_interaction()
            pause 0.1
            $ story_lighting_restore_after_load()
            assert eval sd_event_current == "ch01_sia_omu_argument" and sd_event_variant_id == "01"
            assert eval renpy.get_screen("sd_event_view",layer="sd_events") is not None
        assert eval story_lighting_test.ROOM_ART in story_lighting_test.files()
        assert eval not story_cast and not choice_log
        screenshot f"{kind}_above_night_background.png"


label qa_story_lighting_room_day:
    $ story_begin_chapter(1,"밤 배경 검증")
    $ story_scene("room",light="day",cast=[],location="주인공 방 · 낮")
    narrator "시간대에 따른 방 배경을 확인하는 검증 위치입니다."
    jump qa_story_lighting_hold

label qa_story_lighting_room:
    $ story_begin_chapter(1,"밤 배경 검증")
    $ story_scene("room",light="night",cast=[],location="주인공 방 · 밤")
    narrator "창밖의 밤하늘과 따뜻한 실내 조명을 확인하는 검증 위치입니다."
    jump qa_story_lighting_hold

label qa_story_lighting_night_campus:
    $ story_begin_chapter(3,"밤 캠퍼스 검증")
    $ story_scene("night_campus",light="night",cast=[],location="캠퍼스 산책로 · 밤")
    narrator "캠퍼스의 밤하늘과 가로등을 확인하는 검증 위치입니다."
    jump qa_story_lighting_hold

label qa_story_lighting_legacy_night:
    $ story_begin_chapter(1,"이전 밤 저장 검증")
    $ story_scene("room",light="day",cast=[],location="주인공 방 · 밤")
    $ renpy.show("story_background", what=Transform("images/backgrounds/room.png", xysize=(1920,1080)), layer="master")
    narrator "새 시간대 필드가 없던 저장의 기본값을 모사한 검증 위치입니다."
    jump qa_story_lighting_hold

label qa_story_lighting_rollback:
    $ story_begin_chapter(1,"밤 배경 롤백 검증")
    $ story_scene("room",light="day",cast=[],location="주인공 방 · 낮")
    narrator "낮 장면입니다."
    $ story_scene("room",light="night",cast=[],location="주인공 방 · 밤")
    narrator "밤 장면입니다."
    jump qa_story_lighting_hold

label qa_story_lighting_hold:
    narrator "배경 검증을 위한 대사 위치입니다."
    jump qa_story_lighting_hold

