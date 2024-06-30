from Cliente import Cliente

class Factura(Cliente):
    def __init__(self, nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad, precio, descuento, impuesto):
        super().__init__(nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad, precio, descuento)
        self.impuesto = impuesto
        
    def calcular_subtotal(self):
        subtotal = 0
        for precio in self.precio:
            subtotal += precio['precio'] * precio['cantidad']
        return subtotal

    def calcular_impuesto(self):
        return self.calcular_subtotal() * (self.impuesto / 100)

    def calcular_descuento(self):
        return self.calcular_subtotal() * (self.descuento / 100)

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_impuesto() - self.calcular_descuento()
    
    def siVip(self):
        if self.tipo_entrada:
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
        print(f"Descuento ({self.descuento}%): -{self.calcular_descuento():.2f}")
        print("----------------")
        print(f"Total: {self.calcular_total():.2f}")
        print("----------------")