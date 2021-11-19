from src.iniciarPlaylist import iniciarPlaylist
import pytest

@pytest.mark.iniciarPlaylist
def testSeGuardanNumeros():
    indice = iniciarPlaylist()
    indice()
    indice()
    assert indice() == 3