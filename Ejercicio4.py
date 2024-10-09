#Ejercicio 4
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return 0
        else:
            return a / b
        
calculadora = Calculadora()
print('Suma:', calculadora.sumar(2, 2))
print('Resta:', calculadora.restar(50, 12))
print('Multiplicación:', calculadora.multiplicar(3, 5))
print('División:', calculadora.dividir(25, 3))
print('División:', calculadora.dividir(10, 0))