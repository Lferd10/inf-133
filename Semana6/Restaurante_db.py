import sqlite3


conn = sqlite3.connect("restaurante.db")

try :
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NO NULL);
        """
)
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")


conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza', 10.99, 'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa', 8.99,'Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Sushi', 12.99,'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensalada', 6.99, 'Vegetariana')
    """
)

print("PLATOS")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)


#MESAS
try :
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """
)
except sqlite3.OperationalError:
    print("La tabla MESAS ya existe")

conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)
print("MESAS")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)



#PEDIDOS
try :
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL);
        """
)
except sqlite3.OperationalError:
    print("La tabla PEDIDOS ya existe")


conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (1,2,3,'2024-03-04')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (2,3,1,'2024-04-04')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (3,1,3,'2024-04-05')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (4,4,4,'2024-04-05')
    """
)

print("PEDIDOS")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)




conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)

conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)

print("PEDIDOS")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

#confirmar cambios
conn.commit()


# Cerrar conexión
conn.close()