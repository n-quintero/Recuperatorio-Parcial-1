from Inputs1 import *
from Funciones1 import *

numero_jueces = 3
numero_participantes = 6
nombre_participantes = [""] * numero_participantes
nombres_cargados = False
notas_cargadas = False
matriz_notas = inicializar_matriz_notas(numero_participantes, numero_jueces)


while True:
    mostrar_menu()
    opcion = int(input("Su opcion: "))
    
    if opcion == 0:
        print("Saliendo del sistema...")
        break
    elif opcion == 1:
        nombre_participantes, nombres_cargados = cargar_nombres(nombre_participantes, numero_participantes)
    elif opcion == 2:
        matriz_notas, notas_cargadas = cargar_notas(nombres_cargados, nombre_participantes, matriz_notas, numero_participantes, numero_jueces)
    elif opcion == 3:
        mostrar_calificaciones(nombres_cargados, notas_cargadas, nombre_participantes, matriz_notas, numero_participantes)
    elif opcion == 4:
        promedio_mayor_a_4(nombres_cargados, notas_cargadas, nombre_participantes, matriz_notas, numero_participantes)
    elif opcion == 5:
        promedio_mayor_a_8(nombres_cargados, notas_cargadas, nombre_participantes, matriz_notas, numero_participantes)
    elif opcion == 6:
        jurado_mas_estricto(nombres_cargados, notas_cargadas, matriz_notas, numero_jueces)
    elif opcion == 7:
        mostrar_ganador(nombre_participantes, notas_cargadas, numero_participantes, matriz_notas, nombres_cargados)
    elif opcion == 8:
        buscar_participante(nombres_cargados, notas_cargadas, nombre_participantes, matriz_notas, numero_participantes)
    elif opcion == 9:
        array_original = [55, 12, 98, 3, 70, 24, 60, 41, 19, 85]

        array_a_ordenar = array_original[:]

        array_ordenado = ordenar_array(array_a_ordenar)
        print("\n Algoritmo de Ordenamiento (Burbujeo) ")
        print("Array original: ", array_original)
        print("Array ordenado de Mayor a menor", array_ordenado)
    else:
        print("Opción no válida. Intente de nuevo.")



