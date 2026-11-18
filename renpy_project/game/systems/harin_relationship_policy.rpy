# Harin's authored H04/H05 idealization conflict, using the canonical actor lumi.
# Source: design_docs/story_sources/harin_h06.txt L1054-L1076 requires cumulative
# actions, acknowledged repair and the final answer; no threshold is authored.
# Reviewed implementation: three unresolved major 10-point answers (30) for BAD.
# H06 SC05-H L1135-L1258 supplies the actual apology, mutual communication and
# respect for refusal used by the mixed-path repair hook. No new prose/points.
default harin_ending_path = None
default harin_ending_evidence = {}
default harin_h06_recovery_confirmed = False

init -3 python:
    import re as harin_policy_re

    HARIN_H04_BOUNDARY_CHOICES = {
        "harin_h04_choice03_a": "acknowledge_idealization",
        "harin_h04_choice03_b": "respect_difference",
        "harin_h04_choice03_c": "preserve_ideal",
        "harin_h04_choice03_d": "deny_real_self",
    }
    HARIN_H05_IDENTITY_CHOICES = {
        "harin_h05_choice02_a": "accept_whole_self",
        "harin_h05_choice02_b": "respect_difference",
        "harin_h05_choice02_c": "preserve_ideal",
        "harin_h05_choice02_d": "conditional_affection",
    }
    HARIN_H06_FINAL_CHOICES = {
        "harin_h06_choice02_a": "love_real_harin",
        "harin_h06_choice02_b": "respect_differences",
        "harin_h06_choice02_c": "love_ideal_only",
        "harin_h06_choice02_d": "conditional_affection",
    }

    def harin_relationship_evidence(history=None, conflict04=None,
            conflict05=None, conversation05=None):
        """Only actual current-play Harin choices and lumi's common points.

        Aggregate trust, persistent clears and other heroines' scores cannot
        manufacture missing behaviour. Repeated menus use their latest answer.
        Supplying history explicitly is a pure-policy audit seam, not save state.
        """
        current_play = history is None
        if current_play:
            heart_migrate_save()
            history = choice_log
        selected, common, unknown = {}, {}, []
        for choice_id in history or ():
            if not isinstance(choice_id, str):
                continue
            match = harin_policy_re.fullmatch(r"(harin_h0[1-6]_choice\d{2})_[a-d]", choice_id)
            rule = HEART_CHOICE_RULES.get(choice_id)
            if rule is None:
                if match:
                    unknown.append(choice_id)
                continue
            if current_play and choice_id not in heart_awarded_choices:
                continue
            if match:
                selected[match.group(1)] = choice_id
            elif harin_policy_re.fullmatch(r"(?:LEGACY_)?CH0[1-7]", rule.get("chapter", "")):
                if rule.get("happy", {}).get("lumi", 0) or rule.get("bad", {}).get("lumi", 0):
                    common[choice_id] = True
        choices, common_choices = tuple(selected.values()), tuple(common)
        route_happy = sum(HEART_CHOICE_RULES[key].get("happy", {}).get("lumi", 0) for key in choices)
        route_bad = sum(HEART_CHOICE_RULES[key].get("bad", {}).get("lumi", 0) for key in choices)
        common_happy = sum(HEART_CHOICE_RULES[key].get("happy", {}).get("lumi", 0) for key in common_choices)
        common_bad = sum(HEART_CHOICE_RULES[key].get("bad", {}).get("lumi", 0) for key in common_choices)
        risk = tuple(key for key in choices if HEART_CHOICE_RULES[key].get("bad", {}).get("lumi", 0) > 0)
        h04 = HARIN_H04_BOUNDARY_CHOICES.get(selected.get("harin_h04_choice03"), "")
        h05 = HARIN_H05_IDENTITY_CHOICES.get(selected.get("harin_h05_choice02"), "")
        h06 = HARIN_H06_FINAL_CHOICES.get(selected.get("harin_h06_choice02"), "")
        if conflict04 is None:
            conflict04 = bool(getattr(store, "harin_h04_conflict_resolved", False))
        if conflict05 is None:
            conflict05 = bool(getattr(store, "harin_h05_conflict_resolved", False))
        if conversation05 is None:
            conversation05 = bool(getattr(store, "harin_h05_identity_confrontation_complete", False))
        repaired05 = (h05 in ("accept_whole_self", "respect_difference")
            and bool(conflict05) and bool(conversation05))
        return {
            "schema": 1, "choices": choices, "common_choices": common_choices,
            "raw_route_happy": route_happy, "raw_route_bad": route_bad,
            "raw_common_happy": common_happy, "raw_common_bad": common_bad,
            "happy": min(100, route_happy + common_happy),
            "bad": min(100, route_bad + common_bad),
            "risk_choices": risk,
            "risk_episodes": tuple(sorted(set(key.split("_")[1] for key in risk))),
            "h04_boundary": h04, "h05_identity": h05, "h06_final": h06,
            "h04_resolved_flag": bool(conflict04),
            "h05_resolved_flag": bool(conflict05),
            "h05_conversation_complete": bool(conversation05),
            "h05_repaired": repaired05,
            "unknown_choices": tuple(sorted(set(unknown))),
        }

    def harin_ending_decision(evidence, final_choice=None):
        """A single lapse/taste difference never causes BAD or erases repair.

        H04's explicit refusal of her real self, H05's renewed condition on her
        identity and H06's final demand must all remain unresolved (10+10+10).
        A positive last sentence cannot alone repair that earlier history:
        mixed states must complete the original SC05-H conversation first.
        """
        final = evidence.get("h06_final") or final_choice or ""
        repeated04 = (evidence.get("h04_boundary") in ("preserve_ideal", "deny_real_self")
            and not evidence.get("h04_resolved_flag", False))
        unresolved05 = (evidence.get("h05_identity") in ("preserve_ideal", "conditional_affection")
            and not evidence.get("h05_resolved_flag", False)
            and not evidence.get("h05_repaired", False))
        if (final in ("love_ideal_only", "conditional_affection")
                and repeated04 and unresolved05 and evidence.get("bad", 0) >= 30):
            return "bad"
        if (final in ("love_real_harin", "respect_differences")
                and evidence.get("h05_repaired", False) and evidence.get("happy", 0) >= 30):
            return "happy"
        return "recover"

    def harin_evaluate_ending():
        evidence = harin_relationship_evidence()
        result = harin_ending_decision(evidence, getattr(store, "harin_h06_final_choice", ""))
        evidence["decision"] = result
        store.harin_ending_evidence = evidence
        store.harin_ending_path = result
        store.harin_h06_recovery_confirmed = False
        return result

    def harin_confirm_recovery():
        """Called only after original H06 SC05-H's full repair conversation.

        Reaching its authored agreement is the evidence; this adds no score,
        changes no recorded answer, and does not erase earlier black hearts.
        """
        if (getattr(store, "harin_ending_path", None) not in ("happy", "recover")
                or getattr(store, "story_chapter_number", None) != 506):
            return False
        evidence = dict(getattr(store, "harin_ending_evidence", {}))
        if evidence.get("h06_final") not in HARIN_H06_FINAL_CHOICES.values():
            return False
        evidence["h05_completed"] = True
        evidence["mutual_communication_confirmed"] = True
        evidence["decision_after_h05"] = "happy"
        store.harin_ending_evidence = evidence
        store.harin_h06_recovery_confirmed = True
        store.harin_ending_path = "happy"
        return True

    def harin_happy_completion_allowed():
        evidence = getattr(store, "harin_ending_evidence", {})
        return (getattr(store, "harin_ending_path", None) == "happy"
            and bool(getattr(store, "harin_h06_recovery_confirmed", False))
            and bool(evidence.get("mutual_communication_confirmed", False))
            and bool(getattr(store, "harin_happy_end_complete", False)))

    def harin_bad_completion_allowed():
        evidence = getattr(store, "harin_ending_evidence", {})
        return (getattr(store, "harin_ending_path", None) == "bad"
            and evidence.get("decision") == "bad"
            and harin_ending_decision(evidence) == "bad"
            and bool(getattr(store, "harin_bad_end_complete", False)))
