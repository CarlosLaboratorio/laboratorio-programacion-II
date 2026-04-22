# Ejercicio 3: Funciones en Python

print("=== 1. FUNCIONES BÁSICAS ===\n")

# Función sin parámetros ni retorno
def saludar():
    print("¡Hola! Esta función no recibe nada ni retorna nada.")

saludar()

# Función con un parámetro
def cuadrado(n):
    print(f"El cuadrado de {n} es {n**2}")

cuadrado(5)

# Función con varios parámetros
def suma(a, b, c):
    print(f"{a} + {b} + {c} = {a+b+c}")

suma(3, 5, 7)

# Función con retorno
def multiplicar(x, y):
    return x * y

resultado = multiplicar(4, 6)
print(f"multiplicar(4,6) retorna: {resultado}")

# Función con valores por defecto
def potencia(base, exponente=2):
    return base ** exponente

print(f"potencia(3) = {potencia(3)} (usando exponente por defecto 2)")
print(f"potencia(3,4) = {potencia(3,4)}")

print("\n=== 2. FUNCIONES DENTRO DE FUNCIONES ===\n")

def funcion_exterior(mensaje):
    def funcion_interior():
        print(f"Mensaje desde interior: {mensaje}")
    funcion_interior()
    print("Esto es de la función exterior")

funcion_exterior("Hola anidación")

# También se puede retornar una función interna
def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar

duplicar = crear_multiplicador(2)
print(f"duplicar(10) = {duplicar(10)}")
triplicar = crear_multiplicador(3)
print(f"triplicar(7) = {triplicar(7)}")

print("\n=== 3. FUNCIONES YA CREADAS EN EL LENGUAJE ===\n")

# Ejemplos de funciones built-in
numeros = [5, 2, 8, 1, 9]
print(f"Lista original: {numeros}")
print(f"len() -> longitud: {len(numeros)}")
print(f"max() -> máximo: {max(numeros)}")
print(f"min() -> mínimo: {min(numeros)}")
print(f"sorted() -> ordenada: {sorted(numeros)}")
print(f"sum() -> suma: {sum(numeros)}")
print(f"type(123) -> {type(123)}")

# Función map
cuadrados = list(map(lambda x: x**2, numeros))
print(f"map con lambda: cuadrados de {numeros} -> {cuadrados}")

print("\n=== 4. VARIABLES LOCALES Y GLOBALES ===\n")

# Variable global
contador_global = 10

def usar_global():
    global contador_global  # Para modificar la global
    print(f"Dentro de la función, contador_global vale: {contador_global}")
    contador_global += 5
    print(f"Modificada a: {contador_global}")

def variable_local():
    local = 100  # Variable local
    print(f"Dentro de variable_local, local = {local}")
    # Si intentamos print(contador_global) aquí, funciona porque se puede leer global
    print(f"Puedo leer la global: {contador_global}")

print(f"Antes de llamar a usar_global(): contador_global = {contador_global}")
usar_global()
print(f"Después de usar_global(): contador_global = {contador_global}")

variable_local()
# print(local)  # Esto daría error porque local no existe fuera

# Ejemplo de ambigüedad: si declaras una variable con mismo nombre dentro de función, es local
ambigua = 50
def probar_ambigua():
    ambigua = 999  # Local, no modifica la global
    print(f"Dentro: ambigua = {ambigua}")

probar_ambigua()
print(f"Fuera: ambigua = {ambigua}")  # Sigue siendo 50

print("\n" + "="*50)
print("=== DIFICULTAD EXTRA ===")
print("="*50 + "\n")

def fizzbuzz_custom(texto1: str, texto2: str) -> int:
    """
    Imprime números del 1 al 100.
    - Si múltiplo de 3 -> texto1
    - Si múltiplo de 5 -> texto2
    - Si múltiplo de 3 y 5 -> texto1 + texto2
    - En otro caso -> el número
    Retorna la cantidad de veces que se imprimió un número (no los textos).
    """
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

# Prueba de la función extra
veces = fizzbuzz_custom("Fizz", "Buzz")
print(f"\n--- La función retornó: {veces} números impresos (sin reemplazar por textos) ---")

# También podemos probar con otras cadenas
print("\n--- Otra prueba con 'Python' y 'Rock' ---")
veces2 = fizzbuzz_custom("Python", "Rock")
print(f"\nRetorno: {veces2} números impresos")