class ProductoRestaurante:
    def __init__(self, nombre, cantidad, precio, adicional, stock):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.adicional = adicional
        self.stock = stock
        self.sold = 0

    def show(self):
        return f"""
            name = {self.nombre}
            quantity = {self.cantidad}
            price = {self.precio}
            adicional = {self.adicional}
            stock = {self.stock}
            """