# Definimos la clase Producto para representar los articulos del almacen
class Producto:
    # Inicializamos los atributos del producto en el constructor
    def __init__(self, nombre, precio_unitario, cantidad_en_stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_en_stock = cantidad_en_stock

    # Definimos el metodo para calcular el valor total en stock
    def calcular_valor_total(self):
        # Multiplicamos el precio unitario por la cantidad en stock y devolvemos el resultado
        return self.precio_unitario * self.cantidad_en_stock

    # Definimos el metodo str para mostrar la informacion del producto de forma legible
    def __str__(self):
        # Devolvemos una cadena formateada con f-strings mostrando nombre, precio y stock
        return f"Producto: {self.nombre} | Precio: {self.precio_unitario} Gs | Stock: {self.cantidad_en_stock} unidades"

# Creamos el primer producto de despensa
producto_1 = Producto("Yerba Mate", 15000, 20)
# El segundo producto de despensa
producto_2 = Producto("Azucar", 7000, 50)
# El tercer producto de despensa
producto_3 = Producto("Fideo", 5000, 30)

# Mostramos los datos del primer producto 
print(producto_1)
# Imprimimos el valor total en stock del primer producto llamando a su metodo
print(f"Valor total de {producto_1.nombre} en stock: {producto_1.calcular_valor_total()} Gs\n")
# Mostramos los datos del segundo producto 
print(producto_2)
# Imprimimos el valor total en stock del segundo producto llamando a su metodo
print(f"Valor total de {producto_2.nombre} en stock: {producto_2.calcular_valor_total()} Gs\n")
# Mostramos los datos del tercer producto 
print(producto_3)
# Imprimimos el valor total en stock del tercer producto llamando a su metodo
print(f"Valor total de {producto_3.nombre} en stock: {producto_3.calcular_valor_total()} Gs")