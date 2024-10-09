#Ejercicio 9
import random

def numeroadivinado():

    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Adivina el número entre 1 y 100!")

    while not adivinado:
        try:
            intento = int(input("Ingresa tu intento: "))
            intentos += 1
            
            if intento < numero_aleatorio:
                print("El número es mayor.")
            elif intento > numero_aleatorio:
                print("El número es menor.")
            else:
                adivinado = True
                print(f"¡Felicitaciones! Has adivinado el número en {intentos} intentos.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")

numeroadivinado()
