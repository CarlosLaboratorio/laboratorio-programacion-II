# numeros para los ejemplos
a = 5
b = 3
c = -2

# aritmeticos
print("Suma:          ", a + b)    
print("Resta:         ", a - b)    
print("Multiplicación: ", a * c)   
print("División:      ", a / b)    
print("Div. Entera:   ", a // b)   
print("Módulo/Residuo:", a % b)    
print("Potencia:      ", c ** b)

# operadores logicos

p = True
q = False
print("AND (y):         ", p and q)  
print("OR (o):          ", p or q)   
print("NOT (no):        ", not p)   


# de comparación

print("Igualdad:        ", a == b)  
print("Desigualdad:     ", a != b)  
print("Mayor que:       ", b > a)   
print("Menor que:       ", b < a)   
print("Mayor o igual:   ", c >= b)  
print("Menor o igual:   ", c <= a)  

# de asignación

val = 10
val += 3
val -= 2
val *= 2
val /= 4
val //= 2 
val **= 3 
print("Valor final tras asignaciones compuestas:", val) 

# de identidad
# comparan si dos variables apuntan al MISMO objeto en memoria

lista1 = [1, 2, 3]
lista2 = lista1          # Apunta al mismo objeto
lista3 = [1, 2, 3]       # Objeto nuevo, mismo contenido
print("lista1 is lista2:     ", lista1 is lista2)      # True
print("lista1 is lista3:     ", lista1 is lista3)      # False
print("lista1 is not lista3: ", lista1 is not lista3)  # True

# de pertenencia
# Verifican si un valor existe dentro de una secuencia

texto = "bian"
frutas = ["manzana", "pera", "uva"]
print("'i' in texto:          ", 'i' in texto)           # True
print("'z' not in texto:      ", 'z' not in texto)       # True
print("'pera' in frutas:      ", 'pera' in frutas)       # True
print("'naranja' not in frutas:", 'naranja' not in frutas)# True

# operadores de bit 
# operan a nivel binario sobre enteros

m, n = 5, 3  # 5 → 0b101, 3 → 0b011
print("AND  (&): ", m & n)   # 1  → 0b001
print("OR   (|): ", m | n)   # 7  → 0b111
print("XOR  (^): ", m ^ n)   # 6  → 0b110
print("NOT  (~): ", ~m)      # -6 → complemento a dos de 0b101
print("<< (izq): ", m << 1)  # 10 → 0b1010 (desplaza 1 bit a la izquierda)
print(">> (der): ", m >> 1)  # 2  → 0b0010 (desplaza 1 bit a la derecha)

# condicionales

edad = 25
esmiembro = True

if edad >= 65:
    descuento = 0.50
elif edad >= 18 and esmiembro:
    descuento = 0.20
else:
    descuento = 0.0

precio_final = 100 * (1 - descuento)
print(f"   Descuento: {descuento*100}% | Precio final: ${precio_final:.2f}")

# iterativas - for

numeros = range(1, 11)
suma_acumulada = 0

for n in numeros:
    if n % 2 != 0:
        continue                # Salta números impares
    suma_acumulada += n         # Suma solo pares
    if suma_acumulada > 15:
        print(f" break activado en n={n} (suma={suma_acumulada})")
        break
else:
    print(" bucle completado sin interrupciones")

print(f"   Suma acumulada: {suma_acumulada}")

# iterativas - while

contador = 5
factorial = 1

while contador > 0:
    factorial *= contador
    contador -= 1
else:
    print(" Condición del while falsa, bloque else ejecutado")

print(f"   Factorial de 5: {factorial}")

# excepciones

def dividir_seguro(a, b):
    try:
        if b < 0:
            raise ValueError("El divisor no puede ser negativo")
        resultado = a / b
    except ZeroDivisionError as e:
        print(f"    Error capturado: {e}")
        resultado = None
    except ValueError as e:
        print(f"    Error de valor: {e}")
        resultado = None
    else:
        print(f"    Operación exitosa: {a} / {b} = {resultado:.2f}")
    finally:
        print("    Bloque finally ejecutado (siempre corre)")
    return resultado

dividir_seguro(10, 3)
dividir_seguro(10, 0)
dividir_seguro(10, -2)

for n in range(10, 56):
    if n % 2 == 0 and n != 16 and n % 3 != 0:
        print(n)
        
        
        