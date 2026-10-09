# Definimos la clase Cliente para representar los datos requeridos
class Cliente:
    # Inicializamos todos los datos en el constructor
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    # Definimos el metodo str para devolver la ficha legible
    def __str__(self):
        # Usamos f-strings para armar el texto con los atributos
        return f"Cliente: {self.nombre} | CI: {self.cedula} | Tel: {self.telefono}"

# Creamos el primer objeto cliente con sus datos personales
cliente_1 = Cliente("Joaquin Peralta", "4567891", "0981123456")
# Creamos el segundo objeto cliente para comprobar que guarda sus propios datos
cliente_2 = Cliente("Laura Chamorro", "1234567", "0982654321")

# Imprimimos en pantalla la ficha completa del primer cliente
print(cliente_1)
# Imprimimos en pantalla la ficha completa del segundo cliente
print(cliente_2)