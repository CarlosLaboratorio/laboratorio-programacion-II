print("=== EJERCICIO 3: FUNCIONES ===")

# 1) Funcion sin parametros ni retorno
def presentacion():
    print("Hola, estoy practicando funciones en Python y este es mi ejercicio 3.")


presentacion()


# 2) Funcion con un parametro
def saludar_persona(nombre):
    print(f"Bienvenida/o, {nombre}. Vamos a seguir con el ejercicio.")


saludar_persona("Antonella")


# 3) Funcion con varios parametros
def mostrar_materia(nombre, materia, anio):
    print(f"{nombre} cursa {materia} en {anio}° año.")


mostrar_materia("Antonella", "Programación II", 3)


# 4) Funcion con retorno
def multiplicar_valores(a, b):
    resultado = a * b
    return resultado


producto = multiplicar_valores(4, 7)
print("El resultado de multiplicar 4 por 7 es:", producto)


# 5) Funcion dentro de otra funcion
def funcion_externa(mensaje):
    print("Estoy dentro de la funcion externa.")

    def funcion_interna():
        print(f"La funcion interna recibio este mensaje: {mensaje}")

    funcion_interna()


funcion_externa("Python permite definir funciones dentro de otras funciones")


# 6) Uso de funciones ya creadas en el lenguaje
texto = "programacion"
numeros = [8, 3, 15, 2, 10]

print("Largo del texto con len():", len(texto))
print("Numero mayor con max():", max(numeros))
print("Numero menor con min():", min(numeros))
print("Suma total con sum():", sum(numeros))


# 7) Variable local y global
comision = "3ro A"   # variable global


def ejemplo_variables():
    apellido = "Boccalandro"   # variable local
    print("Variable global dentro de la funcion:", comision)
    print("Variable local dentro de la funcion:", apellido)


ejemplo_variables()
print("Variable global fuera de la funcion:", comision)



# ============ DIFICULTAD EXTRA ===============

print("=== DIFICULTAD EXTRA ===")


def reemplazo_textual(palabra1, palabra2):
    contador_numeros = 0

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(palabra1 + palabra2)
        elif numero % 3 == 0:
            print(palabra1)
        elif numero % 5 == 0:
            print(palabra2)
        else:
            print(numero)
            contador_numeros += 1

    return contador_numeros


cantidad = reemplazo_textual("Hola", "Python")
print("Cantidad de veces que se imprimio un numero:", cantidad)