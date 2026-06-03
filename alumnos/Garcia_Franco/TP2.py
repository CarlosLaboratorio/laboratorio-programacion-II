print ("---1. Operadores en Python ---")

# Operadores aritméticos
a = 10  
b = 3
print(f"suma (a + b): {a + b}")
print(f"resta (a - b): {a - b}")
print(f"multiplicación (a * b): {a * b}")
print(f"división (a / b): {a / b}")
print(f"módulo (a % b): {a % b}")
print(f"exponente / potencia (a ** b): {a ** b}")
print(f"División entera (a // b): {a // b}")

# Operadores Logicos
print(f"logico and (True and False): {True and False}")
print(f"logico or (True or False): {True or False}")
print(f"logico not (not True): {not True}") 

# Operadores de comparación
x = 5
y = 8
print(f"igual a (x == y): {x == y}")
print(f"diferente de (x != y): {x != y}")
print(f"menor que (x < y): {x < y}")
print(f"mayor que (x > y): {x > y}")
print(f"menor o igual a (x <= y): {x <= y}")
print(f"mayor o igual a (x >= y): {x >= y}")

#Operadores de asignación
c = 5 #Asignación simple
print(f"Asignacion inicial: C = {c}")
c += 3 #Asignación de suma
print(f"Suma y asignacion (c += 3): C = {c}")
c *= 2 #Asignación de multiplicación
print(f"Multiplicacion y asignacion (c *= 2): C = {c}")

#Operadores de identidad
list1 = [1, 2]
list2 = [1, 2]
list3 = list1
print(f"¿list1 es lista2? (list1 is list3): {list1 is list3}") #true
print(f"¿list1 es lista2? (list1 is list2): {list1 is list2}") #false
print(f"¿list1 NO es lista2? (list1 is not list2): {list1 is not list2}") #true

#Operadores de pertenencia
mi_lista = [10, 20, 30]
print(f"¿20 está en mi_lista? (20 in mi_lista): {20 in mi_lista}")
print(f"¿50 NO está en mi_lista? (50 not in mi_lista): {50 not in mi_lista}")

#Operadores de bit
n1 = 6  # En binario: 0110
n2 = 3  # En binario: 0011
print(f"bitwise AND (6 & 3): {n1 & n2}")  # Resultado: 2 (0010)
print(f"bitwise OR (6 | 3): {n1 | n2}")   # Resultado: 7 (0111)
print(f"bitwise XOR (6 ^ 3): {n1 ^ n2}")   # Resultado: 5 (0101)
print(f"bitwise NOT (~6): {~n1}")          # Resultado: -7
print(f"Desplazamiento a la izquierda (6 << 1): {n1 << 1}")  # Resultado: 12 (1100)

print("\n---2. Estructuras de Control ---")

# Estructura if-else-elif
edad = 18
if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes exactamente 18 años.")
else:
    print("Eres mayor de edad.")
    
#Iterativas While
print ("Resultado bucle WHILE:")
contador = 1
print(f" Contador vale: {contador}")
contador += 1

#Excepciones try-except-finally
print("\nResultado manejo de excepciones:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Este bloque se ejecuta siempre, haya o no error.")
    