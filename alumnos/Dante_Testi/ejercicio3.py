# funcion simple

def saludar():
    print("hola")

saludar()


# funcion con parametros

def suma(a, b):
    print(a + b)

suma(4, 6)


# funcion con retorno

def multiplicacion(a, b):
    return a * b

resultado = multiplicacion(3, 5)

print(resultado)


# funcion dentro de otra funcion

def principal():

    def secundaria():
        print("funcion dentro de otra")

    secundaria()

principal()


# funciones del lenguaje

texto = "python"

print(len(texto))
print(texto.upper())


# variable global

mensaje = "hola desde afuera"

def mostrar():
    print(mensaje)

mostrar()


# variable local

def prueba():
    local = "soy local"
    print(local)

prueba()


# ejercicio extra

def numeros(palabra1, palabra2):

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


resultado = numeros("Dante", "Testi")

print("cantidad:", resultado)