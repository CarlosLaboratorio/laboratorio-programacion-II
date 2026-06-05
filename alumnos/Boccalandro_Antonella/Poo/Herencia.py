class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Auto(Vehiculo):

    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_puertas(self):
        print(f"Cantidad de puertas: {self.puertas}")


auto1 = Auto("Toyota", "Corolla", 4)

auto1.mostrar_datos()
auto1.mostrar_puertas()