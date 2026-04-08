# Actividad 1: Comentarios en Python

"""
Sitio oficial de Python: https://www.python.org/
"""
'''
Ejercicio 1:
1. Escribir las formas de dejar comentarios en Python.
2. Escribir que el programa imprima el mensaje "Hola Python!" pero que Python este en una variable.
3. Coloca tu nombre completo en una variable.
4. Escribir variables con los siguientes tipos de datos: string, int, float, boolean.
5. Mostrar el tipo de dato de cada variable con el formato print(type(variable)).
6. Imprimir en consola el mensaje "Hola, mi nombre es [nombre completo], y estoy conociendo Python!" utilizando la variable que contiene tu nombre completo, todo esto utilizando f-string o cadena formateada.
'''

# Actividad 2: Imprimir mensaje con variable
saludo1 = "Hola Mundo"
saludo2 = "Hola Python"
print(saludo1 + saludo2)
print(saludo1,saludo2)
print("Mi saludo es: ", saludo1, saludo2)
print("Hola ", saludo1 , sep="-")
print(saludo1,saludo2, sep="\n")
print(saludo1,saludo2, end=".")
print("Hola ", saludo1 , sep="-", end=".\n")
print("Otra forma de imprimir: ", saludo1, saludo2, sep="\n", end=".\n")
print("1","2","3","4","5","6",sep=",")

# Actividad 3: Variable con nombre completo
name = "Carlos Aníbal Aguirre"
print("Hola ", name)

# Actividad 4: Variables con diferentes tipos de datos
my_string = "Soy de Corrientes"
my_bool1 = True
my_bool2 = False
my_float = 1.75
my_int = 78

# Actividad 5: Mostrar tipo de dato de cada variable
my_typevble1 = type(my_string)
print("Mi variable my_string es de tipo: ", my_typevble1)
print("Las siguientes variables son: my_bool1: ", type(my_bool1), "y my_bool2: ", type(my_bool2))
print("my_float: ", type(my_float))
print("my_int: ", type(my_int))

# Actividad 6: Imprimir mensaje con nombre completo
print(f"Hola, mi nombre es {name}, y estoy conociendo Python y VSC.")