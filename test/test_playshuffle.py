from src.playShuffle import playShuffle
import pytest
from test.tests import lib

@pytest.mark.playshuffleIntegro
def testBasico():
    assert sorted(list(playShuffle(lib, {}).values())) == sorted(list(lib.keys()))
