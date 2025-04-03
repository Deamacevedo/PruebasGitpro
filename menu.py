from artistas import *
from paises import *
from generos import *
from reportes import *

menu_bienvenida="""
Bienvenido al portal usuario
1.Acceder al menu artistas.
2.Acceder al menu paises.
3.Acceder al menu generos.
4.Acceder al menu reportes.
5.Salir del programa.

"""

menu_artistas="""
Bienvenido al menu artistas
1.Agregar artista.
2.Mostrar lista artistas.
3.Editar un artita.
4.Eliminar artista.
5.Regresar al menu principal.

"""
menu_paises="""
Bienvenido al menu paises
1.Agregar pais.
2.Mostrar pais.
3.Editar pais.
4.Eliminar pais.
5.Regresar al menu principal

"""

menu_generos="""
Bienvenido al menu genero
1.Agregar genero.
2.Mostrar genero.
3.Editar genero.
4.Eliminar genero.
5.Regresar al menu principal

"""

menu_reportes="""

"""

def menu_artistas_():
    while True:
        print(menu_artistas)
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                agregar_artista()
            case "2":
                mostrar_artistas()
            case "3":
                editar_artista()
            case "4":
                eliminar_artista()
            case "5":
                print("")
                break
            case _:
                print("Digite una opcion correcta")


def menu_paises_():
    while True:
        print(menu_paises)
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                agregar_pais()
            case "2":
                mostrar_paises()
            case "3":
                editar_pais()
            case "4":
                eliminar_pais()
            case "5":
                print("")
                break
            case _:
                print("Digite una opcion correcta")

def menu_generos_():
    while True:
        print(menu_generos)
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                agregar_genero()
            case "2":
                mostrar_generos()
            case "3":
                editar_genero()
            case "4":
                eliminar_pais()
            case "5":
                print("")
                break
            case _:
                print("Digite una opcion correcta")

def menu_reportes_():
    print(menu_reportes)

def menu_bienvenida_():
    print(menu_bienvenida)
def mostrar_menu():
    while True:
        menu_bienvenida_()   
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                menu_artistas_()
            case "2":
                menu_paises_()
            case "3":
                menu_generos_()
            case "4":
                menu_reportes_()
            case "5":
                print("Saliendo del portal usuario")
                break
            case _:
                print("Digite una opcion correcta")