class Cliente:
    def __init__(self, nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad, precio, descuento):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido_compra = partido_compra
        self.tipo_entrada = tipo_entrada
        self.mayor_edad = mayor_edad
        self.precio = precio
        self.descuento = descuento
        
    def show(self):
        print(f'''
Nombre: {self.nombre}
Cedula: {self.cedula}
Edad: {self.edad} ({self.siMayorDeEdad()})
Partido: {self.partido_compra}
Sección: {self.siVip()}''')
        
    
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
________________________________

Sub''')
