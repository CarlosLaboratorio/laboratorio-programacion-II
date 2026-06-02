#Instalar Pillow: pip install Pillow
from tkinter import *
from PIL import ImageTk, Image
ventana = Tk()
ventana.title("Reparación de PC")
ventana.geometry("700x450")
ventana.config(bg='MediumPurple1')
ventana.iconbitmap(r'.\ejemplos\ejemploExtra6\imagenes1\picture.ico')
ventana.imagenes = []
def bios():
    imagen = ImageTk.PhotoImage(Image.open(r'.\ejemplos\ejemploExtra6\imagenes1\bios.webp').resize((450,375)))
    label = Label(image=imagen)
    label.place(x=125,y=20)
    label1 = Label(ventana,text="Sistema de la Bios")
    label1.place(x=125,y=20)
    
    ventana.imagenes.append(imagen)

def pc():
    imagen = ImageTk.PhotoImage(Image.open(r'.\ejemplos\ejemploExtra6\imagenes1\placamadre.webp').resize((450,375)))
    label = Label(image=imagen)
    label.place(x=125,y=20)
    label1 = Label(ventana,text="Socket 1200")
    label1.place(x=125,y=20)
    ventana.imagenes.append(imagen)
    
Button(ventana,bg='gray54',text="Bios Uefi",command=bios).place(x=50,y=20)
Button(ventana,bg='gray54',text="Socket 1200",command=pc).place(x=50,y=60)

ventana.mainloop()