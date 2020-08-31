'''
Created on 27 ago. 2020

@author: Adolfo
'''

import sqlite3

conexion = sqlite3.connect("Gestion Productos")

cursor = conexion.cursor()

#se crea la tabla con la primary key con incremento automatico
#cursor.execute("CREATE TABLE PRODUCTOS3(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ARTICULO VARCHAR(50) UNIQUE, PRECIO INTEGER, SECCION VARCHAR(20))")

'''
productos = [("pelota", 10, "jugueteria"), ("pantalon", 15, "ropa"),("taza", 5, "ceramica"),("clavo", 1, "ferreteria")]


cursor.executemany("INSERT INTO PRODUCTOS3 VALUES (NULL,?,?,?)", productos)
'''

#se inserta un articulo con una clave ya creada para que salte un error
#cursor.execute("INSERT INTO PRODUCTOS2 VALUES ('ar03','tren',15,'jugueteria')")


#para leer una parte de la tabla y buscar una seccion en especial
cursor.execute("SELECT * FROM PRODUCTOS3 WHERE SECCION = 'jugueteria'")

productosBBDD = cursor.fetchall()

print(productosBBDD)


#para actualizar un producto en este caso pelota
'''
cursor.execute("UPDATE PRODUCTOS3 SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")
'''

#para eliminar 
cursor.execute("DELETE FROM PRODUCTOS3 WHERE ID=1")



conexion.commit()

conexion.close()
