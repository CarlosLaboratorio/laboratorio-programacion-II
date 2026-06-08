#Punto 1

#------------------------
# Operadores aritmeticos
#------------------------

num1 = 25
num2 = 15

print ("Suma:", num1 + num2)
print ("Resta:", num1 - num2)
print ("Multiplicación:", num1 * num2)
print ("División:", num1 / num2)
print ("Modulo:", num1 % num2)
print ("Potencia", num1 ** num2)

#--------------------
# Operadores logicos
#--------------------

a = True
b = False

print ("AND", a and b)
print ("OR", a or b)
print ("NOT", not b)

#---------------------------
# Operadores de comparación
#---------------------------

print ("num1 == num2:", num1 == num2)
print ("num1 != num2:", num1 != num2)
print ("num1 > num2:", num1 > num2)
print ("num1 < num2:", num1 < num2)
print ("num1 >= num2:", num1 >= num2)
print ("num1 <= num2:", num1 <= num2)


#---------------------------
# Operadores de asignación
#---------------------------

c = 5
c += 2
print ("c += 2:", c)

c -= 1
print ("c -= 1:", c)

c *= 3
print ("c *= 3:", c)

c /= 2
print ("c /= 2:", c)


#---------------------------
# Operadores de identidad
#---------------------------

Lista1 = [1, 2, 3]
Lista2 = Lista1
Lista3 = [1, 2, 3]

print ("Lista1 is Lista2", Lista1 is Lista2)
print ("Lista1 is Lista3", Lista1 is Lista3)
print ("Lista1 is not Lista3", Lista1 is not Lista3)


#---------------------------
# Operadores de pertenencia
#---------------------------

numeros = [1, 2, 3, 4, 5]

print (3 in numeros) # Verdadero
print (10 in numeros) # Falso
print (10 not in numeros) # Verdadero


#--------------------
# Operadores de bit
#--------------------

p = 5 #0101
q = 3 #0011

print ("AND", p & q)
print ("OR", p | q)
print ("XOR", p ^ q)
print ("Shift izquierda", p << 1)
print ("Shift derecha", p >> 1)


#Punto 2

#--------------------
# Condicionales
#--------------------

edad = 18

print ("---CONDICIONALES---")

if edad >= 18:
    
    print ("Es mayor de edad")

elif edad >= 13:

    print ("Es adolescente")

else:

    print ("Es menor de edad")



#--------------------
# Iterativas
#--------------------

print ("\n --- Bucle FOR ---")

for i in range (1, 6):

    print ("i =", i, "-> i * 2 =", i * 2)


print ("\n --- Bucle WHILE ---")

x = 0

while x < 5:

    print ("x =", x)
    x += 1


#--------------------
# Excepciones
#--------------------


n = 10
y = 0

try:

    resultado = n / y
    print ("Resultado:", resultado)

except ZeroDivisionError:

    print ("Error: no se puede dividir por cero")




#--------
# Extra
#--------

for i in range(10, 56):

    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print (i)

    







