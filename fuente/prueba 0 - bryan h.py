from datos.db import conectar, desconectar


def query_data():
    try:
        # Conectar a la base de datos
        conn, cursor = conectar()

        # Realizar una consulta SELECT
        #query = "SELECT * FROM cartas"  
        #cursor.execute(query)

        # Imprimir los resultados
        #rows = cursor.fetchall()
        #for row in rows:
        #    print(row[1])



        #Validacion ci y nombres no se si este bien
        def validar_identificacion(self, identificacion):
            if len(identificacion) != 10:
                return False
            if not identificacion.isdigit():
                return False
            coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
            verificador = int(identificacion[9])
            suma = 0
            for i in range(9):
                digito = int(identificacion[i])
                producto = digito * coeficientes[i]
                if producto >= 10:
                    producto -= 9
                suma += producto
            total = suma if suma % 10 == 0 else suma + (10 - suma % 10)
            if total - suma == verificador:
                return True
            else:
                return False
        # Ejemplo de uso
        identificacion = "XXXXXXXXXX"  # Reemplaza con la cédula a validar
        if validar_cedula(cedula):
            print("La cédula es válida")
        else:
            print("La cédula no es válida")

        #Validar nombres
        def validar_nombres(self, nombres):
            nombres = nombres.strip()  # Elimina espacios en blanco al inicio y al final

            if len(nombres) >= 3 and len(nombres) <= 50 and nombre.isalpha():
                print("El nombre ingresado es válido")
                return True
            else:
                print("El nombre ingresado no es válido")
                return False
    
        def validar_datos_existentes(self, identificacion, nombres): #no se si este correcta esta funcion
            # Validar la identificación
            if not self.validar_identificacion(identificacion):
                return False
            
            # Consultar la base de datos para verificar si la cédula ya está registrada
            if database.cedula_registrada(identificacion):
                print("La cédula ya está registrada")
                
            # Verificar si la identificación ya está registrada
            cursor.execute("SELECT * FROM jugadores WHERE identificacion = ?", (identificacion,))
            resultados = cursor.fetchall()
            if len(resultados) > 0:
                conn.close()
                return False
            else:
                fecha_nacimiento = input("La cédula no está registrada. Por favor ingrese la fecha de nacimiento del usuario: ")
                # Guardar la cédula y la fecha de nacimiento en la base de datos
                database.guardar_cedula(identificacion, fecha_nacimiento)
            return True
        
            # Validar el nombre
            if not self.validar_nombres(nombres):
                return False

            # Verificar si la identificación ya está registrada
            cursor.execute("SELECT * FROM jugadores WHERE identificacion = ?", (identificacion,))
            resultados = cursor.fetchall()
            if len(resultados) > 0:
                conn.close()
                return False

            # Verificar si el nombre ya está registrado
            cursor.execute("SELECT * FROM jugadores WHERE nombres = ?", (nombres,))
            resultados = cursor.fetchall()
            if len(resultados) > 0:
                conn.close()
                return False

        validado = validar_datos_existentes(self, identificacion, nombres)
        if validado:
            print("Datos válidos y no registrados")
        else:
            print("Datos inválidos o ya registrados")



        #Modelo CRUD
        #Create - Tabla jugadores
        def insertar_jugador(conn, nombre, tipo_identificacion, identificacion, edad, fecha_registro):
            consulta = "INSERT INTO jugadores (nombre, tipo_identificacion, identificacion, edad, fecha_registro) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, tipo_identificacion, identificacion, edad, fecha_registro)
            cursor.execute(consulta, valores)
            conn.commit()
            print("Jugador insertado correctamente.")
        #Read - Tabla jugadores
        def leer_jugadores():
            consulta = "SELECT * FROM jugadores"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            for jugador in resultados:
                print(jugador)
        #Update - Tabla jugadores
        def actualizar_jugador(jugador, nuevo_nombre):
            consulta = "UPDATE jugadores SET nombre = %s WHERE jugador = %s"
            valores_jugadores = (nuevo_nombre, jugador)
            cursor.execute(consulta, valores)
            conn.commit()
            print("Jugador actualizado correctamente.")



        #Create - Tabla juego_velocidad_cab
        def insertar_juego_velocidad_cab(conn, jugador, fecha_inicio, fecha_fin):
            consulta = "INSERT INTO juego_velocidad_cab (jugador, fecha_inicio, fecha_fin) VALUES (%s, %s, %s)"
            valores = (jugador, fecha_inicio, fecha_fin)
            cursor.execute(consulta, valores)
            conn.commit()
            print("Juego_velocidad_cab insertado correctamente.")
        #Read - Tabla juego_velocidad_cab
        def leer_juego_velocidad_cab():
            consulta = "SELECT * FROM juego_velocidad_cab"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            for juego_velocidad_cab in resultados:
                print(juego_velocidad_cab)
        #Update - Tabla juego_velocidad_cab
        def actualizar_juego_velocidad_cab(jugador, fecha_inicio, fecha_fin):
            consulta = "UPDATE juego_velocidad_cab SET fecha_inicio = %s, fecha_fin = %s WHERE jugador = %s"
            valores = (fecha_inicio, fecha_fin, jugador)
            cursor.execute(consulta, valores)
            conn.commit()
            print("Juego_velocidad_cab actualizado correctamente.")



        #Create - Tabla juego_memoria
        def insertar_juego_memoria(conn, jugador, fecha_inicio, fecha_fin, errores):
            consulta = "INSERT INTO juego_velocidad_cab (jugador, fecha_inicio, fecha_fin, errores) VALUES (%s, %s, %s, %s)"
            valores = (jugador, fecha_inicio, fecha_fin, errores)
            cursor.execute(consulta, valores)
            conn.commit()
            print("juego_memoria insertado correctamente.")
        #Read - Tabla juego_memoria
        def leer_juego_memoria():
            consulta = "SELECT * FROM juego_memoria"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            for juego_memoria in resultados:
                print(juego_memoria)
        #Update - Tabla juego_memoria
        def actualizar_juego_memoria(jugador, fecha_inicio, fecha_fin, errores):
            consulta = "UPDATE juego_memoria SET fecha_inicio = %s, fecha_fin = %s, errores = %s WHERE jugador = %s"
            valores = (fecha_inicio, fecha_fin, errores, jugador)
            cursor.execute(consulta, valores)
            conn.commit()
            print("juego_memoria actualizado correctamente.")






    except Exception as e:
        print("Error:", e)
    finally:
        # Asegurarse de cerrar la conexión y el cursor
        desconectar(conn, cursor)

# Llamar a la función para ejecutar la consulta
query_data()










    

    




