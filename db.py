import sqlite3

class Parent:
    def __init__(self, db):
        self.conn = sqlite3 .connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parent_data (id INTEGER PRIMARY KEY, fName TEXT, lName TEXT, street TEXT, city TEXT, state TEXT, zip TEXT)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parent_data")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self,fNmae,lName,street,city, state, zip):
        self.cur.execute("INSERT INTO parent_data VALUES (null, ?, ?,?,?,?,?)",(fNmae, lName, street, city, state, zip))
        self.conn.commit()
    
    def remove(self,id):
        self.cur.execute("DELETE FROM parent_data WHERE id=?",(id,))
        self.conn.commit()

    def update(self, fNmae, lName, street, city, state, zip, id):
        self.cur.execute("UPDATE parent_data SET fName = ?, lName=?, street=?, city=?, state=?, zip=? WHERE id=?",(fNmae, lName, street, city, state, zip, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

class Child(Parent):
    def __init__(self, db):
        self.conn = sqlite3 .connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS child_data (id TEXT, fName TEXT, lName TEXT)")
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM child_data")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, id, fName, lName):
        self.cur.execute("INSERT INTO child_data VALUES (?, ?, ?)",(id , fName, lName))
        self.conn.commit()
    
    def remove(self, id, fName, lName):
        self.cur.execute("DELETE FROM child_data WHERE id=? and fName=? and lName=?",(id, fName, lName))
        self.conn.commit()

    def removeAllChild(self,id):
        self.cur.execute("DELETE FROM child_data WHERE id=?",(id,))
        self.conn.commit()

    def update(self, fName, lName, id):
        self.cur.execute("UPDATE child_data SET fName = ?, lName=? WHERE id=?",(fName, lName, id))
        self.conn.commit()