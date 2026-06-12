class Personaje:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Semidios(Personaje):
    def __init__(self, nombre, edad, gran_runa):
        super().__init__(nombre, edad)
        self.gran_runa = gran_runa


class Empireo(Semidios):
    def __init__(self, nombre, edad, gran_runa, dios_exterior):
        super().__init__(nombre, edad, gran_runa)
        self.dios_exterior = dios_exterior


class Malenia(Empireo):
    def __init__(self):
        super().__init__(
            "Malenia",
            33,
            "Gran Runa de Malenia",
            "Diosa de la Putrefacción"
        )

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, portadora de la {self.gran_runa}."
    
    def presentacion(self):
        print(f"I am {self.nombre}, Blade of Miquella.")
    
        
mipjfavorito = Malenia()

print(mipjfavorito)
mipjfavorito.presentacion()