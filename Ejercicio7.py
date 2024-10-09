#Ejercicio 7

try:
    numero = 12
    
    print(f"Tabla de multiplicacion del {numero}:")
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Por favor, ingrese un número válido.")