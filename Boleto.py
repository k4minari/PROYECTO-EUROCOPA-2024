from Cliente import Cliente

class Boleto(Cliente):
    def __init__(self, nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad, precio, descuento, id, dni, tipo_boleto, asiento, partido):
        super().__init__(nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad, precio, descuento)
        self.id = id
        self.dni = dni
        self.tipo_boleto = tipo_boleto
        self.asiento = asiento
        self.partido = partido
        self.attendance = False

    def show(self):
        return f'''
---------------------------------
----------- ENTRADA -------------
---------------------------------
id: {self.id}
dni: {self.dni}
tipo_boleto: {self.tipo_boleto}
asiento: {self.asiento}
partido: {self.partido}
'''