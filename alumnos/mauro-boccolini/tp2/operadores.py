a = 115
b = 10

print("OPERADORES ARITMETICOS:")
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicacion:", a * b)
print("Division:", a / b)
print("Division real:", a // b)
print("Potencia:", a**b)
print("Modulo:", a % b)
print("")

print("OPERADORES DE COMPARACION:")
print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor:", a > b)
print("Menor:", a < b)
print("Menor o igual que:", a <= b)
print("Mayor o igual que:", a >= b)
print("")

print("OPERADORES LOGICOS:")
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)
print("")

print("OPERADORES DE ASIGNACION:")
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
print("")

print("OPERADORES DE PERTENENCIA:")
print('b' in 'Boccolini')
print("a" not in "boccolini")
print("")


print(f"ESTRUCTURAS DE CONTROL:\n")
print("CONDICIONALES -> IF-ELIF-ELSE")
x = 10

if x > 0:
    print("positivo")
elif x == 0:
    print("cero")
else:
    print("negativo")
print("")
print("OPERADOR TERNARIO")
print("Positivo") if x > 0 else print("Negativo")
print("")

print(f"ITERATIVOS:\n")
print("FOR")

for i in range(5):
    print(i)

print(f"\nWHILE")
i = 0
while i < 5:
    print(i)
    i += 1
print("")
