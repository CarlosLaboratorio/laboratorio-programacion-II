"""
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

rex = Perro("Rex", 3, "Labrador")
rex.ladrar()
"""



class perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
class raza(perro):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre}, de 3 años y de raza {self.raza} dice: ¡Guau!")
        

lobito = raza("lobito", 3, "Labrador")
lobito.ladrar()
