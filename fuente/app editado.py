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
    insert(cartas).values(carta=2, descripcion='Emma Watson', imagen='Actores\Emma Watson.png', estado=1, categoria=4)
    insert(cartas).values(carta=3, descripcion='Jennifer Aniston', imagen='Actores\Jennifer Aniston.png', estado=1, categoria=4)
    insert(cartas).values(carta=4, descripcion='Johnny Depp', imagen='Actores\Johnny Depp.png', estado=1, categoria=4)
    insert(cartas).values(carta=5, descripcion='Keanu Reeves', imagen='Actores\Keanu Reeves.png', estado=1, categoria=4)
    insert(cartas).values(carta=6, descripcion='Leonardo DiCaprio', imagen='Actores\Leonardo DiCaprio.png', estado=1, categoria=4)
    insert(cartas).values(carta=7, descripcion='Megan Fox', imagen='Actores\Megan Fox.png', estado=1, categoria=4)
    insert(cartas).values(carta=8, descripcion='Morgan Freeman', imagen='Actores\Morgan Freeman.png', estado=1, categoria=4)
    insert(cartas).values(carta=9, descripcion='Scarlett Johansson', imagen='Actores\Scarlett Johansson.png', estado=1, categoria=4)
    insert(cartas).values(carta=10, descripcion='Will Smith', imagen='Actores\Will Smith.png', estado=1, categoria=4)
    insert(cartas).values(carta=11, descripcion='Bob Marley', imagen='Cantantes\Bob Marley.png', estado=1, categoria=0)
    insert(cartas).values(carta=12, descripcion='Dua Lipa', imagen='Cantantes\Dua Lipa.png', estado=1, categoria=0)
    insert(cartas).values(carta=13, descripcion='Elvis Presley', imagen='Cantantes\Elvis Presley.png', estado=1, categoria=0)
    insert(cartas).values(carta=14, descripcion='Freddie Mercury', imagen='Cantantes\Freddie Mercury.png', estado=1, categoria=0)
    insert(cartas).values(carta=15, descripcion='Justin Bieber', imagen='Cantantes\Justin Bieber.png', estado=1, categoria=0)
    insert(cartas).values(carta=16, descripcion='Michael Jackson', imagen='Cantantes\Michael Jackson.png', estado=1, categoria=0)
    insert(cartas).values(carta=17, descripcion='Rauw Alejandro', imagen='Cantantes\Rauw Alejandro.png', estado=1, categoria=0)
    insert(cartas).values(carta=18, descripcion='Shakira', imagen='Cantantes\Shakira.png', estado=1, categoria=0)
    insert(cartas).values(carta=19, descripcion='Taylor Swift', imagen='Cantantes\Taylor Swift.png', estado=1, categoria=0)
    insert(cartas).values(carta=20, descripcion='The Weekend', imagen='Cantantes\The Weekend.png', estado=1, categoria=0)
    insert(cartas).values(carta=21, descripcion='Catedral de San Basilio', imagen='Lugares turisticos\Catedral de San Basilio.png', estado=1, categoria=1)
    insert(cartas).values(carta=22, descripcion='Coliseo de Roma', imagen='Lugares turisticos\Coliseo de Roma.png', estado=1, categoria=1)
    insert(cartas).values(carta=23, descripcion='Cristo Redentor', imagen='Lugares turisticos\Cristo Redentor.png', estado=1, categoria=1)
    insert(cartas).values(carta=24, descripcion='Estatua de la Libertad', imagen='Lugares turisticos\Estatua de la Libertad.png', estado=1, categoria=1)
    insert(cartas).values(carta=25, descripcion='Machu Picchu', imagen='Lugares turisticos\Machu Picchu.png', estado=1, categoria=1)
    insert(cartas).values(carta=26, descripcion='Mitad del Mundo', imagen='Lugares turisticos\Mitad del Mundo.png', estado=1, categoria=1)
    insert(cartas).values(carta=27, descripcion='Pailón del Diablo', imagen='Lugares turisticos\Pailón del Diablo.png', estado=1, categoria=1)
    insert(cartas).values(carta=28, descripcion='Taj Mahal', imagen='Lugares turisticos\Taj Mahal.png', estado=1, categoria=1)
    insert(cartas).values(carta=29, descripcion='Torre de Pisa', imagen='Lugares turisticos\Torre de Pisa.png', estado=1, categoria=1)
    insert(cartas).values(carta=30, descripcion='Torre Eiffel', imagen='Lugares turisticos\Torre Eiffel.png', estado=1, categoria=1)
    insert(cartas).values(carta=31, descripcion='bulbasaur', imagen='Pokemones\003 bulbasaur.png', estado=1, categoria=2)
    insert(cartas).values(carta=32, descripcion='charmander', imagen='Pokemones\004 charmander.png', estado=1, categoria=2)
    insert(cartas).values(carta=33, descripcion='squirtle', imagen='Pokemones\007 squirtle.png', estado=1, categoria=2)
    insert(cartas).values(carta=34, descripcion='butterfree', imagen='Pokemones\012 butterfree.png', estado=1, categoria=2)
    insert(cartas).values(carta=35, descripcion='spearow', imagen='Pokemones\021 spearow.png', estado=1, categoria=2)
    insert(cartas).values(carta=36, descripcion='pikachu', imagen='Pokemones\025 pikachu.png', estado=1, categoria=2)
    insert(cartas).values(carta=37, descripcion='meowth', imagen='Pokemones\052 meowth.png', estado=1, categoria=2)
    insert(cartas).values(carta=38, descripcion='mr mime', imagen='Pokemones\122 mr mime.png', estado=1, categoria=2)
    insert(cartas).values(carta=39, descripcion='dragonite', imagen='Pokemones\149 dragonite.png', estado=1, categoria=2)
    insert(cartas).values(carta=40, descripcion='mewtwo', imagen='Pokemones\150 mewtwo.png', estado=1, categoria=2)
    insert(cartas).values(carta=41, descripcion='celebi', imagen='Pokemones\celebi.png', estado=1, categoria=2)
    insert(cartas).values(carta=42, descripcion='charizard', imagen='Pokemones\charizard.png', estado=1, categoria=2)
    insert(cartas).values(carta=43, descripcion='jolteon', imagen='Pokemones\jolteon.png', estado=1, categoria=2)
    insert(cartas).values(carta=44, descripcion='lugia', imagen='Pokemones\lugia.png', estado=1, categoria=2)
    insert(cartas).values(carta=45, descripcion='mew', imagen='Pokemones\mew.png', estado=1, categoria=2)
    insert(cartas).values(carta=46, descripcion='mewtwo', imagen='Pokemones\mewtwo.png', estado=1, categoria=2)
    insert(cartas).values(carta=47, descripcion='pikachu', imagen='Pokemones\pikachu.png', estado=1, categoria=2)
    insert(cartas).values(carta=48, descripcion='torchic', imagen='Pokemones\torchic.png', estado=1, categoria=2)
    insert(cartas).values(carta=49, descripcion='treecko', imagen='Pokemones\treecko.png', estado=1, categoria=2)
    insert(cartas).values(carta=50, descripcion='vulpix', imagen='Pokemones\vulpix.png', estado=1, categoria=2)
    insert(cartas).values(carta=51, descripcion='Batman', imagen='Personajes UCM - DC\Batman.png', estado=1, categoria=5)
    insert(cartas).values(carta=52, descripcion='Bruja Escarlata', imagen='Personajes UCM - DC\Bruja Escarlata.png', estado=1, categoria=5)
    insert(cartas).values(carta=53, descripcion='Capitán América', imagen='Personajes UCM - DC\Capitán América.png', estado=1, categoria=5)
    insert(cartas).values(carta=54, descripcion='El Guasón', imagen='Personajes UCM - DC\El Guasón.png', estado=1, categoria=5)
    insert(cartas).values(carta=55, descripcion='Harley Quinn', imagen='Personajes UCM - DC\Harley Quinn.png', estado=1, categoria=5)
    insert(cartas).values(carta=56, descripcion='Hulk', imagen='Personajes UCM - DC\Hulk.png', estado=1, categoria=5)
    insert(cartas).values(carta=57, descripcion='Iron Man', imagen='Personajes UCM - DC\Iron Man.png', estado=1, categoria=5)
    insert(cartas).values(carta=58, descripcion='Mujer Maravilla', imagen='Personajes UCM - DC\Mujer Maravilla.png', estado=1, categoria=5)
    insert(cartas).values(carta=59, descripcion='Superman', imagen='Personajes UCM - DC\Superman.png', estado=1, categoria=5)
    insert(cartas).values(carta=60, descripcion='Viuda Negra', imagen='Personajes UCM - DC\Viuda Negra.png', estado=1, categoria=5)
    insert(cartas).values(carta=61, descripcion='Arroz con menestra y carne', imagen='Comida típica\Arroz con menestra y carne.png', estado=1, categoria=3)#comida
    insert(cartas).values(carta=62, descripcion='Bolón', imagen='Comida típica\Bolón.png', estado=1, categoria=3)
    insert(cartas).values(carta=63, descripcion='Ceviche de pescado', imagen='Comida típica\Ceviche de pescado.png', estado=1, categoria=3)
    insert(cartas).values(carta=64, descripcion='Chaulafán', imagen='Comida típica\Chaulafán.png', estado=1, categoria=3)
    insert(cartas).values(carta=65, descripcion='Churrasco', imagen='Comida típica\Churrasco.png', estado=1, categoria=3)
    insert(cartas).values(carta=66, descripcion='Encebollado', imagen='Comida típica\Encebollado.png', estado=1, categoria=3)
    insert(cartas).values(carta=67, descripcion='Fritada', imagen='Comida típica\Fritada.png', estado=1, categoria=3)
    insert(cartas).values(carta=68, descripcion='Llapingacho', imagen='Comida típica\Llapingacho.png', estado=1, categoria=3)
    insert(cartas).values(carta=69, descripcion='Locro de papa', imagen='Comida típica\Locro de papa.png', estado=1, categoria=3)
    insert(cartas).values(carta=70, descripcion='Seco de pollo', imagen='Comida típica\Seco de pollo.png', estado=1, categoria=3)



    cartas = session.query(cartas).filter(cartas.categoria == categoria).all()
    cartas_dict = [object_as_dict(cat) for cat in cartas]

    session.close()
    return cartas_dict
    


 

eel.init('frontend')

eel.start('./template/index.html', jinja_templates="template", size=(1200,720), mode="chrome")