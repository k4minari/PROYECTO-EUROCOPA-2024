class Cliente:
    def __init__(self, nombre, cedula, edad, partido_compra, tipo_entrada, mayor_edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido_compra = partido_compra
        self.tipo_entrada = tipo_entrada
        self.mayor_edad = mayor_edad
        
    def show(self):
        print(f'''
Nombre: {self.nombre}
Cedula: {self.cedula}
Edad: {self.edad}
Partido: {self.partido_compra}
Sección: {self.siVip()}''')
        
    
    def siVip(self):
        if self.tipo_entrada:
            return 'VIP'
        else:
            return 'GENERAL'
    
    def siMayorDeEdad(self):
        if self.mayor_edad:
            return True
        else:
            return False
    
    def siVampiro(self):
        pass