# Definimos la clase Empleado para representar a los trabajadores de la empresa
class Empleado:
    # Inicializamos los atributos del empleado en el constructor
    def __init__(self, nombre, cargo, salario_mensual):

        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    # Definimos el metodo para calcular el salario anual
    def calcular_salario_anual(self):
        # Multiplicamos el salario por 13 para contemplar los 12 meses mas el aguinaldo
        return self.salario_mensual * 13

    # Definimos el metodo str para mostrar la informacion del empleado de forma legible
    def __str__(self):
        # Devolvemos una cadena usando f-strings con nombre, cargo y salario
        return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario: {self.salario_mensual} Gs"

# Creamos el primer objeto empleado con sus respectivos datos
empleado_1 = Empleado("Carlos Isasi", "Soporte Tecnico", 3500000)
# Creamos el segundo objeto empleado con sus respectivos datos
empleado_2 = Empleado("Laura Martinez", "Contadora", 6500000)

# los datos del primer empleado
print(empleado_1)
# Calculamos y mostramos el salario anual 
print(f"Salario anual cobrado (con aguinaldo): {empleado_1.calcular_salario_anual()} Gs\n")

# los datos del segundo empleado 
print(empleado_2)
# Calculamos y mostramos el salario anual d
print(f"Salario anual cobrado (con aguinaldo): {empleado_2.calcular_salario_anual()} Gs")