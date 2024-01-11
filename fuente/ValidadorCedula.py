class ValidadorCedula:
    def __init__(self, cedula):
        self.cedula = cedula

    def validar_cedula(self):
        if len(self.cedula) == 10 and self.cedula.isdigit():
            return True
        else:
            print("Cédula incorrecta. Debe contener exactamente 10 números.")
            return False

    def verificar_existencia(self):
        if not self.validar_cedula():
            return False

        condiciones_existencia = True  # Lógica ficticia para la existencia de la cédula

        if condiciones_existencia:
            print("La cédula existe.")
            return True
        else:
            print("La cédula no existe.")
            return False

# Ejemplo de uso
cedula_input = input("Ingrese la cédula: ")
validador = ValidadorCedula(cedula_input)
validador.verificar_existencia()