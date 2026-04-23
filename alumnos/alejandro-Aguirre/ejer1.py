""" mi primer hola mundo  """
print("Hola me llamo Alejandro")
print("mi primera suma")
print(2+2)
print("mi primera resta")
print(2-2)
print("mi primera multiplicacion")
print(2*2)
print("mi primera division")
print(2/2)
""" Algo mas complejo hacemos preguntas """



print("=== Ejercicio 2: Suma ===")
num1 = 15
num2 = 27
resultado = num1 + num2
print(f"La suma de {num1} + {num2} = {resultado}")
print()

# Ejercicio 3: Datos personales con input
print("=== Ejercicio 3: Tus datos ===")
nombre_usuario = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
print(f"Mucho gusto {nombre_usuario}, tienes {edad} años. Yo me llamo Alejandro.")
print()

# Ejercicio 4: Área de un rectángulo
print("=== Ejercicio 4: Área de rectángulo ===")
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))
area = base * altura
print(f"El área del rectángulo es: {area}")
print()

# Ejercicio 5: Conversor de temperatura
print("=== Ejercicio 5: Celsius a Fahrenheit ===")
celsius = float(input("Ingresa grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C son equivalentes a {fahrenheit}°F")
print("¡Muchas gracias por usar este programa!")