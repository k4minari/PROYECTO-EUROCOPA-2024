from Equipo import Equipo
from Estadio import Estadio

class GestionEquipos:
    def __init__(self, data_equipo, data_estadio):
        self.data_equipo = data_equipo
        self.data_estadio = data_estadio
        self.equipos = []
        self.estadios = []
        
    def registro_equipos(self):
        for e in self.data_equipo:
            id = e["id"]
            codigo = e["code"]
            nombre = e["name"]
            grupo = e["group"]
            nuevo_equipo = Equipo(id, codigo, nombre, grupo)
            self.equipos.append(nuevo_equipo)
    
    def registro_estadios(self):
        for o in self.data_estadio:
            id = o["id"]
            nombre = o["name"]
            ciudad = o["city"]
            capacidad = o["capacity"]
            restaurantes = o["restaurants"]
            nuevo_estadio = Estadio(id, nombre, ciudad, capacidad, restaurantes)
            self.estadios.append(nuevo_estadio)
            
            
    def registro_datos(self):
        self.registro_equipos()
        self.registro_estadios()
        
    def mostrar_equipos(self):
        for equi in self.equipos:
            print(equi.show())
    
    def mostrar_estadios(self):
        for esta in self.estadios:
            print(esta.show())     
            
               
    def menu(self):
        self.registro_datos()

        print('--BIENVENIDO/A A LA EURO 2024--')
        while True:
            print('''
1. Ver Equipos
2. Ver estadios
''')
            seleccion = input('Ingrese el número asociado a su selección: ')
            while not seleccion.isnumeric() or int(seleccion) not in range(1,6):
                print('Error')
                seleccion = input('Ingrese el número asociado a su selección: ')

            if seleccion == '1':
                print(f'''
---------------------
------ EQUIPOS ------
---------------------''')
                self.mostrar_equipos()
            elif seleccion == '2':
                print(f'''
----------------------
------ ESTADIOS ------
----------------------
''')
                self.mostrar_estadios()
                