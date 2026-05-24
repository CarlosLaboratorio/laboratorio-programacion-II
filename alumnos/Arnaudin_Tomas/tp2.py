# . Operadores

a = 10
b = 3

# Aritméticos
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# Comparación
print(a > b)
print(a == b)
print(a != b)

# Lógicos
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > 5))

# Asignación
c = 5
c += 2
print(c)

# Identidad
x = [1, 2, 3]
y = x
print(x is y)
print(x is not y)

# Pertenencia
print(2 in x)
print(5 not in x)

# Bit
print(a & b)
print(a | b)

#  Estructuras de control

# Condicional
if a > b:
    print("a es mayor que b")
else:
    print("b es mayor o igual que a")