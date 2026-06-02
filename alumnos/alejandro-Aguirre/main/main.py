from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datos import Database
import os

# ====================== BASE DE DATOS ======================
datos = Database()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Ventas - Laboratorio II")
        self.root.geometry("1100x700")
        self.root.configure(bg="#f0f2f5")
        
        self.producto_var = StringVar()
        self.cliente_var = StringVar()
        self.vendedor_var = StringVar()
        self.precio_var = StringVar()
        self.search_var = StringVar()
        
        self.create_widgets()
        self.load_data()
        
    def create_widgets(self):
        # ================== TÍTULO ==================
        title = Label(self.root, text="🛒 GESTIÓN DE VENTAS", 
                     font=("Helvetica", 20, "bold"), bg="#f0f2f5", fg="#1e3a8a")
        title.pack(pady=15)

        # ================== FORMULARIO ==================
        form_frame = LabelFrame(self.root, text="Nuevo Registro", font=("Helvetica", 11, "bold"),
                              padx=20, pady=15, bg="#ffffff")
        form_frame.pack(fill="x", padx=20, pady=10)

        # Grid para el formulario
        entries = [
            ("Producto:", self.producto_var),
            ("Cliente:", self.cliente_var),
            ("Vendedor:", self.vendedor_var),
            ("Precio ($):", self.precio_var)
        ]
        
        for i, (text, var) in enumerate(entries):
            Label(form_frame, text=text, bg="#ffffff", font=("Helvetica", 10)).grid(
                row=i, column=0, sticky=W, pady=8)
            Entry(form_frame, textvariable=var, width=40, font=("Helvetica", 10)).grid(
                row=i, column=1, padx=10, pady=8)

        # Botones
        btn_frame = Frame(form_frame, bg="#ffffff")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=15)

        Button(btn_frame, text="💾 Insertar", command=self.insert_item, 
               bg="#10b981", fg="white", font=("Helvetica", 10, "bold"), width=12, height=2).pack(side=LEFT, padx=8)
        Button(btn_frame, text="✏️ Actualizar", command=self.update_item, 
               bg="#3b82f6", fg="white", font=("Helvetica", 10, "bold"), width=12, height=2).pack(side=LEFT, padx=8)
        Button(btn_frame, text="🗑️ Eliminar", command=self.remove_item, 
               bg="#ef4444", fg="white", font=("Helvetica", 10, "bold"), width=12, height=2).pack(side=LEFT, padx=8)
        Button(btn_frame, text="🧹 Limpiar", command=self.clear_fields, 
               bg="#6b7280", fg="white", font=("Helvetica", 10, "bold"), width=12, height=2).pack(side=LEFT, padx=8)

        # ================== BUSCADOR ==================
        search_frame = Frame(self.root, bg="#f0f2f5")
        search_frame.pack(fill="x", padx=20, pady=5)
        
        Label(search_frame, text="🔎 Buscar:", bg="#f0f2f5", font=("Helvetica", 10)).pack(side=LEFT)
        Entry(search_frame, textvariable=self.search_var, width=40, font=("Helvetica", 10)).pack(side=LEFT, padx=10)
        Button(search_frame, text="Buscar", command=self.search_data, bg="#64748b", fg="white").pack(side=LEFT)
        Button(search_frame, text="Mostrar Todo", command=self.load_data, bg="#64748b", fg="white").pack(side=LEFT, padx=5)

        # ================== TABLA ==================
        columns = ("ID", "Producto", "Cliente", "Vendedor", "Precio")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
        style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor=CENTER)

        self.tree.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y, padx=(0,20))

        self.tree.bind("<Double-1>", self.on_double_click)

        # ================== TOTAL VENTAS ==================
        self.total_label = Label(self.root, text="Total Vendido: $ 0", 
                                font=("Helvetica", 14, "bold"), bg="#f0f2f5", fg="#1e40af")
        self.total_label.pack(pady=10)

    def load_data(self, rows=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if rows is None:
            rows = datos.fetch()
        
        total = 0
        for row in rows:
            self.tree.insert("", END, values=row)
            try:
                total += int(row[4])
            except:
                pass
                
        self.total_label.config(text=f"Total Vendido: $ {total:,}".replace(",", "."))

    def search_data(self):
        term = self.search_var.get().strip().lower()
        if not term:
            self.load_data()
            return
            
        all_rows = datos.fetch()
        filtered = [row for row in all_rows if term in str(row).lower()]
        self.load_data(filtered)

    def insert_item(self):
        if not all([self.producto_var.get().strip(), self.cliente_var.get().strip(), 
                   self.vendedor_var.get().strip(), self.precio_var.get().strip()]):
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return
            
        datos.insert(self.producto_var.get(), self.cliente_var.get(),
                    self.vendedor_var.get(), self.precio_var.get())
        
        self.load_data()
        self.clear_fields()
        messagebox.showinfo("Éxito", "✅ Registro insertado correctamente")

    def remove_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Error", "Selecciona un registro para eliminar")
            return
            
        if messagebox.askyesno("Confirmar", "¿Eliminar este registro?"):
            id_item = self.tree.item(selected[0])['values'][0]
            datos.remove(id_item)
            self.load_data()
            messagebox.showinfo("Eliminado", "Registro eliminado correctamente")

    def update_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Error", "Selecciona un registro para actualizar")
            return
            
        id_item = self.tree.item(selected[0])['values'][0]
        
        datos.update(id_item, 
                    self.producto_var.get(),
                    self.cliente_var.get(),
                    self.vendedor_var.get(),
                    self.precio_var.get())
        
        self.load_data()
        messagebox.showinfo("Éxito", "Registro actualizado correctamente")

    def clear_fields(self):
        self.producto_var.set("")
        self.cliente_var.set("")
        self.vendedor_var.set("")
        self.precio_var.set("")
        self.search_var.set("")

    def on_double_click(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])['values']
            self.producto_var.set(values[1])
            self.cliente_var.set(values[2])
            self.vendedor_var.set(values[3])
            self.precio_var.set(values[4])


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()