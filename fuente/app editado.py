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


    if not (len(cedula) == 10 and cedula.isdigit()):
        return "Cédula no válida"
    
    if not(len(nombres) >= 3 and len(nombres) <= 60 and nombres.isalpha()):
        return "El nombre ingresado no es válido"
    
    db = Database()    
    session = db.get_session()
    jugadores = db.base.classes.jugadores
    jugadores = session.query(jugadores).filter(jugadores.identificacion == cedula).count()
    
    session.close()
    if jugadores > 0:
        eel.go_to('/template/categorias.html')
    else:
        eel.go_to('/template/fecha_nacimiento.html')    
    

@eel.expose
def login2(_fecha_nacimiento):
    global nombres, cedula, idUsuario
    fecha_nacimiento = _fecha_nacimiento
    
    validar_fecha = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    if not (validar_fecha < datetime.now()):
        return "Fecha incorrecta"
    elif not((datetime.now().year - validar_fecha.year) > 10):
        return "El usuario debe tener al menos 10 años"
    edad=datetime.now().year - validar_fecha.year # variable agregada para determinar la edad
    db = Database()    
    session = db.get_session()
    jugadores = db.base.classes.jugadores
    
    nuevo_registro = jugadores(nombres=nombres, tipo_identificacion="C", identificacion=cedula, edad=edad)
    session.add(nuevo_registro)
    session.commit()
    
    idUsuario = nuevo_registro.jugador
    
    print(idUsuario)
    if(idUsuario >= 0):
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
    

    cartas = session.query(cartas).filter(cartas.categoria == categoria).all()
    cartas_dict = [object_as_dict(cat) for cat in cartas]

    session.close()
    return cartas_dict
    

eel.init('frontend')

eel.start('./template/index.html', jinja_templates="template", size=(1200,720), mode="chrome")