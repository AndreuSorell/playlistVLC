def playShuffleVLC(Canciones):
    try:
        assert isinstance(Canciones, dict)
    except:
        return "Porfavor, ingresa un diccionario"
    try:
        assert len(Canciones) > 0
    except:
        return "Porfavor, ingresa un documento con archivos"


