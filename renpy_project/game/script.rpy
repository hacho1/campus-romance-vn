label start:
    # Official SC01 contains the original name input at its authored position.
    $ _quit_slot = STORY_RESUME_SLOT
    jump chapter01

label rename_player:
    $ player_name = clean_name(renpy.input("새 이름을 입력해 주세요.", default=player_name, length=12))
    return
