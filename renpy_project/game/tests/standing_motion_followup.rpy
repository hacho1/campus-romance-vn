# Focused standing presentation regressions. No story route or relationship edits.
# Run with an isolated CAMPUS_SAVE_DIR. All fixtures are excluded from builds.
init python in standing_test:
    def transform_for(actor, function):
        screen = renpy.get_screen("story_stage_view")
        if screen is None:
            return None
        found = []
        def visit(displayable):
            callback = getattr(displayable,"function",None)
            if getattr(callback,"func",None) is function and getattr(callback,"args",())[:1] == (actor,):
                found.append(displayable)
        screen.visit_all(visit)
        return found[-1] if found else None

    def focus(actor):
        return transform_for(actor,renpy.store.story_focus_transform)

    def motion(actor):
        return transform_for(actor,renpy.store.story_actor_motion_transform)

    def assert_focus(speaker, actors=("roman","sia")):
        for actor in actors:
            transform = focus(actor)
            assert transform is not None, actor
            assert transform.alpha == 1.0, (actor,transform.alpha)
            brightness = getattr(transform.matrixcolor,"value",None)
            if speaker is None or len(actors)<2:
                assert abs(transform.zoom-1.0)<0.001 and brightness == 0.0, (actor,transform.zoom,brightness)
            elif actor == speaker:
                assert abs(transform.zoom-1.0)<0.001 and brightness>0, (actor,transform.zoom,brightness)
            else:
                assert abs(transform.zoom-1.0)<0.001 and brightness<0, (actor,transform.zoom,brightness)


testsuite standing_motion_followup:
    setup:
        python:
            import os
            assert os.environ.get("CAMPUS_SAVE_DIR")
            assert os.path.normcase(os.path.abspath(config.savedir)) == os.path.normcase(os.path.abspath(os.environ["CAMPUS_SAVE_DIR"]))
            assert os.path.normcase(os.path.abspath(config.savedir)) != os.path.normcase(os.path.join(config.basedir,"saves"))
        $ _test.timeout = 15.0
        $ _test.transition_timeout = 0.02
        $ _test.screenshot_directory = "D:/CampusRomance_VN/tests/standing-motion-screenshots"
        $ _preferences.text_cps = 0
        $ _preferences.afm_enable = False
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        $ _preferences.transitions = 2
    teardown:
        exit

    testcase speaker_changes_and_same_speaker_continuity:
        run Start("qa_standing_focus")
        pause until screen "say"
        pause 0.22
        $ standing_test.assert_focus("roman")
        $ renpy._standing_focus_before = (story_focus_serial,story_focus_started)
        screenshot "focus_roman.png"
        advance
        assert eval (story_focus_serial,story_focus_started) == renpy._standing_focus_before
        $ standing_test.assert_focus("roman")
        advance
        pause 0.22
        assert eval story_focus_actor == "sia" and story_focus_serial == renpy._standing_focus_before[0]+1
        $ standing_test.assert_focus("sia")
        screenshot "focus_sia.png"
        advance
        pause 0.22
        assert eval story_focus_actor is None
        $ standing_test.assert_focus(None)
        $ renpy._standing_offcast_serial = story_focus_serial
        screenshot "focus_narrator_neutral.png"
        advance
        pause 0.1
        assert eval story_focus_actor is None and story_focus_serial == renpy._standing_offcast_serial
        $ standing_test.assert_focus(None)

    testcase single_actor_stays_neutral:
        run Start("qa_standing_single")
        pause until screen "say"
        pause 0.22
        assert eval story_cast == ["roman"] and story_focus_actor is None
        $ standing_test.assert_focus(None,("roman",))
        screenshot "focus_single_neutral.png"

    testcase jump_shake_do_not_restart_on_next_line:
        run Start("qa_standing_focus")
        pause until screen "say"
        run Function(story_effect,"jump","roman")
        pause until eval standing_test.motion("roman") is not None and standing_test.motion("roman").yoffset < -1 timeout 1
        $ renpy._standing_motion_before = (story_effects["roman"],story_effect_times["roman"])
        screenshot "motion_jump.png"
        advance
        assert eval (story_effects["roman"],story_effect_times["roman"]) == renpy._standing_motion_before
        pause 0.30
        assert eval abs(standing_test.motion("roman").yoffset)<0.01
        run Function(story_effect,"shake","sia")
        pause until eval standing_test.motion("sia") is not None and abs(standing_test.motion("sia").xoffset)>0.5 timeout 1
        screenshot "motion_shake.png"
        pause 0.25
        assert eval abs(standing_test.motion("sia").xoffset)<0.01

    testcase horizontal_entry_exit_cleanup:
        run Start("qa_standing_single")
        pause until screen "say"
        run Function(story_enter,"sia","right",position=(1310,795))
        pause until eval standing_test.motion("sia") is not None and standing_test.motion("sia").xoffset>30 timeout 1
        assert eval story_cast == ["roman","sia"] and len(story_render_entries())<=3
        screenshot "slide_enter_right.png"
        pause 0.33
        assert eval abs(standing_test.motion("sia").xoffset)<0.01 and story_positions["sia"] == (1310,795)
        run Function(story_exit,"roman","left")
        assert eval "roman" not in story_cast
        pause until eval standing_test.motion("roman") is not None and standing_test.motion("roman").xoffset < -30 timeout 1
        screenshot "slide_exit_left.png"
        pause 0.33
        assert eval not story_exiting and "roman" not in story_cast
        assert eval renpy.get_widget("story_stage_view","standing_actor_roman") is None
        assert eval len(story_render_entries())<=3

    testcase short_reaction_icon:
        parameter icon = ["heart","exclamation","lightbulb"]
        run Start("qa_standing_focus")
        pause until screen "say"
        run Function(story_icon,"roman",icon)
        pause 0.08
        assert eval renpy.loadable("images/ui/stage_effects/"+icon+".svg")
        assert eval renpy.get_widget("story_stage_view","standing_icon_roman") is not None
        screenshot f"reaction_{icon}.png"
        pause 1.0
        assert eval not story_reaction_icons and renpy.get_widget("story_stage_view","standing_icon_roman") is None

    testcase load_settles_transient_effects_without_ghost:
        run Start("qa_standing_save_exit")
        pause until screen "say"
        assert eval story_cast == ["sia"] and "roman" in story_exiting
        $ renpy._standing_saved_pose = (dict(story_positions),dict(story_facing),story_effects["sia"],dict(affection),dict(trust),list(choice_log))
        run FileSave("standing",page="12",confirm=False)
        assert eval renpy.can_load("12-standing")
        run Function(story_enter,"roman","right")
        run Function(story_effect,"jump","sia")
        run FileLoad("standing",page="12",confirm=False)
        pause until screen "say"
        pause until eval not story_exiting and not story_reaction_icons and story_effect_settled.get("sia") == story_effects["sia"][1] timeout 2
        assert eval story_cast == ["sia"] and renpy.get_widget("story_stage_view","standing_actor_roman") is None
        assert eval (dict(story_positions),dict(story_facing),story_effects["sia"],dict(affection),dict(trust),list(choice_log)) == renpy._standing_saved_pose
        pause 0.1
        assert eval abs(standing_test.motion("sia").xoffset)<0.01 and abs(standing_test.motion("sia").yoffset)<0.01
        screenshot "load_no_replayed_effect_or_exit_ghost.png"

    testcase rollback_exit_and_replay_cleanup:
        run Start("qa_standing_rollback")
        pause until screen "say"
        assert eval story_cast == ["roman","sia"]
        advance
        pause 0.33
        assert eval story_cast == ["roman"] and not story_exiting
        run Rollback(force=True,checkpoints=1)
        pause until eval story_cast == ["roman","sia"] timeout 2
        assert eval not story_exiting
        assert eval renpy.get_widget("story_stage_view","standing_actor_sia") is not None
        advance
        pause 0.33
        assert eval story_cast == ["roman"] and not story_exiting
        assert eval renpy.get_widget("story_stage_view","standing_actor_sia") is None
        screenshot "rollback_replayed_exit_settled.png"

    testcase whole_cut_never_composes_standing_actors:
        parameter cut = ["sd","ld"]
        run Start("qa_standing_focus")
        pause until screen "say"
        if eval cut == "sd":
            run Function(sd_event_start,"ch02_rival_introduction","02",transition=0)
        else:
            run Function(cg_start,"ld_08",transition=0)
        pause 0.1
        assert eval story_cast == [] and not story_effects
        assert eval renpy.get_widget("story_stage_view","standing_actor_roman") is None
        python:
            assert not story_enter("roman","left")
            assert not story_exit("sia","right")
            assert not story_icon("roman","heart")
            story_effect("jump","roman")
            story_move("sia",300,795)
            assert not story_cast and not story_effects
        screenshot f"{cut}_no_standing_composition.png"

    testcase reduced_motion_commits_final_state:
        $ _preferences.transitions = 0
        run Start("qa_standing_focus")
        pause until screen "say"
        run Function(story_effect,"jump","roman")
        run Function(story_enter,"lumi","right")
        pause 0.08
        assert eval abs(standing_test.motion("roman").yoffset)<0.01 and abs(standing_test.motion("lumi").xoffset)<0.01
        run Function(story_exit,"lumi","right")
        pause 0.08
        assert eval "lumi" not in story_cast and not story_exiting
        $ standing_test.assert_focus("roman")
        screenshot "reduced_motion_final_state.png"

    testcase developer_live_preview:
        enabled config.developer
        run Start("standing_motion_preview")
        advance until screen "standing_motion_demo_controls" timeout 20
        assert eval story_cast == ["roman","sia"] and not sd_event_is_active() and not cg_is_active()
        screenshot "standing_live_preview_controls.png"
        click "전구"
        assert screen "standing_motion_demo_controls"
        assert eval story_reaction_icons.get("roman")[0] == "lightbulb"
        click "왼쪽 퇴장"
        assert screen "standing_motion_demo_controls"
        assert eval "roman" not in story_cast
        click "왼쪽 입장"
        assert screen "standing_motion_demo_controls"
        assert eval "roman" in story_cast
        click "시연 끝내기"
        pause until screen "main_menu" timeout 5
        assert screen "main_menu"


label qa_standing_focus:
    $ story_begin_chapter(0,"스탠딩 강조 검증")
    $ story_scene("clubroom",mode="normal",cast=["roman","sia"])
    roman "첫 번째 로만 대사입니다."
    roman "같은 화자의 두 번째 대사입니다."
    sia "이제 시아의 차례입니다."
    narrator "해설은 어느 인물도 강조하지 않습니다."
    mc "화면 밖의 목소리도 모두 기본 상태입니다."
    jump qa_standing_hold

label qa_standing_single:
    $ story_begin_chapter(0,"한 명의 스탠딩 검증")
    $ story_scene("clubroom",mode="normal",cast=["roman"])
    $ story_stage(positions={"roman":(610,795)})
    roman "혼자일 때는 기본 크기를 유지합니다."
    jump qa_standing_hold

label qa_standing_save_exit:
    $ story_begin_chapter(0,"스탠딩 저장 검증")
    $ story_scene("clubroom",mode="normal",cast=["roman","sia"])
    $ story_stage(positions={"roman":(610,795),"sia":(1310,795)},facing={"roman":1,"sia":-1})
    $ story_effect("shake","sia")
    $ story_icon("sia","heart")
    $ story_exit("roman","left")
    sia "이 대사의 저장은 퇴장자와 짧은 효과를 다시 재생하지 않습니다."
    jump qa_standing_hold

label qa_standing_rollback:
    $ story_begin_chapter(0,"스탠딩 롤백 검증")
    $ story_scene("clubroom",mode="normal",cast=["roman","sia"])
    roman "이 대사에는 두 사람이 있습니다."
    $ story_exit("sia","right")
    roman "이 대사에는 로만만 남습니다."
    jump qa_standing_hold

label qa_standing_hold:
    mc "스탠딩 검증 대기 장면입니다."
    jump qa_standing_hold
