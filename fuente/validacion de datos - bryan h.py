# Verificar si la identificación está registrada en la tabla "identificacion"
def verificar_identificacion(identificacion):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM jugadores WHERE identificacion = %s", (identificacion,))
    resultados = cursor.fetchall()
    if len(resultados) > 0:
        return True
    else:
        return False

def identificacion_ecuatoriana(identificacion):
    if len(identificacion) != 10:
        return False
    if not identificacion.isdigit():
        return False
    provincia = int(identificacion[0:2])
    if provincia < 1 or provincia > 24:
        return False
    tercer_digito = int(identificacion[2])
    if tercer_digito < 0 or tercer_digito > 6:
        return False
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
        digito = int(identificacion[i])
        coeficiente = coeficientes[i]
        producto = digito * coeficiente
        if producto >= 10:
            producto -= 9
        total += producto
    verificador = (10 - (total % 10)) % 10
    if verificador != int(identificacion[9]):
        return False
    return True

# Solicitar el nombre del usuario y la identificación
usuario_identificacion = input("Ingrese su identificación: ")

# Validar la identificación
if verificar_identificacion(usuario_identificacion):
    print("Su cédula está registrada.")
    nuevo_nombre = input("Ingrese su nuevo nombre: ")
    cursor.execute("UPDATE jugadores SET nombres = %s WHERE identificacion = %s", (nuevo_nombre, usuario_identificacion))
    mydb.commit()
    print("Nombre actualizado correctamente.")
else:
    print("Su cédula no está registrada.")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (formato: AA-MM-DD): ")
    cursor.execute("INSERT INTO identificacion (identificacion, fecha_nacimiento) VALUES (%s, %s)", (usuario_identificacion, fecha_nacimiento))
    mydb.commit()
    print("Identificación y fecha de nacimiento registrados correctamente.")
