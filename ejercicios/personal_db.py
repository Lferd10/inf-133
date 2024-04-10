import sqlite3


conn = sqlite3.connect("personal.db")


#SALARIOS
try :
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion DATE NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
)
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (1, 3000.00, '2024-04-01', '2025-04-30', '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (2, 3500.00, '2023-07-01', '2024-04-30', '2023-07-01')
    """
)
print("\nSALARIOS:")
cursor = conn.execute(
    "SELECT * FROM SALARIOS"
)

for row in cursor:
    print(row)


#EMPLEADOS
try :
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id),);
        """
)
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")


conn.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES ('Juan', 'Gonzales', 'Perez', '15-05-2023', 1, 1, '15-05-2023')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion,departamento_id fecha_creacion)
    VALUES ('Maria', 'Lopez', 'Martinez', '20-06-2023', 2, 2 '20-06-2023')
    """
)
print("\nEMPLEADOS:")
cursor = conn.execute(
    "SELECT * FROM EMPLEADOS"
)

for row in cursor:
    print(row)



#DEPARTAMENTOS
try :
    conn.execute(
        """
        CREATE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
)
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Ventas', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Marketing', '11-04-2020')
    """
)
print("\nDEPARTAMENTOS:")
cursor = conn.execute(
    "SELECT * FROM DEPARTAMENTOS"
)

for row in cursor:
    print(row)




#CARGOS
try :
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
)
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")


conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Gerente de Ventas', 'Senior', '10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Analista de Marketing', 'Junior', '11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Representante de Ventas', 'Junior', '12-04-2020')
    """
)
print("\nCARGOS:")
cursor = conn.execute(
    "SELECT * FROM CARGOS"
)

for row in cursor:
    print(row)



#confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()