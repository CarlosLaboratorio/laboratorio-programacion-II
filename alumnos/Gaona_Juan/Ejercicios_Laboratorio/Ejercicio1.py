# 1. Comentario con la URL del sitio web oficial de Python
# https://www.python.org/

# 2. Diferentes sintaxis para comentarios en Python

# Comentario de una sola línea (línea 1)


"""
Comentario de varias líneas usando triple comilla doble.
Esto es técnicamente una cadena multilínea no asignada,
pero funciona como comentario.
"""

'''
También se puede usar triple comilla simple.
Esto es otro comentario de varias líneas.
'''

# 3. Variable y constante (Python no tiene constantes nativas; por convención se usan mayúsculas)
variable_normal = "Esto es una variable"
CONSTANTE_POR_CONVENCION = 3.1416  # Convención para constante

# 4. Variables con tipos de datos primitivos de Python
cadena = "Hola, mundo"          # str
entero = 42                     # int
flotante = 3.1416               # float
booleano_verdadero = True       # bool
booleano_falso = False          # bool
nulo = None                     # NoneType (tipo especial)

# Opcional: otros tipos primitivos como complex, bytes
complejo = 2 + 3j               # complex
bytes_ = b"Python"              # bytes

# 5. Impresión por terminal
lenguaje = "Python"
print(f"¡Hola, {lenguaje}!")    # Salida: ¡Hola, Python!