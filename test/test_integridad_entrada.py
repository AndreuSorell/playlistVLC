from src.playshuffleVLC import playshuffleVLC
import pytest

@pytest.mark.integridad_entrada
def test_diccionario_vacio():
    assert playshuffleVLC({}) == "Porfavor, ingresa un documento con archivos"
@pytest.mark.integridad_entrada
def test_no_diccionario():
    assert playshuffleVLC(["Spam"]) == "Porfavor, ingresa un diccionario"
