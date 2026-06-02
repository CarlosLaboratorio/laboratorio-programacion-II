"""
Operadores y estructuras de control.
"""

def mostrar_aritmeticos(a=10, b=3):
    print("== Aritméticos ==")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ** {b} = {a ** b}")
    print(f"{a} // {b} = {a // b}")
    print()

def mostrar_comparadores():
    print("== Comparadores ==")
    print(f"10 == 3 -> {10 == 3}")
    print(f"10 != 3 -> {10 != 3}")
    print(f"10 > 3  -> {10 > 3}")
    print(f"10 < 3  -> {10 < 3}")
    print(f"10 >= 10 -> {10 >= 10}")
    print(f"10 <= 3 -> {10 <= 3}")
    print()

def mostrar_logicos():
    print("== Lógicos ==")
    print(f"(10 + 3 == 13) and (5 - 1 == 4) -> {10 + 3 == 13 and 5 - 1 == 4}")
    print(f"(10 + 3 == 14) or  (5 - 1 == 4) -> {10 + 3 == 14 or 5 - 1 == 4}")
    print(f"not (10 + 3 == 14) -> {not (10 + 3 == 14)}")
    print()

def mostrar_asignacion():
    print("== Asignación ==")
    n = 11
    print(n)
    n += 1; print(n)
    n -= 1; print(n)
    n *= 2; print(n)
    n /= 2; print(n)
    n %= 2; print(n)
    n **= 1; print(n)
    n //= 1; print(n)
    print()

def mostrar_identidad_y_pertenencia():
    print("== Identidad y pertenencia ==")
    x = 5
    y = x
    print(f"x is y -> {x is y}")
    print(f"x is not y -> {x is not y}")
    print(f"'u' in 'lasala' -> {'u' in 'lasala'}")
    print(f"'b' not in 'lasala' -> {'b' not in 'lasala'}")
    print()

def mostrar_bitwise():
    a, b = 10, 3
    print("== Bitwise ==")
    print(f"{a} & {b} = {a & b}")
    print(f"{a} | {b} = {a | b}")
    print(f"{a} ^ {b} = {a ^ b}")
    print(f"~{a} = {~a}")
    print(f"{a} >> 2 = {a >> 2}")
    print(f"{a} << 2 = {a << 2}")
    print()

def estructuras_control():
    print("== Estructuras de control ==")
    nombre = "Leo"
    if nombre == "Leo":
        print("mi nombre es 'Leo'")
    elif nombre == "Leonel":
        print("mi nombre es 'Leonel'")
    else:
        print("mi nombre no es 'Leo' ni 'Leonel'")

    print("-- for 0..10 --")
    for i in range(11):
        print(i, end=" ")
    print("\n-- while 0..10 --")
    i = 0
    while i <= 10:
        print(i, end=" ")
        i += 1
    print("\n")

def manejo_excepciones():
    print("== Manejo de excepciones ==")
    try:
        resultado = 10 / 0
        print(resultado)
    except ZeroDivisionError:
        print("error: no se puede dividir por cero")
    finally:
        print("ha finalizado el manejo de excepciones")
    print()

def extra():
    print("== Extra: números en rango ==")
    for numero in range(10, 56):
        if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
            print(numero, end=" ")
    print("\n")

def main():
    mostrar_aritmeticos()
    mostrar_comparadores()
    mostrar_logicos()
    mostrar_asignacion()
    mostrar_identidad_y_pertenencia()
    mostrar_bitwise()
    estructuras_control()
    manejo_excepciones()
    extra()

if __name__ == "__main__":
    main()
