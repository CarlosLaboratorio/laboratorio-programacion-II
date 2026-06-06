# 1. Comentarios en Python

# Comentario de una sola línea

"""
Comentario de múltiples líneas
usando comillas triples
"""

'''
También se pueden usar comillas simples triples
para comentarios largos
'''

# 2. Imprimir "Hola Python!" usando una variable

lenguaje = "Python"
print("Hola " + lenguaje + "!")

# 3. Colocar tu nombre completo en una variable

nombre_completo = "Juan Martin Dans"

# 4. Variables con diferentes tipos de datos

texto = "Esto es un string"   # string
numero_entero = 10           # int
numero_decimal = 3.14        # float
es_estudiante = True         # boolean

# 5. Mostrar el tipo de dato de cada variable

print(type(texto))
print(type(numero_entero))
print(type(numero_decimal))
print(type(es_estudiante))

# 6. Imprimir mensaje usando f-string

print(f"Hola, mi nombre es {nombre_completo}, y estoy conociendo Python!")