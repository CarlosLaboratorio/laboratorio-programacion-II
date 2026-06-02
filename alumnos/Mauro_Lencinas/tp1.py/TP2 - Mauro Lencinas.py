# Tpabajo Practico 2

# Operadores aritmeticos
print(f"Suma 34 + 33 = {34 + 33}")
print(f"Resta 10 - 5 = {10 - 5}")
print(f"Multiplicacion 6 * 7 = {6 * 7}")
print(f"Division 10 / 2 = {10 / 2}")
print(f"Division entera 10 // 3 = {10 // 3}")
print(f"Exponente 10 ** 2 = {10 ** 2}")
print(f"Modulo 10 % 3 = {10 % 3}")

# Operadores de comparación 
print(f"Igualdad: 10 == 5 es {10 == 5}")
print(f"Desigualdad: 10 != 8 es {10 != 8}")
print(f"Mayor que: 10 > 9 es {10 > 9}")
print(f"Menor que: 10 < 6 es {10 < 6}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") # Ambas condiciones deben cumplirse para que sea Verdadero
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") # Al menos una sola condición debe cumplirse para que sea Verdadero 
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}") # Niega una condicion o variable

# Operadores de asignación
mi_num = 11  # asignación
print(mi_num)
mi_num += 1  # suma y asignación
print(mi_num)
mi_num -= 1  # resta y asignación
print(mi_num)
mi_num *= 2  # multiplicación y asignación
print(mi_num)
mi_num /= 2  # división y asignación
print(mi_num)
mi_num %= 2  # módulo y asignación
print(mi_num)
mi_num **= 1  # exponente y asignación
print(mi_num)
mi_num //= 1  # división entera y asignación
print(mi_num)

# Operadores de pertenencia
print(f"'u' in 'Mauro' = {'u' in 'Mauro'}")
print(f"'b' not in 'Mauro' = {'b' not in 'Mauro'}")

# Operadores de identidad
mi_nuevo_num = mi_num
print(f"mi_num is mi_nuevo_num es {mi_num is mi_nuevo_num}")
print(f"mi_num is not mi_nuevo_num es {mi_num is not mi_nuevo_num}")

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")  # -11   
print(f"Desplazamiento a la izquierda: 10 << 1 = {10 << 1}")  # 20 (10100)
print(f"Desplazamiento a la derecha: 10 >> 1 = {10 >> 1}")  # 5 (0101)

""" 
Estructuras de control 
"""
# Estructura de control if
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
# Estructura de control if-else
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
# Estructura de control if-elif-else
if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes exactamente 18 años.")
else:
    print("Eres mayor de edad.")
    
# Estructura de control while
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
    
# Estructura de control for
for i in range(5):
    print(f"Iteración: {i}")
    
    # Estructura de control for con lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
    
    # Estructura de control for con diccionario
persona = {"nombre": "Mauro", "edad": 30, "ciudad": "Buenos Aires"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
    
    # Estructura de control for con rango personalizado
for i in range(1, 10, 2):
    print(f"Número impar: {i}")
    
    # Manejo de excepciones con try-except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally  :
    print("Este bloque se ejecuta siempre, haya o no una excepción.")
       
