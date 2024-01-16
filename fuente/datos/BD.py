import mysql.connector

# Configuración de conexión
config = {
    'host': '127.0.0.1',
    'database': 'proyectopoobd',
    'user': 'root',
    'password': '',
}

# Intentar establecer la conexión
try:
    connection = mysql.connector.connect(**config)

    # Aquí puedes realizar operaciones en la base de datos

    # Cerrar la conexión
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
