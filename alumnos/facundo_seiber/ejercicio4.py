productos = {
    1:  {"nombre": "Sensor Ultrasonido HC-SR04",  "categoria": "Sensores",    "precio": 1800, "stock": 25},
    2:  {"nombre": "Placa Arduino UNO R3",         "categoria": "Placas",      "precio": 9500, "stock": 12},
    3:  {"nombre": "Servo Motor SG90",             "categoria": "Motores",     "precio": 1200, "stock": 30},
    4:  {"nombre": "Módulo Bluetooth HC-05",       "categoria": "Módulos",     "precio": 2500, "stock": 18},
    5:  {"nombre": "Sensor de Temperatura DHT11",  "categoria": "Sensores",    "precio": 1600, "stock": 22},
    6:  {"nombre": "Motor DC 6V",                  "categoria": "Motores",     "precio":  900, "stock": 40},
    7:  {"nombre": "Módulo RFID RC522",             "categoria": "Módulos",     "precio": 2800, "stock": 15},
    8:  {"nombre": "Display LCD 16x2",             "categoria": "Pantallas",   "precio": 3100, "stock": 10},
    9:  {"nombre": "Matriz LED 8x8",               "categoria": "Pantallas",   "precio": 2900, "stock": 14},
    10: {"nombre": "Sensor Infrarrojo",            "categoria": "Sensores",    "precio": 1100, "stock": 28},
    11: {"nombre": "Placa ESP32 WiFi",             "categoria": "Placas",      "precio": 8500, "stock":  9},
    12: {"nombre": "Buzzer Activo 5V",             "categoria": "Sonido",      "precio":  700, "stock": 45},
    13: {"nombre": "Joystick Módulo KY-023",       "categoria": "Control",     "precio": 1300, "stock": 20},
    14: {"nombre": "Sensor de Luz LDR",            "categoria": "Sensores",    "precio":  600, "stock": 50},
    15: {"nombre": "LED RGB Difuso",               "categoria": "Iluminación", "precio":  400, "stock": 60},
    16: {"nombre": "Fuente 9V 1A",                 "categoria": "Fuentes",     "precio": 2100, "stock": 17},
    17: {"nombre": "Cable USB Arduino",            "categoria": "Accesorios",  "precio":  900, "stock": 35},
    18: {"nombre": "Módulo Rele 5V",               "categoria": "Módulos",     "precio": 1700, "stock": 25},
    19: {"nombre": "Sensor de Gas MQ-2",           "categoria": "Sensores",    "precio": 1900, "stock": 13},
    20: {"nombre": "Shield Motores L293D",         "categoria": "Placas",      "precio": 3700, "stock": 11},
}

def mostrar_productos():
    print("\n========================================")
    print("      LISTADO DE PRODUCTOS DISPONIBLES  ")
    print("========================================")
    print(f"{'ID':<4} {'Nombre':<35} {'Categoría':<14} {'Precio':>8}  {'Stock':>6}")
    print("-" * 72)
    for id, datos in productos.items():
        print(f"{id:<4} {datos['nombre']:<35} {datos['categoria']:<14} ${datos['precio']:>7}  {datos['stock']:>6}")
    print("-" * 72)


def agregar_producto():
    print("\n--- AGREGAR NUEVO PRODUCTO ---")

    nuevo_id = max(productos.keys()) + 1

    nombre    = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio    = float(input("Precio: "))   
    stock     = int(input("Stock disponible: "))  
   
    productos[nuevo_id] = {
        "nombre":    nombre,
        "categoria": categoria,
        "precio":    precio,
        "stock":     stock
    }

    print(f"\nProducto '{nombre}' agregado correctamente con ID {nuevo_id}.")


def modificar_stock():
    print("\n--- MODIFICAR STOCK ---")
    mostrar_productos()

    id_modificar = int(input("\nIngrese el ID del producto a modificar: "))


    if id_modificar in productos:
        print(f"  Producto: {productos[id_modificar]['nombre']}")
        print(f"  Stock actual: {productos[id_modificar]['stock']}")
        nuevo_stock = int(input("  Nuevo stock: "))


        productos[id_modificar]["stock"] = nuevo_stock

        print("Stock actualizado correctamente.")
    else:
        print("ID no encontrado.")


# ----------------------------
# FUNCIÓN: Eliminar producto
# ----------------------------

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    mostrar_productos()

    id_eliminar = int(input("\nIngrese el ID del producto a eliminar: "))


    if id_eliminar in productos:

        eliminado = productos.pop(id_eliminar)
        print(f"Producto '{eliminado['nombre']}' eliminado correctamente.")
    else:
        print("ID no válido.")


# ----------------------------
# MENU
# ---------------------------

def menu():
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE PRODUCTOS DE ROBÓTICA =====")
        print("  1. Mostrar todos los productos")
        print("  2. Buscar producto por nombre")
        print("  3. Agregar nuevo producto")
        print("  4. Modificar stock")
        print("  5. Eliminar producto")
        print("  6. Salir")
        print("========================================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            termino = input("Ingrese nombre o parte del nombre: ")

            encontrado = False
            for id, datos in productos.items():
                if termino.lower() in datos["nombre"].lower():
                    print(f"  {id:02d} | {datos['nombre']} | ${datos['precio']} | Stock: {datos['stock']}")
                    encontrado = True
            if not encontrado:
                print("No se encontró ningún producto.")
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            modificar_stock()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("\nSaliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print(" Opción inválida. Intente nuevamente.")

menu()