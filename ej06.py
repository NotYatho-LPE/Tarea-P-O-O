# Definimos la clase CuentaCorriente para manejar el saldo y consumos del cliente
class CuentaCorriente:
    # Inicializamos la cuenta con el nombre del cliente y un saldo que por defecto es cero
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial
    # Definimos el metodo para cargar saldo a la cuenta
    def acreditar(self, monto):
        # Verificamos que el monto a cargar sea un numero estrictamente positivo
        if monto > 0:
            # Sumamos el monto al saldo actual de la cuenta
            self.saldo += monto
            # Imprimimos un mensaje confirmando la operacion exitosa
            print(f"Se acreditaron {monto} Gs. Saldo actual: {self.saldo} Gs.")
        # Si el monto es cero o negativo, ejecutamos esta rama
        else:
            # Mostramos un mensaje de error sin alterar el saldo
            print("Error: El monto a acreditar debe ser mayor a cero.")
    # Definimos el metodo para registrar una compra o consumo
    def consumir(self, monto):
        # Validamos si el saldo actual es suficiente para cubrir el consumo
        if monto <= self.saldo:
            # Restamos el monto del saldo disponible
            self.saldo -= monto
            # Imprimimos un mensaje de aprobacion
            print(f"Consumo de {monto} Gs aprobado. Saldo restante: {self.saldo} Gs.")
        # Si el saldo es menor al monto solicitado, rechazamos la compra
        else:
            # Mostramos un aviso de fondos insuficientes y no modificamos el saldo
            print(f"Aviso: Consumo de {monto} Gs rechazado por falta de fondos. Saldo actual: {self.saldo} Gs.")
    # Definimos el metodo str para mostrar el estado general de la cuenta
    def __str__(self):
        # Retornamos el titular y su saldo actual usando f-strings
        return f"Cuenta Corriente de {self.cliente} | Saldo total: {self.saldo} Gs\n"
# Creamos un objeto de cuenta corriente para el cliente Joaquin Peralta
cuenta = CuentaCorriente("Joaquin Peralta")
# Mostramos el estado inicial de la cuenta imprimiendo el objeto
print("--- Estado Inicial ---")
print(cuenta)
# Simulamos la secuencia de operaciones solicitada
print("--- Movimientos ---")
# Acreditamos saldo valido a la cuenta
cuenta.acreditar(150000)
# Registramos un consumo valido que sera aprobado
cuenta.consumir(50000)
# Intentamos registrar un consumo que supere el saldo restante (debe rechazarse)
cuenta.consumir(200000)
# El estado final 
print("\n--- Estado Final ---")
print(cuenta)