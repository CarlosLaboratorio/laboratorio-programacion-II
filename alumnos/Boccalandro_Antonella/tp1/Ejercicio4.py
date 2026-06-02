# ============================
# SISTEMA DE STOCK - TECNOLOGÍA
# ============================

productos = {
    1: {"nombre": "Teclado mecánico RGB", "categoria": "Periféricos", "precio": 15000, "stock": 8},
    2: {"nombre": "Mouse gamer", "categoria": "Periféricos", "precio": 8000, "stock": 15},
    3: {"nombre": "Auriculares inalámbricos", "categoria": "Audio", "precio": 12000, "stock": 10}
}

def mostrar_productos():
    print("\n--- LISTADO DE PRODUCTOS ---")
    for id, datos in productos.items():
        print(f"{id} - {datos['nombre']} | {datos['categoria']} | ${datos['precio']} | Stock: {datos['stock']}")

def buscar_producto():
    nombre = input("Ingrese nombre del producto: ").lower()
    encontrado = False

    for id, datos in productos.items():
        if nombre in datos["nombre"].lower():
            print(f"{id} - {datos['nombre']} | Stock: {datos['stock']}")
            encontrado = True

    if not encontrado:
        print("Producto no encontrado")

def agregar_producto():
    nuevo_id = max(productos.keys()) + 1

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    productos[nuevo_id] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    print("Producto agregado correctamente")


def modificar_producto():
    id_mod = int(input("Ingrese ID a modificar: "))

    if id_mod in productos:
        nuevo_stock = int(input("Nuevo stock: "))
        productos[id_mod]["stock"] = nuevo_stock
        print("Stock actualizado")
    else:
        print("ID no encontrado")


def eliminar_producto():
    id_elim = int(input("Ingrese ID a eliminar: "))

    if id_elim in productos:
        eliminado = productos.pop(id_elim)
        print(f"Producto {eliminado['nombre']} eliminado")
    else:
        print("ID inválido")

def menu():
    while True:
        print("\n===== TIENDA DE TECNOLOGÍA =====")
        print("1. Mostrar productos")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Modificar stock")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

menu()