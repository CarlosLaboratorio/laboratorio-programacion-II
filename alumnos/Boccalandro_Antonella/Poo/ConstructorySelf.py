class Estudiante:

    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

alumno1 = Estudiante("Antonella", "Desarrollo de Software")

print(alumno1.nombre)
print(alumno1.carrera)