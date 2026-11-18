# Short public introductions from CH02, scenes 03–04. No progress gates.
init -7 python:
    _met_people_data = read_data("met_people")
    MET_PEOPLE = _met_people_data["people"]
    MET_PEOPLE_ORDER = tuple(key for key in _met_people_data["order"] if key in MET_PEOPLE)
    MET_PEOPLE_PAGE_SIZE = 2

    def met_people_page_count():
        return max(1, (len(MET_PEOPLE_ORDER) + MET_PEOPLE_PAGE_SIZE - 1) // MET_PEOPLE_PAGE_SIZE)

    def met_person_portrait(actor):
        """Prefer a complete profile photo, with the standing pack as fallback."""
        photo = MET_PEOPLE[actor].get("portrait_image")
        if photo and renpy.loadable(photo):
            return photo
        art = story_asset(actor, "normal")
        if not art:
            return None
        width, height = renpy.image_size(art)
        left, top, crop_width, crop_height = MET_PEOPLE[actor].get(
            "portrait_crop", (0.17, 0.0, 0.66, 0.43))
        return Transform(art, crop=(int(width * left), int(height * top),
            int(width * crop_width), int(height * crop_height)))
