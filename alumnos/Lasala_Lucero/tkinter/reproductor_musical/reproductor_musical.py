from PIL import Image
import customtkinter as ctk
import pygame
from tkinter import filedialog
import os

# ---------------- config de la interfaz ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

pygame.mixer.init()

cancion_actual = None
pausado = False

# ---------------- funciones ----------------

def cargar_cancion():
    global cancion_actual, pausado

    archivo = filedialog.askopenfilename(
        title="select you fav song",
        filetypes=[("MP3", "*.mp3")]
    )

    if archivo:
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(archivo)

            cancion_actual = archivo
            pausado = False

            nombre = os.path.basename(archivo)
            label_cancion.configure(text=f"♪ {nombre}")

            label_estado.configure(text="loaded… (¬‿¬)")

            btn_play.configure(state="normal")
            btn_pause.configure(state="normal")
            btn_stop.configure(state="normal")

        except Exception as e:
            label_estado.configure(text="error loading file")


# cancion recomendada establecida por defecto
def cargar_default():
    global cancion_actual

    try:
        ruta = r"C:\Users\lucer\Documents\labprog2\laboratorio-programacion-II\alumnos\Lasala_Lucero\tkinter\reproductor_musical\lapatita.mp3" 
        pygame.mixer.music.load(ruta)

        cancion_actual = ruta

        nombre = os.path.basename(ruta)
        label_cancion.configure(text=f"♪ {nombre} (canción recomendada por lucero)")

        label_estado.configure(text="dale a play y disfrutá (¬‿¬)")

        btn_play.configure(state="normal")
        btn_pause.configure(state="normal")
        btn_stop.configure(state="normal")

    except Exception:
        label_estado.configure(text="no default song found")


def reproducir():
    global pausado

    if not cancion_actual:
        return

    if pausado:
        pygame.mixer.music.unpause()
        pausado = False
    else:
        pygame.mixer.music.play()

    label_estado.configure(text="▶ playing…")

def pausar():
    global pausado

    if cancion_actual:
        pygame.mixer.music.pause()
        pausado = True
        label_estado.configure(text="⏸ paused")

def detener():
    global pausado

    if cancion_actual:
        pygame.mixer.music.stop()
        pausado = False
        label_estado.configure(text="■ stopped")

# ---------------- ui ----------------

ventana = ctk.CTk()
ventana.title("♯ reproductor alternativo ♯")
ventana.geometry("600x650")
ventana.configure(fg_color="#0d0d0d")

frame = ctk.CTkFrame(
    ventana,
    fg_color="#111111",
    corner_radius=0,
    border_width=1,
    border_color="#2a2a2a"
)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# ---------------- img ----------------

try:
    img = Image.open(r"C:\Users\lucer\Documents\labprog2\laboratorio-programacion-II\alumnos\Lasala_Lucero\tkinter\reproductor_musical\imagen.png")

    img_ctk = ctk.CTkImage(
        light_image=img,
        dark_image=img,
        size=(320, 320)
    )

    label_img = ctk.CTkLabel(frame, image=img_ctk, text="")
    label_img.image = img_ctk
    label_img.pack(pady=15)

except Exception as e:
    ctk.CTkLabel(frame, text="(no image)", text_color="#8a8a8a").pack(pady=15)

# ---------------- text ----------------

ctk.CTkLabel(
    frame,
    text="♯ reproductor musical ♯",
    font=("Consolas", 20, "bold"),
    text_color="#d0d0d0"
).pack(pady=5)

label_cancion = ctk.CTkLabel(
    frame,
    text="no track loaded",
    font=("Consolas", 14),
    text_color="#8a8a8a"
)
label_cancion.pack(pady=5)

label_estado = ctk.CTkLabel(
    frame,
    text="waiting… (¬‿¬)",
    font=("Consolas", 12),
    text_color="#8a8a8a"
)
label_estado.pack(pady=5)

# ---------------- buttons ----------------

botones = ctk.CTkFrame(frame, fg_color="transparent")
botones.pack(pady=25)

ctk.CTkButton(
    botones,
    text="⟐ load",
    command=cargar_cancion,
    fg_color="#1a1a1a",
    hover_color="#3a0000",
    text_color="#d0d0d0",
    border_width=1,
    border_color="#2a2a2a",
    font=("Consolas", 12)
).grid(row=0, column=0, padx=6, pady=6)

btn_play = ctk.CTkButton(
    botones,
    text="▶ play",
    command=reproducir,
    state="disabled",
    fg_color="#1a1a1a",
    hover_color="#3a0000",
    text_color="#d0d0d0",
    border_width=1,
    border_color="#2a2a2a",
    font=("Consolas", 12)
)
btn_play.grid(row=0, column=1, padx=6, pady=6)

btn_pause = ctk.CTkButton(
    botones,
    text="⏸ pause",
    command=pausar,
    state="disabled",
    fg_color="#1a1a1a",
    hover_color="#3a0000",
    text_color="#d0d0d0",
    border_width=1,
    border_color="#2a2a2a",
    font=("Consolas", 12)
)
btn_pause.grid(row=1, column=0, padx=6, pady=6)

btn_stop = ctk.CTkButton(
    botones,
    text="■ stop",
    command=detener,
    state="disabled",
    fg_color="#1a1a1a",
    hover_color="#3a0000",
    text_color="#d0d0d0",
    border_width=1,
    border_color="#2a2a2a",
    font=("Consolas", 12)
)
btn_stop.grid(row=1, column=1, padx=6, pady=6)

# ---------------- cargar tema recomendado ----------------

cargar_default()

# ---------------- correr reproductor ----------------

ventana.mainloop()