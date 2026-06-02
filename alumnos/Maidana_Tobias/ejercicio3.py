# =========================================
# EJERCICIO 3 - FUNCIONES EN PYTHON
# =========================================

# -----------------------------------------
# 1) FUNCIONES BÁSICAS
# -----------------------------------------

# Función sin parámetros ni retorno
def saludo():
    print("Hola, esta es una función sin parámetros ni retorno")

saludo()


# Función con un parámetro
def mostrar_nombre(nombre):
    print("Tu nombre es:", nombre)

mostrar_nombre("Tobias")


# Función con varios parámetros
def suma(a, b):
    print("La suma es:", a + b)

suma(10, 5)


# Función con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)
print("El resultado de la multiplicación es:", resultado)


# -----------------------------------------
# 2) FUNCIONES DENTRO DE FUNCIONES
# -----------------------------------------

def funcion_externa():

    def funcion_interna():
        print("Esta es una función interna")

    funcion_interna()

funcion_externa()


# -----------------------------------------
# 3) FUNCIONES YA CREADAS EN PYTHON
# -----------------------------------------

# len() -> cuenta elementos
texto = "Python"
print("Cantidad de letras:", len(texto))

# max() -> devuelve el número más grande
numeros = [3, 8, 1, 10]
print("Número mayor:", max(numeros))

# min() -> devuelve el número más chico
print("Número menor:", min(numeros))


# -----------------------------------------
# 4) VARIABLES LOCALES Y GLOBALES
# -----------------------------------------

# Variable global
mensaje = "Soy una variable global"

def ejemplo_variables():

    # Variable local
    numero = 100

    print(mensaje)
    print("Variable local:", numero)

ejemplo_variables()

# La variable global puede usarse afuera
print(mensaje)

# La variable local NO puede usarse afuera
# print(numero) -> daría error


# =========================================
# DIFICULTAD EXTRA
# =========================================

def multiplos(texto1, texto2):

    contador_numeros = 0

    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)

        elif i % 3 == 0:
            print(texto1)

        elif i % 5 == 0:
            print(texto2)

        else:
            print(i)
            contador_numeros += 1

    return contador_numeros


resultado_final = multiplos("Fizz", "Buzz")

print("Cantidad de veces que se imprimieron números:", resultado_final)