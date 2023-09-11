from lista_espacios import lista_espacios
from espacios import espacios
from lista_posicion import lista_posicion
from posicion import posicion

lista_espacios_temp = lista_espacios()

def crear_espacios():

    lista_posicion_temp = lista_posicion()

    print("")
    print("")
    print("Escriba las filas del tablero:")
    filas = int(input())
    print("Escriba las columnas del tablero:")
    columnas = int(input())
    recorrido = columnas*filas
    condicion = '1'
    contador = 0

    while condicion == '1' and contador<recorrido:
        print("")
        print("Escriba en qué fila desea poner la pieza")
        puesto_fila =  int(input())
        print("Escriba en qué columna desea poner la pieza")
        puesto_columna = int(input())
        print("")
        print("")
        print("Escriba el color que desea agregar")
        print("A para azul")
        print("R para rojo")
        print("V para verde")
        print("P para púrpura")
        print("N para naranja")
        color = input()

        dato = posicion(puesto_fila,puesto_columna,color)
        lista_posicion_temp.agregar(dato)
        
        print("Desea poner otra pieza?")
        print("Escriba 1 si desea poner otra pieza")
        print("Escriba 2 si no desea poner otra pieza")
        
        condicion = input()
        contador +=1


    nuevo_tablero = espacios(filas,columnas,lista_posicion_temp)
    lista_espacios_temp.crear_espacios(nuevo_tablero)
    lista_espacios_temp.recorrer_espacios()
    print("Generando grafica...")
    lista_espacios_temp.generar_grafica()

def menu_principal():
    print("---------------------COLORÉALO------------------------")
    print("1. Crear Tablero")
    print("2. Mostra información del Estudiantew")
    print("3. Salir")
    print("Seleccione una opción")
    print("---------------------GUATEMATEL------------------------")

    opcion = input()

    if opcion == '1':
        crear_espacios()
    elif opcion == '2':
        print("Datos del Estudiante")
        print("Estuardo Josué Vaquiax Reyes")
        print("202201336")
        print("Introducción a la Programación y Computación 2 Sección  C ")
        menu_principal()
    elif opcion == '3':
        print("Gracias por visitarnos")
        
    else:
        print("Opción no válida")
        menu_principal()

menu_principal()