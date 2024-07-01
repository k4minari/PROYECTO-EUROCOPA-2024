
class Restaurant:

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def show(self):
        return f'''
Nombre: {self.nombre}
Productos: {self.productos}
'''