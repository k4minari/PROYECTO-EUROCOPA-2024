
from Equipo import Equipo

class GestionEquipos:
    def __init__(self, data_equipo):
        self.data_equipo = data_equipo
        self.equipos = []
        
    def registro_equipos(self):
        for e in self.data_equipo:
            id = e["id"]
            codigo = e["code"]
            nombre = e["name"]
            grupo = e["group"]
            nuevo_equipo = Equipo(id, codigo, nombre, grupo)
            self.equipos.append(nuevo_equipo)
            
    def registro_datos(self):
        self.registro_equipos()
        
    def mostrar_equipos(self):
        for equi in self.equipos:
            print(equi.show())
            
    def menu(self):
        self.registro_datos()

        print('--BIENVENIDO/A A LA EURO 2024--')
        while True:
            print('''
1. ...
2. Ver Equipos
''')
            seleccion = input('Ingrese el número asociado a su selección: ')
            while not seleccion.isnumeric() or int(seleccion) not in range(1,6):
                print('Error')
                seleccion = input('Ingrese el número asociado a su selección: ')

            if seleccion == '1':
                print('LIBROS DISPONIBLES')
                self.available_books()
            elif seleccion == '2':
                print('Equipos: ')
                self.mostrar_equipos()