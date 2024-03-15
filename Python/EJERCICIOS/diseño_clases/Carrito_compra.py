class Carrito_compra:
    def __init__(self):
        self.productos = {}#sera de tipo diccionario

    def agregar_producto(self, pruducto, cantidad):
        if pruducto in self.productos:
            self.productos[pruducto] += cantidad
        else:
            self.productos[pruducto] = cantidad


    def calcular_total(self):
        total_precio = 0
        for producto, cantidad in self.productos:
            total_precio = producto.precio * cantidad
        return total_precio



