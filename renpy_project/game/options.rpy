init -100 python:
    import os
    config.name = "우리 사이, 그 이상"
    config.version = "0.6.11-test"
    config.window_title = "우리 사이, 그 이상 · 첫 번째 봄"
    # Shared otter artwork: the running game's window/taskbar icon.
    config.window_icon = "images/ui/app_icon.png"
    config.screen_width = 1920
    config.screen_height = 1080
    config.physical_width = 1280
    config.physical_height = 720
    config.save_directory = None
    config.savedir = os.environ.get("CAMPUS_SAVE_DIR", os.path.join(config.basedir, "saves"))
    config.has_sound = True
    config.has_music = True
    config.has_voice = False
    config.default_text_cps = 38
    config.default_afm_time = 12
    config.history_length = 250
    config.autosave_on_choice = True
    config.autosave_on_quit = True
    config.autosave_slots = 6
    config.quicksave_slots = 6
    config.thumbnail_width = 384
    config.thumbnail_height = 216
    config.window = "auto"
    config.end_splash_transition = Dissolve(0.5)
    config.enter_transition = Dissolve(0.18)
    config.exit_transition = Dissolve(0.18)
    config.intra_transition = Dissolve(0.15)
    config.after_load_transition = Dissolve(0.2)
    config.developer = os.environ.get("CAMPUS_DEVELOPER", "0") == "1"
    config.default_language = "korean"
    config.check_conflicting_properties = True
    config.main_menu_music = None
    config.game_menu_action = ShowMenu("preferences")

init python:
    build.name = "CampusRomance"
    build.directory_name = "CampusRomance-0.6.0-test"
    build.executable_name = "CampusRomance"
    build.include_update = False
    build.classify("game/tests/**", None)
    build.classify("game/cache/**", None)
    build.classify("game/saves/**", None)
    build.classify("saves/**", None)
    build.classify("tests/**", None)
    build.classify("backups/**", None)
    build.classify("design_docs/**", None)
    build.classify("docs/**", None)
    build.classify("artwork/**", None)
    build.classify("tools/**", None)
    build.classify("**.save", None)
    build.classify("**/persistent", None)
    build.classify("**/.env", None)
    build.classify("**/.env.*", None)
    build.classify("**/credentials.json", None)
    build.classify("**/*service-account*.json", None)
    build.classify("**/id_rsa*", None)
    build.classify("**/id_ed25519*", None)
    build.classify("**.pem", None)
    build.classify("**.key", None)
    build.classify("**.pfx", None)
    build.classify("**.p12", None)
    build.classify("**.psd", None)
    build.classify("**.psb", None)
    build.classify("**.kra", None)
    build.classify("**.xcf", None)
    build.classify("**.clip", None)
    build.classify("**.ora", None)
    build.classify("**.afphoto", None)
    build.classify("**.blend", None)
    build.classify("**.aep", None)
    build.classify("**.bak", None)
    build.classify("**.log", None)
    build.classify("traceback.txt", None)
    build.classify("errors.txt", None)
    build.classify("game/images/cg/README.txt", None)
    build.classify("game/images/sd_events/README.txt", None)
    build.classify("**.rpy", None)
    build.classify("**.rpyc", "all")
    build.documentation("README.html")
