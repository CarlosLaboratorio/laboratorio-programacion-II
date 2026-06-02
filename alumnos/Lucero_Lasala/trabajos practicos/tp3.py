# tp3 - lucero lasala
# funciones de python

# 1. funciones basicas

# sin parametros ni retorno
def saludar():
    print("hola, soy lucero")

saludar()

# con un parametro
def saludar_persona(nombre):
    print(f"hola, {nombre}")

saludar_persona("lucero")

# con varios parametros
def sumar(a, b):
    print(f"{a} + {b} = {a + b}")

sumar(5, 3)

# con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)
print(f"4 x 5 = {resultado}")


# 2. funcion dentro de una funcion
def funcion_externa():
    print("soy la función externa")

    def funcion_interna():
        print("soy la función interna")

    funcion_interna()

funcion_externa()


# 3. funciones ya creadas
print(len("lucero lasala"))
print(max(3, 7, 1, 9, 2))
print(min(3, 7, 1, 9, 2))
print(round(3.14159, 2))
print(type("hola"))


# 4. variable global y local
variable_global = "soy global"

def probar_variables():
    variable_local = "soy local"
    print(variable_global)
    print(variable_local)

probar_variables()
print(variable_global)


# extra
def fizzbuzz(texto1, texto2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            contador += 1
    return contador

veces = fizzbuzz("fizz", "buzz")
print(f"\nse imprimio un numero en lugar de texto {veces} veces")