# Definimos la clase Producto para gestionar el inventario y sus movimientos
class Producto:
    # Inicializamos el producto con su nombre, precio, stock actual y el limite minimo
    def __init__(self, nombre, precio, stock_inicial, stock_minimo):
    
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial
        self.stock_minimo = stock_minimo

    # Definimos el metodo para sumar unidades al stock existente
    def ingresar_mercaderia(self, cantidad):
        # Verificamos que la cantidad a ingresar sea positiva
        if cantidad > 0:
            # Sumamos las unidades al atributo de stock
            self.stock += cantidad
            # Mostramos un mensaje confirmando el ingreso
            print(f"Ingreso exitoso: Se sumaron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

    # Definimos el metodo para registrar la salida de mercaderia por ventas
    def registrar_venta(self, cantidad):
        # Validamos que haya suficientes unidades para cubrir la venta sin dejar saldo negativo
        if cantidad <= self.stock:
            # Restamos las unidades vendidas del stock actual
            self.stock -= cantidad
            # Confirmamos la venta por consola
            print(f"Venta registrada: Salieron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")
            
            # Comprobamos si el stock restante quedo por debajo del umbral minimo
            if self.stock < self.stock_minimo:
                # Mostramos la alerta de reposicion solicitada por el ejercicio
                print(f"*** ALERTA: El stock de {self.nombre} ({self.stock}) esta por debajo del minimo ({self.stock_minimo}). Reponer mercaderia. ***")
        # Si la cantidad solicitada supera el stock, rechazamos la operacion
        else:
            # Imprimimos un mensaje de error detallando el motivo
            print(f"Error de venta: No hay stock suficiente de {self.nombre}. Stock disponible: {self.stock}")

    # Definimos el metodo str para devolver la informacion principal del articulo
    def __str__(self):
        # Usamos f-strings para armar el texto con el nombre y su nivel de stock
        return f"Producto: {self.nombre} | Stock actual: {self.stock} | Stock minimo: {self.stock_minimo}\n"

# Creamos un objeto producto con 20 unidades iniciales y alerta configurada al bajar de 10
producto = Producto("Cafe Molido", 25000, 20, 10)

# Imprimimos el estado inicial del producto
print("--- Estado Inicial ---")
print(producto)

# Simulamos las operaciones de ingreso y venta
print("--- Movimientos ---")
# Registramos una venta normal que no dispara la alerta (quedan 15)
producto.registrar_venta(5)
# Registramos una venta grande que hace caer el stock por debajo del minimo de 10
producto.registrar_venta(8)
# Intentamos vender mas de lo que queda en stock para probar la validacion (quedan 7)
producto.registrar_venta(10)
# Ingresamos mercaderia para recuperar los niveles de inventario
producto.ingresar_mercaderia(15)