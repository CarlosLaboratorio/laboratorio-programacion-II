# Ejercicio 2: Operadores y estructuras de control en Python

print("=== OPERADORES ===\n")

# 1. Operadores Aritméticos
print("--- Aritméticos ---")
a, b = 15, 4
print(f"a = {a}, b = {b}")
print(f"Suma: a + b = {a + b}")
print(f"Resta: a - b = {a - b}")
print(f"Multiplicación: a * b = {a * b}")
print(f"División: a / b = {a / b}")
print(f"División entera: a // b = {a // b}")
print(f"Módulo: a % b = {a % b}")
print(f"Potencia: a ** b = {a ** b}")

# 2. Operadores Lógicos
print("\n--- Lógicos ---")
x, y = True, False
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# 3. Operadores de Comparación
print("\n--- Comparación ---")
p, q = 10, 20
print(f"p = {p}, q = {q}")
print(f"p == q: {p == q}")
print(f"p != q: {p != q}")
print(f"p > q: {p > q}")
print(f"p < q: {p < q}")
print(f"p >= q: {p >= q}")
print(f"p <= q: {p <= q}")

# 4. Operadores de Asignación
print("\n--- Asignación ---")
z = 5
print(f"z = {z}")
z += 3
print(f"z += 3 -> {z}")
z -= 2
print(f"z -= 2 -> {z}")
z *= 4
print(f"z *= 4 -> {z}")
z /= 2
print(f"z /= 2 -> {z}")
z //= 2
print(f"z //= 2 -> {z}")
z %= 3
print(f"z %= 3 -> {z}")
z = 2
z **= 3
print(f"z **= 3 -> {z}")
z &= 1   # AND bit a bit
print(f"z &= 1 -> {z}")
z |= 2
print(f"z |= 2 -> {z}")
z ^= 1
print(f"z ^= 1 -> {z}")
z >>= 1
print(f"z >>= 1 -> {z}")
z <<= 2
print(f"z <<= 2 -> {z}")

# 5. Operadores de Identidad
print("\n--- Identidad ---")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(f"lista1 = {lista1}, lista2 = {lista2}, lista3 = lista1")
print(f"lista1 is lista2: {lista1 is lista2}")  # False, distintos objetos
print(f"lista1 is lista3: {lista1 is lista3}")  # True, mismo objeto
print(f"lista1 is not lista2: {lista1 is not lista2}")  # True

# 6. Operadores de Pertenencia
print("\n--- Pertenencia ---")
frutas = ["manzana", "pera", "uva"]
fruta = "pera"
print(f"frutas = {frutas}, fruta = '{fruta}'")
print(f"fruta in frutas: {fruta in frutas}")
print(f"'naranja' not in frutas: {'naranja' not in frutas}")

# 7. Operadores de Bit
print("\n--- Bit a bit ---")
m, n = 6, 2  # 6=110, 2=010
print(f"m = {m} (binario: {bin(m)}), n = {n} (binario: {bin(n)})")
print(f"m & n (AND): {m & n}")   # 010 = 2
print(f"m | n (OR): {m | n}")    # 110 = 6
print(f"m ^ n (XOR): {m ^ n}")   # 100 = 4
print(f"~m (NOT): {~m}")         # -7 (complemento a dos)
print(f"m << 1: {m << 1}")       # 1100 = 12
print(f"m >> 1: {m >> 1}")       # 11 = 3

print("\n=== ESTRUCTURAS DE CONTROL ===\n")

# 1. Condicionales (if, elif, else)
print("--- Condicionales ---")
numero = 7
print(f"numero = {numero}")
if numero > 10:
    print("El número es mayor que 10")
elif numero == 10:
    print("El número es igual a 10")
else:
    print("El número es menor que 10")

# 2. Iterativas (for, while)
print("\n--- Iterativas ---")
# for loop
print("For loop: números del 0 al 4")
for i in range(5):
    print(f"  i = {i}")

# while loop
print("While loop: cuenta regresiva desde 3")
contador = 3
while contador > 0:
    print(f"  contador = {contador}")
    contador -= 1

# 3. Excepciones (try, except, else, finally)
print("\n--- Excepciones ---")
try:
    dividendo = 10
    divisor = 0
    print(f"Intentando dividir {dividendo} entre {divisor}")
    resultado = dividendo / divisor
except ZeroDivisionError as e:
    print(f"Error capturado: {e} (división por cero)")
else:
    print(f"Resultado: {resultado} (esto no se ejecuta si hay error)")
finally:
    print("Bloque finally: siempre se ejecuta")

# Otro ejemplo con excepción personalizada y entrada
print("\n--- Otro ejemplo de excepción ---")
try:
    valor = int(input("Ingresa un número entero: "))
    print(f"El doble es {valor * 2}")
except ValueError:
    print("Error: No ingresaste un número entero válido.")
else:
    print("Operación exitosa.")
finally:
    print("Fin del bloque de excepciones.")
    
    
#EJERCICIO EXTRA 
  
# Programa que imprime números del 10 al 55 (inclusive) que sean pares,
# excluyendo el número 16 y los múltiplos de 3.

for num in range(10, 56):  # 56 para incluir 55
    if num % 2 == 0:       # Verifica si es par
        if num != 16 and num % 3 != 0:  # No es 16 ni múltiplo de 3
            print(num)
    
    
    