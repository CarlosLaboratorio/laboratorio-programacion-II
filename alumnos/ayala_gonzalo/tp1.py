
# comentario


"""
comentario multilinea
"""

nombre = "Ayala Gonzalo Ezequiel"

texto = "hola mundo"

entero = 120

decimal = 120.5

print(type(texto), type(entero), type(decimal))

print("Hola, mi nombre " + nombre + ", y estoy conociendo Python!")

sum = 1 + 1

resta = 2 - 1

multi = 3 * 3

potencia = 2**2

divi = 4 / 2

diviEntera = 10 // 5

mayorA = 42 > 2

menorA = 2 < 4

conjuncion = 3 > 2 and 5 > 8

disyuncion = 3 == 3 or 4 % 2 == 0

negacion = not True

# operadores de asignación

asignacion = 10
suma = 10
resta = 10
div = 10
mul = 10

suma += 10
resta -= 5
div /= 2
mul *= 10

# operadores de identidad

x = [1,2,3]
y = [4,5,6]
z = x

print(x is y)
print(y is not z)
print(z is x)

# operadores de pertenencia

arr = [1,2,3,4,5]

print(1 in arr)
print(6 in arr)
print(7 not in arr)