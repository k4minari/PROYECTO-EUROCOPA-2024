from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido

# Clase para el modulo que opera el gestionamiento de equipos/partidos/estadios

class GestionEquipos:
    def __init__(self, data_equipo, data_estadio, data_partido):
        self.data_equipo = data_equipo
        self.data_estadio = data_estadio
        self.data_partido = data_partido
        self.equipos = []
        self.estadios = []
        self.partidos = []
        
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
            
    def registro_partidos(self):
        for p in self.data_partido:
            id = p["id"]
            numero = p["number"]
            equipo_local = p["home"]["name"]
            equipo_visitante = p["away"]["name"]
            fecha = p["date"]
            grupo = p["group"]
            id_estadio = p["stadium_id"]
            nuevo_partido = Partido(id, numero, equipo_local, equipo_visitante, fecha, grupo, id_estadio)
            self.partidos.append(nuevo_partido)
            
                
    def registro_datos(self):
        self.registro_equipos()
        self.registro_estadios()
        self.registro_partidos()
        
    def mostrar_equipos(self):
        for equi in self.equipos:
            print(equi.show())
    
    def mostrar_estadios(self):
        for esta in self.estadios:
            print(esta.show())     
            
    def mostrar_partidos(self):
        for parti in self.partidos:
            print(parti.show())
            
    # FILTROS DE BUSQUEDA 
    
    def filtro_pais(self):
        pais_filtrado = [pais for pais in self.partidos if pais["equipo_local"] == self or pais["equipo_visitante"] == self]
        print(pais_filtrado)
    
    def filtro_por_pais(self):
        print(f'''
----------------------------
SELECCIONE EL PAIS DESEADO:
----------------------------

1. Alemania     2. Escocia
3. Hungria      4. Suiza
5. España       6. Croacia
7. Italia       8. Albania
9. Eslovenia    10. Dinamarca
11. Serbia      12. Inglaterra
13. Polonia     14. Países Bajos
15. Austria     16. Francia
17. Rumania     18. Ucrania
19. Belgica     20. Eslovaquia
21. Turquia     22. Georgia
23. Portugal    24. República Checa
''')
        
        seleccion = input('Ingrese el número asociado a su selección: ')
        while not seleccion.isnumeric() or int(seleccion) not in range(1,25):
            print('Error')
            seleccion = input('Ingrese el número asociado a su selección: ')
        
        if seleccion == '1':
            pass 

            
                       
    def menu(self):
        self.registro_datos()

        print('--BIENVENIDO/A A LA EURO 2024--')
        while True:
            print('''
1. Ver Equipos
2. Ver estadios
3. PARTIDOS
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
            
            elif seleccion == '3':
               
               self.sub_menu_partidos()
                
                
    def sub_menu_partidos(self):
        self.registro_datos()

        print(f'''
----------------------
------ PARTIDOS ------
----------------------
''')
        while True:
            print('''
1. Busqueda por país
2. Busqueda por estadio
3. Busqueda por fecha
4. Mostrar TODOS los partidos
5. Volver 
''')
            seleccion = input('Ingrese el número asociado a su selección: ')
            while not seleccion.isnumeric() or int(seleccion) not in range(1,6):
                print('Error')
                seleccion = input('Ingrese el número asociado a su selección: ')
                
            if seleccion == '1':
                print(f'''
BUSQUEDA POR EQUIPO
--------------------------''')
                self.filtro_por_pais()
            
            elif seleccion == '4':
                print(f'''
----------------------
------ PARTIDOS ------
----------------------
''')
                self.mostrar_partidos()
                
            elif seleccion == '5':
                self.menu()
