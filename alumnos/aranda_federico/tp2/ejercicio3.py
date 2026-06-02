# FUNCIONES BÁSICAS

# Sin parámetros ni retorno
def saludo():
    print("Hola desde una función sin parámetros")

saludo()

# Con parámetros
def sumar(a, b):
    print("La suma es:", a + b)
    
sumar(3, 5)

# Con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)
print("Resultado de multiplicar:", resultado)

# FUNCIONES DENTRO DE FUNCIONES

def funcion_externa():
    print("Estoy en la función externa")
    
    def funcion_interna():
        print("Estoy en la función interna")
        
        funcion_interna()

funcion_externa()

# FUNCIONES NATIVAS

lista = [1, 2, 3, 4]

print("Longitud de la lista:", len(lista))
print("Valor máximo:", max(lista))
print("Valor mínimo:", min(lista))
print("Suma total:", sum(lista))

# VARIABLES LOCAL Y GLOBAL

x=10 # variable global

def mostrar_variable():
    x = 5  # variable local
    print("Variable local:", x)

mostrar_variable()
print("Variable global:", x)

# EXTRA

def funcion_especial(texto1, texto2):
    contador_numeros = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(texto1 + texto2)
        elif num % 3 == 0:
            print(texto1)
        elif num % 5 == 0:
            print(texto2)
        else:
            print(num)
            contador_numeros += 1
    
    return contador_numeros

resultado = funcion_especial("Fizz", "Buzz")
print("Cantidad de veces que se imprimieron números:", resultado)
