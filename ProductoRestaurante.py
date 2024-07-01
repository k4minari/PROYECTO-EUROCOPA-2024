class ProductoRestaurante:
    def __init__(self, nombre, cantidad, precio, adicional, stock):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.adicional = adicional
        self.stock = stock
        self.sold = 0

    def show(self):
        return f'''
Nombre: {self.nombre}
Vendido: {self.cantidad}
Precio = {self.precio}
Tipo de producto: {self.adicional}
stock: {self.stock}
'''