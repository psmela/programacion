from listadecanciones import crearcanciones
from buscarcanciones import identificarcancion
from AlmacenarNuevasCanciones import almacenarnuevascanciones
from modificarcancion import modificarCanciones
from listarCanciones import listarCanciones


def biblioteca(opcion):
    while opcion  != 5:
        if opcion ==1 :
            identificarcancion(canciones)
        elif opcion == 2  :
            almacenarnuevascanciones(canciones)
        elif opcion == 3: 
            modificarCanciones(canciones)
        elif opcion == 4 :
            print(opcion)
            listarCanciones(canciones) 
        opcion = int(input("ingresar opcion  :  "))
    print("salida")
            

print("Biblioteca de canciones")
canciones = crearcanciones()
print("Ingrese: \n1: identificar canciones \n2:almacenar nuevas canciones \n3:modificar canciones \n4:listar canciones \n5:salir")
opcion =int(input())
biblioteca(opcion)





