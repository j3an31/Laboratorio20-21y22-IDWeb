class Libro:
    def __init__(self, titulo, autor, año, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"> '{self.titulo}' ha sido prestado"
        else:
            return f"> '{self.titulo}' no está disponible"
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"> '{self.titulo}' ha sido devuelto"
        else:
            return f"> '{self.titulo}' ya estaba disponible"
    def mostrar_info(self):
        return f"Libro: {self.titulo} Autor: {self.autor} Publicado: ({self.año}) Disponible: {self.disponible}"

class Biblioteca:
    def __init__(self):
        self.lista_libros = []
    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"> Libro '{libro.titulo}' agregado a la biblioteca")
    def listar_libros(self):
        print("\n" + "=" * 30)
        print("LIBROS EN LA BIBLIOTECA")
        print("=" * 30)
        if not self.lista_libros:
            print("> ¡No hay libros en la biblioteca!")
        else:
            for i in range(len(self.lista_libros)):
                print(f"{i+1}.- {self.lista_libros[i].mostrar_info()}")
            print()
    def buscar_por_autor(self, autor):
        se_encontro = False
        for i in range(len(self.lista_libros)):
            if autor.lower() == self.lista_libros[i].autor.lower():
                print("> ¡Libro encontrado!")
                print(self.lista_libros[i].mostrar_info())
                se_encontro = True
        if not se_encontro:
            print(">¡No se encontró el libro!")
    def prestar_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.titulo.lower() == titulo.lower():
                return libro.prestar()
        return f"> No se encontró el libro '{titulo}'"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, formato, tamañoMB):
        super().__init__(titulo, autor, año, disponible=True)
        self.formato = formato
        self.tamañoMB = tamañoMB
    def prestar(self):
        return f"> '{self.titulo}' (en {self.formato}) está disponible para descarga"
    def mostrar_info(self):
        return f"Libro: {self.titulo} Autor: {self.autor} Publicado: ({self.año}) Formato: {self.formato} Tamaño: {self.tamañoMB} MB"

# Creando biblioteca
biblioteca = Biblioteca()

# Creando libros físicos
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

# Creando libros digitales
libroD1 = LibroDigital("Python Crash Course", "Eric Matthes", 2019, "PDF", 5.2)
libroD2 = LibroDigital("Clean Code", "Robert Martin", 2008, "WORD", 3.8)

# Agregando libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libroD1)
biblioteca.agregar_libro(libroD2)

# 1. Listar todos los libros
biblioteca.listar_libros()

# 2. Prestar un libro físico
print("--- Prestando libro físico ---")
print(biblioteca.prestar_libro("1984"))
print()

# 3. Prestar un libro digital 5 veces
print("--- Prestando libro digital 5 veces ---")
for i in range(1, 6):
    print(f"{i}. {biblioteca.prestar_libro('Clean Code')}")
print()

# 4. Intentar prestar un libro ya prestado
print("--- Intentando prestar libro ya prestado ---")
print(biblioteca.prestar_libro("1984"))
print()

# 5. Buscar por autor
print("--- Buscando libro por autor ---")
biblioteca.buscar_por_autor("Gabriel García Márquez")