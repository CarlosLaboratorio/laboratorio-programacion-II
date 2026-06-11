class Budin:

    def __init__(self, sabor, tamano, precio, relleno):
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

print(budin1.mostrar_info())
print(budin2.mostrar_info())