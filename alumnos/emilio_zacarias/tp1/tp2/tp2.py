var1 = 10
var2 = 20

#aritmeticos
print("Suma:", var1 + var2)
print("Resta:", var1 - var2)
print("Multiplicacion:", var1 * var2)
print("Division:", var1 / var2)
print("Potencia:", var1**var2)
print("Modulo:", var1 % var2)


#comparacion
print("Igual:", var1 == var2)
print("Distinto:", var1 != var2)
print("Menor o igual que:", var1 <= var2)
print("Mayor o igual que:", var1 >= var2)


#logicos
x = True
y = False
print("and", x and y)

print("or", x or y)

print("not", not x)


#asignacion
num = 2
print(num)
num += 1
print(num)
num -= 1
print(num)
num *= 2
print(num)
num /= 2
print(num)
num **= 2
print(num)


#pertenencia
print('h' in "hola")
print("s" not in "hola")


#estructuras de control
#condicional
x = 1

if x > 0:
    print(" el numero es positivo")
elif x == 0:
    print("0")
else:
    print("el numero es negativo")


#iterativo
print("FOR")

for i in range(5):
    print(i)

#excepcion
while True:
    try:
        x = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Intente ingresar un numero valido")#devuelve un error al ingresar algo que no sea un entero