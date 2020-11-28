from event_logic import EventLogic
from categoriaEventos_logic import CategoriaEventLogic
from tipoEventos_logic import TipoEventLogic
from eventos_views import EventosView
from prettytable import PrettyTable
import datetime

viewEObj = EventosView()
def menuEventos(idUser):
    
    while True:
        print("Bienvenido al menu de eventos\n")
        opcion = int(input(" |Inserte '0' para salir |\n |'1' para ingresar un nuevo evento |\n |'2' para actualizar un evento|\n |'3' para remover un evento|\n |'4' para ver todos los eventos|\n |'5' para ver un evento por ID|\n"))
        print("------------------------------------------------------------------------------------------------------------------")
        if opcion == 0:
            break
        elif opcion == 1:
            viewEObj.CrearEvento(idUser)

        elif opcion == 2:
           viewEObj.UpdateEvent()

        elif opcion == 3:
            viewEObj.DeleteEvent

        elif opcion == 4:
            viewEObj.SeeAllEvents()

        elif opcion == 5:
            viewEObj.SeeOneEvent()

        
