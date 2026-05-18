# Ejemplos de estructuras de control en Python

# 1. Estructura condicional: if-elif-else
numero = 10
if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")

# 2. Bucle for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# 3. Bucle while
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# 4. Break en un bucle
for i in range(10):
    if i == 5:
        break
    print(i)

# 5. Continue en un bucle
for i in range(5):
    if i == 2:
        continue
    print(i)

# 6. Pass (para código vacío)
def funcion_vacia():
    pass  # No hace nada

# 7. Manejo de excepciones: try-except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")

# 8. Try-except-else-finally
try:
    numero = int("123")
except ValueError:
    print("Error: no es un número")
else:
    print(f"Número convertido: {numero}")
finally:
    print("Esto siempre se ejecuta")

# 9. With (context manager, aunque no es estrictamente control)
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola mundo")
# El archivo se cierra automáticamente