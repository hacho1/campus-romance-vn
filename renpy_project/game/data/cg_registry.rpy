# LD cut paths and gallery metadata live in JSON, separate from dialogue.
init -11 python:
    _cg_registry_data = read_data("cg_registry")
    CG_REGISTRY = _cg_registry_data["items"]
    # Keep old save IDs in the registry without listing them in the gallery.
    CG_ORDER = _cg_registry_data["order"]
    CG_TABS = _cg_registry_data["tabs"]
    CG_SETTINGS = _cg_registry_data["settings"]
