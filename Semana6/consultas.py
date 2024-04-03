import sqlite3


conn = sqlite3.connect("restaurante.db")

# conn.execute(
#     """
#     INSERT INTO ESTUDIANTES(nombre, apellido, fecha:nacimiento)
#     VALUES ('Carlos', 'Perez', '2001-02-10')
#     """
# )
# conn.execute(
#     """
#     INSERT INTO CARRERAS(nombre, duracion)
#     VALUES ('Licenciatura en Contabilidad', 4)
#     """
# )


print("\nPEDIDOS")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)

for row in cursor:
    print(row)




#confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()