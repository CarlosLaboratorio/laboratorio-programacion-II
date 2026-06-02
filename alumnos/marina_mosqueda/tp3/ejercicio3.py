# FUNCIONES BÁSICAS

# a) Sin parámetros ni retorno
def saludar():
    print("Esta función no recibe parámetros ni retorna valor")
saludar()


# b) Con un parámetro
def mostrar_nombre(nombre):
    print("Nombre:", nombre)
mostrar_nombre("Marina")


# c) Con varios parámetros
def sumar(a, b):
    print("Suma:", a + b)
sumar(5, 3)


# d) Con retorno
def multiplicar(a, b):
    return a * b
resultado = multiplicar(4, 6)
print("Multiplicación:", resultado)

# FUNCIONES DENTRO DE FUNCIONES

def funcion_externa(x):
    def funcion_interna(y):
        return y * 2
    return funcion_interna(x)
print("Función dentro de función:", funcion_externa(5))


# FUNCIONES YA CREADAS (BUILT-IN)
# son funciones que ya vienen incluidas en el lenguaje, no es necesario importarlas ni definirlas

numeros = [1, 2, 3, 4, 5]

print("Longitud de la lista:", len(numeros))
print("Valor máximo:", max(numeros))
print("Suma total:", sum(numeros))

# VARIABLES LOCALES Y GLOBALES

# Variable global
x = 10

def ejemplo_variables():
    # Variable local
    x = 5
    print("Variable local:", x)

ejemplo_variables()
print("Variable global:", x)


# Uso de global para modificar la variable global
def modificar_global():
    global x
    x = 20

modificar_global()
print("Variable global modificada:", x)