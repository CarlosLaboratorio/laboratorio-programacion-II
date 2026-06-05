class Celular:

    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        return f"""
Marca: {self.marca}
Modelo: {self.modelo}
Precio: ${self.precio}
"""

celular1 = Celular("Samsung", "S26", 650000)
celular2 = Celular("Iphone", "15pro", 700000)

print(celular1.mostrar_info())
print(celular2.mostrar_info())