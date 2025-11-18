def validar_nombre_apellido(mensaje):
    while True:
        Ingresar = input(mensaje)

        contador_espacios = 0
        for n in Ingresar:
            if n == ' ':
                contador_espacios += 1
        
        if contador_espacios != 1:
            print("Se debe ingresar nombre y apellido separados por un espacio!")
            continue
        
        nombre = " "
        apellido = " "
        encontrar_nombre = False

        for n in Ingresar:
            if n == " ":
                encontrar_nombre = True
                continue
            if not encontrar_nombre:
                nombre += n
            else:
                apellido += n
            
        if len(nombre) < 3 or len(apellido) < 3:
            print("Se debe ingresar como minimo 3 caracteres para el nombre y el apellido")
            continue
        
        return Ingresar

def validar_nota_rango(mensaje, min_val, max_val):

    while True:
        ingreso = input(mensaje)

        if not ingreso:
            print("No puedes dejar la casilla en blanco")
        
        es_entero =  False

        for n in ingreso:
            if '0' <= ingreso <= '9':
                es_entero = True
                break
        
        if not es_entero:
            print("Ingrese un numero Entero")
            continue

        numero=int(ingreso)

        if min_val <= numero <= max_val:
            return numero
        else:
            print(f"La nota debe estar entre {min_val} y {max_val}.")
