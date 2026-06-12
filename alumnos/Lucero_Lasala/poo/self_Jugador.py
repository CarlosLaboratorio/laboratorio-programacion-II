class Jugador: 
    def __init__(self, nickname, level):
        self.nickname = nickname
        self.level = level
       
       
    def resumen_jugador(self):
        return f"El usuario de este jugador es {self.nickname} y está en el nivel {self.level} del juego."

jugador1 = Jugador("metanoia323", 203)
jugador2 = Jugador("cocteautwinslover235", 442)
print(jugador1.resumen_jugador())
print(jugador2.resumen_jugador())