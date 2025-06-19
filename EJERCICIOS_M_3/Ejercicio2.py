class Empleado:
    def __init__ (self, salario):
        self ._salario=salario
        
class Gerente(Empleado):
    def __init__ (self, salario):
        super()._init_(salario)
        self._salario *= 1.20
    def obtener_salario (self):
        return self._salario