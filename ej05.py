# Definimos la clase Vehiculo para representar los rodados de la agencia automotriz
class Vehiculo:
    # Inicializamos los atributos del vehiculo en el constructor
    def __init__(self, marca, modelo, anho, precio):
        
        self.marca = marca
        self.modelo = modelo
        self.anho = anho
        self.precio = precio

    # Definimos el metodo para armar la descripcion comercial
    def obtener_descripcion_comercial(self):
        # Formateamos el precio con separador de miles usando f-strings y reemplazamos la coma por punto
        precio_formateado = f"{self.precio:,}".replace(",", ".")
        # Devolvemos la cadena formateada como se pide en el requerimiento
        return f"{self.marca} {self.modelo} {self.anho} - {precio_formateado} Gs."

    # Definimos el metodo str para mostrar el objeto de forma legible
    def __str__(self):
        # Retornamos directamente el resultado del metodo de descripcion comercial
        return self.obtener_descripcion_comercial()

# Creamos el primer objeto vehiculo con sus datos
vehiculo_1 = Vehiculo("Toyota", "Auris", 2020, 95000000)
# Creamos el segundo objeto vehiculo con sus datos
vehiculo_2 = Vehiculo("Kia", "Soluto", 2019, 45000000)

# la descripcion del primer vehiculo 
print(vehiculo_1)
# la descripcion del segundo vehiculo 
print(vehiculo_2)