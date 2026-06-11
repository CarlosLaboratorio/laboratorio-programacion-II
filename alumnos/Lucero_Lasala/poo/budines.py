class Budin:

    def __init__(self, sabor, tamano, relleno, precio):
        self.sabor = sabor
        self.tamano = tamano
        self.relleno = relleno
        self.precio = precio
        
    def mostrar_info(self):
        return f"""
Sabor: {self.sabor}
Tamaño: {self.tamano}
Relleno: {self.relleno}
Precio: ${self.precio}
"""

budin1 = Budin("Marmolado", "Grande", "Dulce de leche", 3500)
budin2 = Budin("Banana", "Mediano", "Chips de chocolate", 2700)
budin3 = Budin("Coco y dulce de leche", "Mini", "Sin relleno", 1800)
budin4 = Budin(Naranja, "Grande", "Chips de chocolate blanco", 3800)

print(budin1.mostrar_info())
print(budin2.mostrar_info())
print(budin3.mostrar_info())
print(budin4.mostrar_info())