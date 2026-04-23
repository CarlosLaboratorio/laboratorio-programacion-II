# ==============================
# 1. TIPOS DE OPERADORES
# ==============================

# Operadores aritméticos
a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("Módulo:", a % b)
print("Potencia:", a ** b)
print("División entera:", a // b)

# Operadores lógicos
x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# Operadores de comparación
print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor que:", a > b)
print("Menor que:", a < b)
print("Mayor o igual:", a >= b)
print("Menor o igual:", a <= b)

# Operadores de asignación
c = 5
print("Valor inicial:", c)

c += 2
print("Suma y asigna:", c)

c -= 1
print("Resta y asigna:", c)

c *= 2
print("Multiplica y asigna:", c)

c /= 2
print("Divide y asigna:", c)



# ==============================
# 2. ESTRUCTURAS DE CONTROL
# ==============================

# Condicionales
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Iterativas
for i in range(1, 6):
    print("For:", i)

contador = 1
while contador <= 5:
    print("While:", contador)
    contador += 1

# Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
finally:
    print("Fin del bloque try-except")

# ==============================
# 3. EXTRA
# ==============================

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)