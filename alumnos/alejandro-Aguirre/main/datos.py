import sqlite3
import os

class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_folder = os.path.join(base_dir, "db")
        db_path = os.path.join(db_folder, "ventas.db")
        
        os.makedirs(db_folder, exist_ok=True)
        
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        
        self.cur.execute("""CREATE TABLE IF NOT EXISTS cliente (
                            id INTEGER PRIMARY KEY,
                            producto TEXT,
                            cliente TEXT,
                            vendedor TEXT,
                            precio TEXT)""")
        self.conn.commit()

        # === FORZAR DATOS DE EJEMPLO (nueva versión) ===
        self.insert_sample_data()   # Se ejecuta siempre que abras el programa
    
    def insert_sample_data(self):
        # Primero borramos los datos anteriores para que siempre tengas los nuevos
        self.cur.execute("DELETE FROM cliente")
        self.conn.commit()

        muestras = [
            ("Laptop HP Pavilion 15", "Carlos Gómez", "Ana Torres", "1450000"),
            ("Mouse Logitech M330", "María López", "Juan Pérez", "45000"),
            ("Teclado Mecánico RGB", "Roberto Sánchez", "Ana Torres", "95000"),
            ("Monitor Samsung 24\"", "Laura Fernández", "Pedro Ruiz", "320000"),
            ("Auriculares Sony WH-1000XM4", "Diego Morales", "Ana Torres", "420000"),
            ("Impresora HP DeskJet", "Valentina Ruiz", "Juan Pérez", "280000"),
            ("SSD Kingston 1TB", "Lucas Herrera", "Pedro Ruiz", "135000"),
            ("RAM 16GB DDR4", "Camila Torres", "Ana Torres", "85000"),
            ("Router WiFi TP-Link", "Sofía Ramírez", "Juan Pérez", "75000"),
            ("Tablet Samsung Galaxy Tab", "Martín Vargas", "Pedro Ruiz", "650000"),
            ("Smartphone Xiaomi Redmi Note 12", "Lucía Mendoza", "Ana Torres", "890000"),
            ("Cámara Web Logitech C920", "Fernando Castro", "Juan Pérez", "120000"),
            ("Power Bank 20000mAh", "Paula Navarro", "Ana Torres", "65000"),
            ("Monitor Curvo 27\" LG", "Andrés Silva", "Pedro Ruiz", "480000"),
            ("Fuente Corsair 650W", "Julián Acosta", "Juan Pérez", "185000"),
            ("Webcam 1080p", "Natalia Vega", "Ana Torres", "95000"),
            ("Disco Duro Externo 2TB", "Emiliano Ruiz", "Juan Pérez", "220000")
        ]
        
        self.cur.executemany("INSERT INTO cliente VALUES (NULL, ?, ?, ?, ?)", muestras)
        self.conn.commit()
        print("✅ Base de datos reiniciada con 17 registros de ejemplo")
   
    def fetch(self):
        self.cur.execute("SELECT * FROM cliente")
        return self.cur.fetchall()
   
    def insert(self, producto, cliente, vendedor, precio):
        self.cur.execute("INSERT INTO cliente VALUES (NULL, ?, ?, ?, ?)",
                        (producto, cliente, vendedor, precio))
        self.conn.commit()
        
    def remove(self, id):
        self.cur.execute("DELETE FROM cliente WHERE id=?", (id,))
        self.conn.commit()
       
    def update(self, id, producto, cliente, vendedor, precio):
        self.cur.execute("""UPDATE cliente 
                            SET producto = ?, cliente = ?, 
                                vendedor = ?, precio = ? 
                            WHERE id = ?""", 
                        (producto, cliente, vendedor, precio, id))
        self.conn.commit()
       
    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()