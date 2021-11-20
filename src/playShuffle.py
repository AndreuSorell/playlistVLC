from src.checkCancionRandom import checkCancionRandom
from src.iniciarPlaylist import iniciarPlaylist
from src.seleccionCancionRandom import seleccionCancionRandom
from src.seleccionCancionRandom import lib
from src.checkPlayShuffle import checkPlayShuffle
def playShuffle(lib, playlist):
    assert isinstance(lib, dict)# and isinstance(playlist(dict))
    assert len(playlist) == 0 and len(lib) > 0 
    siguienteNumero = iniciarPlaylist()
    while len(playlist) != len(lib):
        cancionRandom = seleccionCancionRandom(lib)
        if checkCancionRandom(playlist, cancionRandom):
            playlist[siguienteNumero()] = cancionRandom
    checkPlayShuffle(lib, playlist)
    return playlist

