"""
operadores en python
"""

# aritmeticos
print(f"suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"multiplicación: 10 * 3 = {10 * 3}")
print(f"división: 10 / 3 = {10 / 3}")
print(f"modulo: 10 % 3 = {10 % 3}")
print(f"exponente: 10 ** 3 = {10 ** 3}")
print(f"división entera: 10 // 3 = {10 // 3}")

# comparadores
print(f"igualdad: 10 == 3 es {10 == 3}")
print(f"desigualdad: 10 != 3 es {10 != 3}")
print(f"mayor que: 10 > 3 es {10 > 3}")
print(f"menor que: 10 < 3 es {10 < 3}")
print(f"mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"menor o igual que: 10 <= 3 es {10 <= 3}")

# logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación
my_number = 11  # asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 2  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 2  # módulo y asignación
print(my_number)
my_number **= 1  # exponente y asignación
print(my_number)
my_number //= 1  # división entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'u' in 'lasala' = {'u' in 'lasala'}")
print(f"'b' not in 'lasala' = {'b' not in 'lasala'}")

# Operadores de bit
a = 10  # 1010
b = 3   # 0011
print(f"AND: 10 & 3 = {10 & 3}")                          # 0010
print(f"OR: 10 | 3 = {10 | 3}")                           # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")                          # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

"""
Estructuras de control
"""

# Condicionales
my_string = "Lucero"
if my_string == "Lucero":
    print("my_string es 'Lucero'")
elif my_string == "Lasala":
    print("my_string es 'Lasala'")
else:
    print("my_string no es 'Lucero' ni 'Lasala'")

# Iterativas
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)