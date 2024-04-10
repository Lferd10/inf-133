import sqlite3


conn = sqlite3.connect("personal.db")

try :
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id),
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion DATE NOT NULL);
        """
)
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")


conn.execute(
    """
    INSERT INTO SALARIOS (salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES ('20-04-2024', '21-04-2024', '22-04-2024')
    """
)


try :
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id),
        fecha_creacion TEXT NOT NULL);
        """
)
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")


conn.execute(
    """
    INSERT INTO EMPLEADOS (nombre, apellido_paterno, apellido_materno, fecha_contratacion, fecha_creacion)
    VALUES ('', '', '')
    """
)



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


try :
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT FULL,
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




#confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()