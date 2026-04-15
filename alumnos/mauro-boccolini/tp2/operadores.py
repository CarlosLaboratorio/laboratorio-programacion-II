a = 115
b = 10

# OPERADORES ARITMETICOS
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicacion:", a * b)
print("Division:", a / b)
print("Division real:", a // b)
print("Potencia:", a**b)
print("Modulo:", a % b)

# OPERADORES DE COMPARACION
print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor:", a > b)
print("Menor:", a < b)
print("Menor o igual que:", a <= b)
print("Mayor o igual que:", a >= b)

# OPERADORES LOGICOS
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# OPERADORES DE ASIGNACION
mi_num = 120
print(mi_num)
mi_num += 1
print(mi_num)
mi_num -= 1
print(mi_num)
mi_num *= 2
print(mi_num)
mi_num /= 2
print(mi_num)
mi_num **= 2
print(mi_num)

# OPERADORES DE PERTENENCIA
print('b' in 'Boccolini')
print("a" not in "boccolini")

# ESTRUCTURAS DE CONTROL

# CONDICINALES -> IF-ELSE-ELSEIF
x = 10

if x > 0:
    print("positivo")
elif x == 0:
    print("cero")
else:
    print("negativo")

# ITERATIVAS
# FOR
for i in range(5):
    print(i)

# WHILE
i = 0
while i < 5:
    print(i)
    i += 1

# extra

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
