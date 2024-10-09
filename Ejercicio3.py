#Ejercicio 3

class CuentaBancaria:
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, cantidad):
        self.saldo = cantidad + self.saldo

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad  
        else:
            print('Saldo insuficiente')

    def mostrar_saldo(self):
        print('Saldo actual:', self.saldo)

cuenta = CuentaBancaria('Jonathan Alberto Enamorado ')
print('Cuenta bancaria de: ' + cuenta.titular) 
cuenta.mostrar_saldo()
cuenta.depositar(1500)
cuenta.mostrar_saldo()
cuenta.retirar(270)
cuenta.mostrar_saldo()
