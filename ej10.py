# Definimos una version basica de la clase Producto de los ejercicios anteriores
class Producto:
    # Inicializamos el producto con su nombre y precio
    def __init__(self, nombre, precio_unitario):

        self.nombre = nombre
        self.precio_unitario = precio_unitario
        
# Definimos la clase Item que asocia un producto con una cantidad especifica
class Item:
    # Inicializamos el item recibiendo un objeto de tipo Producto y la cantidad
    def __init__(self, producto, cantidad):
        # Guardamos la referencia al objeto producto
        self.producto = producto
        # Guardamos la cantidad que el cliente desea comprar
        self.cantidad = cantidad

    # Definimos el metodo para calcular el costo de este item en particular
    def calcular_subtotal(self):
        # Multiplicamos el precio del producto por la cantidad solicitada
        return self.producto.precio_unitario * self.cantidad

    # Definimos el metodo str para mostrar la fila de detalle del item
    def __str__(self):
        # Armamos el texto mostrando la cantidad, el nombre y el subtotal calculado
        return f"{self.cantidad}x {self.producto.nombre} | Subtotal: {self.calcular_subtotal()} Gs"

# Definimos la clase Carrito para agrupar toda la compra del cliente
class Carrito:
    # Inicializamos el carrito creando una coleccion vacia
    def __init__(self):
        # Creamos una lista interna para guardar los objetos Item
        self.items = []

    # Definimos el metodo para ingresar un nuevo item al carrito
    def agregar_item(self, item):
        # Insertamos el item en la lista usando append
        self.items.append(item)
        # Mostramos un mensaje confirmando que se agrego al carrito
        print(f"Agregado: {item.cantidad}x {item.producto.nombre}.")

    # Definimos el metodo para calcular la suma de todos los subtotales
    def calcular_total(self):
        # Inicializamos una variable acumuladora en cero
        total_general = 0
        # Iniciamos un bucle para recorrer cada item guardado
        for item in self.items:
            # Sumamos el subtotal del item actual al acumulador general
            total_general += item.calcular_subtotal()
        # Devolvemos el importe final
        return total_general
    # Definimos el metodo str para generar el ticket o resumen de la compra
    def __str__(self):
        # Creamos la variable de texto con el encabezado del resumen
        resumen = "\n--- Resumen de Compra ---\n"
        # Recorremos la lista de items
        for item in self.items:
            # Agregamos la representacion textual de cada item al resumen
            resumen += f"- {item}\n"
        # Agregamos una linea separadora visual
        resumen += "-------------------------\n"
        # Agregamos el total general llamando al metodo de calculo
        resumen += f"TOTAL A PAGAR: {self.calcular_total()} Gs\n"
        # Devolvemos todo el texto construido
        return resumen
# Creamos tres objetos producto con sus respectivos precios
producto_1 = Producto("Auriculares con cable", 50000)
producto_2 = Producto("Protector de pantalla", 70000)
producto_3 = Producto("Cargador Rapido", 80000)

# Creamos los items asociando cada producto con la cantidad deseada
item_1 = Item(producto_1, 1)
item_2 = Item(producto_2, 3)
item_3 = Item(producto_3, 2)

# Creamos el objeto carrito de compras vacio
mi_carrito = Carrito()

# Simulamos la accion del usuario agregando los items
print("--- Agregando al Carrito ---")
# Agregamos el primer item
mi_carrito.agregar_item(item_1)
# Agregamos el segundo item
mi_carrito.agregar_item(item_2)
# Agregamos el tercer item
mi_carrito.agregar_item(item_3)

# Imprimimos el carrito, lo que mostrara el detalle por item y el total a pagar
print(mi_carrito)