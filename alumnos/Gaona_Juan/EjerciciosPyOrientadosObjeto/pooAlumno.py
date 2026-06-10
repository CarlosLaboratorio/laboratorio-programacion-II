class alumno: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
       
       
    def resumen(self):
        return f"El alumno se llama {self.nombre} y tiene {self.edad} años."

"""
alumno1 = alumno("Juan", 31)
alumno2 = alumno("Juan", 31)
print(alumno1.nombre, alumno2.edad)
"""

alumno1 = alumno("Juan", 31)
alumno2 = alumno("Juan", 31)
print(alumno1.resumen())
print(alumno2.resumen())