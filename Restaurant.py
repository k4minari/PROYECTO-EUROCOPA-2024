
class Restaurant:

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def show(self):
        return f"""
            name: {self.nombre}
            products: {self.productos}"""