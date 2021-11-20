from src.checkPlayShuffle import checkPlayShuffle
from test.tests import playlist_correcta
from test.tests import playlist_incorrecta1
from test.tests import playlist_incorrecta2
from test.tests import lib
import pytest


@pytest.mark.checkPlayShuffle
def testCorrecto():
    assert checkPlayShuffle(lib, playlist_correcta)
@pytest.mark.checkPlayShuffle
def testIncorrectoCancionRepetida():
    assert not checkPlayShuffle(lib, playlist_incorrecta1)
@pytest.mark.checkPlayShuffle
def testIncorrectoOutOfRange():
    assert not checkPlayShuffle(lib, playlist_incorrecta2)
