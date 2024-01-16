from datos.db import conectar, desconectar


def query_data():
    try:
        # Conectar a la base de datos
        conn, cursor = conectar()
        conn.start_transaction()

        # Realizar una consulta SELECT
        # Los selects no van en transacciones 
        
        
        
        
        query = "SELECT * FROM cartas"  
        cursor.execute(query)
        
        
        # query()
        
        # Imprimir los resultados
        rows = cursor.fetchall()
        for row in rows:
            print(row[1])
            
        conn.commit()

    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        # Asegurarse de cerrar la conexión y el cursor
        desconectar(conn, cursor)

# Llamar a la función para ejecutar la consulta
query_data()