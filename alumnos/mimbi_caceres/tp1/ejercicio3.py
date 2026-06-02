##EJEMPLOS

##funcion sin parametro ni retorno
def saludar():
    print("Hola, esta es una función sin parámetros ni retorno")

saludar()

## funcion con un parametro
def saludar_persona(nombre):
    print("Hola", nombre)

saludar_persona("Mimbi")

##funcion con varios parametros
def sumar(a, b):
    resultado = a + b
    print("La suma es:", resultado)

sumar(5, 3)

##funcion con retorno
def multiplicar(a, b):
    resultado = a * b
    return resultado

resultado = multiplicar(4, 6)
print("El resultado de la multiplicación es:", resultado)

##funciones dentro de funciones
def funcion_externa():
    
    def funcion_interna():
        print("Esta es una función dentro de otra función")

    funcion_interna()

funcion_externa()

##funciones propias del lenguaje
lista = [3, 7, 2, 9]

print("Longitud de la lista:", len(lista))
print("Número mayor:", max(lista))
print("Tipo de dato:", type(lista))

##variables local y global
# Variable global
numero = 10

def ejemplo_variables():
    # Variable local
    numero_local = 5
    print("Variable local:", numero_local)
    print("Variable global dentro de la función:", numero)

ejemplo_variables()

print("Variable global fuera de la función:", numero)

##extra
def funcion_extra(texto1, texto2):
    
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


resultado = funcion_extra("Fizz", "Buzz")
print("Cantidad de veces que se imprimieron números:", resultado)

