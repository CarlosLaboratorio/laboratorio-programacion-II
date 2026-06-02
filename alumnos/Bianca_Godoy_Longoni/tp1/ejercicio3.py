# ── 1a. Sin parámetros ni retorno ──────────────────────────
def saludar():
    print("alooooo")

saludar()


# ── 1b. Con un parámetro ───────────────────────────────────
def saludar_persona(nombre):
    print(f"bienvenido, {nombre}!")

saludar_persona("bianca")


# ── 1c. Con varios parámetros ──────────────────────────────
def sumar(a, b):
    print(f"{a} + {b} = {a + b}")

sumar(3, 7)


# ── 1d. Con retorno ────────────────────────────────────────
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)
print(f"4 x 5 = {resultado}")


# ── 2. Función dentro de función ───────────────────────────
def exterior():
    def interior():
        return "función interna"
    mensaje = interior()
    print(f"exterior() llamó a interior(): '{mensaje}'")

exterior()


# ── 3. Funciones built-in del lenguaje ─────────────────────
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista original : {numeros}")
print(f"len()  → longitud  : {len(numeros)}")
print(f"max()  → máximo    : {max(numeros)}")
print(f"min()  → mínimo    : {min(numeros)}")
print(f"sum()  → suma      : {sum(numeros)}")
print(f"sorted() → ordenada: {sorted(numeros)}")

texto = "  Python es genial  "
print(f"strip()  → '{texto.strip()}'")
print(f"upper()  → '{texto.strip().upper()}'")
print(f"replace()→ '{texto.strip().replace('genial', 'increíble')}'")


# ── 4. Variables LOCAL y GLOBAL ────────────────────────────
contador = 0          # variable GLOBAL

def incrementar():
    local_var = 10    # variable LOCAL (solo existe aquí)
    global contador   # accedemos a la variable global
    contador += 1
    print(f"  Dentro de incrementar() → local_var={local_var}, contador={contador}")

print(f"Antes de llamar: contador={contador}")
incrementar()
incrementar()
print(f"Después de 2 llamadas: contador={contador}")

# local_var no existe aquí fuera:
try:
    print(local_var)
except NameError:
    print("local_var NO existe fuera de la función (es LOCAL)")