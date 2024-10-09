#Ejercicio5

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

try:
    numero = 12
    if es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
