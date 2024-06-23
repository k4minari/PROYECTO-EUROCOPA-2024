
class Partido:
    def __init__(self, id, numero, equipo_local, equipo_visitante, fecha, grupo, id_estadio):
        self.id = id
        self.numero = numero
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.grupo = grupo
        self.id_estadio = id_estadio
        
    def show(self):
        print(f'''
-------------------------------------------
Equipo local: {self.equipo_local}                 

VS

Equipo visitante: {self.equipo_visitante}
___________________________________
Fecha del encuentro: {self.fecha}
Lugar: {self.id_estadio}
___________________________________
--------------------------------------------
''')