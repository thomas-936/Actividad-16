from traceback import print_tb

print("Actividad 16")

class Libros:
    def __init__(self, titulo, autor, año_publicacion, codigo):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.codigo = codigo

    def __str__(self):
        return (f"Titulo del libro: {self.titulo}|   "
                f"Autor del libro: {self.autor}|   "
                f"Año de publicacion del libro: {self.año_publicacion}|   "
                f"Codigo del libro: {self.codigo}")

class Registrar_Libros:
    def __init__(self):
        self.dicc_libros = {}

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un dato Valido")

    def agregar_libro(self):

        cantidad = self.pedir_entero("Ingrese la cantidad de libros para registrar: ")
        for i in  range(cantidad):
            print("-----------------------------------------")
            print(f"Ingrese el libro {i+1}")
            while True:
                codigo = input("Ingrese el codigo del libro: ")
                if codigo in self.dicc_libros:
                    print("Este l")

