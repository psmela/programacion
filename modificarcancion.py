#from listadecanciones import cancion1
def modificarCanciones (listadecanciones):
    modificar = input("ingrese cancion a modificar : ")
    pos=0
    for cancion1 in listadecanciones:
        if modificar == cancion1["nombre"]:
            nombre =input("ingrese nuevo nombre")
            artista =input("ingrese artista a modificar : ")
            letra =input ("ingrese letra a modificar: ")
            print("nombre de la cancion",modificar,"artista:",artista,"letra:",letra)
            print("modificacion con exito")
            listadecanciones[pos]["nombre"]=nombre
            listadecanciones[pos]["artista"]=artista
            listadecanciones[pos]["letra"]=letra
            return
        pos = pos+1
        