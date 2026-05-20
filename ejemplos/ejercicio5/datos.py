import sqlite3

class Database:
    def __init__(self, datos):
        self.conn = sqlite3.connect(datos)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY, producto text, cliente text, vendedor text, precio text)")
        self.conn.commit()

        
    def fetch(self):
        self.cur.execute("SELECT * FROM cliente")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, producto,cliente,vendedor,precio):
        self.cur.execute("INSERT INTO cliente VALUES (NULL, ?, ?, ?, ?)",(producto,cliente,vendedor,precio))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM cliente WHERE id=?", (id,))
        self.conn.commit()
        
    def update(self, id, producto,cliente,vendedor,precio):
        self.cur.execute("UPDATE cliente SET producto = ?,cliente = ?,vendedor = ?,precio = ? WHERE id = ?", (producto,cliente,vendedor,precio,id))
        self.conn.commit()
        
    def __del__(self):    
        self.conn.close()

datos= Database('./ejemplos/ejercicio5/ventas.db')

#datos.insert("4GB DDR4 RAM", "Luis Gomez", "Corrientes Sistemas", "1800")
#datos.insert("Laptop","Juan Martinez","Luis A. Cuadrado","18950")
#datos.insert("Tablet","Luisa Perez","Carrefour","5800")        
        
        #self.cur.execute("INSERT INTO cliente select * from cliente")
        #self.conn.commit()