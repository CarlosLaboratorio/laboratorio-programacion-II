# 3_bucles_y_listas.py
# Ejercicios básicos - Bucles for/while y listas
# Autor: Alejandro

# Ejercicio 1: Contador del 1 al 10
print("=== Ejercicio 1: Contador con for ===")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# Ejercicio 2: Tabla de multiplicar
print("=== Ejercicio 2: Tabla de multiplicar ===")
num = int(input("Ingresa un número para ver su tabla: "))
print(f"Tabla del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# Ejercicio 3: Suma con while
print("=== Ejercicio 3: Sumar hasta que pongas 0 ===")
suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))
print(f"La suma total es: {suma}. Muchas gracias por usar mi programa, soy Alejandro")
print()

# Ejercicio 4: Lista de nombres
print("=== Ejercicio 4: Lista de amigos ===")
amigos = ["Alejandro", "Sofía", "Mateo", "Valentina", "Lucas"]
print("Mis amigos son:")
for amigo in amigos:
    print(f"- {amigo}")
print()

# Ejercicio 5: Promedio de notas
print("=== Ejercicio 5: Promedio con listas ===")
cantidad = int(input("¿Cuántas notas vas a ingresar? "))
notas = []
for i in range(cantidad):
    nota = float(input(f"Ingresa la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"Las notas fueron: {notas}")
print(f"Tu promedio es: {promedio:.2f}")
if promedio >= 6:
    print("¡Aprobaste! Muchas gracias por usar el programa")
else:
    print("A seguir practicando. ¡Gracias por usar el programa!")