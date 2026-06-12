class Juego:
    def __init__(self, nombre, genero, dificultad, favorito):
        self.nombre = nombre
        self.genero = genero
        self.dificultad = dificultad
        self.favorito = favorito
                
juego1 = Juego ("Elden Ring", "RPG", "Dificil", True)
juego2 = Juego ("Stardew Valley", "Simulación", "Fácil", True)
juego3 = Juego("League of Legends", "MOBA", "Media", False)

print(juego1.nombre) 
print(juego1.genero) 
print(juego1.dificultad)
print(juego1.favorito)

print(juego2.nombre) 
print(juego2.genero) 
print(juego2.dificultad)
print(juego2.favorito)

print(juego3.nombre) 
print(juego3.genero) 
print(juego3.dificultad)
print(juego3.favorito)