def iniciarPlaylist():
    numeroCancion = 0
    def siguienteNumero():
        nonlocal numeroCancion
        numeroCancion += 1
        return numeroCancion
    return siguienteNumero

numero = iniciarPlaylist()
print(numero())
print(numero())
print(numero())
print(numero())
print(numero())
