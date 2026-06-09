class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.leido = False

libro1 = Libro("Cien años de soledad", "García Márquez", 500)
print(libro1.titulo) 
print(libro1.autor) 
print(libro1.paginas)   
print(libro1.leido)   
   