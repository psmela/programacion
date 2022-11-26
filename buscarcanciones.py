#from listadecanciones import cancion0,cancion1,cancion2,cancion3,cancion4

#pide una cancion y la busca en el cancionero.
def identificarcancion(canciones):
    nombreCancion =input("ingrese nombre cancion ")
    for cancion in canciones:
        if nombreCancion == cancion["nombre"]:
            print("cancion encontrada")
            print(cancion)
            return
    print("cancion no almacenada")