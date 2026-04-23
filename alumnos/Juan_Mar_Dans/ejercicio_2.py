
print("--- 1. OPERADORES ---")

# Aritméticos
a, b = 15, 4
print(f"Aritméticos: Suma: {a + b}, Potencia: {a ** b}, División Entera: {a // b}")

# Lógicos
es_valido = True
es_mayor = False
print(f"Lógicos: AND: {es_valido and es_mayor}, OR: {es_valido or es_mayor}, NOT: {not es_valido}")

# Comparación
print(f"Comparación: {a} > {b} es {a > b}, {a} == 15 es {a == 15}")

# Asignación
x = 10
x += 5  # x = 15
x *= 2  # x = 30
print(f"Asignación: Resultado final de x es {x}")

# Identidad (is, is not)
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a
print(f"Identidad: ¿Mismo objeto? {lista_a is lista_b}, ¿Misma referencia? {lista_a is lista_c}")

# Pertenencia (in, not in)
frutas = ["manzana", "pera", "uva"]
print(f"Pertenencia: ¿Hay pera? {'pera' in frutas}, ¿No hay coco? {'coco' not in frutas}")

# Bitwise (Operadores de bit)
# 5 es 0101, 3 es 0011 en binario
print(f"Bitwise: AND: {5 & 3}, OR: {5 | 3}, XOR: {5 ^ 3}")

print("-" * 30)

# --- 2. ESTRUCTURAS DE CONTROL ---

print("--- 2. ESTRUCTURAS DE CONTROL ---")

# Condicionales (if, elif, else)
puntuacion = 85
if puntuacion >= 90:
    print("Resultado: Excelente")
elif puntuacion >= 70:
    print("Resultado: Aprobado")
else:
    print("Resultado: Desaprobado")

# Iterativas: For (con pertenencia)
print("Iterativa For:")
colores = ["Rojo", "Verde", "Azul"]
for color in colores:
    print(f"  Color actual: {color}")

# Iterativas: While (con comparación y asignación)
print("Iterativa While:")
contador = 3
while contador > 0:
    print(f"  Cuenta regresiva: {contador}")
    contador -= 1

# Excepciones (try, except, finally)
print("Manejo de Excepciones:")
try:
    divisor = 0
    resultado = 10 / divisor
except ZeroDivisionError:
    print("  Error: No se puede dividir por cero.")
finally:
    print("  Finalización del bloque de control.")

print("-" * 30)