# Darim's autonomy/conflict evidence uses actual choices in this playthrough.
# The canonical gauges remain the existing independent red/black heart system.
default darim_ending_path = None
default darim_ending_evidence = {}
default darim_d06_recovery_confirmed = False

init -3 python:
    import re as darim_policy_re

    DARIM_D04_BOUNDARY_CHOICES = {
        "darim_d04_choice03_a": "acknowledge",
        "darim_d04_choice03_b": "ask_first",
        "darim_d04_choice03_c": "take_control",
        "darim_d04_choice03_d": "dismiss_feelings",
    }
    DARIM_D05_PERMISSION_CHOICES = {
        "darim_d05_choice03_a": "respect",
        "darim_d05_choice03_b": "negotiate",
        "darim_d05_choice03_c": "insist_accompany",
        "darim_d05_choice03_d": "demand_approval",
    }
    DARIM_D05_FINAL_CHOICES = {
        "darim_d05_choice04_a": "acknowledge_control",
        "darim_d05_choice04_b": "manage_worry",
        "darim_d05_choice04_c": "justify_control",
        "darim_d05_choice04_d": "emotional_pressure",
    }
    DARIM_D06_FINAL_CHOICES = {
        "darim_d06_choice02_a": "respect_autonomy",
        "darim_d06_choice02_b": "communicate_worry",
        "darim_d06_choice02_c": "justify_control",
        "darim_d06_choice02_d": "guilt_pressure",
    }

    def darim_relationship_evidence(history=None, conflict04=None, conflict05=None, conversation05=None):
        """Only Darim's reviewed choices, with actual conflict-resolution flags.

        Legacy aggregate affection/trust and cross-play persistent collections
        cannot reconstruct missing behaviour. A repeated menu describes the
        latest answer. Neutral tastes/public safety inquiries are not control.
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
            match = darim_policy_re.fullmatch(r"(darim_d0[1-6]_choice\d{2})_[a-d]", choice_id)
            rule = HEART_CHOICE_RULES.get(choice_id)
            if rule is None:
                if match:
                    unknown.append(choice_id)
                continue
            if current_play and choice_id not in heart_awarded_choices:
                continue
            if match:
                selected[match.group(1)] = choice_id
            elif darim_policy_re.fullmatch(r"(?:LEGACY_)?CH0[1-7]", rule.get("chapter", "")):
                if rule.get("happy", {}).get("darim", 0) or rule.get("bad", {}).get("darim", 0):
                    common[choice_id] = True
        choices = tuple(selected.values())
        common_choices = tuple(common)
        route_happy = sum(HEART_CHOICE_RULES[key].get("happy", {}).get("darim", 0) for key in choices)
        route_bad = sum(HEART_CHOICE_RULES[key].get("bad", {}).get("darim", 0) for key in choices)
        common_happy = sum(HEART_CHOICE_RULES[key].get("happy", {}).get("darim", 0) for key in common_choices)
        common_bad = sum(HEART_CHOICE_RULES[key].get("bad", {}).get("darim", 0) for key in common_choices)
        risk = tuple(key for key in choices if HEART_CHOICE_RULES[key].get("bad", {}).get("darim", 0) > 0)
        d04 = DARIM_D04_BOUNDARY_CHOICES.get(selected.get("darim_d04_choice03"), "")
        d05_permission = DARIM_D05_PERMISSION_CHOICES.get(selected.get("darim_d05_choice03"), "")
        d05_final = DARIM_D05_FINAL_CHOICES.get(selected.get("darim_d05_choice04"), "")
        d06 = DARIM_D06_FINAL_CHOICES.get(selected.get("darim_d06_choice02"), "")
        if conflict04 is None:
            conflict04 = bool(getattr(store, "darim_d04_conflict_resolved", False))
        if conflict05 is None:
            conflict05 = bool(getattr(store, "darim_d05_conflict_resolved", False))
        if conversation05 is None:
            conversation05 = bool(getattr(store, "darim_d05_final_conversation_complete", False))
        repaired05 = (d05_final in ("acknowledge_control", "manage_worry") and
            bool(conflict05) and bool(conversation05))
        return {
            "schema": 1, "choices": choices, "common_choices": common_choices,
            "raw_route_happy": route_happy, "raw_route_bad": route_bad,
            "raw_common_happy": common_happy, "raw_common_bad": common_bad,
            "happy": min(100, route_happy + common_happy),
            "bad": min(100, route_bad + common_bad),
            "risk_choices": risk,
            "risk_episodes": tuple(sorted(set(key.split("_")[1] for key in risk))),
            "d04_boundary": d04, "d05_permission": d05_permission,
            "d05_final": d05_final, "d06_final": d06,
            "d04_resolved_flag": bool(conflict04),
            "d05_resolved_flag": bool(conflict05),
            "d05_conversation_complete": bool(conversation05),
            "d05_repaired": repaired05,
            "unknown_choices": tuple(sorted(set(unknown))),
        }

    def darim_ending_decision(evidence, final_choice=None):
        """D06's total happy/bad/mixed decision, grounded in repeated actions.

        Three actual major ten-point controlling answers are needed for bad:
        unresolved D05 and the final answer, preceded by unresolved D04 or
        D05's unwanted accompaniment/approval demand. One bad final answer
        cannot erase a repaired relationship. Mixed states must perform the
        original H05 mutual scheduling and respect for refusal before happy.
        """
        final = evidence.get("d06_final") or final_choice or ""
        repeated_control = (
            (evidence.get("d04_boundary") in ("take_control", "dismiss_feelings") and
             not evidence.get("d04_resolved_flag", False)) or
            evidence.get("d05_permission") in ("insist_accompany", "demand_approval")
        )
        unresolved05 = (evidence.get("d05_final") in ("justify_control", "emotional_pressure") and
            not evidence.get("d05_resolved_flag", False))
        if (final in ("justify_control", "guilt_pressure") and repeated_control and
                unresolved05 and not evidence.get("d05_repaired", False) and evidence.get("bad", 0) >= 30):
            return "bad"
        if (final in ("respect_autonomy", "communicate_worry") and
                evidence.get("d05_repaired", False) and evidence.get("happy", 0) >= 30):
            return "happy"
        return "recover"

    def darim_evaluate_ending():
        evidence = darim_relationship_evidence()
        result = darim_ending_decision(evidence, getattr(store, "darim_d06_final_choice", ""))
        evidence["decision"] = result
        store.darim_ending_evidence = evidence
        store.darim_ending_path = result
        store.darim_d06_recovery_confirmed = False
        return result

    def darim_confirm_recovery():
        """At original H05 end only; no extra points or rewritten old choices."""
        path = getattr(store, "darim_ending_path", "")
        if path not in ("happy", "recover") or not getattr(store, "darim_d06_mutual_schedule", False):
            return False
        evidence = dict(getattr(store, "darim_ending_evidence", {}))
        evidence["h05_completed"] = True
        evidence["mutual_schedule_confirmed"] = True
        evidence["decision_after_h05"] = "happy"
        store.darim_ending_evidence = evidence
        store.darim_d06_recovery_confirmed = True
        store.darim_ending_path = "happy"
        return True
