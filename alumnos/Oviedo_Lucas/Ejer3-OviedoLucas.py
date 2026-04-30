# -----------------------------
# 1) FUNCIONES BÁSICAS
# -----------------------------

# Sin parámetros ni retorno
def inicio():
    print("Arrancó el programa")

inicio()


# Con un parámetro
def saludar(nombre):
    print("Hola", nombre)

saludar("Lucas")


# Con varios parámetros
def suma(a, b):
    print("La suma es:", a + b)

suma(8, 4)


# Con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(3, 5)
print("La multiplicación es:", resultado)


# -----------------------------
# 2) FUNCIÓN DENTRO DE OTRA
# -----------------------------

def principal():
    print("Estoy en la función principal")

    def secundaria():
        print("Estoy en la función secundaria")

    secundaria()

principal()


# -----------------------------
# 3) FUNCIONES YA CREADAS
# -----------------------------

numeros = [2, 4, 6, 8]

print("Cantidad:", len(numeros))
print("Mayor:", max(numeros))
print("Menor:", min(numeros))
print("Suma total:", sum(numeros))


# -----------------------------
# 4) VARIABLE LOCAL Y GLOBAL
# -----------------------------

# Variable global
mensaje = "Soy global"

def mostrar():
    print(mensaje)

mostrar()


# Variable local
def ejemplo():
    texto = "Soy local"
    print(texto)

ejemplo()


print("Fin del programa")