class Producto:
    ID_producto = 0
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_productos = cantidad_disponible
        self.id_producto = Producto.ID_producto
        self.id_producto += 1

    def __str__(self):
        return f'idP: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}, cantidad disponible: {self.cantidad_productos}'

