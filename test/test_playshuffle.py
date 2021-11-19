from src.playshuffle import playshuffle
import pytest
from src.seleccionCancionRandom import lib

@pytest.mark.playshuffleIntegro
def testBasico():
    assert sorted(list(playshuffle(lib, {}).values())) == sorted(list(lib.keys()))
