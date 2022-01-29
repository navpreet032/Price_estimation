import sqlite3
class Database:
    def __init__(self,db): 
     #with sqlite3.connect('Users.db') as db:
     self.conn=sqlite3.connect(db)
     self.c = self.conn.cursor()
     self.c.execute("""CREATE TABLE IF NOT EXISTS Pdetails (id INTEGER PRIMARY KEY,P_name text,P_MRP text,
                    P_price double,P_age int)""") 
     self.conn.commit()
     
    def fetch(self):
        self.c.execute("SELECT * FROM Pdetails")
        data=self.c.fetchall()
        return data

    def insert(self,name,mrp,price,age):
        self.c.execute("INSERT INTO  Pdetails VALUES(NULL,?,?,?,?)",(name,mrp,price,age))
        self.conn.commit()

    def remove(self,id):
        self.c.execute("DELETE FROM Pdetails WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,name,mrp,price,age):
        self.c.execute("UPDATE Pdetails SET P_name=?,P_MRP=?,P_price=?,P_age=? WHERE id=?",(name,mrp,price,age,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()