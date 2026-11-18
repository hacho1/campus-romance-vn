# Sia endings use this playthrough's reviewed choices, never old trust or a
# cross-play persistent choice collection. Display gauges keep their global sum.
default sia_ending_evidence = {}
default sia_ending_path = None
default sia_s06_recovery_confirmed = False

init -3 python:
    import re as sia_policy_re

    SIA_S04_FINAL_CHOICES = {
        "sia_s04_choice03_a": "communicate",
        "sia_s04_choice03_b": "negotiate",
        "sia_s04_choice03_c": "dismiss",
    }
    SIA_S05_FINAL_CHOICES = {
        "sia_s05_choice03_a": "face_conflict",
        "sia_s05_choice03_b": "make_plan",
        "sia_s05_choice03_c": "minimize",
        "sia_s05_choice03_d": "withdraw",
    }
    SIA_S06_FINAL_CHOICES = {
        "sia_s06_choice01_a": "communicate",
        "sia_s06_choice01_b": "explain",
        "sia_s06_choice01_c": "minimize",
        "sia_s06_choice01_d": "withdraw",
    }

    def sia_relationship_evidence(history=None, reconciliation_attempted=None):
        """Return literal S01-S06 evidence; no score or story flag mutation.

        A completed current-playthrough menu is required. Flags alone, old
        aggregate gauges and persistent.choice_memories cannot invent bad acts.
        For a replayed menu, only its latest answer informs narrative memory.
        """
        current_play = history is None
        if current_play:
            heart_migrate_save()
            history = choice_log
        selected = {}
        unknown = []
        for choice_id in history or ():
            if not isinstance(choice_id, str):
                continue
            match = sia_policy_re.fullmatch(r"(sia_s0[1-6]_choice\d{2})_[a-d]", choice_id)
            if not match:
                continue
            if choice_id not in HEART_CHOICE_RULES:
                unknown.append(choice_id)
                continue
            if current_play and choice_id not in heart_awarded_choices:
                continue
            selected[match.group(1)] = choice_id
        choices = tuple(selected.values())
        happy = min(100, sum(HEART_CHOICE_RULES[key].get("happy", {}).get("sia", 0) for key in choices))
        bad = min(100, sum(HEART_CHOICE_RULES[key].get("bad", {}).get("sia", 0) for key in choices))
        risk = tuple(key for key in choices if HEART_CHOICE_RULES[key].get("bad", {}).get("sia", 0) > 0)
        s04 = SIA_S04_FINAL_CHOICES.get(selected.get("sia_s04_choice03"), "")
        s05 = SIA_S05_FINAL_CHOICES.get(selected.get("sia_s05_choice03"), "")
        s06 = SIA_S06_FINAL_CHOICES.get(selected.get("sia_s06_choice01"), "")
        if reconciliation_attempted is None:
            reconciliation_attempted = bool(getattr(store, "sia_s05_reconciliation_attempted", False))
        # The answer and its authored follow-through must both have happened.
        repaired = s05 in ("face_conflict", "make_plan") and bool(reconciliation_attempted)
        return {
            "schema": 1,
            "choices": choices,
            "happy": happy, "bad": bad,
            "risk_choices": risk,
            "risk_episodes": tuple(sorted(set(key.split("_")[1] for key in risk))),
            "s04_final": s04, "s05_final": s05, "s06_final": s06,
            "s05_repaired": repaired,
            "unknown_choices": tuple(sorted(set(unknown))),
        }

    def sia_ending_decision(evidence, final_choice=None):
        """Pure total decision: happy, bad, or the authored H05 recovery scene.

        Three unresolved 10-point decisions (S04, S05, S06) are the smallest
        proven repeated avoidance path. A repaired S05 is never undone by one
        later hesitant answer. A positive last answer without follow-through
        goes through the original H05 dialogue instead of erasing the past.
        """
        final = evidence.get("s06_final") or final_choice or ""
        prior_unresolved = (
            evidence.get("s04_final") == "dismiss" and
            evidence.get("s05_final") in ("minimize", "withdraw")
        )
        repaired = bool(evidence.get("s05_repaired"))
        if (final in ("minimize", "withdraw") and prior_unresolved and
                not repaired and evidence.get("bad", 0) >= 30):
            return "bad"
        if (final in ("communicate", "explain") and repaired and
                evidence.get("happy", 0) >= 30):
            return "happy"
        # Missing legacy/test history and intermediate states have a valid path.
        return "recover"

    def sia_evaluate_ending():
        evidence = sia_relationship_evidence()
        result = sia_ending_decision(evidence, getattr(store, "sia_s06_final_choice", ""))
        evidence["decision"] = result
        store.sia_ending_evidence = evidence
        store.sia_ending_path = result
        store.sia_s06_recovery_confirmed = False
        return result

    def sia_confirm_recovery():
        """Called only after the existing H05 mutual planning dialogue finishes.

        This records actual follow-through and never grants another 5/10 award,
        clears bad hearts, unlocks an ending early, or touches other heroines.
        """
        path = getattr(store, "sia_ending_path", "")
        if path not in ("happy", "recover"):
            return False
        evidence = dict(getattr(store, "sia_ending_evidence", {}))
        evidence["h05_completed"] = True
        evidence["decision_after_h05"] = "happy"
        store.sia_ending_evidence = evidence
        store.sia_s06_recovery_confirmed = True
        store.sia_ending_path = "happy"
        return True
