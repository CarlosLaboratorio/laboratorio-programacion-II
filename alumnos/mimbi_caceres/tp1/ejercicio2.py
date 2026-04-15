#ejemplo operadores python

# Variables
a = 10
b = 5
c = 20

# Operadores aritméticos

print("Operadores aritméticos")

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("Módulo:", a % b)
print("Potencia:", a ** b)
print("División entera:", a // b)



# Operadores de comparación
print("\nOperadores de comparación")

print("a es igual a b:", a == b)
print("a es diferente de b:", a != b)
print("a es mayor que b:", a > b)
print("a es menor que b:", a < b)
print("a es mayor o igual que b:", a >= b)
print("a es menor o igual que b:", a <= b)


# Operadores lógicos

print("\nOperadores lógicos")

print("a > b and c > a:", a > b and c > a)
print("a > b or a > c:", a > b or a > c)
print("not(a > b):", not(a > b))

#Operadores de asignación
x = 10
y = 5

x += 3   
y *= 2  

print("Asignación:")
print("x =", x)
print("y =", y)


#Operadores de identidad
a = [1,2,3]
b = a
c = [1,2,3]

print("\nIdentidad:")
print(a is b)      
print(a is c)      
print(a is not c)  


#Operadores de pertenencia
numeros = [10,20,30,40]

print("\nPertenencia:")
print(20 in numeros)      
print(50 not in numeros)   


#Operadores de bit
n1 = 5
n2 = 3

print("\nOperadores de bit:")
print("AND:", n1 & n2)
print("OR:", n1 | n2)
print("XOR:", n1 ^ n2)
print("NOT:", ~n1)
print("Shift izquierda:", n1 << 1)
print("Shift derecha:", n1 >> 1)

##ejemplo con estructuras de control 
a = 10
b = 5

#CONDICIONAL


if (a + b) > 10 and a > b:
    print("La suma es mayor que 10 y a es mayor que b")
elif (a * b) == 50:
    print("La multiplicación es 50")
else:
    print("No se cumple ninguna condición")


#ITERATIVA-for

print("\nBucle for:")
for i in range(1,6):
    resultado = i * 2   
    print("Número:", i, "Resultado:", resultado)


#ITERATIVA-while

print("\nBucle while:")
contador = 1

while contador <= 3:  
    print("Contador:", contador)
    contador += 1     


#EXCEPCIONES

print("\nEjemplo de excepciones:")

try:
    x = 20
    y = 0
    division = x / y   
    print(division)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero")

finally:
    print("Programa finalizado")
   
##ejercicio extra

for numero in range(10, 56):
    
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)       