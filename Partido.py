class Partido:
    def __init__(self, equipo_local, equipo_visitante, fecha, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.estadio = estadio
        
    def show(self):
        print(f'''
Equipo local: {self.equipo_local}
Equipo visitante: {self.equipo_visitante}
Fecha del encuentro: {self.fecha}
Lugar: {self.estadio}
''')