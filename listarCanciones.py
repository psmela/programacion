#from listaddecanciones import cancion1,cancion2,cancion3,cancion4,cancion5
#pide un nombre de cancion y la b usca en el cancionero
def listarCanciones(canciones):
    for cancion in canciones:
        print("cancion: ")
        print(cancion["nombre"])
        print(cancion["artista"])
        print(cancion["letra"])