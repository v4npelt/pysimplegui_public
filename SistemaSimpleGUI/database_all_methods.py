import sqlite3 

# Cria e ativa a database

dbase = sqlite3.connect('produtos.db')
c = dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS produtos(  
                    ID INT PRIMARY KEY NOT NULL,
                    NAME TEXT NOT NULL,
                    PRICE REAL,
                    QTDE REAL  )''')
                    
# Aplica todas as mudanças da nossa database
dbase.commit()

def write (ID, NAME):
    c.execute(""" INSERT into produtos(ID, NAME) VALUES(?, ?)""", (ID, NAME))
    dbase.commit()
	

def delete(x):
    c.execute(""" DELETE from produtos where NAME=?""", (x,) )
    dbase.commit()


# Método direto
def update():
    c.execute(""" UPDATE produtos SET NAME='plate' where ID='2'""")
    dbase.commit()

# Método passando argumentos
def update_name(x):
    c.execute(""" UPDATE produtos SET NAME=? where ID='2'""", (x,))
    dbase.commit()

# Método passando argumentos
def update_price(x):
    c.execute(""" UPDATE produtos SET PRICE=? where ID='2'""", (x,))
    dbase.commit()

# Método passando argumentos
def update_qtde(x):
    c.execute(""" UPDATE produtos SET QTDE=? where ID='2'""", (x,))
    dbase.commit()

def read_data():
    c = dbase.cursor()
    c.execute(""" SELECT ID, NAME from produtos""")
    data = c.fetchall()
    dbase.commit()
    return data


