print("======================================")
print("Ejercicio 3")
print("Alumno: Carlos Plasencia")
print("Carrera: Desarrollo de Software")
print("Instituto: Institut San Jose")
print("======================================\n")

# 1. FUNCIONES BÁSICAS

print("=== 1. FUNCIONES BÁSICAS ===")

# 🔹 Sin parámetros ni retorno
def saludo():
    print("Hola Carlos, bienvenido a Desarrollo de Software")

saludo()


# 🔹 Con parámetros (sin retorno)
def mostrar_materia(nombre, materia):
    print(f"Alumno: {nombre} - Materia: {materia}")

mostrar_materia("Carlos", "Laboratorio de Programación")


# 🔹 Con parámetros y retorno
def sumar(a, b):
    return a + b

resultado_suma = sumar(10, 5)
print("Resultado de la suma:", resultado_suma)


# 2. FUNCIONES DENTRO DE FUNCIONES

print("\n=== 2. FUNCIONES DENTRO DE FUNCIONES ===")

def funcion_externa():
    print("Ejecutando función externa...")

    def funcion_interna():
        print("Ejecutando función interna...")

    funcion_interna()

funcion_externa()

# 3. FUNCIONES DEL LENGUAJE

print("\n=== 3. FUNCIONES DEL LENGUAJE ===")

numeros = [5, 2, 9, 1, 7]

print("Lista original:", numeros)
print("Cantidad de elementos (len):", len(numeros))
print("Valor máximo (max):", max(numeros))
print("Valor mínimo (min):", min(numeros))
print("Lista ordenada (sorted):", sorted(numeros))


# 4. VARIABLES LOCAL Y GLOBAL

print("\n=== 4. VARIABLES LOCAL Y GLOBAL ===")

mensaje = "Soy una variable GLOBAL"

def mostrar_variables():
    mensaje_local = "Soy una variable LOCAL"
    print(mensaje_local)
    print(mensaje)  # accede a la global

mostrar_variables()

print("Accediendo a la variable global fuera de la función:", mensaje)


# DIFICULTAD EXTRA

print("\n=== DIFICULTAD EXTRA ===")

def funcion_extra(texto1, texto2):
    contador = 0

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + " " + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            contador += 1

    return contador


resultado = funcion_extra("Carlos", "Desarrollo de Software")

print("\nCantidad de veces que se imprimieron números:", resultado)

