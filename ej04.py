# Definimos la clase Libro para registrar el inventario de la biblioteca
class Libro:
    # Inicializamos los atributos del libro en el constructor
    def __init__(self, titulo, autor, disponible):
        
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    # Definimos el metodo str para mostrar la ficha del libro
    def __str__(self):
        # Evaluamos el valor booleano para asignar un texto descriptivo al estado
        estado_texto = "Disponible" if self.disponible else "Prestado"
        # Devolvemos una cadena formateada con titulo, autor y el estado actual
        return f"Libro: '{self.titulo}' | Autor: {self.autor} | Estado: {estado_texto}"

# Creamos un primer objeto libro con estado disponible
libro_1 = Libro("Estructuras de Datos", "Jhon Legal", True)
# Creamos un segundo objeto libro con estado prestado
libro_2 = Libro("Redes de Computadoras", "Andres Recalde", False)

# la ficha del primer libro 
print(libro_1)
# la ficha del segundo libro 
print(libro_2)