def lanzarVLC(libreria, playList):
    # Las canciones han de estar en un directorio llamado biblioteca
    # en el directorio de la aplicacion.
    # Han de ser expresamente las incluidas en el diccionario libreria.
    # La extensión a este  programa es incluir la capa de acceso a datos
    # para extraer los titulos de las canciones y las rutas
    # a los ficheros del fichero XML playlist.xspf que genera VLC
    # o Rhythmbox con las canciones de la biblioteca

    import subprocess
    import shlex
    import os

    pathVLC = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN"
    lineaComandoVLC = pathVLC
    separador = " "

    for numeroCancion in sorted(playList.keys()):
        tituloCancion = playList[numeroCancion]
        try:
            rutaAccesoFichero = libreria[tituloCancion]["location"]
        except KeyError:
            print("la cancion " + str(tituloCancion) + " no se encuentra en la biblioteca")
        else:
            # compruebo si la ruta de acceso al fichero cancion es correcto
            if os.path.exists(str(rutaAccesoFichero)):
                # anhado la ruta de acceso a la cancion
                # a la linea de comandos para invocar a VLC
                lineaComandoVLC = lineaComandoVLC + separador + str(rutaAccesoFichero)
            else:
                pass

    # Popen necesita una lista de string
    # Esta libreria optimiza la division de los strings que forman
    # la entrada de un comando en argumentos
    args = shlex.split(lineaComandoVLC)

    try:
        # lanzo el subproceso VLC con las opciones adecuada:
        # la ruta de acceso a las canciones de la playList
        procesoVLC = subprocess.Popen(args)
        # procesoVLC = subprocess.Popen(["/usr/bin/vlc", "California_Uber_Alles.mp3", "Seattle_Party.flac"])
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("lanzando VLC con lista aleatoria")
