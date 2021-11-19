
def checkCancionRandom(playlist, cancionRandom):
    assert isinstance(playlist, dict)
    assert isinstance(cancionRandom, str)
    if cancionRandom not in playlist.values():
        return True
    else:
        return False


