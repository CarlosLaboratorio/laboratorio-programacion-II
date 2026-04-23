"""
EJERCICIO 2 - Operadores y Estructuras de Control
"""


"""
Operadores
"""

# Operadores aritméticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")

# Operadores de comparación
print(f"\nIgualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"\nAND: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación
print("\nOperadores de asignación:")
my_number = 11
print(my_number)
my_number += 5
print(my_number)
my_number -= 2
print(my_number)
my_number *= 2
print(my_number)
my_number /= 2
print(my_number)
my_number %= 3
print(my_number)
my_number **= 2
print(my_number)
my_number //= 2
print(my_number)

# Operadores de identidad
print("\nOperadores de identidad:")
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print("\nOperadores de pertenencia:")
print(f"'u' in 'aguirre' = {'u' in 'aguirre'}")
print(f"'b' not in 'aguirre' = {'b' not in 'aguirre'}")

# Operadores de bit
print("\nOperadores de bit:")
a = 10
b = 3
print(f"AND: 10 & 3 = {a & b}")
print(f"OR: 10 | 3 = {a | b}")
print(f"XOR: 10 ^ 3 = {a ^ b}")
print(f"NOT: ~10 = {~a}")
print(f"Desplazamiento derecha: 10 >> 2 = {a >> 2}")
print(f"Desplazamiento izquierda: 10 << 2 = {a << 2}")


"""
Estructuras de control
"""

# Condicionales
my_string = "Carlos"

if my_string == "Carlos":
    print("\nmy_string es 'Carlos'")
elif my_string == "Aníbal":
    print("my_string es 'Aníbal'")
else:
    print("my_string no es 'Carlos' ni 'Aníbal'")


# Iterativas
print("\nIterativa con for:")
for i in range(11):
    print(i)

print("\nIterativa con while:")
i = 0
while i <= 10:
    print(i)
    i += 1


# Manejo de excepciones
print("\nManejo de excepciones:")
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")



# Extra


print("\nExtra - Números pares entre 10 y 55 (sin 16 y sin múltiplos de 3):")
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)