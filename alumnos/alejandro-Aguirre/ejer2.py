# 2_condicionales_y_operadores.py
# Ejercicios básicos - Condicionales if/else y operadores
# Autor: Alejandro

# Ejercicio 1: Número par o impar
print("=== Ejercicio 1: Par o Impar ===")
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
print()

# Ejercicio 2: Mayor de edad
print("=== Ejercicio 2: Mayor de edad ===")
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad. Puedes votar.")
else:
    print(f"Te faltan {18 - edad} años para ser mayor de edad.")
print("Gracias Alejandro por hacer este programa")
print()

# Ejercicio 3: Nota aprobatoria
print("=== Ejercicio 3: ¿Aprobaste? ===")
nota = float(input("Ingresa tu nota de 0 a 10: "))
if nota >= 6:
    print("¡Felicidades! Aprobaste :)")
elif nota >= 4:
    print("A recuperatorio. ¡Vos podés!")
else:
    print("Desaprobado. A estudiar más para la próxima.")
print()

# Ejercicio 4: Calculadora básica
print("=== Ejercicio 4: Calculadora ===")
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
operacion = input("Elige operación (+, -, *, /): ")

if operacion == "+":
    print(f"Resultado: {n1 + n2}")
elif operacion == "-":
    print(f"Resultado: {n1 - n2}")
elif operacion == "*":
    print(f"Resultado: {n1 * n2}")
elif operacion == "/":
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Error: No se puede dividir por cero")
else:
    print("Operación no válida")
print()

# Ejercicio 5: Saludo según la hora
print("=== Ejercicio 5: Saludo por hora ===")
hora = int(input("Ingresa la hora actual (0-23): "))
if 6 <= hora < 12:
    print("Buenos días, Alejandro te saluda")
elif 12 <= hora < 20:
    print("Buenas tardes, Alejandro te saluda")
else:
    print("Buenas noches, Alejandro te saluda")
print("Muchas gracias por probar el código")