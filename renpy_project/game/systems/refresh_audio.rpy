# Original 0.5 sound cues. Source score/synthesis lives in tools/create_refresh_audio.cjs.
init -3 python:
    REFRESH_SFX = {
        "game_start": {"file":"audio/generated_refresh/game_start.wav", "volume":0.70},
        "game_fail": {"file":"audio/generated_refresh/game_fail.wav", "volume":0.70},
        "game_clear": {"file":"audio/generated_refresh/game_clear.wav", "volume":0.70},
        "heartbeat": {"file":"audio/generated_refresh/heartbeat.wav", "volume":0.58},
    }

    def refresh_sfx(key, volume=None):
        """Play a short original cue once; missing optional audio stays harmless."""
        entry = REFRESH_SFX.get(key)
        if not entry or not renpy.loadable(entry["file"]):
            return False
        level = entry["volume"] if volume is None else max(0.0, min(1.0, float(volume)))
        renpy.music.play(entry["file"], channel="sound", loop=False, relative_volume=level)
        return True
