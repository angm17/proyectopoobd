import configparser
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

class Database:
    def __init__(self, config_file = 'config.ini'):
        self.config = self.read_config(config_file)
        self.engine = self.create_engine()
        self.base = self.reflect_tables()
        self.Session = sessionmaker(bind=self.engine)

    def read_config(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config['mysql']

    def create_engine(self):
        connection_string = f"mysql+pymysql://{self.config['user']}:{self.config['password']}@{self.config['host']}/{self.config['database']}"
        return create_engine(connection_string)
    def reflect_tables(self):
        base = automap_base()
        base.prepare(self.engine, reflect=True)
        return base
    def get_session(self):
        return self.Session()
    
    
def read_all_rows(session, table_class):
    try:
        rows = session.query(table_class).all()
        return rows
    except Exception as e:
        print("Error al leer las filas:", e)
        return None
    finally:
        session.close()
def object_as_dict(obj):
    if obj is None:
        return None
    # Convierte un objeto SQLAlchemy en un diccionario
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
# import configparser
# import mysql.connector
# from mysql.connector import Error


# def leer_configuracion(filename='config.ini', section='mysql'):
#     """ Lee la base de datos de configuración y devuelve un diccionario de conexión """
#     parser = configparser.ConfigParser()
#     parser.read(filename)

#     # Obtener la sección de conexión a base de datos
#     db = {}
#     if parser.has_section(section):
#         items = parser.items(section)
#         for item in items:
#             db[item[0]] = item[1]
#     else:
#         raise Exception(f'{section} no se encontró en {filename}')
#     return db

# def conectar():
#     """ Conecta a la base de datos MySQL y devuelve el objeto de conexión y cursor """
#     conn = None
#     try:
#         # Leer la configuración de conexión
#         db_config = leer_configuracion()
#         conn = mysql.connector.connect(**db_config)
#         if conn.is_connected():
#             print('Conexión establecida.')
#             cursor = conn.cursor()
#             return conn, cursor
#     except Error as e:
#         print(e)


# def desconectar(conn, cursor):
#     """ Cierra el cursor y la conexión """
#     cursor.close()
#     conn.close()
#     print('Conexión cerrada.')