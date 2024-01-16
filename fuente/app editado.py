from datos.db import  Database, read_all_rows, object_as_dict
import eel
from sqlalchemy import insert ### agregado
from datetime import datetime ### agregado

idUsuario = -1
nombres = ""
cedula = ""
fecha_nacimiento = ""
categoria = -1

@eel.expose
def login(_nombres, _cedula):
    global nombres, cedula
    nombres = _nombres
    cedula = _cedula

    if not(len(nombres) >= 3 and len(nombres) <= 60 and nombres.isalpha()):
        return "El nombre ingresado no es válido"

    if not (len(cedula) == 10 and cedula.isdigit()):
        return "Cédula no válida"

    db = Database()    
    session = db.get_session()
    jugadores = db.base.classes.jugadores
    jugadores = session.query(jugadores).filter(jugadores.identificacion == cedula).count()
    session.close()
    if jugadores >= 0:
        eel.go_to('/template/categorias.html')
    else:
        eel.go_to('/template/fecha_nacimiento.html')    
    

    ############
    # Crea una instancia de la tabla "jugadores"
    #tabla_jugadores = Table('jugadores', metadata, Column('identificacion', Integer))
    # Realiza una consulta para verificar si existe una identificación específica
    #identificacion = cedula
    #query_cedula = tabla_jugadores.select().where(tabla_jugadores.c.identificacion == identificacion)
    # Ejecuta la consulta y verifica si se encontró alguna fila
    #if query_cedula.execute().fetchone():
    #    return f'La identificación {identificacion} está registrada.'
    #    eel.go_to('/template/categorias.html')
    #else:
    #    return f'La identificación {identificacion} no está registrada.'
    #    eel.go_to('/template/fecha_nacimiento.html')
    #############


@eel.expose
def login2(_fecha_nacimiento):
    global nombres, cedula, idUsuario
    fecha_nacimiento = _fecha_nacimiento
    
    validar_fecha = datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
    if not (validar_fecha < datetime.now()):
        return "La fecha de nacimiento no puede ser una fecha futura"
    elif not((datetime.now().year - validar_fecha.year) > 10):
        return "El usuario debe tener al menos 10 años"
        
    edad=datetime.now().year - validar_fecha.year # variable agregada para determinar la edad

# No se está retornando idUsuario
    
    db = Database()    
    session = db.get_session()
    validar_fecha = db.base.classes.jugadores
    insert(jugadores).values(nombres=nombres, tipo_identificacion="C", identificacion=cedula, edad=edad, fecha_registro=fecha_registro)
    session.close()
    if(idUsuario >= 0 and validar_fecha==True): #### editado
        eel.go_to('/template/categorias.html')


@eel.expose
def ObtieneCategorias():
    db = Database()

    session = db.get_session()

    categorias = session.query(db.base.classes.categorias).all()
    categorias_dict = [object_as_dict(cat) for cat in categorias]

    session.close()
    return categorias_dict
        

@eel.expose
def IniciaJuegoMemoria(categoriaId):
    global categoria
    categoria = categoriaId
    eel.go_to('/template/juego.html')

@eel.expose
def ObtieneCartas():
    db = Database()
    print(categoria)
    
    session = db.get_session()
    cartas = db.base.classes.cartas
    insert(cartas).values(carta=1, descripcion='Dwayne Johnson', imagen='Actores\Dwayne Johnson.png', estado=1, categoria=4)
    insert(cartas).values(carta=2, descripcion='', imagen='', estado=1, categoria=4)
    insert(cartas).values(carta=3, descripcion='', imagen='', estado=1, categoria=4)
    insert(cartas).values(carta=3, descripcion='', imagen='', estado=1, categoria=4)








    cartas = session.query(cartas).filter(cartas.categoria == categoria).all()
    cartas_dict = [object_as_dict(cat) for cat in cartas]

    session.close()
    return cartas_dict
    


 

eel.init('frontend')

eel.start('./template/index.html', jinja_templates="template", size=(1200,720), mode="chrome")