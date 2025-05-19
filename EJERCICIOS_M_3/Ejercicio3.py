class Producto:
    def __init__(self, precio):
        self.__precio = precio  # Atributo privado

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")

# Crear un producto con precio inicial
producto = Producto(50000)
print("Precio Inicial:", producto.precio)

# Cambiar el precio a uno válido
producto.precio = 60000
print("Nuevo Precio:", producto.precio)

# Intentar asignar un precio negativo
try:
    producto.precio = -1000
except ValueError as e:
    print("Error:", e)
