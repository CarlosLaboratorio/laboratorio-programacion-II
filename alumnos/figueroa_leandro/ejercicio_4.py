# =====================================================
# Sistema de Gestión de Productos de Robótica
# Autor: Alumno de 6º Año - Laboratorio de Programación III
# =====================================================

# Base de datos simulada con diccionario
productos = {
    1: {"nombre": "Sensor Ultrasonido HC-SR04", "categoria": "Sensores", "precio": 1800, "stock": 20},
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


# ----------------------------
# FUNCIONES DEL PROGRAMA
# ----------------------------

def mostrar_productos():
    print("\nListado de productos disponibles:\n")
    for id, datos in productos.items():
        print(f"{id:02d} | {datos['nombre']} | {datos['categoria']} | ${datos['precio']} | Stock: {datos['stock']}")


def buscar_producto(nombre_buscar):
    print(f"\n🔍 Resultados de búsqueda para: '{nombre_buscar}'\n")
    encontrado = False
    for id, datos in productos.items():
        if nombre_buscar.lower() in datos["nombre"].lower():
            print(f"{id:02d} | {datos['nombre']} | ${datos['precio']} | Stock: {datos['stock']}")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún producto con ese nombre.")


def agregar_producto():
    nuevo_id = max(productos.keys()) + 1
    nombre = input("Ingrese nombre del producto: ")
    categoria = input("Ingrese categoría: ")
    precio = float(input("Ingrese precio: "))
    stock = int(input("Ingrese stock disponible: "))

    productos[nuevo_id] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    print(f"\n✅ Producto '{nombre}' agregado correctamente con ID {nuevo_id}.")


def modificar_stock():
    mostrar_productos()
    id_modificar = int(input("\nIngrese el ID del producto a modificar stock: "))
    if id_modificar in productos:
        nuevo_stock = int(input("Ingrese nuevo stock: "))
        productos[id_modificar]["stock"] = nuevo_stock
        print("✅ Stock actualizado correctamente.")
    else:
        print("❌ ID no encontrado.")


def eliminar_producto():
    mostrar_productos()
    id_eliminar = int(input("\nIngrese el ID del producto a eliminar: "))
    if id_eliminar in productos:
        eliminado = productos.pop(id_eliminar)
        print(f"❌ Producto '{eliminado['nombre']}' eliminado correctamente.")
    else:
        print("ID no válido.")


# ----------------------------
# MENÚ PRINCIPAL
# ----------------------------

def menu():
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE PRODUCTOS DE ROBÓTICA =====")
        print("1. Mostrar todos los productos")
        print("2. Buscar producto por nombre")
        print("3. Agregar nuevo producto")
        print("4. Modificar stock")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            buscar_producto(input("Ingrese nombre o parte del nombre: "))
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
            print("Opción inválida. Intente nuevamente.")


# Programa principal
menu()