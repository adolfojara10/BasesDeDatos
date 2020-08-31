'''
Created on 25 ago. 2020

@author: Adolfo
'''

import sqlite3

#INICIAR CONEXION con base de datos
conexion=sqlite3.connect("Primera base de datos")


#crear cursor o puntero
cursor = conexion.cursor()


#ejecutar el sqlite(****SOLO SE DEBE EJECUTAR UNA VEZ POR LO QUE SE COMENTA)
'''
cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARITUCLO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
'''

#para guardar un producto(dos formas: un solo producto o sino mediante una lista o tupla varios productos)
'''
cursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")


variosProductos=[("Camiseta",10,"Deportes"),("Jarron",90, "Ceramica"),
    ("Camion", 20, "Jugueteria")]
    


cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
'''

#para leer una base de datos
cursor.execute("SELECT * FROM PRODUCTOS")
#devuelve una lista
variosProductos = cursor.fetchall()

print(variosProductos)

for i in variosProductos:
    print("Nombre: " + i[0] + "    Seccion:" + i[2])
    


#para confirmar el cambio
conexion.commit()




#cerrar conexion con base de datos
conexion.close()

