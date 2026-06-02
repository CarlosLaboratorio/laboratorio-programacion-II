"""
nombre = input("¿Cómo te llamás? ")
resultado =0
numero1 = int(input("Ingresa el primer numero que desea sumar: "))
numero2= int (input("Ingresa el segundo numero que desea sumar: "))
print("Hola,", nombre, "👋")
print("Bienvenido a tu primer programa en Python 🚀")
resultado = numero1 + numero2
print(nombre ,"El resultado de la suma es:", resultado)
print("Esta es una prueba para ver si salio todo bien")
"""
#EJERCICIO 1 
# 1) Formas de dejar comentarios en Python
"""
ACA DEJO UN COMENTARIO
DE VARIAS LINEAS
"""
'''
ACA ESTA LA OTRA FORMA DE DEJAR
UN COMENTARIO DE VARIAS LINEAS
'''
# 2) Imprimir "Hola Python!" usando una variable
palabra= "Python!"
print("hola " + palabra)
# 3) Colocar tu nombre completo en una variable 
nombre_completo= "Aaron Amuedo"
 # 4) Variables con distintos tipos de datos
texto = "Del tipo string"
numero_entero = 120
numero_decimal = 5.20
verdadero = True
# 5) Mostrar el tipo de dato de cada variable
print(type(texto))
print(type(numero_entero))
print(type(numero_decimal))
print(type(verdadero))
# 7) Imprimir mensaje usando f-string
print(f"Hola, mi nombre es {nombre_completo}, y estoy conociendo {palabra}")
#EJERCICIO 2
#1) Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Operadores AritMéticos
a = 30
b = 5

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

# Operadores de comparación
print("Mayor que:", a > b)
print("Menor que:", a < b)
print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor o igual:", a >= b)
print("Menor o igual:", a <= b)
# Operadores lógicos
x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)
# Operadores de asignación
c = 5
c += 2
print("+=:", c)

c -= 1
print("-=:", c)

c *= 3
print("*=:", c)

c /= 2
print("/=:", c)
# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print("is:", lista1 is lista2)
print("is not:", lista1 is not lista3)
# Operadores de pertenencia
print("in:", 2 in lista1)
print("not in:", 5 not in lista1)
# Operadores de bit
m = 5   # 0101
n = 3   # 0011
print("AND bit:", m & n)
print("OR bit:", m | n)
print("XOR bit:", m ^ n)
print("Desplazamiento izquierda:", m << 1)
print("Desplazamiento derecha:", m >> 1)
# Condicionales
edad = 18

if edad >= 18:
    print("Es mayor de edad")
elif edad == 17:
    print("Casi mayor")
else:
    print("Menor de edad")

# Iterativas (for)
for i in range(3):
    print("For:", i)

# Iterativas (while)
contador = 0
while contador < 3:
    print("While:", contador)
    contador += 1

# Excepciones
try:
    numero = int("abc")  # Esto falla
except ValueError:
    print("Error: no se pudo convertir a número")
finally:
    print("Fin del bloque try-except")
    #EXTRA
for num in range(10, 56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)