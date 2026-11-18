# Profile decorations and the event-gated official collection are separate.
init -15 python:
    PROFILE_PAGES = read_data("profile_pages")

default profile_debug_unlock = False
default persistent.profile_discoveries = set()

init -10 python:
    def diary_photo(key):
        candidates = ["images/heroines/profile_{}.png".format(key),
            "images/heroines/{}/profile.png".format(key)]
        return next((path for path in candidates if renpy.loadable(path)),
            "images/ui/profile/photo_placeholder.svg")

    def diary_sticker(key):
        path = "images/ui/spring/stickers_atlas.png"
        if renpy.loadable(path):
            atlas_width, atlas_height = renpy.image_size(path)
            cell_w, cell_h = atlas_width // 3, atlas_height // 2
            cell = {"roman":(0,0), "sia":(1,0), "darim":(2,0), "omu":(0,1), "lumi":(1,1), "common":(2,1)}[key]
            return Transform(path, crop=(cell[0]*cell_w, cell[1]*cell_h, cell_w, cell_h))
        return "images/ui/profile/sticker_{}.svg".format(key) if key != "common" else "images/ui/spring/flowers.svg"

    def profile_secret_ready(key, preview=False):
        return secret_note_ready(key, 1)

    def diary_secret_ready(key, index=0, preview=False):
        return secret_note_ready(key, index + 1)

    def open_profile_detail(key, point, preview=False):
        if point in ("secret1", "secret2", "secret3"):
            renpy.show_screen("profile_secret_notes", heroine=key, initial=int(point[-1]))
            renpy.restart_interaction()
            return
        data = PROFILE_PAGES[key]
        if point == "sticker":
            title, body = data["sticker_title"], data["sticker_text"]
            if not preview and key + ".sticker" not in persistent.profile_discoveries:
                persistent.profile_discoveries.add(key + ".sticker")
                renpy.save_persistent()
        elif point == "photo":
            title = "사진 뒤에 적힌 말"
            close = preview or profile_secret_ready(key) or key + ".note" in persistent.profile_discoveries
            body = data["photo_close"] if close else data["photo_text"]
        else:
            return
        renpy.show_screen("profile_note", heroine=key, note_title=title, note_body=body,
                          note_footer="보드에 남겨 둔 작은 메모")
        renpy.restart_interaction()
