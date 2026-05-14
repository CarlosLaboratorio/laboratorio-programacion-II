# ==========================================
# EJERCICIO 3: FUNCIONES Y SCOPE
# ==========================================

# --- 1. FUNCIONES BÁSICAS ---

# Sin parámetros ni retorno
def saludo_simple():
    print("Hola! Esta es una función básica sin parámetros.")

# Con parámetros
def saludar_estudiante(nombre, institucion):
    print(f"Hola {nombre}, un gusto saludarte en {institucion}.")

# Con retorno
def calcular_area_rectangulo(base, altura):
    return base * altura

# --- 2. FUNCIONES DENTRO DE FUNCIONES ---

def funcion_externa(texto):
    print("Ejecutando la función externa...")
    
    def funcion_interna():
        print(f"Soy la función interna y recibí: '{texto}'")
    
    # Llamamos a la interna desde adentro
    funcion_interna()

# --- 3. FUNCIONES INTEGRADAS (BUILT-IN) ---

# Python ya trae muchas funciones listas para usar
numeros = [10, 50, 2, 100, 45]
maximo = max(numeros) # Encuentra el valor más alto
longitud = len(numeros) # Cuenta los elementos
redondeo = round(3.14159, 2) # Redondea a 2 decimales

# --- 4. VARIABLE LOCAL Y GLOBAL ---

variable_global = "Soy Global (estoy fuera)"

def prueba_scope():
    variable_local = "Soy Local (solo vivo aquí dentro)"
    print(f"Dentro de la función: {variable_global}")
    print(f"Dentro de la función: {variable_local}")

# --- IMPRESIÓN DE RESULTADOS ---

print("--- RESULTADOS EJERCICIO 3 ---")

saludo_simple()

saludar_estudiante("Juan", "UNNE")

resultado_area = calcular_area_rectangulo(5, 10)
print(f"El área calculada es: {resultado_area}")

print("-" * 20)
funcion_externa("Aprendiendo Python")

print("-" * 20)
print(f"Uso de max(): {maximo}")
print(f"Uso de len(): {longitud}")
print(f"Uso de round(): {redondeo}")

print("-" * 20)
prueba_scope()

# Intentar imprimir la local aquí daría error:
# print(variable_local) # <--- Si borras el '#' verás que Python falla
print(f"Fuera de la función: {variable_global}")

print("-" * 30)