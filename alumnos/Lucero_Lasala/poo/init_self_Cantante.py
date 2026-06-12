class Cantante:
    def __init__(self, nombre, edad, rango_vocal):
        self.nombre = nombre
        self.edad = edad
        self.rango_vocal = rango_vocal
        
    def presentarse(self):
        return f"Hola, buenas tardes! Soy {self.nombre}, tengo {self.edad} años y mi rango vocal es {self.rango_vocal}."
        
        
vozprincipal1 = Cantante ("Lucero", 23, "Contralto")
vozsecundaria1 = Cantante ("Leo", 22, "Tenor")
vozsecundaria2 = Cantante ("Lola", 13, "Soprano")

print(vozprincipal1.nombre)
print(vozprincipal1.rango_vocal)
print(vozprincipal1.presentarse())
print(vozsecundaria1.nombre)
print(vozsecundaria1.rango_vocal)
print(vozsecundaria1.presentarse())
print(vozsecundaria2.nombre)
print(vozsecundaria2.rango_vocal)
print(vozsecundaria2.presentarse()) 