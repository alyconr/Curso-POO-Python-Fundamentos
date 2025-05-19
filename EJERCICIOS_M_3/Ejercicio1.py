class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.__saldo=saldo
    def consultar_saldo (self):
        return self.__saldo
    
cuenta = CuentaBancaria("Sergio", 800)
print ("titular: ", cuenta.titular)
print("saldo: ", cuenta.consultar_saldo())

try:
    print ("Acceso directo al saldo: ", cuenta.saldo)
except AttributeError as e:
    print ("Acceso directo: ", e)