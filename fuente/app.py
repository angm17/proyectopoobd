from datos.db import  Database, read_all_rows, object_as_dict
import eel
from sqlalchemy import insert, asc,desc ### agregado
from datetime import datetime ### agregado
from sqlalchemy.inspection import inspect

idUsuario = -1
nombres = ""
cedula = ""
fecha_nacimiento = ""
categoria = -1

@eel.expose
def login(_cedula):
    global cedula, idUsuario
    
    cedula = _cedula


    if not (len(cedula) == 10 and cedula.isdigit()):
        return "Cédula no válida"
    
    db = Database()    
    session = db.get_session()
    jugadores = db.base.classes.jugadores
    jugadores = session.query(jugadores).filter(jugadores.identificacion == cedula).first()
    
    session.close()
    if jugadores:
        idUsuario = jugadores.jugador
        eel.go_to('/template/categorias.html')
    else:
        eel.go_to('/template/fecha_nacimiento.html')    
    

@eel.expose
def login2(_nombres, _fecha_nacimiento):
    global nombres, cedula, idUsuario
    fecha_nacimiento = _fecha_nacimiento
    nombres = _nombres
    
    
    if not(len(nombres) >= 3 and len(nombres) <= 60):
        return "El nombre ingresado no es válido"
    
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
    # print(idUsuario)
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
    # print(categoria) 
    session = db.get_session()
    cartas = db.base.classes.cartas
    cartas = session.query(cartas).filter(cartas.categoria == categoria).limit(10)
    cartas_dict = [object_as_dict(cat) for cat in cartas]
    session.close()
    return cartas_dict

@eel.expose
def GuardaJuego(tiempo, errores):
    global idUsuario
    try:
        puntuacion = calcula_puntuacion(tiempo, int(errores))
        db = Database()    
        session = db.get_session()
        jugadores = db.base.classes.juego_memoria
        nuevo_registro = jugadores(jugador=idUsuario, tiempo=tiempo, errores=errores, puntuacion = puntuacion)
        session.add(nuevo_registro)
        session.commit()    
        return str(puntuacion)
    except Exception as err: 
        print(f"Unexpected {err=}, {type(err)=}")
        return ""
@eel.expose
def ObtienePuntuaciones():
    db = Database()
    # print(categoria) 
    session = db.get_session()
    cartas = db.base.classes.juego_memoria
    jugadores = db.base.classes.jugadores
    
    # cartas = session.query(cartas).order_by(asc(cartas.puntuacion)).limit(10)

    cartas = session.query(cartas.id, cartas.jugador, cartas.tiempo, cartas.errores, cartas.puntuacion, jugadores.nombres).join(jugadores, cartas.jugador == jugadores.jugador).order_by(desc(cartas.puntuacion)).limit(10)
    
    # cartas_dict = [object_as_dict(cat) for cat in cartas]
    
    cartas_dict = [
    {
        'id': row.id,
        'jugador': row.jugador,
        'tiempo': row.tiempo,
        'errores': row.errores,
        'puntuacion': str(row.puntuacion),
        'nombres': row.nombres
    }
    for row in cartas
]
    
    session.close()
    return cartas_dict

def calcula_puntuacion(tiempo, errores):
    constante_segundos = 60
    constante_errores = 15
    minutos, segundos = map(int, tiempo.split(":"))
    total_segundos = minutos * 60 + segundos
    porcentaje_tiempo = (constante_segundos / total_segundos) * 1000
    porcentaje_errores = (constante_errores / errores) * 1000
    return (porcentaje_tiempo + porcentaje_errores) / 2


eel.init('frontend')
eel.start('./template/index.html', jinja_templates="template", size=(1200,720), mode="chrome")