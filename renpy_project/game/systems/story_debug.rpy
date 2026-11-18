label debug_ch03_roman:
    if not config.developer:
        return
    $ story_begin_chapter(3, "개인 장면 미리보기")
    $ story_flag("ch03_partner", "roman")
    jump ch03_sc06_roman

label debug_ch03_sia:
    if not config.developer:
        return
    $ story_begin_chapter(3, "개인 장면 미리보기")
    $ story_flag("ch03_partner", "sia")
    jump ch03_sc06_sia

label debug_ch03_darim:
    if not config.developer:
        return
    $ story_begin_chapter(3, "개인 장면 미리보기")
    $ story_flag("ch03_partner", "darim")
    jump ch03_sc06_darim

label debug_ch03_omu:
    if not config.developer:
        return
    $ story_begin_chapter(3, "개인 장면 미리보기")
    $ story_flag("ch03_partner", "omu")
    jump ch03_sc06_omu

label debug_ch03_lumi:
    if not config.developer:
        return
    $ story_begin_chapter(3, "개인 장면 미리보기")
    $ story_flag("ch03_partner", "lumi")
    jump ch03_sc06_lumi
