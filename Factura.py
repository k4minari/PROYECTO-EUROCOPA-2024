from Cliente import Cliente

class Factura(Cliente):
    def __init__(self, nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad, precio, descuento, impuesto, cedula_descuento):
        super().__init__(nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad, precio, descuento)
        self.impuesto = impuesto
        self.cedula_descuento = cedula_descuento
        
    def calcular_subtotal(self):
        if self.tipo_entrada:
            subtotal = 75
            return subtotal
        else:
            subtotal = 35
            return subtotal

    def calcular_impuesto(self):
        return self.calcular_subtotal() * (self.impuesto / 100)

    def calcular_descuento(self):
        return self.calcular_subtotal() * (self.cedula_descuento / 100)

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_impuesto() - self.calcular_descuento()
    
    def siVip(self):
        if self.tipo_entrada == 1:
            return 'VIP'
        else:
            return 'GENERAL'
    
    def siMayorDeEdad(self):
        if self.mayor_edad:
            return '(Mayor de edad)'
        else:
            return '(Menor de edad)'
    
    def siVampiro(self):
        if self.descuento:
            return 'Usted obtiene un descuento del 50%'  
        else:
            return 'Descuentos o cupones no aplicados'
    
    def mostrar_factura(self):
        print(f'''
--------------------------------
----------- FACTURA ------------
--------------------------------
    COMPROBANTE DE COMPRA
________________________________

Nombre: {self.nombre}
Cedula: {self.cedula}
Edad: {self.edad} ({self.siMayorDeEdad()})
Partido: {self.partido_compra}
Sección: {self.siVip()}
Descuento: {self.siVampiro()}
________________________________''')
        print("----------------")
        print(f"Subtotal: {self.calcular_subtotal():.2f}")
        print(f"Impuesto ({self.impuesto}%): {self.calcular_impuesto():.2f}")
        print(f"Descuento ({self.cedula_descuento}%): -{self.calcular_descuento():.2f}")
        print("----------------")
        print(f"Total: {self.calcular_total():.2f}")
        print("----------------")