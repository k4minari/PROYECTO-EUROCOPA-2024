class Estadio:
    def __init__(self, id, nombre, ciudad, capacidad, restaurantes):
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.restaurates = restaurantes
        
    def show(self):
        print(f'''
ID del estadio: {self.id}
------------------------------------
Estadio: {self.nombre}
Ciudad de ubicación: {self.ciudad}
Capacidad actual: {self.capacidad}
____________________________________
''')
