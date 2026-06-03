import customtkinter as ctk
import pygame
import tkinter.filedialog as filedialog
import os

# --- Configuración de CustomTkinter ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Inicializar pygame mixer ---
pygame.mixer.init()

# --- Variables globales ---
cancion_actual = None
reproduciendo = False
pausado = False

# --- Funciones del reproductor ---

def cargar_cancion():
    global cancion_actual, reproduciendo, pausado
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo MP3",
        filetypes=[("Archivos MP3", "*.mp3")]
    )
    if archivo:
        cancion_actual = archivo
        pygame.mixer.music.load(cancion_actual)
        nombre = os.path.basename(cancion_actual)
        label_cancion.configure(text=f"🎵 {nombre}")
        reproduciendo = False
        pausado = False
        label_estado.configure(text="📀 Cargada")
        btn_play.configure(state="normal")
        btn_stop.configure(state="normal")

def reproducir():
    global reproduciendo, pausado
    if cancion_actual is None:
        return
    if pausado:
        pygame.mixer.music.unpause()
        pausado = False
        label_estado.configure(text="▶️ Reproduciendo")
    else:
        pygame.mixer.music.play()
        reproduciendo = True
        label_estado.configure(text="▶️ Reproduciendo")
    btn_pause.configure(state="normal")

def pausar():
    global pausado, reproduciendo
    if cancion_actual and pygame.mixer.music.get_busy() and not pausado:
        pygame.mixer.music.pause()
        pausado = True
        label_estado.configure(text="⏸️ Pausado")

def detener():
    global reproduciendo, pausado
    if cancion_actual:
        pygame.mixer.music.stop()
        reproduciendo = False
        pausado = False
        label_estado.configure(text="⏹️ Detenido")

# --- Crear la ventana principal ---
ventana = ctk.CTk()
ventana.title("🎧 Reproductor Simple CustomTkinter")
ventana.geometry("500x350")
ventana.resizable(False, False)

frame = ctk.CTkFrame(ventana, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label_titulo = ctk.CTkLabel(frame, text="Reproductor de Música", font=("Helvetica", 20, "bold"))
label_titulo.pack(pady=15)

label_cancion = ctk.CTkLabel(frame, text="Ninguna canción cargada", font=("Helvetica", 14))
label_cancion.pack(pady=5)

label_estado = ctk.CTkLabel(frame, text="⚪ Esperando", font=("Helvetica", 12))
label_estado.pack(pady=5)

frame_botones = ctk.CTkFrame(frame, fg_color="transparent")
frame_botones.pack(pady=20)

btn_cargar = ctk.CTkButton(frame_botones, text="📂 Cargar MP3", command=cargar_cancion, width=120)
btn_cargar.grid(row=0, column=0, padx=8, pady=5)

btn_play = ctk.CTkButton(frame_botones, text="▶️ Reproducir", command=reproducir, state="disabled", width=120)
btn_play.grid(row=0, column=1, padx=8, pady=5)

btn_pause = ctk.CTkButton(frame_botones, text="⏸️ Pausar", command=pausar, state="disabled", width=120)
btn_pause.grid(row=1, column=0, padx=8, pady=5)

btn_stop = ctk.CTkButton(frame_botones, text="⏹️ Detener", command=detener, state="disabled", width=120)
btn_stop.grid(row=1, column=1, padx=8, pady=5)

ventana.mainloop()