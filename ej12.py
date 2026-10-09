# Definimos la clase CuentaServicio para gestionar el plan de datos del cliente
class CuentaServicio:
    # Inicializamos la cuenta con el titular y la cantidad de gigas del plan
    def __init__(self, titular, gigas_incluidos):
        
        self.titular = titular
        self.gigas_incluidos = gigas_incluidos
        self.gigas_consumidos = 0
    # Definimos el metodo para calcular y devolver los datos disponibles
    def gigas_disponibles(self):
        # Restamos los gigas consumidos de los gigas originalmente incluidos
        return self.gigas_incluidos - self.gigas_consumidos

    # Definimos el metodo para registrar el uso de internet del cliente
    def registrar_consumo(self, cantidad):
        # Obtenemos el saldo actual disponible llamando al metodo anterior
        disponible = self.gigas_disponibles()
        # Validamos si los gigas disponibles alcanzan para el consumo solicitado
        if cantidad <= disponible:
            # Sumamos la cantidad utilizada al acumulador de consumo
            self.gigas_consumidos += cantidad
            # Mostramos un mensaje aprobando el consumo y mostrando el saldo restante
            print(f"Consumo de {cantidad} GB registrado. Quedan {self.gigas_disponibles()} GB disponibles.")
        # Si la cantidad pedida supera lo que queda en el plan
        else:
            # Mostramos un aviso de agotamiento y no sumamos el consumo para evitar saldo negativo
            print(f"AVISO: No se puede consumir {cantidad} GB. El paquete se agoto (Saldo actual: {disponible} GB).")
    # Definimos el metodo str para mostrar la informacion completa de la linea
    def __str__(self):
        # Armamos el resumen usando f-strings para mostrar el detalle completo
        return f"Linea: {self.titular} | Plan: {self.gigas_incluidos} GB | Consumidos: {self.gigas_consumidos} GB | Disponibles: {self.gigas_disponibles()} GB"
# Creamos un objeto cuenta para un cliente con un plan de 15 GB
mi_linea = CuentaServicio("Joaquin Peralta", 15)
# Mostramos el estado inicial de la linea
print("--- Estado Inicial ---")
print(mi_linea)
# Simulamos algunos dias de uso de internet
print("\n--- Registro de Consumos ---")
# Registramos un primer consumo valido
mi_linea.registrar_consumo(5)
# Registramos un segundo consumo valido
mi_linea.registrar_consumo(8)
# Intentamos registrar un consumo que excede lo que sobra en el plan (quedan 2 GB)
mi_linea.registrar_consumo(5)

# Mostramos el estado final de la linea telefonica
print("\n--- Estado Final ---")
print(mi_linea)