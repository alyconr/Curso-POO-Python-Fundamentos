
from abc import ABC, abstractmethod

# 📌 Clase Cliente (Asociación con Envío)
class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} - {self.telefono}"


# 📌 Clase Paquete (Composición dentro de Envío)
class Paquete:
    def __init__(self, peso, dimensiones, contenido):
        self._peso = peso  # Encapsulado protegido
        self.dimensiones = dimensiones
        self.contenido = contenido

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if valor > 0:
            self._peso = valor
        else:
            raise ValueError("El peso debe ser positivo")

    def __str__(self):
        return f"Paquete de {self.peso}kg, {self.dimensiones}, Contenido: {self.contenido}"


# 📌 Clase abstracta Envio (Herencia y Polimorfismo)
class Envio(ABC):
    def __init__(self, cliente, paquete):
        self.cliente = cliente          # Asociación
        self.paquete = paquete          # Composición
        self._estado = "Registrado"     # Encapsulado

    def actualizar_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    @property
    def estado(self):
        return self._estado

    @abstractmethod
    def calcular_costo(self):
        pass

    def __str__(self):
        return f"{self.cliente} | {self.paquete} | Estado: {self.estado}"


# 📌 Envío Estándar (Herencia)
class EnvioEstandar(Envio):
    def calcular_costo(self):
        return 5000 + (self.paquete.peso * 1000)


# 📌 Envío Exprés (Herencia y polimorfismo)
class EnvioExpress(Envio):
    def calcular_costo(self):
        return 10000 + (self.paquete.peso * 2000)


# 📌 Transportadora (Composición con múltiples envíos)
class Transportadora:
    def __init__(self, nombre):
        self.nombre = nombre
        self._envios = []  # Lista privada

    def agregar_envio(self, envio):
        self._envios.append(envio)

    def listar_envios(self):
        print(f"\n📦 Envíos registrados en {self.nombre}:")
        for envio in self._envios:
            print(envio)


# 📌 Factura (Agregación: cliente y envío viven fuera)
class Factura:
    def __init__(self, cliente, envio):
        self.cliente = cliente
        self.envio = envio

    def generar_factura(self):
        costo = self.envio.calcular_costo()
        return f"""
        📄 FACTURA
        Cliente: {self.cliente.nombre}
        Dirección: {self.cliente.direccion}
        Teléfono: {self.cliente.telefono}
        Tipo de envío: {type(self.envio).__name__}
        Estado del envío: {self.envio.estado}
        Detalles del paquete: {self.envio.paquete}
        Costo Total: ${costo:,}
        """


# -------------------------------
# 🧪 Simulación del sistema
# -------------------------------

if __name__ == "__main__":
    # Crear cliente
    cliente1 = Cliente("Ivan Yate", "Kra 48 b #68 f 40 Sur", "3024340814")

    # Crear paquete
    paquete1 = Paquete(2, "3,5 OZ", "Postres de Fresa Marca Ázura Desserts")

    # Crear envío express
    envio1 = EnvioExpress(cliente1, paquete1)
    envio1.actualizar_estado("En tránsito")

    # Crear empresa transportadora
    empresa = Transportadora("Rápidos S.A.")
    empresa.agregar_envio(envio1)

    # Crear factura
    factura = Factura(cliente1, envio1)

    # Mostrar factura
    print(factura.generar_factura())

    # Listar envíos
    empresa.listar_envios()

