# PixAI is the default LD pack. The earlier pack still provides manual poses.
init -9 python:
    LD_STANDING_ROOT = "images/standings/"
    PIXAI_STANDING_ROOT = LD_STANDING_ROOT + "pixai_20261105/"
    LEGACY_STANDING_ROOT = LD_STANDING_ROOT + "title_matched_20261105/"
    # Keep the same character design when a planned face has no exact export.
    PIXAI_STANDING_FALLBACKS = {
        "angry": ("serious",),
        "confused": ("surprised",),
        "embarrassed": ("shy", "surprised"),
        "sad": ("shy", "serious", "embarrassed"),
        "deadpan": ("serious",),
        "shy": ("embarrassed",),
        "smug": ("playful", "happy"),
    }
    PIXAI_STANDING_OVERRIDES = {
        "sia": {"angry": ("shy",), "embarrassed": ("awkward",)},
        "darim": {"sad": ("serious",)},
        "hess": {"smug": ("serious",)},
    }
    # (embarrassment expression, playful expression, pose B, pose C)
    LD_STANDING_VARIANTS = {
        "roman": ("shy", "playful", "happy", "playful"),
        "sia": ("shy", "playful", "playful", "serious"),
        "darim": ("shy", "playful", "serious", "playful"),
        "omu": ("shy", "playful", "serious", "playful"),
        "rumi": ("shy", "playful", "playful", "shy"),
        "ski": ("embarrassed", "playful", "happy", "embarrassed"),
        "hess": ("shy", "deadpan", "serious", "deadpan"),
        "bambam": ("shy", "playful", "happy", "playful"),
        "hyeophap": ("embarrassed", "playful", "serious", "happy"),
    }

    def ld_standing_path(key, expression="normal", pose="a"):
        if key == "visitor":
            path = LD_STANDING_ROOT + "visitors/visitor_normal.png"
            return path if renpy.loadable(path) else None
        slug = "rumi" if key == "lumi" else key
        variants = LD_STANDING_VARIANTS.get(slug)
        if variants is None or pose not in ("a", "b", "c"):
            return None
        if pose == "a":
            pixai_slug = "lumi" if slug == "rumi" else slug
            # Omu's later neutral pose is the base for the PixAI expression set.
            base_face = "direct" if pixai_slug == "omu" else "normal"
            requested_face = base_face if expression == "normal" else expression
            character_faces = PIXAI_STANDING_OVERRIDES.get(pixai_slug, {}).get(expression, ())
            shared_faces = PIXAI_STANDING_FALLBACKS.get(expression, ())
            prefix = PIXAI_STANDING_ROOT + pixai_slug + "/" + pixai_slug + "_"
            for face in dict.fromkeys((requested_face, *character_faces, *shared_faces, base_face, "normal")):
                path = prefix + face + ".png"
                if renpy.loadable(path):
                    return path
        shy, playful, pose_b, pose_c = variants
        if pose == "b":
            face = pose_b
        elif pose == "c":
            face = pose_c
        else:
            face = {
                "normal": "normal",
                "happy": "happy",
                "surprised": "surprised",
                "confused": "surprised",
                "serious": "serious",
                "angry": "serious",
                "shy": shy,
                "embarrassed": shy,
                "sad": shy,
                "playful": playful,
                "deadpan": playful,
                "smug": playful,
            }.get(expression, "normal")
        return LEGACY_STANDING_ROOT + slug + "/" + slug + "_pose_" + pose + "_" + face + ".png"
