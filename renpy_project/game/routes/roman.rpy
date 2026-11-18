label route_roman:
    $ route_name = ROUTES["roman"]["title"]
    call roman_r01
    if _in_replay:
        return
    call screen endings
    return
