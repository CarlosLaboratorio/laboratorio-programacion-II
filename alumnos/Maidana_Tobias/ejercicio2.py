# ------------------------------
# 1. TIPOS DE OPERADORES
# ------------------------------

print("=== OPERADORES ARITMÉTICOS ===")
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)


print("\n=== OPERADORES LÓGICOS ===")
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)


print("\n=== OPERADORES DE COMPARACIÓN ===")
print("Mayor:", a > b)
print("Menor:", a < b)
print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor o igual:", a >= b)
print("Menor o igual:", a <= b)


print("\n=== OPERADORES DE ASIGNACIÓN ===")
c = 5
print("Valor inicial:", c)
c += 2
print("c += 2:", c)
c -= 1
print("c -= 1:", c)
c *= 3
print("c *= 3:", c)
c /= 2
print("c /= 2:", c)


print("\n=== OPERADORES DE IDENTIDAD ===")
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
print("lista1 is lista2:", lista1 is lista2)
print("lista1 is lista3:", lista1 is lista3)
print("lista1 is not lista3:", lista1 is not lista3)


print("\n=== OPERADORES DE PERTENENCIA ===")
numeros = [1, 2, 3, 4]
print("2 in numeros:", 2 in numeros)
print("5 not in numeros:", 5 not in numeros)


print("\n=== OPERADORES DE BIT ===")
p = 5  # 0101
q = 3  # 0011
print("AND:", p & q)
print("OR:", p | q)
print("XOR:", p ^ q)
print("Shift izquierda:", p << 1)
print("Shift derecha:", p >> 1)


# ------------------------------
# 2. ESTRUCTURAS DE CONTROL
# ------------------------------

print("\n=== CONDICIONAL ===")
edad = 18
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


print("\n=== BUCLE FOR ===")
for i in range(3):
    print("Iteración:", i)


print("\n=== BUCLE WHILE ===")
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1


print("\n=== MANEJO DE EXCEPCIONES ===")
try:
    num = int("abc")  # error a propósito
except ValueError:
    print("Error: no es un número válido")
finally:
    print("Esto se ejecuta siempre")


# ------------------------------
# 3. EXTRA
# ------------------------------

print("\n=== EXTRA ===")
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)