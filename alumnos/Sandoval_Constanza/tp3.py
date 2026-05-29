
#FUNCIONES


#Sin parámetros ni retorno
def saludo():
    print("Hola, bienvenido!")

saludo()


#Con un parámetro
def mostrar_nombre(nombre):
    print("Nombre:", nombre)

mostrar_nombre("Constanza")


#Con varios parámetros
def sumar(a, b):
    print("Resultado:", a + b)

sumar(10, 5)


#Con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)
print("Multiplicación:", resultado)



#FUNCIONES DENTRO DE FUNCIONES


def funcion_externa():
    print("Función externa")

    def funcion_interna():
        print("Función interna")

    funcion_interna()

funcion_externa()



#FUNCIONES DEL LENGUAJE


numeros = [5, 2, 8, 1]

print("Longitud:", len(numeros))
print("Máximo:", max(numeros))
print("Mínimo:", min(numeros))
print("Suma:", sum(numeros))

texto = "python"
print("Mayúsculas:", texto.upper())



#VARIABLES LOCALES Y GLOBALES


#Variable global
mensaje = "variable global"

def mostrar_global():
    print(mensaje)

mostrar_global()


def ejemplo_local():
    variable_local = "variable local"
    print(variable_local)

ejemplo_local()




contador = 0

def modificar_global():
    global contador
    contador += 1

modificar_global()
print("Contador global:", contador)