define narrator = Character(None, callback=story_speaking("narrator"))
define mc = Character("[player_name]", color="#355f84", callback=story_speaking("mc"))
define roman = Character("로만", color="#a45470", callback=story_speaking("roman"))
define sia = Character("시아", color="#7058a0", callback=story_speaking("sia"))
define darim = Character("다림", color="#3f7864", callback=story_speaking("darim"))
define omu = Character("오므", color="#98633e", callback=story_speaking("omu"))
define lumi = Character("하린", color="#426c91", callback=story_speaking("lumi"))
define team = Character("축제 준비 단톡방", color="#4a7690")

transform left_slot:
    xalign 0.18
    yalign 1.0
transform center_slot:
    xalign 0.5
    yalign 1.0
transform right_slot:
    xalign 0.82
    yalign 1.0

init -5 python:
    for heroine_id in HEROINE_ORDER:
        for expression in ["neutral", "smile", "shy", "surprised", "serious"]:
            path = "images/heroines/{}/{}.png".format(heroine_id, expression)
            fallback = "images/heroines/{}/neutral.png".format(heroine_id)
            if renpy.loadable(path):
                displayable = Transform(path, fit="contain", xsize=620, ysize=920)
            elif renpy.loadable(fallback):
                displayable = Transform(fallback, fit="contain", xsize=620, ysize=920)
            else:
                displayable = Null(width=620, height=920)
            renpy.image("{} {}".format(heroine_id, expression), displayable)
    for location in ["campus", "clubroom", "sunset"]:
        replacement = "images/backgrounds/{}.png".format(location)
        if location == "sunset" and not renpy.loadable(replacement) and renpy.loadable("images/backgrounds/campus.png"):
            renpy.image("bg sunset", Transform("images/backgrounds/campus.png", xysize=(1920,1080), matrixcolor=TintMatrix("#ffe1db")))
        else:
            renpy.image("bg " + location, Transform(replacement if renpy.loadable(replacement) else "images/backgrounds/{}.svg".format(location), xysize=(1920, 1080)))
