from datos.db import  Database, read_all_rows, object_as_dict
import eel


nombres = ""
cedula = ""
fecha_nacimiento = ""
categoria =-1

@eel.expose
def login(_nombres, _cedula):
    global nombres, cedula
    nombres = _nombres
    cedula = _cedula
    existe = False
    
    if(existe):
        eel.go_to('/template/categorias.html')
    else:
        eel.go_to('/template/fecha_nacimiento.html')    
    

@eel.expose
def login2(_fecha_nacimiento):
    global nombres, cedula
    fecha_nacimiento = _fecha_nacimiento
    
    existe = True
    
    if(existe):
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