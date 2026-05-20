# =====================================================
# Sistema de Gestión de Productos de Robótica
# Autor: Alumno de 6º Año - Laboratorio de Programación III
# =====================================================

# Base de datos simulada con diccionario

#1. Elegir uno de estos temas para el ejemplo de simulación de manejo de stock de robótica desde la terminal utilizando diccionarios (tipo de datos de colección):
    
#    Creación de diccionario, listado de productos disponibles, busqueda del producto y salir del sistema.
#    Listado del menú del sistema, funciones para Agregar, modificar y eliminar los productos.


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



def menu():
    
    print("Bienvenido al sistema de Control de productos de Robotica")
    print("1. Mostrar todos los productos")
    print("2. Buscar producto por nombre")
    print("3. Agregar nuevo producto")
    print("4. Modificar stock")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    return opcion

def mostrarProductos():

    for id, datos in productos.items():
        print(f"{id:02d} | {datos['nombre']} | {datos['categoria']} | ${datos['precio']} | Stock: {datos['stock']}")
       
    print("\n")

def buscarProducto(nombre):
    
    print(f"Nombre a buscar {nombre}")
    encontrado = False
    for id, datos in productos.items():
        if(nombre.lower() in datos["nombre"].lower()):
            print(f"ID: {id:02d} | {datos['nombre']} | {datos['categoria']} | ${datos['precio']} | Stock: {datos['stock']}")
            encontrado = True

    if not encontrado:
        print("El producto no se encontro")



def agregarProducto():

    nuevo_id = max(productos.keys()) + 1
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    precio = int(input("Ingrese el precio: "))
    stock = int(input("Ingrese la cantidad de productos: "))

    productos[nuevo_id] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    print(f"se agrego el producto {nombre} con el id {nuevo_id}")


def modificarStock(idProducto):

    if(idProducto in productos):
        nuevoStock = int(input("Ingrese el nuevo stock: "))
        productos[idProducto]["stock"] = nuevoStock
        print("Stock actualizado \n") 
    else:
        print("No se encontro el id \n") 
   
def eliminarProducto():
    
    mostrarProductos()
    idProducto = int(input("Ingrese el id del producto a eliminar: "))
    if(idProducto in productos):
        productos.pop(idProducto)
        print("El producto se elimino correctamente \n")
    else:
        print("No se encontro el id del producto")


def main():
    
    while True:
        
        opcion = menu()

        match opcion:

            case "1":
                mostrarProductos()

            case "2":
                buscarProducto(input("Ingrese el nombre completo o parcial del producto: "))

            case "3":
                agregarProducto()
            
            case "4":
                modificarStock(int(input("Ingrese el id del producto: ")))

            case "5":
                eliminarProducto()

            case "6":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opcion no valida")



main()