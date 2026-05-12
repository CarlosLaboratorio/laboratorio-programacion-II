# =========================================
# 1. FUNCIONES BÁSICAS
# =========================================

# Sin parámetros ni retorno
def saludo():
    print("Hola Python")

saludo()


# Con parámetros
def saludar(nombre):
    print("Hola", nombre)

saludar("Facundo")


# Con varios parámetros
def sumar(a, b):
    print("La suma es:", a + b)

sumar(5, 3)


# Con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 2)
print("Resultado:", resultado)


# =========================================
# 2. FUNCIONES DENTRO DE FUNCIONES
# =========================================

def externa():

    def interna():
        print("Función interna")

    interna()

externa()


# =========================================
# 3. FUNCIONES PREDEFINIDAS
# =========================================

numeros = [1, 5, 8, 2]

print(max(numeros))
print(min(numeros))
print(len(numeros))
print(sum(numeros))


# =========================================
# 4. VARIABLE LOCAL Y GLOBAL
# =========================================

# Variable global
x = 100

def mostrar_global():
    print("Variable global:", x)

mostrar_global()


# Variable local
def variable_local():
    y = 50
    print("Variable local:", y)

variable_local()


# Modificar variable global
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()

print("Contador:", contador)


# =========================================
# DIFICULTAD EXTRA
# =========================================

def imprimir_textos(texto1, texto2):

    contador_numeros = 0

    for numero in range(1, 101):

        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)

        elif numero % 3 == 0:
            print(texto1)

        elif numero % 5 == 0:
            print(texto2)

        else:
            print(numero)
            contador_numeros += 1

    return contador_numeros


resultado = imprimir_textos("Python", "Hola")

print("Cantidad de veces que se imprimió un número:", resultado)