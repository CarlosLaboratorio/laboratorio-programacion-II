# Ejercicio 2

# 1)
# #Variables
a = 10
b = 5

# Operadores aritméticos
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Exponenciación:", a ** b)

# Operadores de comparación
print("a es mayor que b:", a > b)
print("a es igual a b:", a == b)
print("a es distinto de b:", a != b)

# Operadores lógicos
print("a > 0 y b > 0:", a > 0 and b > 0)
print("a > 0 o b < 0:", a > 0 or b < 0)
print("No (a > b):", not (a > b))

# Operadores de asignación
x = 10
x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)

# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print("lista1 is lista2:", lista1 is lista2)
print("lista1 is lista3:", lista1 is lista3)
print("lista1 is not lista3:", lista1 is not lista3)

# Operadores de pertenencia
print("2 in lista1:", 2 in lista1)
print("4 not in lista1:", 4 not in lista1)

# Operadores de bits
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Desplazamiento izquierda:", a << 1)
print("Desplazamiento derecha:", a >> 1)

#2)
# EJEMPLOS
# ESTRUCTURAS DE CONTROL

# Condicional
numero = 8

if numero > 10:
    print("Mayor que 10")
elif numero == 10:
    print("Igual a 10")
else:
    print("Menor que 10")

# Iterativa FOR
print("Bucle for:")
for i in range(3):
    print(i)
    
# Iterativa WHILE 
print("Bucle while:")
contador = 0
while contador < 3:
    print(contador)
    contador += 1

# Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")
finally:
    print("Fin del bloque try-except")
    
# 3)
# EXTRA

print("Números entre 10 y 55 (condiciones):")

for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)