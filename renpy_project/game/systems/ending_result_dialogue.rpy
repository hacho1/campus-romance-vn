# Ending names share the ordinary dialogue window and the canonical title data.
# This read-only presentation cannot unlock an ending or alter relationship points.
init -3 python:
    def ending_result_title(ending_id):
        entry = ENDINGS.get(ending_id)
        if (not entry or not entry.get("implemented", False)
                or ending_id not in persistent.endings
                or entry.get("kind") not in ("happy", "bad")):
            return None
        prefix = "해피엔딩" if entry["kind"] == "happy" else "배드엔딩"
        return "{} <{}>".format(prefix, entry["title"])

label ending_result_dialogue(ending_id):
    $ _ending_result_message = ending_result_title(ending_id)
    if _ending_result_message:
        narrator "[_ending_result_message]"
    return
