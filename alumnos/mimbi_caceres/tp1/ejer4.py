productos = {
    "sensor": {"precio": 1500, "cantidad": 10},
    "motor": {"precio": 3000, "cantidad": 5}
}


def mostrar_productos():
    print("\n--- LISTADO DE PRODUCTOS ---")
    for nombre, datos in productos.items():
        print(f"{nombre} -> Precio: {datos['precio']} | Cantidad: {datos['cantidad']}")


def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in productos:
        datos = productos[nombre]
        print(f"Encontrado: {nombre} -> Precio: {datos['precio']} | Cantidad: {datos['cantidad']}")
    else:
        print("Producto no encontrado")


def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = int(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    productos[nombre] = {"precio": precio, "cantidad": cantidad}
    print("Producto agregado correctamente")


def modificar_producto():
    nombre = input("Producto a modificar: ")
    if nombre in productos:
        precio = int(input("Nuevo precio: "))
        cantidad = int(input("Nueva cantidad: "))

        productos[nombre]["precio"] = precio
        productos[nombre]["cantidad"] = cantidad
        print("Producto modificado")
    else:
        print("Producto no existe")


def eliminar_producto():
    nombre = input("Producto a eliminar: ")
    if nombre in productos:
        del productos[nombre]
        print("Producto eliminado")
    else:
        print("Producto no existe")


def menu():
    while True:
        print("\n--- SISTEMA DE STOCK ROBÓTICA ---")
        print("1. Ver productos")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Modificar producto")
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