class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        
estudiante1 = Estudiante ("Juan Maria", 31)
print(estudiante1.nombre)