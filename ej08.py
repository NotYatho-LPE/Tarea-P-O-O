# Definimos la clase Cancion para representar las pistas individuales
class Cancion:
    # Inicializamos los atributos de la cancion en el constructor
    def __init__(self, titulo, artista, duracion):
    
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    # Definimos el metodo str para mostrar la informacion de la cancion
    def __str__(self):
        # Retornamos una cadena usando f-strings con titulo, artista y duracion
        return f"{self.titulo} de {self.artista} ({self.duracion} min)"


# Definimos la clase ListaReproduccion que agrupara varias canciones
class ListaReproduccion:
    # Inicializamos la lista con un nombre y una coleccion vacia
    def __init__(self, nombre):
        # Asignamos el nombre de la lista de reproduccion
        self.nombre = nombre
        # Creamos una lista de Python vacia para almacenar los objetos Cancion
        self.canciones = []

    # Definimos el metodo para agregar una nueva cancion a la coleccion
    def agregar_cancion(self, cancion):
        # Usamos append para insertar el objeto cancion en nuestra lista interna
        self.canciones.append(cancion)
        # Imprimimos un mensaje confirmando la accion
        print(f"Pista '{cancion.titulo}' agregada a la lista '{self.nombre}'.")

    # Definimos el metodo para recorrer la coleccion y sumar la duracion
    def calcular_duracion_total(self):
        # Inicializamos una variable acumuladora en cero
        total = 0
        # Iniciamos un ciclo for para recorrer cada objeto cancion guardado
        for cancion in self.canciones:
            # Sumamos el atributo duracion de la cancion actual al acumulador
            total += cancion.duracion
        # Retornamos la sumatoria total
        return total

    # Definimos el metodo str para mostrar todas las canciones y la duracion final
    def __str__(self):
        # Creamos una variable de texto con el encabezado de la lista
        texto_salida = f"\n--- Lista de Reproduccion: {self.nombre} ---\n"
        
        # Recorremos nuevamente las canciones para listarlas una por una
        for cancion in self.canciones:
            # Concatenamos la representacion str de cada cancion agregando un salto de linea
            texto_salida += f"- {cancion}\n"
            
        # Obtenemos la duracion total llamando al metodo interno de la clase
        duracion_final = self.calcular_duracion_total()
        # Concatenamos la duracion total al final del bloque de texto
        texto_salida += f"\nDuracion total de la lista: {duracion_final} minutos"
        
        # Devolvemos todo el texto construido
        return texto_salida


# Creamos tres objetos Cancion independientes
cancion_1 = Cancion("Wonderwall", "Oasis", 4.40)
cancion_2 = Cancion("Song 2", "Blur", 2.03)
cancion_3 = Cancion("Supersonic", "Oasis", 4.30)

# Creamos un objeto ListaReproduccion para agrupar temas clasicos
mi_lista = ListaReproduccion("Rock Ingles")

# Agregamos la primera cancion pasando el objeto completo como parametro
mi_lista.agregar_cancion(cancion_1)
# Agregamos la segunda cancion
mi_lista.agregar_cancion(cancion_2)
# Agregamos la tercera cancion
mi_lista.agregar_cancion(cancion_3)

print(mi_lista)