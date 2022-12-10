import sqlite3 

# Cria e ativa a database

dbase = sqlite3.connect('produtos.db')
c = dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS produtos(  
                    ID INT NOT NULL,
                    NAME VARCHAR NOT NULL,
                    QTD INT NOT NULL
                                  )''')


# Create database with primary key
dbase.execute(''' CREATE TABLE IF NOT EXISTS clientes(  
                    ID INT PRIMARY KEY NOT NULL,
                    NAME NOT NULL,
                    TEL REAL
                                  )''')

dbase.execute(''' CREATE TABLE IF NOT EXISTS entradas(  
                    ID INT PRIMARY KEY NOT NULL,
                    NAME_CLI NOT NULL,
                    QTD REAL,
                    PRICE REAL
                                  )''')

#dbase.execute(''' CREATE TABLE IF NOT EXISTS vendas(  
#                    id INT NOT NULL AUTO_INCREMENT,
#                    NAME_CLI NOT NULL,
#                    TEL REAL,
#                    NAME NOT NULL,
#                    QTD REAL,
#                    PRICE,
#                    TOTAL,
#                    PRIMARY KEY (id)
#                                  )''')
                    
# Aplica todas as mudanças da nossa database
dbase.commit()

def write(ID, NAME, QTD):
    c.execute(""" INSERT into produtos(ID, NAME, QTD) VALUES(?, ?, ?)""", (ID, NAME, QTD))
    dbase.commit()
	

def delete(x):
    try: 
        c.execute(""" DELETE from produtos where NAME=?""", x )
        dbase.commit()

    except:
        print("Error: Not found name!")

def update(NAME, ID):
    c.execute(""" UPDATE produtos SET NAME=? where ID=?""", (NAME, ID ))
    dbase.commit()


def read_data():
    c = dbase.cursor()
    c.execute(""" SELECT ID, NAME, QTD FROM produtos """)
    data = c.fetchall()
    #for items in data:
    return data
    dbase.commit()

def read_data_full():
    c = dbase.cursor()
    c.execute(""" SELECT * FROM produtos""")
    data = c.fetchall()
    dbase.commit()
    return data

def read_one():
    c = dbase.cursor()
    c.execute(""" SELECT ID, NAME FROM produtos""")
    data = c.fetchone()
    dbase.commit()
    for items in data:
        print(items[0])

def read_factory_full():
    dbase.row_factory = sqlite3.Row
    c = dbase.cursor()
    data = c.fetchall()
    for member in data:
        return member

def read_factory():
    dbase.row_factory = sqlite3.Row
    c = dbase.cursor()
    data = c.fetchall()
    return data[QTD]

    # Others
    # data.keys()
    # data[0]
    # data[ID]
    # data[NAME]
    # data[QTD]

def read_filter():
    c.execute("""SELECT ID, NAME FROM prod Where ID='3'""")