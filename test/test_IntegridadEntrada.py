from src.playshuffleVLC import playShuffleVLC
import pytest

@pytest.mark.integridadEntrada
def testDiccionarioVacio():
    assert playShuffleVLC({}) == "Porfavor, ingresa un documento con archivos"
@pytest.mark.integridadEntrada
def testNoDiccionario():
    assert playShuffleVLC(["Spam"]) == "Porfavor, ingresa un diccionario"
