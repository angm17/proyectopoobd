from datos.db import conectar, desconectar


def query_data():
    try:
        # Conectar a la base de datos
        conn, cursor = conectar()

        # Realizar una consulta SELECT
        query = "SELECT * FROM cartas"  
        cursor.execute(query)

        # Imprimir los resultados
        rows = cursor.fetchall()
        for row in rows:
            print(row[1])

    except Exception as e:
        print("Error:", e)
    finally:
        # Asegurarse de cerrar la conexión y el cursor
        desconectar(conn, cursor)

# Llamar a la función para ejecutar la consulta
query_data()