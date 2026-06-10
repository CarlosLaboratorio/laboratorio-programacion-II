 #ejercicios del power point
 
 #ejer8
 
class Auto:
    marca = "Toyota"
    color = "Blanco"
    modelo = "Corolla"
    precio = 25000

miAuto = Auto()

print(miAuto.marca)


#----------------------------------------


#ejer9
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

m1 = Mascota("Firulais", 5)

#-----------------------------------------

#ejer10
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
        
#------------------------------------------

#ejer11
class Celular:
    def __init__(self, marca, modelo, precio, color):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.encendido = False
        
#_____________________________________________________

#ejer12

class Auto:

    def __init__(self, marca, modelo, precio, color):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color

    def infoAuto(self):
        info = f"Descripción del auto:\n Marca: {self.marca}\n Modelo: {self.modelo}\n Precio: ${self.precio:.2f}\n Color: {self.color}"
        return info
    
    
#-----------------------------------------------------

#ejer13
class Zapatillas:
    def __init__(self, marca, precio, talle, color):
        self.marca = marca
        self.precio = precio
        self.talle = talle
        self.color = color

    def aplicarDescuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def infoProducto(self):
        return f"{self.marca} - ${self.precio} - Talle: {self.talle} - Color: {self.color}"

zapatillas = Zapatillas("Adidas", 120, "42", "azul")
zapatillasNike = Zapatillas("Nike", 180, "40", "negro")

print(zapatillas.precio)
print(zapatillasNike.marca)

zapatillasNike.aplicarDescuento(50)
print(zapatillasNike.precio)

print(zapatillas.infoProducto())
print(zapatillasNike.infoProducto())

#------------------------------------------------------
#ejer15


class Vehiculo:
    def __init__(self, nombre, tipo, material, marca, peso, dimensions, año_fabricado):
        self.nombre = nombre
        self.tipo = tipo
        self.material = material
        self.marca = marca
        self.peso = peso
        self.dimensions = dimensions
        self.año_fabricado = año_fabricado


class AutoDeportivo(Vehiculo):
    def __init__(self, nombre, tipo, material, marca, peso, dimensions, año_fabricado, n_cilindros, tipo_motor, turbo, alerón):
        super().__init__(nombre, tipo, material, marca, peso, dimensions, año_fabricado)
        self.n_cilindros = n_cilindros
        self.tipo_motor = tipo_motor
        self.turbo = turbo
        self.alerón = alerón
        
    def __str__(self):
        return f"Deportivo {self.nombre} ({self.marca}) - {self.n_cilindros} cilindros, Motor: {self.tipo_motor}"



   




