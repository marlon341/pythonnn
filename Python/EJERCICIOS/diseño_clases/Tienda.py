class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = {}

    def agregar_producto(self, pruducto, cantidad):
        if pruducto in self.inventario:
            self.inventario[pruducto] += cantidad
        else:
            self.productos[pruducto] = cantidad

    def realizar_ventas(self, carrito):
        for producto, valor in carrito:
            producto

