#Ejercicio 10
import random
import string

def generar_contraseña(longitud):
    longitud = 10    
    
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

try:
    longitud = 10
    contraseña_generada = generar_contraseña(longitud)
    print(f"Contraseña generada: {contraseña_generada}")
except ValueError as e:
    print(e)
