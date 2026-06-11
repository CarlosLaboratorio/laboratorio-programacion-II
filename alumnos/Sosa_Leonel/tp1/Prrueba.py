class Ropa:
    def __init__(self, talla, color, marca):
        self.talla = talla
        self.color = color
        self.marca = marca




pantalons = Ropa("L", "Azul", "Levi's")
remerona = Ropa("M", "Roja", "Nike")
campera = Ropa("S", "Negra", "Adidas")



def infoproducto(producto):
    print(f"Producto: {producto.marca}, Color: {producto.color}, Talla: {producto.talla}")  
infoproducto(remerona)
infoproducto(pantalons)
infoproducto(campera)
