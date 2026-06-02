# =========================================
# 1. OPERADORES
# =========================================

a = 10
b = 5

print("=== OPERADORES ARITMÉTICOS ===")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

print("\n=== OPERADORES LÓGICOS ===")
print(True and False)
print(True or False)
print(not True)

print("\n=== OPERADORES DE COMPARACIÓN ===")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("\n=== OPERADORES DE ASIGNACIÓN ===")
c = 5
c += 2
print(c)

c -= 1
print(c)

c *= 2
print(c)

print("\n=== OPERADORES DE IDENTIDAD ===")
lista1 = [1, 2]
lista2 = lista1
lista3 = [1, 2]

print(lista1 is lista2)
print(lista1 is not lista3)

print("\n=== OPERADORES DE PERTENENCIA ===")
texto = "Python"

print("P" in texto)
print("Z" not in texto)

print("\n=== OPERADORES DE BIT ===")
x = 5
y = 3

print(x & y)
print(x | y)
print(x ^ y)
print(x << 1)
print(x >> 1)


# =========================================
# 2. ESTRUCTURAS DE CONTROL
# =========================================

print("\n=== CONDICIONALES ===")

edad = 20

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


print("\n=== BUCLE FOR ===")

for i in range(1, 6):
    print(i)


print("\n=== BUCLE WHILE ===")

contador = 0

while contador < 3:
    print(contador)
    contador += 1


print("\n=== EXCEPCIONES ===")

try:
    numero = int("hola")
except ValueError:
    print("Ocurrió un error al convertir el texto")


# =========================================
# 3. EXTRA
# =========================================

print("\n=== EXTRA ===")

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)