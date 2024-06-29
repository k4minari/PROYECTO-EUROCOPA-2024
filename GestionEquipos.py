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

            # Referenciar objeto de tipo Equipo
            equipo_local_id = p["home"]["id"]
            for equipo in self.equipos:
                if equipo_local_id == equipo.id:
                    equipo_local = equipo.nombre

            # Referenciar objeto de tipo Equipo
            equipo_visitante_id = p["away"]["id"]
            for equipo in self.equipos:
                if equipo_visitante_id == equipo.id:
                    equipo_visitante = equipo.nombre

            fecha = p["date"]
            grupo = p["group"]

            # Referenciar objeto de tipo Estadio
            id_estadio = p["stadium_id"]
            for estadio in self.estadios:
                if estadio.id == id_estadio:
                    estadioGuardar = estadio.nombre

            estadio = None
            nuevo_partido = Partido(id, numero, equipo_local, equipo_visitante, fecha, grupo, estadioGuardar)
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
    
    def filtro_por_pais(self):
        
        def buscar_partido_nombre(self, nombre):
            resultado = []
            for partido in self.partidos:
                if nombre in partido.equipo_local or nombre in partido.equipo_visitante:
                    resultado.append(partido)
            
            print("\n")
            if len(resultado) != 0:
                for partido in resultado:
                    print(partido.show())
        
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
            nombre = 'Germany'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '2':
            nombre = 'Scotland'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '3':
            nombre = 'Hungary'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '4':
            nombre = 'Switzerland'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '5':
            nombre = 'Spain'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '6':
            nombre = 'Croatia'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '7':
            nombre = 'Italy'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '8':
            nombre = 'Albania'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '9':
            nombre = 'Slovenia'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '10':
            nombre = 'Denmark'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '11':
            nombre = 'Serbia'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '12':
            nombre = 'England'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '13':
            nombre = 'Poland'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '14':
            nombre = 'Netherlands'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '15':
            nombre = 'Austria'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '16':
            nombre = 'France'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '17':
            nombre = 'Romania'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '18':
            nombre = 'Ukraine'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '19':
            nombre = 'Belgium'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '20':
            nombre = 'Slovakia'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '21':
            nombre = 'Turkey'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '22':
            nombre = 'Georgia'
            buscar_partido_nombre(self, nombre)
            
        elif seleccion == '23':
            nombre = 'Portugal'
            buscar_partido_nombre(self, nombre)
            
        else:
            nombre = 'Czech Republic'
            buscar_partido_nombre(self, nombre)
            
    def filtro_por_estadio(self):
        
        def buscar_partido_estadio(self, nombre):
            resultado = []
            for estadio in self.partidos:
                if nombre in estadio.estadio:
                    resultado.append(estadio)
            
            print("\n")
            if len(resultado) != 0:
                for estadio in resultado:
                    print(estadio.show())
        
        print(f'''
----------------------------
SELECCIONE EL ESTADIO DESEADO:
----------------------------

1. Estadio Olímpico de Berlín
2. Allianz Arena
3. Signal Iduna Park
4. MHPArena
5. Veltins-Arena
6. Volksparkstadion
7. Deutsche Bank Park
8. Estadio Rhein Energie
9. Red Bull Arena
10. Merkur Spiel-Arena
''')
        
        seleccion = input('Ingrese el número asociado a su selección: ')
        while not seleccion.isnumeric() or int(seleccion) not in range(1,11):
            print('Error')
            seleccion = input('Ingrese el número asociado a su selección: ')
            
        if seleccion == '1':
            nombre = 'Estadio Olímpico de Berlín'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '2':
            nombre = 'Allianz Arena'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '3':
            nombre = 'Signal Iduna Park'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '4':
            nombre = 'MHPArena'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '5':
            nombre = 'Veltins-Arena'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '6':
            nombre = 'Volksparkstadion'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '7':
            nombre = 'Deutsche Bank Park'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '8':
            nombre = 'Estadio Rhein Energie'
            buscar_partido_estadio(self, nombre)
            
        elif seleccion == '9':
            nombre = 'Red Bull Arena'
            buscar_partido_estadio(self, nombre)
            
        else:
            nombre = 'Merkur Spiel-Arena'
            buscar_partido_estadio(self, nombre)
            
    def filtro_por_fecha(self):
        
        def buscar_partido_fecha(self, fecha):
            resultado = []
            for dia in self.partidos:
                if fecha in dia.fecha:
                    resultado.append(dia)
            
            print("\n")
            if len(resultado) != 0:
                for dia in resultado:
                    print(dia.show())
        
        print(f'''
----------------------------
SELECCIONE LA FECHA DESEADA:
----------------------------

1. Partidos para la fecha: 2024-06-14
2. Partidos para la fecha: 2024-06-15
3. Partidos para la fecha: 2024-06-16
4. Partidos para la fecha: 2024-06-17
5. Partidos para la fecha: 2024-06-18
6. Partidos para la fecha: 2024-06-19
7. Partidos para la fecha: 2024-06-20
8. Partidos para la fecha: 2024-06-21
9. Partidos para la fecha: 2024-06-22
10. Partidos para la fecha: 2024-06-23
11. Partidos para la fecha: 2024-06-24
12. Partidos para la fecha: 2024-06-25
13. Partidos para la fecha: 2024-06-26
''')
        
        seleccion = input('Ingrese el número asociado a su selección: ')
        while not seleccion.isnumeric() or int(seleccion) not in range(1,14):
            print('Error')
            seleccion = input('Ingrese el número asociado a su selección: ')
            
        if seleccion == '1':
            fecha = '2024-06-14'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '2':
            fecha = '2024-06-15'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '3':
            fecha = '2024-06-16'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '4':
            fecha = '2024-06-17'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '5':
            fecha = '2024-06-18'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '6':
            fecha = '2024-06-19'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '7':
            fecha = '2024-06-20'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '8':
            fecha = '2024-06-21'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '9':
            fecha = '2024-06-22'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '10':
            fecha = '2024-06-23'
            buscar_partido_fecha(self, fecha)
            
        elif seleccion == '11':
            fecha = '2024-06-24'
            buscar_partido_fecha(self, fecha)
        
        elif seleccion == '12':
            fecha = '2024-06-25'
            buscar_partido_fecha(self, fecha)
            
        else:
            fecha = '2024-06-26'
            buscar_partido_fecha(self, fecha)

            
                       
    def menu(self):
        self.registro_datos()

        print(f'''
--BIENVENIDO/A A LA EURO 2024--
''')
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
        while True:
            print(f'''
----------------------
------ PARTIDOS ------
----------------------
''')
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
--------------------------
BUSQUEDA POR EQUIPO
--------------------------
''')
                self.filtro_por_pais()
                
            elif seleccion == '2':
                print(f'''
--------------------------
BUSQUEDA POR ESTADIO
--------------------------
''')
                self.filtro_por_estadio()
                
            elif seleccion == '3':
                print(f'''
--------------------------
BUSQUEDA POR FECHA
--------------------------
''')
                self.filtro_por_fecha()
            
            elif seleccion == '4':
                print(f'''
----------------------
------ PARTIDOS ------
----------------------
''')
                self.mostrar_partidos()
                
            elif seleccion == '5':
                self.menu()
