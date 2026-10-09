# Definimos la clase Turno para representar la reserva de un paciente
class Turno:
    # Inicializamos los atributos del turno en el constructor
    def __init__(self, paciente, hora):

        self.paciente = paciente
        self.hora = hora
        self.estado = "Pendiente"

    # Definimos el metodo para marcar el turno como atendido
    def marcar_atendido(self):
        # Cambiamos el valor del atributo estado
        self.estado = "Atendido"
        # Imprimimos un mensaje de confirmacion en consola
        print(f"El turno de {self.paciente} a las {self.hora} fue marcado como Atendido.")

    # Definimos el metodo str para mostrar la informacion del turno
    def __str__(self):
        # Devolvemos una cadena formateada con los datos del turno y su estado
        return f"Paciente: {self.paciente} | Hora: {self.hora} | Estado: {self.estado}"

# Definimos la clase Agenda para administrar los turnos de la jornada
class Agenda:
    # Inicializamos la agenda creando una coleccion vacia
    def __init__(self):
        # Creamos una lista para almacenar los objetos Turno
        self.turnos = []
    # Definimos el metodo para agendar nuevos turnos
    def agregar_turno(self, turno):
        # Insertamos el objeto turno en nuestra lista interna
        self.turnos.append(turno)
        # Mostramos un mensaje de exito confirmando la operacion
        print(f"Turno agendado para {turno.paciente} a las {turno.hora}.")
    # Definimos el metodo para listar unicamente los turnos que siguen pendientes
    def listar_pendientes(self):
        # Imprimimos un encabezado para la lista filtrada
        print("\n--- Turnos Pendientes ---")
        # Iniciamos un bucle para recorrer la coleccion de turnos
        for turno in self.turnos:
            # Comprobamos si el estado actual del turno es Pendiente
            if turno.estado == "Pendiente":
                # Imprimimos el turno porque cumple la condicion
                print(turno)
        # Imprimimos un salto de linea para separar bloques visualmente
        print("")

    # Definimos el metodo str para mostrar el total de turnos agendados en el dia
    def __str__(self):
        # Inicializamos una variable de texto con el titulo
        texto_salida = "--- Agenda Completa del Dia ---\n"
        # Recorremos todos los turnos sin importar su estado
        for turno in self.turnos:
            # Agregamos la representacion de cada turno al texto
            texto_salida += f"- {turno}\n"
        # Devolvemos el registro completo
        return texto_salida


# Creamos tres objetos Turno para distintos pacientes
turno_1 = Turno("Angel Gabriel", "08:00")
turno_2 = Turno("Angel Jose", "08:30")
turno_3 = Turno("Lucia Catalina", "09:00")

# Creamos el objeto Agenda vacio
mi_agenda = Agenda()

# Simulamos la jornada agregando los turnos a la agenda
print("--- Agendando Turnos ---")

mi_agenda.agregar_turno(turno_1)
mi_agenda.agregar_turno(turno_2)
mi_agenda.agregar_turno(turno_3)

# Mostramos los turnos pendientes antes de empezar a atender a la gente
mi_agenda.listar_pendientes()

# Atendemos a los primeros dos pacientes marcando sus estados
print("--- Atendiendo Pacientes ---")
# Marcamos como atendido el turno 1
turno_1.marcar_atendido()
# Marcamos como atendido el turno 2
turno_2.marcar_atendido()

# Mostramos nuevamente los pendientes para comprobar que solo queda uno
mi_agenda.listar_pendientes()

# la agenda completa para validar los cambios de estado finales
print(mi_agenda)