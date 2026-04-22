
# ======== EJERCICIO 1 ========

# comentario
"""comentario"""

nombre = "Boccalandro Antonella"
texto = "Hola Mundo"
entero = 8
decimal = 5.5
lenguaje = "Python"
booleano = True

print(type(texto))
print(type(entero))
print(type(decimal))
print(type(booleano))
print(f"Hola {lenguaje}!")
print(f"Hola, mi nombre es {nombre} y estoy conociendo {lenguaje}!")


# ======== EJERCICIO 2 ========

# ARITMETICOS

a = 10
b = 5

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

# DE COMPARACION

print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor:", a > b)
print("Menor:", a < b)

# LOGICOS

x = True
y = False

print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# OPERADORES DE ASIGNACION

a = 10
print("Valor inicial de a:", a)

a += 5
print("a += 5:", a)

a -= 3
print("a -= 3:", a)

a *= 2
print("a *= 2:", a)

a /= 4
print("a /= 4:", a)

a = 10
a //= 3
print("a //= 3:", a)

a = 10
a %= 3
print("a %= 3:", a)

a = 2
a **= 3
print("a **= 3:", a)


# OPERADORES DE IDENTIDAD

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print("lista1 is lista2:", lista1 is lista2)
print("lista1 is lista3:", lista1 is lista3)
print("lista1 is not lista2:", lista1 is not lista2)


# OPERADORES DE PERTENENCIA

frutas = ["Arandano", "kiwi", "Frutilla"]

print("'manzana' in frutas:", "manzana" in frutas)
print("'uva' in frutas:", "uva" in frutas)
print("'uva' not in frutas:", "uva" not in frutas)


# OPERADORES DE BIT

x = 5
y = 3 

print("x & y:", x & y)
print("x | y:", x | y)
print("x ^ y:", x ^ y)
print("~x:", ~x)
print("x << 1:", x << 1) 
print("x >> 1:", x >> 1) 


# ====== ESTRUCTURAS DE CONTROL =======

# CONDICIONALES

edad = 20

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ITERATIVAS

# for
print("Numeros del 1 al 5 con for:")
for i in range(1, 6):
    print(i)

# while
print("Numeros del 1 al 5 con while:")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1


# EXCEPCIONES

try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Fin del bloque try-except")

# EXTRA

print("Numeros entre 10 y 55, pares, que no son 16 ni multiplos de 3:")

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
        

# ============ EJERCICIO 3 =============

print("=== EJERCICIO 3: FUNCIONES ===")


# 1) Funcion sin parametros ni retorno
def presentacion():
    print("Hola, estoy practicando funciones en Python y este es mi ejercicio 3.")


presentacion()


# 2) Funcion con un parametro
def saludar_persona(nombre):
    print(f"Bienvenida/o, {nombre}. Vamos a seguir con el ejercicio.")


saludar_persona("Antonella")


# 3) Funcion con varios parametros
def mostrar_materia(nombre, materia, anio):
    print(f"{nombre} cursa {materia} en {anio}° año.")


mostrar_materia("Antonella", "Programación II", 3)


# 4) Funcion con retorno
def multiplicar_valores(a, b):
    resultado = a * b
    return resultado


producto = multiplicar_valores(4, 7)
print("El resultado de multiplicar 4 por 7 es:", producto)


# 5) Funcion dentro de otra funcion
def funcion_externa(mensaje):
    print("Estoy dentro de la funcion externa.")

    def funcion_interna():
        print(f"La funcion interna recibio este mensaje: {mensaje}")

    funcion_interna()


funcion_externa("Python permite definir funciones dentro de otras funciones")


# 6) Uso de funciones ya creadas en el lenguaje
texto = "programacion"
numeros = [8, 3, 15, 2, 10]

print("Largo del texto con len():", len(texto))
print("Numero mayor con max():", max(numeros))
print("Numero menor con min():", min(numeros))
print("Suma total con sum():", sum(numeros))


# 7) Variable local y global
comision = "3ro A"   # variable global


def ejemplo_variables():
    apellido = "Boccalandro"   # variable local
    print("Variable global dentro de la funcion:", comision)
    print("Variable local dentro de la funcion:", apellido)


ejemplo_variables()
print("Variable global fuera de la funcion:", comision)



# ============ DIFICULTAD EXTRA ===============

print("=== DIFICULTAD EXTRA ===")


def reemplazo_textual(palabra1, palabra2):
    contador_numeros = 0

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(palabra1 + palabra2)
        elif numero % 3 == 0:
            print(palabra1)
        elif numero % 5 == 0:
            print(palabra2)
        else:
            print(numero)
            contador_numeros += 1

    return contador_numeros


cantidad = reemplazo_textual("Hola", "Python")
print("Cantidad de veces que se imprimio un numero:", cantidad)