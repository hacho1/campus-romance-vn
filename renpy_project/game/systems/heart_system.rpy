# Canonical happy/bad gauges; old saved red/black names remain stable.
default red_hearts = {key: 0 for key in HEROINE_ORDER}
default black_hearts = {key: 0 for key in HEROINE_ORDER}
default heart_schema_version = 0
default heart_awarded_choices = {}
default heart_migration_archive = {}
default heart_migration_partial = False

init -19 python:
    import re
    import copy
    from collections.abc import Mapping, Sequence
    from renpy.revertable import RevertableDict
    from renpy.rollback import UnfreezeException as HeartLoadUnfreeze
    HEART_SCHEMA = 2
    HEART_RED = "#b53d59"
    HEART_BLACK = "#333344"
    HEART_TRACK = "#e3d8e2"
    # Compatibility-only counters never add points a second time.
    HEART_COUNTER_RULES = {
        "roman": {
            "red": ("roman_mutual_respect", "roman_mutual_understanding", "roman_creative_autonomy", "roman_relationship_balance"),
            "black": ("roman_unrealistic_promise", "roman_reassurance_dependency", "roman_approval_dependency", "roman_dependency_risk"),
        },
        "sia": {"red": (), "black": ()}, "darim": {"red": (), "black": ()},
        "omu": {"red": (), "black": ()}, "lumi": {"red": (), "black": ()},
    }
    HEART_CHOICE_RULES = {}
    for _heart_catalog in ("relationship_choices", "sia_relationship_choices", "omu_relationship_choices", "darim_relationship_choices", "harin_relationship_choices"):
        if renpy.loadable("data/" + _heart_catalog + ".json"):
            _heart_data = read_data(_heart_catalog)
            if _heart_data.get("schema") != 2 or _heart_data.get("unit") != 5:
                raise ValueError("호감도 자료는 schema2 / 5점 단위여야 합니다: " + _heart_catalog)
            for _heart_key, _heart_rule in _heart_data["choices"].items():
                if _heart_key in HEART_CHOICE_RULES:
                    raise ValueError("중복 선택지 호감도 ID: " + _heart_key)
                for _heart_kind in ("happy", "bad"):
                    for _heart_actor, _heart_points in _heart_rule.get(_heart_kind, {}).items():
                        if _heart_actor not in HEROINE_ORDER or type(_heart_points) is not int or _heart_points not in (0, 5, 10):
                            raise ValueError("선택지 호감도는 0/5/10만 허용됩니다: " + _heart_key)
                HEART_CHOICE_RULES[_heart_key] = _heart_rule

    def heart_actor(actor):
        return "lumi" if actor in ("lumi", "rumi", "harin") else actor

    def heart_clamp(value):
        return max(0, min(100, int(value) // 5 * 5))

    def heart_counter_units(actor, kind):
        return sum(max(0, getattr(store, key, 0)) for key in
            HEART_COUNTER_RULES.get(heart_actor(actor), {}).get(kind, ()))

    def heart_rebuild_history(history):
        happy = {actor: 0 for actor in HEROINE_ORDER}
        bad = {actor: 0 for actor in HEROINE_ORDER}
        awarded = {}
        unknown = []
        for choice_id in history or ():
            if not isinstance(choice_id, str) or choice_id in awarded:
                continue
            rule = HEART_CHOICE_RULES.get(choice_id)
            if rule is None:
                unknown.append(choice_id)
                continue
            awarded[choice_id] = True
            for kind, target in (("happy", happy), ("bad", bad)):
                for actor, points in rule.get(kind, {}).items():
                    actor = heart_actor(actor)
                    if actor in target:
                        target[actor] = heart_clamp(target[actor] + points)
        return happy, bad, awarded, unknown

    def heart_legacy_snapshot():
        # Never infer a relationship's meaning from affection/trust totals.
        happy, bad, _, _ = heart_rebuild_history(choice_log)
        return happy, bad

    def heart_migrate_save():
        if heart_schema_version >= HEART_SCHEMA:
            return
        if renpy.session.get("campus_heart_load_ready", False):
            # The native loader rewinds the previous checkpoint. Retain this
            # one-time conversion through the next save/load, while leaving
            # ordinary choice rollback available (no global rollback block).
            renpy.retain_after_load()
        prior = {
            "schema": heart_schema_version,
            "relationship_scale_version": relationship_scale_version,
            "affection": dict(affection), "trust": dict(trust),
            "red_hearts": dict(red_hearts), "black_hearts": dict(black_hearts),
            "choice_log": list(choice_log),
        }
        happy, bad, awarded, unknown = heart_rebuild_history(choice_log)
        unknown_choices = [key for key in unknown if not any(token in key for token in
            ("_flag_", "_complete", "_finished", "_entered"))]
        prior["unclassified_ids"] = unknown_choices
        prior["method"] = "reviewed_choice_history_only"
        has_old_totals = any(any(value for value in prior[name].values())
            for name in ("affection", "trust", "red_hearts", "black_hearts"))
        # Even a nonempty log can contain only progress markers, or omit older
        # choices. Old nonzero totals are archived and conservatively labelled
        # as reclassified; never present a guessed full reconstruction as fact.
        partial = bool(unknown_choices or has_old_totals)
        store.heart_migration_archive = RevertableDict(prior)
        store.red_hearts = RevertableDict(happy)
        store.black_hearts = RevertableDict(bad)
        store.heart_awarded_choices = RevertableDict(awarded)
        store.heart_migration_partial = partial
        store.heart_schema_version = HEART_SCHEMA
        heart_attach_saved_summary()

    def heart_attach_saved_summary():
        """Keep save-time totals apart from Ren'Py's rewound checkpoint.

        Only JSON metadata is read. It never initializes either new gauge.
        Old 5-point-scale compatibility dictionaries can be restored exactly;
        pre-scale raw checkpoint values are retained rather than guessed.
        """
        if not renpy.session.get("campus_heart_load_ready", False):
            return
        metadata = renpy.session.get("campus_heart_load_metadata") or {}
        summary = metadata.get("campus_hearts") or {}
        if not metadata or summary.get("version", 0) >= HEART_SCHEMA or not heart_migration_archive:
            return
        archive = store.heart_migration_archive
        archive["saved_slot_summary"] = copy.deepcopy(metadata)
        archive["resumed_choice_log"] = list(choice_log)
        _, _, _, unknown = heart_rebuild_history(choice_log)
        archive["unclassified_ids"] = list(dict.fromkeys(key for key in unknown
            if not any(token in key for token in ("_flag_", "_complete", "_finished", "_entered"))))
        if archive["unclassified_ids"]:
            store.heart_migration_partial = True
        old_scores = metadata.get("campus_relationship")
        if archive.get("relationship_scale_version", 0) >= 1 and isinstance(old_scores, Sequence) and len(old_scores) >= 2:
            for name, values in zip(("affection", "trust"), old_scores[:2]):
                if isinstance(values, Mapping) and all(type(value) is int for value in values.values()):
                    archive.setdefault("checkpoint_" + name, dict(archive.get(name, {})))
                    archive[name] = dict(values)
                    setattr(store, name, RevertableDict(values))
        for name, field in (("red_hearts", "red"), ("black_hearts", "black")):
            values = summary.get(field)
            if isinstance(values, Mapping):
                archive.setdefault("checkpoint_" + name, dict(archive.get(name, {})))
                archive[name] = dict(values)
        # Summary-only nonzero evidence also requires a reclassification notice.
        if any(any(value for value in (summary.get(kind) or {}).values()) for kind in ("red", "black")):
            store.heart_migration_partial = True

    def heart_loaded_summary_on_interact():
        if renpy.session.get("campus_heart_load_ready", False):
            heart_attach_saved_summary()
            renpy.session.pop("campus_heart_load_metadata", None)
            renpy.session.pop("campus_heart_load_ready", None)

    def heart_load_with_summary(filename):
        # A thin application bridge covers native FileLoad, QuickLoad and
        # Continue. The original signed-save loader/confirmation is untouched.
        try:
            metadata = renpy.slot_json(filename) or {}
        except Exception:
            metadata = {}
        if not isinstance(metadata, Mapping):
            metadata = {}
        renpy.session["campus_heart_load_metadata"] = copy.deepcopy({key: metadata[key]
            for key in ("_version", "campus_hearts", "campus_relationship") if key in metadata})
        renpy.session["campus_heart_load_ready"] = False
        try:
            result = _heart_original_load(filename)
        except HeartLoadUnfreeze:
            # Confirmation/signature prompts may interact before acceptance.
            # Only an accepted native load may consume the target metadata.
            renpy.session["campus_heart_load_ready"] = True
            raise
        except BaseException:
            renpy.session.pop("campus_heart_load_metadata", None)
            renpy.session.pop("campus_heart_load_ready", None)
            raise
        else:
            renpy.session.pop("campus_heart_load_metadata", None)
            renpy.session.pop("campus_heart_load_ready", None)
            return result

    def heart_apply_choice(affection_delta=None, trust_delta=None, counters=None, hearts=None, choice_id=None):
        """Literal reviewed points; legacy affection/trust/counters are ignored."""
        heart_migrate_save()
        if choice_id and choice_id in heart_awarded_choices:
            return []
        rule = HEART_CHOICE_RULES.get(choice_id)
        if rule is None:
            rule = {"happy": {}, "bad": {}}
            for actor, effect in (hearts or {}).items():
                actor = heart_actor(actor)
                if actor not in HEROINE_ORDER:
                    raise ValueError("알 수 없는 인물 호감도: " + str(actor))
                for kind, alias in (("happy", "red"), ("bad", "black")):
                    points = effect.get(kind, effect.get(alias, 0))
                    if type(points) is not int or points not in (-10, -5, 0, 5, 10):
                        raise ValueError("호감도 변화는 5점 또는 10점이어야 합니다.")
                    rule[kind][actor] = points
        feedback = []
        for kind, color, scores in (("happy", "red", red_hearts), ("bad", "black", black_hearts)):
            for actor, points in rule.get(kind, {}).items():
                actor = heart_actor(actor)
                before = heart_clamp(scores.get(actor, 0))
                after = heart_clamp(before + points)
                scores[actor] = after
                if after != before:
                    feedback.append((actor, color, after - before))
        if choice_id:
            store.heart_awarded_choices[choice_id] = True
        return feedback

    def heart_value(actor, kind="red"):
        relationship_migrate_save()
        return (black_hearts if kind in ("black", "bad") else red_hearts).get(heart_actor(actor), 0)

    def heart_route_scores(actor):
        # Cinematic cue compatibility only. Ending rules use literal points.
        return heart_value(actor, "bad") // 5, heart_value(actor, "happy") // 5

    def heart_risk_evidence(actor):
        actor = heart_actor(actor)
        choices = [key for key in heart_awarded_choices if
            HEART_CHOICE_RULES.get(key, {}).get("bad", {}).get(actor, 0) > 0]
        episodes = set()
        for key in choices:
            match = re.match(r"roman_(r\d+)_", key)
            if match:
                episodes.add(match.group(1))
        return len(choices), len(episodes)

    def heart_roman_ending(happy, bad, boundary, risk_count, risk_episodes):
        """All thresholds are literal points, plus repeated distinct actions.

        A healthy final answer cannot erase an established repeated pattern.
        Authored maximum before the final choice is 45 bad points, so 40 is
        reachable on the respect path. No single final choice forces a bad end.
        """
        repeated = risk_episodes >= 2
        if boundary == "respect":
            return "bad" if bad >= 40 and risk_count >= 5 and risk_episodes >= 3 else "happy"
        if boundary == "negotiate":
            serious = bad >= 40 and risk_count >= 4 and repeated
            unresolved = bad >= 30 and risk_count >= 4 and repeated and happy < 40
            return "bad" if serious or unresolved else "happy"
        if boundary == "surrender":
            established = bad >= 30 and risk_count >= 3 and repeated
            vulnerable = bad >= 20 and risk_count >= 3 and repeated and happy < 25
            return "bad" if established or vulnerable else "happy"
        # A legacy save with no recorded final decision must still load.
        return "happy"

    def heart_write_save_summary(metadata):
        if heart_schema_version >= HEART_SCHEMA:
            happy, bad, partial = dict(red_hearts), dict(black_hearts), heart_migration_partial
        else:
            happy, bad = heart_legacy_snapshot()
            partial = True
        metadata["campus_hearts"] = {"version": HEART_SCHEMA, "red": happy, "black": bad,
            "partial": partial, "route_flags": [flag for flag in event_flags if flag.endswith("_route_entered")]}

    def heart_profile_values():
        slot = renpy.newest_slot() if main_menu else None
        if not slot:
            return red_hearts, black_hearts, event_flags
        summary = (renpy.slot_json(slot) or {}).get("campus_hearts") or {}
        if summary.get("version", 0) < HEART_SCHEMA:
            return {}, {}, summary.get("route_flags", ())
        return summary.get("red", {}), summary.get("black", {}), summary.get("route_flags", ())

    def heart_profile_notice():
        slot = renpy.newest_slot() if main_menu else None
        if slot:
            summary = (renpy.slot_json(slot) or {}).get("campus_hearts") or {}
            if summary.get("version", 0) < HEART_SCHEMA:
                return "이전 저장을 불러오면 선택 기록을 기준으로 다시 확인합니다."
            partial = summary.get("partial", False)
        else:
            partial = heart_migration_partial
        return "이전 수치는 보관되어 있으며, 확인 가능한 선택만 반영했습니다." if partial else ""

    def heart_icon(kind, size=28):
        return Transform("images/ui/hearts/" + ("black" if kind in ("black", "bad") else "red") + ".svg", xysize=(size, size))

    config.save_json_callbacks.append(heart_write_save_summary)
    if not getattr(renpy.load, "_campus_heart_summary_bridge", False):
        _heart_original_load = renpy.load
        heart_load_with_summary._campus_heart_summary_bridge = True
        renpy.load = heart_load_with_summary
    config.start_interact_callbacks.append(heart_loaded_summary_on_interact)

