#Ejercicio 2

class Libro:
    def __init__(self,titulo,autor,anio_publicacion,numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f'Titulo',self.titulo)
        print(f'Autor',self.autor)
        print(f'Año de publicacion',self.anio_publicacion)
        print(f'Numero de pagina',self.numero_paginas)


Libro = Libro('El Principito','Antoine Exupery','1986','90')

Libro.mostrar_informacion()


