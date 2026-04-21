# FUNCION SIN PARAMETROS NI RETORNO
def saludo():
    print("Hola Mundo!")


saludo()  # Sin valor de retorno, si se asigna saludo() a una variable, el resultado de imprimir dicha variable será None


# FUNCION SIN RETORNO PERO CON PARAMETROS
def saludo_persona(nombre):  # recibe un parametro
    print(f"Hola {nombre}")


# Al igual que la funcion anterior, sigue sin retornar nada
saludo_persona("Juan")


# FUNCION CON PARAMETROS Y RETORNO
def suma(a, b):  # recibe varios parametros
    return a + b  # retorna el resultado de una suma, para poder utilizarlo


res = suma(5, 10)  # se puede alamcenar el resultado en una varible para su posterior uso o directamente usar el resultado del return e imprimirlo en consola
print(suma(8, 9))
print(res)


# FUNCIONES ANIDADAS
def suma_exponencial(a, b):

    def exponente(c):
        return (a + b) ** c
    return exponente


print(suma_exponencial(5, 10)(2))  # 225

# BUILT-IN FUNCTIONS DE PYTHON
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(num))  # indica la cantidad de elementos dentro de la lista num[]
print(sum(num))  # devuelve la sumatoria de todos los elementos
inverso = list(reversed(num))
print(inverso)


nombre = "Mauro"

print(len(nombre))
print(type(nombre))

# Devuele True si el valor pasado como primer argumento es del tipo especifado en el segundo argumento, de lo contrario devuelve False
print(isinstance(nombre, str))
