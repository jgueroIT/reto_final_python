# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os
import psycopg2

# Carga las variables de entorno desde el archivo .env
load_dotenv()

print("Host:", os.getenv("DB_HOST"))
print("Intentando conectar.......")

for key in ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]:
    value = os.getenv(key)
    print(f"{key} -> {value} | bytes: {value.encode('utf-8', 'replace')}")

def get_connection():
    try:
        # Construir DSN (Data Source Name)
        dsn = (
            f"host={os.getenv('DB_HOST', 'localhost')} "
            f"port={os.getenv('DB_PORT', '5432')} "
            f"dbname={os.getenv('DB_NAME', 'reto_db_utf8')} "
            f"user={os.getenv('DB_USER', 'reto_user')} "
            f"password={os.getenv('DB_PASSWORD', '1234')}"
        )
        print("DSN generado:", dsn)  # Imprime el DSN para verificar si hay algo raro en él

        # Conectar usando DSN y establecer codificación a UTF-8
        conn = psycopg2.connect(dsn)
        conn.set_client_encoding('UTF8')

        print("¡Conexión exitosa a PostgreSQL!")
        return conn
    except psycopg2.Error as e:
        print("Error de conexión:", e.pgcode, "-", e.pgerror)
        return None

get_connection()
