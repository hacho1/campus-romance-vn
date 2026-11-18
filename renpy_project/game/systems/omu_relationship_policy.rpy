# Omu 0.6.9: repeated invalidation and distorted memories affect the relationship;
# the exhibition succeeds and Omu remains alive in both authored endings.
default omu_ending_path = None
default omu_ending_evidence = {}
default omu_o06_recovery_confirmed = False

init -3 python:
    import re as omu_policy_re

    OMU_O04_BOUNDARY_CHOICES = {
        "omu_o04_choice03_a": "respect",
        "omu_o04_choice03_b": "communicate",
        "omu_o04_choice03_c": "invalidate_feelings",
    }
    OMU_O05_RELATIONSHIP_CHOICES = {
        "omu_o05_choice04_a": "support_autonomy",
        "omu_o05_choice04_b": "negotiate",
        "omu_o05_choice04_c": "reverse_blame",
        "omu_o05_choice04_d": "invalidate_and_blame",
    }
    OMU_O06_FINAL_CHOICES = {
        "omu_o06_choice01_a": "validate_feelings",
        "omu_o06_choice01_b": "verify_together",
        "omu_o06_choice01_c": "deny_memory",
        "omu_o06_choice01_d": "dismiss_emotion",
    }

    OMU_DISTORTION_CHOICES = {
        "omu_o04_choice02_c": ("omu_o04_schedule_response", "guilt_reframe"),
        "omu_o04_choice03_c": ("omu_o04_boundary_choice", "invalidate_feelings"),
        "omu_o05_choice03_c": ("omu_o05_online_permission", "misattribute_intent"),
        "omu_o05_choice04_c": ("omu_o05_relationship_choice", "reverse_blame"),
        "omu_o05_choice04_d": ("omu_o05_relationship_choice", "invalidate_and_blame"),
    }

    def omu_has_distortion_history():
        """A new-authored event must actually have happened in this save.

        Stable choice IDs retain their old award history, while old scalar values
        do not silently become the different 0.6.9 events or invented memories.
        """
        return any(getattr(store, name, None) == value
            for name, value in OMU_DISTORTION_CHOICES.values())

    def omu_relationship_evidence(history=None, conflict04=None, conflict05=None, conversation05=None):
        """Current-play O01-O06 plus Omu's own reviewed common-route points.

        Private/public photo tastes and art suggestions are not invented bad
        evidence. Old aggregate trust, persistent cross-play memories and other
        heroines' points never supply missing choices. For repeated menus only
        the latest answer describes the current narrative state.
        """
        current_play = history is None
        if current_play:
            heart_migrate_save()
            history = choice_log
        selected, common = {}, {}
        unknown = []
        for choice_id in history or ():
            if not isinstance(choice_id, str):
                continue
            match = omu_policy_re.fullmatch(r"(omu_o0[1-6]_choice\d{2})_[a-d]", choice_id)
            rule = HEART_CHOICE_RULES.get(choice_id)
            if rule is None:
                if match:
                    unknown.append(choice_id)
                continue
            if current_play and choice_id not in heart_awarded_choices:
                continue
            if match:
                selected[match.group(1)] = choice_id
            elif omu_policy_re.fullmatch(r"(?:LEGACY_)?CH0[1-7]", rule.get("chapter", "")):
                if rule.get("happy", {}).get("omu", 0) or rule.get("bad", {}).get("omu", 0):
                    common[choice_id] = True
        choices = tuple(selected.values())
        common_choices = tuple(common)
        route_happy = sum(HEART_CHOICE_RULES[key].get("happy", {}).get("omu", 0) for key in choices)
        route_bad = sum(HEART_CHOICE_RULES[key].get("bad", {}).get("omu", 0) for key in choices)
        common_happy = sum(HEART_CHOICE_RULES[key].get("happy", {}).get("omu", 0) for key in common_choices)
        common_bad = sum(HEART_CHOICE_RULES[key].get("bad", {}).get("omu", 0) for key in common_choices)
        risk = tuple(key for key in choices if HEART_CHOICE_RULES[key].get("bad", {}).get("omu", 0) > 0)
        o04 = OMU_O04_BOUNDARY_CHOICES.get(selected.get("omu_o04_choice03"), "")
        o05 = OMU_O05_RELATIONSHIP_CHOICES.get(selected.get("omu_o05_choice04"), "")
        o06 = OMU_O06_FINAL_CHOICES.get(selected.get("omu_o06_choice01"), "")
        distorted = tuple(key for key in choices if key in OMU_DISTORTION_CHOICES and
            (not current_play or getattr(store, OMU_DISTORTION_CHOICES[key][0], None) == OMU_DISTORTION_CHOICES[key][1]))
        if current_play:
            # A pre-revision save can contain the same menu IDs with old actions.
            # Preserve points and IDs, and keep new event memories unasserted.
            if o04 == "invalidate_feelings" and "omu_o04_choice03_c" not in distorted:
                o04 = "legacy_boundary_conflict"
            if o05 in ("reverse_blame", "invalidate_and_blame") and selected.get("omu_o05_choice04") not in distorted:
                o05 = "legacy_relationship_conflict"
            actual_final = getattr(store, "omu_o06_final_choice", None)
            if actual_final not in OMU_O06_FINAL_CHOICES.values():
                o06 = actual_final or ""
        if conflict04 is None:
            conflict04 = bool(getattr(store, "omu_o04_conflict_resolved", False))
        if conflict05 is None:
            conflict05 = bool(getattr(store, "omu_o05_conflict_resolved", False))
        if conversation05 is None:
            conversation05 = bool(getattr(store, "omu_o05_final_conversation_complete", False))
        repaired05 = (o05 in ("support_autonomy", "negotiate") and
            bool(conflict05) and bool(conversation05))
        return {
            "schema": 2,
            "choices": choices, "common_choices": common_choices,
            "raw_route_happy": route_happy, "raw_route_bad": route_bad,
            "raw_common_happy": common_happy, "raw_common_bad": common_bad,
            "happy": min(100, route_happy + common_happy),
            "bad": min(100, route_bad + common_bad),
            "risk_choices": risk,
            "risk_episodes": tuple(sorted(set(key.split("_")[1] for key in risk))),
            "distortion_choices": distorted,
            "distortion_episodes": tuple(sorted(set(key.split("_")[1] for key in distorted))),
            "o04_boundary": o04, "o05_relationship": o05, "o06_final": o06,
            "o04_resolved_flag": bool(conflict04),
            "o05_resolved_flag": bool(conflict05),
            "o05_conversation_complete": bool(conversation05),
            "o05_repaired": repaired05,
            "unknown_choices": tuple(sorted(set(unknown))),
        }

    def omu_ending_decision(evidence, final_choice=None):
        """Total decision from actual repeated O04/O05 events and the final answer.

        O04/O05/O06 can award at most 50 bad points. The lightest repeated
        distortion chain is O04 +10, O05 +5 and O06 +10 = 25. Requiring both
        prior episodes and an unresolved O05 prevents one lapse becoming BAD.
        Positive last answers with unresolved history require the entire original
        H05 mutual planning conversation before any ending is unlocked.
        """
        final = evidence.get("o06_final") or final_choice or ""
        distorted_episodes = evidence.get("distortion_episodes", ())
        prior_repeated = "o04" in distorted_episodes and "o05" in distorted_episodes
        unresolved = (not evidence.get("o05_resolved_flag", False) and
            not evidence.get("o05_repaired", False))
        if (final in ("deny_memory", "dismiss_emotion") and prior_repeated and
                unresolved and evidence.get("bad", 0) >= 25):
            return "bad"
        if (final in ("validate_feelings", "verify_together") and
                evidence.get("o05_repaired", False) and evidence.get("happy", 0) >= 30):
            return "happy"
        return "recover"

    def omu_evaluate_ending():
        evidence = omu_relationship_evidence()
        result = omu_ending_decision(evidence, getattr(store, "omu_o06_final_choice", ""))
        evidence["decision"] = result
        store.omu_ending_evidence = evidence
        store.omu_ending_path = result
        store.omu_o06_recovery_confirmed = False
        return result

    def omu_confirm_recovery():
        """Only after original H05 both-person future planning has completed.

        Records actual follow-through without another reward, score decrease,
        premature ending unlock, or any invented consent to publish a photo.
        """
        path = getattr(store, "omu_ending_path", "")
        if path not in ("happy", "recover"):
            return False
        evidence = dict(getattr(store, "omu_ending_evidence", {}))
        evidence["h05_completed"] = True
        evidence["decision_after_h05"] = "happy"
        store.omu_ending_evidence = evidence
        store.omu_o06_recovery_confirmed = True
        store.omu_ending_path = "happy"
        return True
