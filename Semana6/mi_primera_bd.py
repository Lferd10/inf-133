import sqlite3


conn = sqlite3.connect("instituto.db")

conn.execute(
    """
    CREATE TABLE CARRERAS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL);
    """
)

conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Ingeniería en Informática', 5)
    """
)

conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Administracion', 4)
    """
)

#construir datos

print("CARRERAS")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)
 

conn.execute(
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL);
    """
)

conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Luis', 'Vallejos', '2003-06-26')
    """
)
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Daniel', 'Caceres', '2002-07-04')
    """
)

# Consultar datos de estudiantes
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)


conn.execute(
    """
    CREATE TABLE MATRICULACION
    (id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    carrera_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
)

# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha) 
    VALUES (2, 2, '2024-01-20')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)

print("\nMATRICULACION")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha 
    FROM MATRICULACION
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)

for row in cursor:
    print(row)


print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)

for row in cursor:
    print(row)


# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)

print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)
for row in cursor:
    print(row)


# Eliminar
conn.execute(
    """
    DELETE FROM MATRICULACION
    WHERE id = 1
    """
)

print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)
for row in cursor:
    print(row)

# Cerrar conexión
conn.close()