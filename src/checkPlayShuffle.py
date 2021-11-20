
def checkPlayShuffle(lib, playlist):
    for cancion in playlist:
        if list(playlist.values()).count(cancion) > 1:
             return False
    if not sorted(list(playlist.values())) == sorted(list(lib.keys())):
        return False
    if sorted(list(playlist.keys())) != list(range(1, len(playlist) + 1)):
        return False
    return True