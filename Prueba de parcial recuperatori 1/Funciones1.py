from Inputs1 import *

def minuscula_caracter(caracter):
    codigo= ord(caracter)

    if codigo >= 65 and codigo <= 90:
        return chr(codigo + 32)
    return caracter


def calcular_promedio(array):
    total = 0

    for i in range(len(array)):
        total += array[i]
    
    return total
    
def calcular_promedios_participantes(matriz_notas):

    promedios = [0.0] * len(matriz_notas)
    for i in range(len(matriz_notas)):
        promedios[i] = calcular_promedio(matriz_notas[i])
        
    return promedios

def calcular_promedios_jurados(matriz_notas):
    num_jurados = len(matriz_notas[0])
    num_participantes = len(matriz_notas)
    promedios_jurados = [0.0] * num_jurados
    
    for j in range(num_jurados):
        suma_jurado = 0
        for i in range(num_participantes):
            suma_jurado += matriz_notas[i][j]
        
        promedios_jurados[j] = suma_jurado / num_participantes
        
    return promedios_jurados

def encontrar_minimo_valor(array):
    if len(array) == 0:
        return None
    min_val = array[0]
    for i in range(1, len(array)):
        if array[i] < min_val:
            min_val = array[i]
    return min_val

def encontrar_maximo_valor(array):
    if len(array) == 0:
        return None
    max_val = array[0]
    for i in range(1, len(array)):
        if array[i] > max_val:
            max_val = array[i]
    return max_val
    
def obtener_nombre_y_apellido(nombre_completo):
    nombre = ""
    apellido = ""
    encontrar_nombre = False

    for n in nombre_completo:
        if n == ' ':
            encontrar_nombre = True
            continue
        if not encontrar_nombre:
            nombre += n
        else:
            apellido += n
    
    return nombre ,apellido

def inicializar_matriz_notas(num_participantes, num_jueces):
    matriz_notas = [""] * num_participantes
    
    for i in range(num_participantes):
        fila_notas = [0] * num_jueces  
        matriz_notas[i] = fila_notas
        
    return matriz_notas

def mostrar_menu():
    print("\n--- Competencia de Baile UTN ---")
    print("1. Cargar Nombre y Apellido")
    print("2. Cargar Calificaciones")
    print("3. Mostrar Calificaciones y Promedios")
    print("4. Filtro: Promedio > 4")
    print("5. Filtro: Promedio > 8")
    print("6. Jurado más Estricto")
    print("7. Mostrar Ganador")
    print("8. Buscar Participante por Apellido")
    print("9. Ordenar Array de Números (Bubble Sort)")
    print("0. Salir")

def mostrar_informacion_participante(nombres_array, matriz_notas, indice):

    nombre_completo = nombres_array[indice]
    notas = matriz_notas[indice]
    
    nombre, apellido = obtener_nombre_y_apellido(nombre_completo)
    promedio = calcular_promedio(notas)
    
    print("\n------------------------------")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Puntuación Jurado 1: {notas[0]}")
    print(f"Puntuación Jurado 2: {notas[1]}")
    print(f"Puntuación Jurado 3: {notas[2]}")
    print(f"Promedio de nota: {promedio:.2f}/10")
    print("------------------------------")
    
    return promedio

#Opcion 1
def cargar_nombres(nombres_array, num_participantes):

    print("\n Carga de Nombre y Apellido")

    for i in range(num_participantes):
        mensaje = f"Ingrese Nombre y Apellido del participante {i + 1}"
        nombres_array[i] = validar_nombre_apellido(mensaje)

    return nombres_array, True

#Opcion 2
def cargar_notas(nombres_cargados, nombres_array, matriz_notas, num_participantes, num_jurados):

    if not nombres_cargados:
        print("Debe cargar Nombres (Opcion 1) ")
        return matriz_notas, False
    
    print("\n Cargar de Calificaciones ")
    for i in range(num_participantes):
        nombre, apellido = obtener_nombre_y_apellido(nombres_array[i])
        print(f"Calificaciones para {nombre} {apellido}")
    
        for j in range(num_jurados):
            mensaje = f"Ingresar nota del jurado {j + 1} (1-10)"
            matriz_notas[i][j] = validar_nota_rango(mensaje, 1, 10)

    print("\n Notas cargadas correctamente. ")
    return matriz_notas, True

#Opcion 3
def mostrar_calificaciones(nombres_cargados, notas_cargadas, nombres_array, matriz_notas, num_participantes):
    if not (nombres_cargados and notas_cargadas):
        print("Debe cargar Nombres y Calificaiones (Opciones 1 y 2). ")
        return False
    
    print("\n Listados de CAlificaciones y Promedios ")

    for i in range(num_participantes):
        mostrar_informacion_participante(nombres_array, matriz_notas, i)
    
    return True

#Opcion 4
def promedio_mayor_a_4(nombres_cargados, notas_cargadas, nombre_array, matriz_notas, num_participantes):

    if not (nombres_cargados and notas_cargadas):
        print("\n Debe cargarNombres y Calificaciones (Opciones 1 y 2). ")
        return False

    print("\n Participantes con promedio > 4.0 ")
    encontrados = 0
    promedio = calcular_promedios_participantes(matriz_notas)

    for i in range(num_participantes):
        if promedio[i] > 4.0:
            mostrar_informacion_participante(nombre_array, matriz_notas, i)
            encontrados += 1
        return True
    
#Opcion 5
def promedio_mayor_a_8(nombres_cargados, notas_cargadas, nombre_array, matriz_notas, num_participantes):
    if not (nombres_cargados and notas_cargadas):
        print("\n Debe cargarNombres y Calificaciones (Opciones 1 y 2). ")
        return False
    
    print("\n Participantes con promedio > 8.0 ")
    encontrados = 0
    promedio = calcular_promedios_participantes(matriz_notas)

    for i in range(num_participantes):
        if promedio[i] > 8.0:
            mostrar_informacion_participante(nombre_array, matriz_notas, i)
            encontrados += 1
        return True

#Opcion 6
def jurado_mas_estricto(nombres_cargados, notas_cargadas, matriz_notas, num_jurado):
    if not (nombres_cargados and notas_cargadas):
        print("\n Debe cargarNombres y Calificaciones (Opciones 1 y 2). ")
        return False
    
    print("\n Jurado más Estricto ")
    promedio_jurados = calcular_promedios_jurados(matriz_notas)
    min_promedio = encontrar_minimo_valor(promedio_jurados)

    jurados_estrictos = []
    for j in range(num_jurado):
        if promedio_jurados[j] == min_promedio:
            jurados_estrictos = jurados_estrictos + [j + 1]
    
    print(f"El puntaje promedio más bajo fue: {min_promedio:.2f}")
    if len(jurados_estrictos) == 1:
        print(f"El jurado mas estricto es el Jurado {jurados_estrictos[0]}.")
    else:
        print(f"No hay jurado mas estricto, los jurados estrictos son: {jurados_estrictos}. ")

    return jurados_estrictos

#Opcion 7
def mostrar_ganador(nombres_array, notas_cargadas, num_participantes, matriz_notas, nombres_cargados):

    if not (nombres_cargados and notas_cargadas):
        print("\n Debe cargarNombres y Calificaciones (Opciones 1 y 2). ")
        return False
    
    print("\n Ganador de la Competencia ")
    promedio = calcular_promedios_participantes(matriz_notas)
    max_promedio = encontrar_maximo_valor(promedio)

    ganadores_indice = []
    for i in range(num_participantes):
        if promedio[i] == max_promedio:
            ganadores_indice = ganadores_indice + [i + 1]
    
    for indice in ganadores_indice:
        mostrar_informacion_participante(nombres_array, matriz_notas, indice)
    
    if len(ganadores_indice) > 1:
        print("Hay un empate en las notas del promedio más alto")
    else:
        print("Tenemos un ganador")
    
    return ganadores_indice
    
#Opcion 8
def buscar_participante(nombres_cargados, notas_cargadas, nombre_participantes, matriz_notas, numero_participantes):

    if not (nombres_cargados and notas_cargadas):
        print("\n Debe cargarNombres y Calificaciones (Opciones 1 y 2). ")
        return False
    
    ingresar_busqueda = input("Ingrese el Apellido a buscar: ")

    if not ingresar_busqueda:
        print("No se puede dejar la busqueda en blanco. ")
        return
    
    print(f"\n Resultados para la búsqueda '{ingresar_busqueda}' ")
    
    encontrar = 0
    for i in range(numero_participantes):
        nombre, apellido = obtener_nombre_y_apellido(nombre_participantes[i])

        coincide = True

        if len(ingresar_busqueda) > len(apellido):
            coincide = False
        else:
            for j in range(len(ingresar_busqueda)):
                caracter_apellido_min = minuscula_caracter(apellido[j])
                caracter_busqueda_min = minuscula_caracter(ingresar_busqueda[j])
                
                if caracter_apellido_min != caracter_busqueda_min:
                    coincide = False
                    break
        if coincide:
            mostrar_informacion_participante(nombre_participantes, matriz_notas, i)
            encontrar += 1

    if encontrar == 0:
        print(f"No se encontraron resultados para la búsqueda '{ingresar_busqueda}'.")
    
    return encontrar

#Opcion 9
def ordenar_array(array_numeros):

    n = len(array_numeros)
    for i in range(n):
        for j in range(0, n - i - 1 ):
            if array_numeros[j] < array_numeros [j + 1]:
                temporal = array_numeros[j]
                array_numeros[j] = array_numeros[j + 1]
                array_numeros[j + 1] = temporal
    return array_numeros
