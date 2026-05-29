
# OPERADORES


a = 10
b = 3

#Operadores aritméticos
print("ARITMÉTICOS")
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

#Operadores lógicos
print("\nLÓGICOS")
print(True and False)
print(True or False)
print(not True)

#Operadores de comparación
print("\nCOMPARACIÓN")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Operadores de asignación
print("\nASIGNACIÓN")
x = 5
print("Valor inicial:", x)

x += 3
print("x += 3:", x)

x -= 2
print("x -= 2:", x)

x *= 4
print("x *= 4:", x)

x /= 2
print("x /= 2:", x)

#Operadores de identidad
print("\nIDENTIDAD")
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print(lista1 is lista2)
print(lista1 is lista3)
print(lista1 is not lista3)

# peradores de pertenencia
print("\nPERTENENCIA")
numeros = [1, 2, 3, 4, 5]

print(3 in numeros)
print(8 in numeros)
print(8 not in numeros)

#Operadores de bit
print("\nBIT A BIT")
print("AND:", 5 & 3)
print("OR:", 5 | 3)
print("XOR:", 5 ^ 3)
print("Desplazamiento izquierda:", 5 << 1)
print("Desplazamiento derecha:", 5 >> 1)

#ESTRUCTURAS DE CONTROL


print("\nCONDICIONALES")

edad = 20

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

print("\nITERATIVAS")

for i in range(1, 6):
    print("For:", i)

contador = 1

while contador <= 3:
    print("While:", contador)
    contador += 1

print("\nEXCEPCIONES")

try:
    numero = 10 / 0
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
finally:
    print("Fin del bloque try-except")


#EXTRA


print("\nEXTRA")

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)