from src.checkCancionRandom import checkCancionRandom
import pytest

playlist = {1: "California_Uber_Alles.mp3", 2: "Spam", 3: "Eggs"}

@pytest.mark.cancionEnLista
def testcancionEnLista():
    assert checkCancionRandom(playlist, "California_Uber_Alles.mp3") == False

@pytest.mark.cancionEnLista
def testcancionNoEnLista():
    assert checkCancionRandom(playlist, "California_Uber_Alles") == True

    