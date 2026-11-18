# Edit data/sd_events.json to replace a whole illustration or add variants.
init -12 python:
    _sd_event_data = read_data("sd_events")
    SD_EVENT_REGISTRY = _sd_event_data["events"]
    SD_EVENT_SETTINGS = _sd_event_data["settings"]
