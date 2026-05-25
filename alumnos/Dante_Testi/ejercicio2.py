#operadores arimetricos

a=10
b=5

print("suma:", a + b)
print("resta", a - b)
print("multiplicacion", a * b)
print("division", a / b)
print("modulo", a % b)
print("potecia", a ** b)

print("AND:", True and False)
print("OR:", True or False)
print("NOT:", not True)


#operadores de comparacion


print("Mayor que:", a > b)
print("Menor que:", a < b)
print("Igual que:", a == b)
print("Distinto que:", a != b)


#operadores de asignacion


c = 10
c += 5

print("Asignación += :", c)


#operadores de identidad


x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)
print("x is not z:", x is not z)


#operadores de pertenencia


lista = [1, 2, 3, 4]

print("2 in lista:", 2 in lista)
print("10 not in lista:", 10 not in lista)


#operadores de bit


print("AND bit a bit:", 5 & 3)
print("OR bit a bit:", 5 | 3)


#estructuras condicionales


edad = 18

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


#estructuras iterativas


for i in range(5):
    print("Número:", i)

contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1


# exepciones try y except


try:
    numero = int("hola")
except:
    print("Ocurrió un error")


#extra


for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)