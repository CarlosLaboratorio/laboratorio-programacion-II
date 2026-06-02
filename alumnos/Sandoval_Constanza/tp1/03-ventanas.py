#Importamos tkinter
from tkinter import *
root = Tk() #Crear ventana principal

#Métodos básicos
root.title("Mi aplicación Tkinter")     #Cambia el título de la ventana
root.geometry("800x500+300+200")                #Define tamaño inicial
root.resizable(True,True)               #Permite redimensionar
#root.iconbitmap("icono.ico")    falta el icono

#Métodos visuales CONFIGURACIÓN DE LA VENTANA
root.config(
    bg="#FF5722",            #Cambia el color de fondo
    cursor = "hand2",        #Cambia cursor del mouse: hand1, hand2, xterm 
    bd=5,                    #Grosor del borde
    relief="ridge",          #Estilo del borde: flat, groove, raised, ridge, solid, sunken
    padx=20,                 #Espaciado horizontal interno
    pady=20,                  #Espaciado vertical interno
)               

#Métodos avanzados
root.attributes("-alpha",0.98)          #Transparencia
root.overrideredirect(False)            #Quita la barra superior si es True
root.state("normal")                    #Estado de ventana, zoomed maximiza la ventana
                      

#Iniciar ventana
root.mainloop()