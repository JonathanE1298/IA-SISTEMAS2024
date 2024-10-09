#ejercicio8

def contar_vocales(frase):
    vocales = 'aeiouAEIOU'
    contador = 0
    
    for vocal in frase:
        if vocal in vocales:
            contador += 1
            
    return contador

# Pide al usuario que ingrese una frase
frase = 'Juro Solemnemente que mis intenciones no son buenas'

numero_de_vocales = contar_vocales(frase)

print(f"El número de vocales en la frase es: {numero_de_vocales}")
