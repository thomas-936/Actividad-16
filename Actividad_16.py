print("Actividad 16")

class Libros:
    def __init__(self,codigo, titulo, autor, a_publicacion):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.a_publicacion = a_publicacion

    def __str__(self):
        return (f"Titulo del libro: {self.titulo}|   "
                f"Autor del libro: {self.autor}|   "
                f"Año de publicacion del libro: {self.a_publicacion}|   "
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
                codigo_libro = str(self.pedir_entero("Ingrese el codigo del libro"))
                if codigo_libro in self.dicc_libros:
                    print("Este libro ya ha sido registrado, intente con otro")
                else:
                    break
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            a_publicacion = self.pedir_entero("Inngrese el año de publicacion del libro")
            self.dicc_libros[codigo_libro] = Libros(codigo_libro, titulo, autor, a_publicacion)

class Usuario:
    def __init__(self, carnet, nombre, carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self):
        return (f"Carnet: {self.carnet}|   "
                f"Nombre: {self.nombre}|   "
                f"Carrera: {self.carrera}")

class Registro_Usuarios:
    def __init__(self):
        self.dicc_Usuarios = {}

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese dato valido... :)")

    def agregar_usuario(self):
        cantidad_usuarios = self.pedir_entero("Ingrese la cantidad de estudiantes para registrar: ")
        for i in range(cantidad_usuarios):
            print(f"Usuario {i+1}")
            while True:
                carnet = str(self.pedir_entero("Ingrese el codigo del estudiante: "))
                if carnet in self.dicc_Usuarios:
                    print(f"Este usuario ya ha sido registrado, intente de nuevo... ")
                else:
                    break
            nombre = input("Ingrese el nombre del estudiante: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            self.dicc_Usuarios[carnet] = Usuario(carnet, nombre, carrera)

