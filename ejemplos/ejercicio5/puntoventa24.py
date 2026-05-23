from tkinter import *
from tkinter import messagebox
from tkinter import ttk                 # para mejorar el estilo de los widgets
from datos import Database

datos = Database('./ejemplos/ejercicio5/ventas.db')

# Funciones
def populate_list():
    Producto_list.delete(*Producto_list.get_children())  # Limpia la tabla
    for row in datos.fetch():
        Producto_list.insert("", "end", values=row)

def add_item():
    if producto_text.get() == '' or cliente_text.get() == '' or vendedor_text.get() == '' or precio_text.get() == '':
        messagebox.showerror('Required Fields', 'Por favor, complete todos los campos')
        return
    datos.insert(producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get())
    clear_text()
    populate_list()

def remove_item():
    selected_item = Producto_list.selection()[0]
    datos.remove(Producto_list.item(selected_item)['values'][0])
    populate_list()

def update_item():
    selected_item = Producto_list.selection()[0]
    datos.update(Producto_list.item(selected_item)['values'][0], producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get())
    populate_list()
    
def salir():
    app.quit()

def acerca_de():
    messagebox.showinfo('Acerca de', 'Aplicación de Control de Ventas - Estilo Mejorado\nVersión 3.0')

def clear_text():
    producto_entry.delete(0, END)
    cliente_entry.delete(0, END)
    vendedor_entry.delete(0, END)
    precio_entry.delete(0, END)

def select_item(event):
    try:
        selected_item = Producto_list.selection()[0]
        values = Producto_list.item(selected_item)['values']
        producto_entry.delete(0, END)
        producto_entry.insert(END, values[1])
        cliente_entry.delete(0, END)
        cliente_entry.insert(END, values[2])
        vendedor_entry.delete(0, END)
        vendedor_entry.insert(END, values[3])
        precio_entry.delete(0, END)
        precio_entry.insert(END, values[4])
    except IndexError:
        pass

# Configuración de la ventana principal
app = Tk()
app.title("Control de Ventas - Estilo Mejorado")
app.geometry("900x600")
app.config(bg="#d9f7f7")

# Título de la aplicación
titulo = Label(app, text="Sistema de Control de Ventas", font=("Arial", 24, "bold"), bg="#d9f7f7")
titulo.pack(pady=20)

# Barra de Menú
menu_bar = Menu(app)
app.config(menu=menu_bar)

# Menú Archivo
archivo_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Salir", command=salir)

# Menú Editar
editar_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Editar", menu=editar_menu)
editar_menu.add_command(label="Agregar", command=add_item)
editar_menu.add_command(label="Eliminar", command=remove_item)
editar_menu.add_command(label="Actualizar", command=update_item)
editar_menu.add_command(label="Limpiar", command=clear_text)

# Menú Ayuda
ayuda_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)
ayuda_menu.add_command(label="Acerca de", command=acerca_de)

# Frame para formulario de ingreso de datos
frame_formulario = Frame(app, bg="#f0f0f0", bd=2, relief=SOLID, padx=20, pady=10)
frame_formulario.pack(pady=10, padx=20, fill=X)

# Etiquetas y entradas del formulario
producto_text = StringVar()
cliente_text = StringVar()
vendedor_text = StringVar()
precio_text = StringVar()

Label(frame_formulario, text="Producto", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky=E)
producto_entry = Entry(frame_formulario, textvariable=producto_text)
producto_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

Label(frame_formulario, text="Cliente", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky=E)
cliente_entry = Entry(frame_formulario, textvariable=cliente_text)
cliente_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

Label(frame_formulario, text="Vendedor", bg="#f0f0f0").grid(row=0, column=2, padx=10, pady=5, sticky=E)
vendedor_entry = Entry(frame_formulario, textvariable=vendedor_text)
vendedor_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

Label(frame_formulario, text="Precio", bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5, sticky=E)
precio_entry = Entry(frame_formulario, textvariable=precio_text)
precio_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

# Botones de acciones
frame_botones = Frame(app, bg="#d9f7f7", padx=10, pady=10)
frame_botones.pack()

btn_add = Button(frame_botones, text="Agregar", command=add_item, bg="#4CAF50", fg="white", width=12)
btn_add.grid(row=0, column=0, padx=10, pady=10)

btn_remove = Button(frame_botones, text="Eliminar", command=remove_item, bg="#f44336", fg="white", width=12)
btn_remove.grid(row=0, column=1, padx=10, pady=10)

btn_update = Button(frame_botones, text="Actualizar", command=update_item, bg="#FFC107", fg="black", width=12)
btn_update.grid(row=0, column=2, padx=10, pady=10)

btn_clear = Button(frame_botones, text="Limpiar", command=clear_text, bg="#2196F3", fg="white", width=12)
btn_clear.grid(row=0, column=3, padx=10, pady=10)

# Frame para la lista de productos
frame_lista = Frame(app, bg="#d9f7f7", bd=2, relief=SOLID, padx=20, pady=10)
frame_lista.pack(pady=10, padx=20, fill=BOTH, expand=True)

# Tabla para mostrar los productos
columns = ('ID', 'Producto', 'Cliente', 'Vendedor', 'Precio')
Producto_list = ttk.Treeview(frame_lista, columns=columns, show='headings', height=8)

for col in columns:
    Producto_list.heading(col, text=col)
    Producto_list.column(col, width=100)

Producto_list.pack(side=LEFT, fill=BOTH, expand=True)
Producto_list.bind('<<TreeviewSelect>>', select_item)

# Añadir scroll a la tabla
scrollbar = Scrollbar(frame_lista, orient=VERTICAL, command=Producto_list.yview)
Producto_list.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

# Poblamos la lista inicialmente
populate_list()

app.mainloop()