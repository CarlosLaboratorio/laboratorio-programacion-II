# -----------------------------------
# FUNCIONES EN PYTHON
# -----------------------------------

# 1. Función sin parámetros y sin retorno
def bienvenida():
    print("Bienvenido al programa")


# 2. Función con parámetros
def mostrar_datos(nombre, edad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")


# 3. Función con retorno
def calcular_area(base, altura):
    area = (base * altura) / 2
    return area


# -----------------------------------
# LLAMADO DE FUNCIONES
# -----------------------------------

bienvenida()

mostrar_datos("Tomás", 20)

resultado = calcular_area(10, 5)
print(f"El área del triángulo es: {resultado}")


# -----------------------------------
# FUNCIONES DENTRO DE FUNCIONES
# -----------------------------------

def principal():

    def secundaria():
        print("Esta función está dentro de otra")

    secundaria()


principal()


# -----------------------------------
# FUNCIONES PROPIAS DE PYTHON
# -----------------------------------

lista = [10, 20, 30, 40]

print("Cantidad de elementos:", len(lista))
print("Valor mínimo:", min(lista))
print("Valor máximo:", max(lista))


# -----------------------------------
# VARIABLES GLOBALES Y LOCALES
# -----------------------------------

# Variable global
curso = "Python"


def ejemplo_variables():

    # Variable local
    profesor = "Juan"

    print("Curso:", curso)
    print("Profesor:", profesor)


ejemplo_variables()

print("Variable global:", curso)

# print(profesor) -> ERROR
# Porque la variable es local


# -----------------------------------
# DIFICULTAD EXTRA
# -----------------------------------

def multiplos(palabra1, palabra2):

    contador = 0

    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print(palabra1 + palabra2)

        elif i % 3 == 0:
            print(palabra1)

        elif i % 5 == 0:
            print(palabra2)

        else:
            print(i)
            contador += 1

    return contador


resultado_final = multiplos("Hola", "Mundo")

print("Cantidad de números impresos:", resultado_final)