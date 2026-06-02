# Base de datos de stock de indumentaria
productos = {
    1: {"nombre": "Remera Básica", "categoria": "Remeras", "precio": 2500, "stock": 40},
    2: {"nombre": "Jean Slim Fit", "categoria": "Pantalones", "precio": 5600, "stock": 20},
    3: {"nombre": "Camisa de Poplin", "categoria": "Camisas", "precio": 4200, "stock": 18},
    4: {"nombre": "Buzo con Capucha", "categoria": "Buzos", "precio": 6900, "stock": 15},
    5: {"nombre": "Falda Denim", "categoria": "Faldas", "precio": 3800, "stock": 22},
    6: {"nombre": "Chaqueta de Cuero Sintético", "categoria": "Abrigos", "precio": 9800, "stock": 10},
    7: {"nombre": "Vestido Casual", "categoria": "Vestidos", "precio": 5200, "stock": 12},
    8: {"nombre": "Pantalón Jogging", "categoria": "Deportes", "precio": 3300, "stock": 25},
    9: {"nombre": "Campera Acolchada", "categoria": "Abrigos", "precio": 11200, "stock": 8},
    10: {"nombre": "Remera Polo", "categoria": "Remeras", "precio": 3100, "stock": 30}
}


# -------------------------
# FUNCIONES
# -------------------------

def mostrar_productos():
    print("\nLISTA DE INDUMENTARIA\n")

    for id, datos in productos.items():
        print(
            id,
            "-",
            datos["nombre"],
            "| Categoria:", datos["categoria"],
            "| Precio: $", datos["precio"],
            "| Stock:", datos["stock"]
        )


def buscar_producto():
    nombre = input("\nIngrese el nombre del producto a buscar: ")

    encontrado = False

    for id, datos in productos.items():
        if nombre.lower() in datos["nombre"].lower():

            print(
                "\nID:", id,
                "|", datos["nombre"],
                "| Precio: $", datos["precio"],
                "| Stock:", datos["stock"]
            )

            encontrado = True

    if encontrado == False:
        print("Producto no encontrado.")


def agregar_producto():

    nuevo_id = max(productos.keys()) + 1

    nombre = input("Nombre del producto: ")
    categoria = input("Categoria: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    productos[nuevo_id] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    print("Producto agregado correctamente.")


def modificar_stock():

    mostrar_productos()

    id_producto = int(input("\nIngrese el ID del producto: "))

    if id_producto in productos:

        nuevo_stock = int(input("Nuevo stock: "))
        productos[id_producto]["stock"] = nuevo_stock

        print("Stock actualizado.")

    else:
        print("El ID ingresado no existe.")


def eliminar_producto():

    mostrar_productos()

    id_producto = int(input("\nIngrese el ID del producto a eliminar: "))

    if id_producto in productos:

        productos.pop(id_producto)

        print("Producto eliminado.")

    else:
        print("No existe ese ID.")


# -------------------------
# MENU PRINCIPAL
# -------------------------

def menu():

    while True:

        print("\n========== MENU ==========")
        print("1 - Mostrar productos")
        print("2 - Buscar producto")
        print("3 - Agregar producto")
        print("4 - Modificar stock")
        print("5 - Eliminar producto")
        print("6 - Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            buscar_producto()

        elif opcion == "3":
            agregar_producto()

        elif opcion == "4":
            modificar_stock()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opcion incorrecta.")


# Programa principal
menu()