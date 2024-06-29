
class Partido:
    def __init__(self, id, numero, equipo_local, equipo_visitante, fecha, grupo, estadio):
        self.id = id
        self.numero = numero
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.grupo = grupo
        self.estadio = estadio
        
    def show(self):
        return(f'''
-------------------------------------------
Equipo local: {self.equipo_local}                 

VS

Equipo visitante: {self.equipo_visitante}
___________________________________
Fecha del encuentro: {self.fecha}
Lugar: {self.estadio}
___________________________________
--------------------------------------------
''')