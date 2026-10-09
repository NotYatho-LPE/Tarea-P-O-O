# Definimos la clase Estudiante para llevar el registro academico
class Estudiante:
    # Inicializamos el estudiante con su nombre y una coleccion para sus notas
    def __init__(self, nombre):

        self.nombre = nombre
        self.materias = {}

    # Definimos el metodo para registrar la nota de una materia especifica
    def registrar_nota(self, materia, nota):
        # Agregamos la nota en el diccionario usando el nombre de la materia como clave
        self.materias[materia] = nota
        # Imprimimos un mensaje confirmando el registro en consola
        print(f"Nota registrada: {nota} en la materia '{materia}'.")

    # Definimos el metodo para calcular el promedio general de las notas
    def calcular_promedio(self):
        # Comprobamos si el diccionario tiene elementos para evitar un error de division por cero
        if len(self.materias) == 0:
            # Si no hay materias registradas, el promedio es cero
            return 0
        # Sumamos todas las notas guardadas en los valores del diccionario
        suma_notas = sum(self.materias.values())
        # Calculamos el promedio dividiendo la suma por la cantidad total de materias
        promedio = suma_notas / len(self.materias)
        # Devolvemos el promedio calculado
        return promedio

    # Definimos el metodo para verificar si el estudiante aprobo
    def esta_aprobado(self):
        # Obtenemos el promedio actual llamando al metodo interno
        promedio = self.calcular_promedio()
        # Consideramos como aprobado si el promedio es mayor o igual a 60 (escala comun del 1 al 100)
        if promedio >= 60:
            # Retornamos un booleano True si cumple la condicion
            return True
        # Si el promedio es menor a 60, entra en esta condicion
        else:
            # Retornamos False indicando que reprobo
            return False

    # Definimos el metodo str para mostrar el boletin completo
    def __str__(self):
        # Creamos una variable de texto con el encabezado del boletin
        boletin = f"\n--- Boletin de {self.nombre} ---\n"
        
        # Iniciamos un bucle para recorrer las materias y notas almacenadas
        for materia, nota in self.materias.items():
            # Concatenamos cada materia y su respectiva nota al texto
            boletin += f"- {materia}: {nota}\n"
        
        # Obtenemos el promedio calculandolo nuevamente
        promedio = self.calcular_promedio()
        # Agregamos una linea de separacion y el promedio al boletin, formateado a dos decimales
        boletin += f"-------------------------\nPromedio general: {promedio:.2f}\n"
        
        # Evaluamos el estado usando el metodo esta_aprobado para definir el texto a mostrar
        condicion = "Aprobado" if self.esta_aprobado() else "Reprobado"
        # Concatenamos el resultado final al boletin
        boletin += f"Condicion Final: {condicion}\n"
        
        # Devolvemos el texto armado en su totalidad
        return boletin

# Creamos un objeto de la clase Estudiante
alumno = Estudiante("Joaquin Peralta")

# Simulamos la carga de notas en el sistema
print("--- Registrando Notas ---")
# Cargamos la primera nota del estudiante
alumno.registrar_nota("Programacion Orientada a Objetos", 85)
# Cargamos la segunda nota del estudiante
alumno.registrar_nota("Base de Datos", 92)
# Cargamos la tercera nota del estudiante
alumno.registrar_nota("Redes de Computadoras", 55)

# Imprimimos el objeto, lo que mostrara el boletin completo formateado por el metodo str
print(alumno)