"""
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio * (1 - porcentaje / 100)

laptop = Producto("Laptop", 1000)
laptop.aplicar_descuento(15)
print(laptop.precio)  
"""








 

class producto:
    def __init__(self, camiseta, precio):
        self.camiseta = camiseta
        self.precio = precio
        
    def descuento(self, porcentaje):
        self.precio = self.precio * (1 - porcentaje / 100)


camiseta1 = producto("camiseta", 2000)
print("valor sin descuento  de la camiseta:", camiseta1.precio)
camiseta1.descuento(10)
print("valor con descuento de la camiseta:", camiseta1.precio)
