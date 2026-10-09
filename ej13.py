# Definimos la clase Habitacion para gestionar la ocupacion del hotel
class Habitacion:
    # Inicializamos los atributos de la habitacion en el constructor
    def __init__(self, numero, tipo, tarifa_por_noche):
        
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.esta_libre = True
    # Definimos el metodo para registrar el ingreso de huespedes
    def ocupar(self):
        # Verificamos si la habitacion se encuentra actualmente libre
        if self.esta_libre:
            # Cambiamos el estado a False para indicar que ahora esta ocupada
            self.esta_libre = False
            # Imprimimos un mensaje confirmando la accion
            print(f"Exito: La habitacion {self.numero} ha sido ocupada.")
        # Si el estado actual ya era ocupado (False) entra en esta rama
        else:
            # Mostramos un mensaje de error indicando la situacion
            print(f"Error: La habitacion {self.numero} ya se encuentra ocupada.")

    # Definimos el metodo para registrar la salida de los huespedes
    def liberar(self):
        # Verificamos si la habitacion esta efectivamente ocupada antes de liberarla
        if not self.esta_libre:
            # Cambiamos el estado de vuelta a True para marcarla como disponible
            self.esta_libre = True
            # Mostramos un mensaje confirmando que ya esta lista para otro cliente
            print(f"Exito: La habitacion {self.numero} ha sido liberada.")
        # Si el usuario intenta liberar una habitacion que ya estaba libre
        else:
            # Mostramos un aviso de que la operacion no es necesaria
            print(f"Aviso: La habitacion {self.numero} ya estaba libre.")

    # Definimos el metodo para calcular cuanto debe pagar el cliente por su estadia
    def calcular_costo_estadia(self, cantidad_noches):
        # Multiplicamos la tarifa base por la cantidad de noches solicitadas
        costo_total = self.tarifa_por_noche * cantidad_noches
        # Imprimimos el calculo en pantalla para informacion del recepcionista
        print(f"Costo por {cantidad_noches} noches en la habitacion {self.numero}: {costo_total} Gs.")
        # Retornamos el valor numerico final
        return costo_total

    # Definimos el metodo str para mostrar el estado actual de la pieza
    def __str__(self):
        # Evaluamos el atributo booleano para asignar un texto descriptivo
        estado_texto = "Libre" if self.esta_libre else "Ocupada"
        # Retornamos una cadena con todos los detalles clave usando f-strings
        return f"Habitacion {self.numero} | Tipo: {self.tipo} | Tarifa: {self.tarifa_por_noche} Gs/noche | Estado: {estado_texto}"


# Creamos un objeto habitacion con sus datos basicos
habitacion_101 = Habitacion(101, "Matrimonial", 350000)

# Imprimimos el estado inicial de la habitacion
print("--- Estado Inicial ---")
print(habitacion_101)

# Simulamos el proceso completo pedido en la tarea
print("\n--- Simulacion de Estadia ---")
# Intentamos ocupar la habitacion que esta libre
habitacion_101.ocupar()
# Intentamos ocupar la misma habitacion para probar la validacion de error
habitacion_101.ocupar()

# Mostramos como cambia el estado intermedio imprimiendo la ficha
print("\n--- Estado Intermedio ---")
print(habitacion_101)

print("\n--- Calculo y Salida ---")
# Calculamos el costo de una estadia de 3 noches pasando el valor al metodo
habitacion_101.calcular_costo_estadia(3)
# Liberamos la habitacion tras el pago del cliente
habitacion_101.liberar()

# Mostramos el estado final para confirmar que vuelve a estar libre
print("\n--- Estado Final ---")
print(habitacion_101)