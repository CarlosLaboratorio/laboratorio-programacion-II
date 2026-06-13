class Personaje:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Semidios(Personaje):
    def __init__(self, nombre, edad, gran_runa):
        super().__init__(nombre, edad)
        self.gran_runa = gran_runa

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, portador de la {self.gran_runa}."


malenia = Semidios(
    "Malenia",
    33,
    "Gran Runa de Malenia"
)

print(malenia)