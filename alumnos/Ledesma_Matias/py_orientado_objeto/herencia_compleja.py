class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada, tipo_motor):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
        self.tipo_motor = tipo_motor

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo} ({self.año}), {self.cilindrada}cc, motor {self.tipo_motor}"

mi_moto = Moto("Honda", "CBR", 2022, 600, "4T")
print(mi_moto)