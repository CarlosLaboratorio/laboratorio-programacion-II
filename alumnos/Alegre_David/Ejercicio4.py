# sistema_stock_robotica.py

productos = {
    1: {"nombre": "Sensor Ultrasonido HC-SR04", "categoria": "Sensores", "precio": 1800, "stock": 25},
    2: {"nombre": "Placa Arduino UNO R3", "categoria": "Placas", "precio": 9500, "stock": 12},
    3: {"nombre": "Servo Motor SG90", "categoria": "Motores", "precio": 1200, "stock": 30},
    4: {"nombre": "Módulo Bluetooth HC-05", "categoria": "Módulos", "precio": 2500, "stock": 18},
    5: {"nombre": "Sensor de Temperatura DHT11", "categoria": "Sensores", "precio": 1600, "stock": 22},
    6: {"nombre": "Motor DC 6V", "categoria": "Motores", "precio": 900, "stock": 40},
    7: {"nombre": "Módulo RFID RC522", "categoria": "Módulos", "precio": 2800, "stock": 15},
    8: {"nombre": "Display LCD 16x2", "categoria": "Pantallas", "precio": 3100, "stock": 10},
    9: {"nombre": "Matriz LED 8x8", "categoria": "Pantallas", "precio": 2900, "stock": 14},
    10: {"nombre": "Sensor Infrarrojo", "categoria": "Sensores", "precio": 1100, "stock": 28},
    11: {"nombre": "Placa ESP32 WiFi", "categoria": "Placas", "precio": 8500, "stock": 9},
    12: {"nombre": "Buzzer Activo 5V", "categoria": "Sonido", "precio": 700, "stock": 45},
    13: {"nombre": "Joystick Módulo KY-023", "categoria": "Control", "precio": 1300, "stock": 20},
    14: {"nombre": "Sensor de Luz LDR", "categoria": "Sensores", "precio": 600, "stock": 50},
    15: {"nombre": "LED RGB Difuso", "categoria": "Iluminación", "precio": 400, "stock": 60},
    16: {"nombre": "Fuente 9V 1A", "categoria": "Fuentes", "precio": 2100, "stock": 17},
    17: {"nombre": "Cable USB Arduino", "categoria": "Accesorios", "precio": 900, "stock": 35},
    18: {"nombre": "Módulo Rele 5V", "categoria": "Módulos", "precio": 1700, "stock": 25},
    19: {"nombre": "Sensor de Gas MQ-2", "categoria": "Sensores", "precio": 1900, "stock": 13},
    20: {"nombre": "Shield Motores L293D", "categoria": "Placas", "precio": 3700, "stock": 11},
}

def listar_productos():
    if not productos:
        print("No hay productos en el inventario.")
        return
    print("\n--- Listado de productos ---")
    print(f"{'ID':<4} {'Nombre':<30} {'Categoría':<15} {'Precio':>8} {'Stock':>6}")
    print("-" * 70)
    for id_prod, datos in productos.items():
        print(f"{id_prod:<4} {datos['nombre']:<30} {datos['categoria']:<15} "
              f"${datos['precio']:>7} {datos['stock']:>6}")
    print()

def buscar_producto():
    if not productos:
        print("No hay productos para buscar.")
        return
    busqueda = input("Ingrese el nombre o parte del producto a buscar: ").lower()
    encontrados = []
    for id_prod, datos in productos.items():
        if busqueda in datos['nombre'].lower():
            encontrados.append((id_prod, datos))
    if encontrados:
        print("\n--- Resultados de búsqueda ---")
        for id_prod, datos in encontrados:
            print(f"ID:{id_prod} | {datos['nombre']} | {datos['categoria']} | ${datos['precio']} | Stock:{datos['stock']}")
    else:
        print("No se encontraron productos con ese nombre.")

def agregar_producto():
    print("\n--- Agregar nuevo producto ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    categoria = input("Categoría: ").strip()
    if not categoria:
        categoria = "General"
    try:
        precio = int(input("Precio (en pesos): "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Error: Precio y stock deben ser números enteros.")
        return
    nuevo_id = max(productos.keys()) + 1 if productos else 1
    productos[nuevo_id] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    print(f"Producto '{nombre}' agregado con ID {nuevo_id}.\n")

def modificar_producto():
    if not productos:
        print("No hay productos para modificar.")
        return
    try:
        id_mod = int(input("Ingrese el ID del producto a modificar: "))
    except ValueError:
        print("ID inválido.")
        return
    if id_mod not in productos:
        print(f"No existe un producto con ID {id_mod}.")
        return
    datos = productos[id_mod]
    print(f"Modificando producto: {datos['nombre']}")
    print("Campos disponibles: nombre, categoria, precio, stock")
    campo = input("¿Qué campo desea modificar? ").lower()
    if campo not in ["nombre", "categoria", "precio", "stock"]:
        print("Campo no válido.")
        return
    nuevo_valor = input(f"Nuevo valor para {campo}: ")
    if campo in ["precio", "stock"]:
        try:
            nuevo_valor = int(nuevo_valor)
        except ValueError:
            print("Error: El precio y stock deben ser números enteros.")
            return
    datos[campo] = nuevo_valor
    print(f"Producto ID {id_mod} actualizado correctamente.\n")

def eliminar_producto():
    if not productos:
        print("No hay productos para eliminar.")
        return
    try:
        id_elim = int(input("Ingrese el ID del producto a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    if id_elim in productos:
        nombre_elim = productos[id_elim]["nombre"]
        confirm = input(f"¿Seguro que desea eliminar '{nombre_elim}'? (s/n): ").lower()
        if confirm == 's':
            del productos[id_elim]
            print(f"Producto ID {id_elim} eliminado.\n")
        else:
            print("Eliminación cancelada.\n")
    else:
        print(f"No existe producto con ID {id_elim}.\n")

def main():
    while True:
        print("\n===== Sistema de Gestión de Stock Robótica =====")
        print("1. Listar productos")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()# Fin del codigo
# Fin del codigo