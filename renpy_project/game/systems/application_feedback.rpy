# Application-only name submission and ephemeral relationship feedback.
# State stays in the rollback store; no persistent collection is written here.
default application_input_active = False
default application_pending_name = "나"
default relationship_feedback_items = []
default relationship_feedback_choice = None
default relationship_feedback_serial = 0
default relationship_feedback_expires = 0.0

init -6 python:
    from renpy.revertable import RevertableDict, RevertableList

    def relationship_feedback_clear(token=None):
        if token is not None and token != relationship_feedback_serial:
            return
        store.relationship_feedback_items = RevertableList()
        store.relationship_feedback_choice = None
        store.relationship_feedback_expires = 0.0
        renpy.hide_screen("relationship_feedback_view")
        renpy.restart_interaction()

    def relationship_feedback_publish(choice_id, changes):
        # This is called only by actual choice-effect execution, never a screen.
        if renpy.predicting():
            return
        grouped = {}
        for actor, kind, delta in changes:
            actor = story_id(actor)
            if kind not in ("red", "black") or not delta:
                continue
            if actor not in grouped:
                grouped[actor] = {"actor":actor, "name":HEROINES.get(actor, {}).get("name", actor),
                    "red":0, "black":0}
            grouped[actor][kind] += delta
        ordered = [actor for actor in HEROINE_ORDER if actor in grouped]
        ordered += sorted(actor for actor in grouped if actor not in HEROINE_ORDER)
        items = [RevertableDict(grouped[actor]) for actor in ordered
            if grouped[actor]["red"] or grouped[actor]["black"]]
        if not items:
            relationship_feedback_clear()
            return
        store.relationship_feedback_serial += 1
        store.relationship_feedback_items = RevertableList(items)
        store.relationship_feedback_choice = choice_id
        store.relationship_feedback_expires = renpy.get_game_runtime() + 2.2
        # A helper can run while a say interaction is already open (actions,
        # native tests, or script UI). Rebuild the visible screen immediately.
        renpy.show_screen("relationship_feedback_view")
        renpy.restart_interaction()

    def relationship_feedback_tick():
        if relationship_feedback_items and renpy.get_game_runtime() >= relationship_feedback_expires:
            relationship_feedback_clear(relationship_feedback_serial)

    def relationship_feedback_will_load():
        # A load restores rollback-store notification data before its first
        # interaction. Keep only this pending UI reset outside that rollback.
        renpy.session["application_feedback_clear_on_interact"] = True

    def relationship_feedback_resume_interact():
        if renpy.session.pop("application_feedback_clear_on_interact", False):
            relationship_feedback_clear()

    if "relationship_feedback_view" not in config.overlay_screens:
        config.overlay_screens.append("relationship_feedback_view")
    if relationship_feedback_clear not in config.after_load_callbacks:
        config.after_load_callbacks.append(relationship_feedback_clear)
    if relationship_feedback_will_load not in config.before_load_callbacks:
        config.before_load_callbacks.append(relationship_feedback_will_load)
    # Clear again at the actual resume boundary: the displayed say screen may
    # already be restored before the native _after_load script has finished.
    if relationship_feedback_resume_interact not in config.start_interact_callbacks:
        config.start_interact_callbacks.append(relationship_feedback_resume_interact)

label application_name_input:
    $ application_input_active = True
    $ application_pending_name = clean_name(renpy.input("프로젝트에서 사용할 이름을 입력해 주세요.", default="", length=12))
    $ application_input_active = False
    # Both Enter and the form button return from the same native input above.
    call screen application_send_animation
    with Dissolve(0.22)
    return application_pending_name
