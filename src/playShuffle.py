from src.checkCancionRandom import checkCancionRandom
from src.iniciarPlaylist import iniciarPlaylist
from src.seleccionCancionRandom import seleccionCancionRandom
from src.seleccionCancionRandom import lib
def playShuffle(lib, playlist):
    assert isinstance(lib, dict)# and isinstance(playlist(dict))
    assert len(playlist) == 0 and len(lib) > 0 
    siguienteNumero = iniciarPlaylist()
    while len(playlist) != len(lib):
        cancionRandom = seleccionCancionRandom(lib)
        if checkCancionRandom(playlist, cancionRandom):
            playlist[siguienteNumero()] = cancionRandom
    assert sorted(playlist.values()) == sorted(lib.keys())
    return playlist

playShuffle(lib, {})
