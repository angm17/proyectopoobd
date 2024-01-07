import configparser
import mysql.connector
from mysql.connector import Error


def leer_configuracion(filename='config.ini', section='mysql'):
    """ Lee la base de datos de configuración y devuelve un diccionario de conexión """
    parser = configparser.ConfigParser()
    parser.read(filename)

    # Obtener la sección de conexión a base de datos
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(f'{section} no se encontró en {filename}')
    return db

def conectar():
    """ Conecta a la base de datos MySQL y devuelve el objeto de conexión y cursor """
    conn = None
    try:
        # Leer la configuración de conexión
        db_config = leer_configuracion()
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Conexión establecida.')
            cursor = conn.cursor()
            return conn, cursor
    except Error as e:
        print(e)


def desconectar(conn, cursor):
    """ Cierra el cursor y la conexión """
    cursor.close()
    conn.close()
    print('Conexión cerrada.')