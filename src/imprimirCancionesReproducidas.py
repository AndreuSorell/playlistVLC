def imprimirCancionesReproducidas(playlist):
    assert isinstance(playlist, dict)
    playlist_indices = sorted(list(playlist.keys()))
    for song in playlist_indices:
        print(str(song) + ": " + str(playlist[song]))