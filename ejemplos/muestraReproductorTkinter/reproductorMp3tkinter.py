# pip install Pillow pygame

from tkinter import *
from PIL import ImageTk, Image
import pygame

# Inicializar pygame mixer
pygame.mixer.init()

ventana = Tk()
ventana.title("Reproductor MP3")
ventana.geometry("700x450")
ventana.config(bg='dark slate gray')

ventana.imagenes = []

# Función reproducir
def reproducir():
    pygame.mixer.music.load(".\ejemplos\muestraReproductorTkinter\musica.mp3")
    pygame.mixer.music.play()

    imagen = ImageTk.PhotoImage(
        Image.open(".\ejemplos\muestraReproductorTkinter\musica.jpg").resize((300,300))
    )

    label = Label(image=imagen)
    label.place(x=300, y=50)

    titulo = Label(
        ventana,
        text="Reproduciendo Poison - Something To Believe In",
        font=("Arial",14)
    )

    titulo.place(x=240, y=20)

    ventana.imagenes.append(imagen)

# Función pausar
def pausar():
    pygame.mixer.music.pause()

# Función continuar
def continuar():
    pygame.mixer.music.unpause()

# Función detener
def detener():
    pygame.mixer.music.stop()

Button(
    ventana,
    text="▶ Reproducir",
    command=reproducir
).place(x=40, y=50)

Button(
    ventana,
    text="⏸ Pausar",
    command=pausar
).place(x=40, y=100)

Button(
    ventana,
    text="⏯ Continuar",
    command=continuar
).place(x=40, y=150)

Button(
    ventana,
    text="⏹ Detener",
    command=detener
).place(x=40, y=200)

ventana.mainloop()