from event_logic import EventLogic
from categoriaEventos_logic import CategoriaEventLogic
from eventos_views import EventosView
from busqueda_main import busquedaView
from pedido_logic import PedidoLogic
from entrada_logic import EntradaLogic
from monedero_logic import MonederoLogic
from prettytable import PrettyTable
import datetime

viewEObj = EventosView()
viewBusqueda = busquedaView()
pedido = PedidoLogic()
entrada = EntradaLogic()
monedero = MonederoLogic()


def menuEventos(idUser):

    while True:
        print(
            "\n--------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print("\n\n¡Bienvenido al menú de eventos! ¿Qué deseas hacer?\n")
        opcion = int(
            input(
                "(0) Salir\n(1) Crear un nuevo evento\n(2) Actualizar un evento\n(3) Eliminar un evento\n(4) Ver tus eventos creados\n(5) Buscar eventos\n(6) Ver historial de pedidos\n(7) Ver historial de entradas\n(8) Tu monedero\n\nTu opción: "
            )
        )
        print(
            "------------------------------------------------------------------------------------------------------------------"
        )
        while True:  # Bloqueamos opciones no disponibles
            if opcion < 0 or opcion > 8:
                opcion = int(
                    input("\n¡Oops! Opción incorrecta\n Por favor intenta de nuevo: ")
                )
            else:
                break
        if opcion == 0:  # Salir del menú de eventos
            break
        elif opcion == 1:  # Creamos un evento
            viewEObj.CrearEvento(idUser)

        elif opcion == 2:  # Actualizamos un evento
            viewEObj.UpdateEvent(idUser)

        elif opcion == 3:  # Eliminamos un evento
            viewEObj.DeleteEvent(idUser)

        elif opcion == 4:  # Mostramos los eventos creados por el usuario
            viewEObj.SeeUserEvents(idUser)

        elif opcion == 5:  # Vamos al menú de búsqueda de eventos
            viewBusqueda.buscar(idUser)

        elif opcion == 6:
            # Mostramos el historial de pedidos
            pedido.mostrarPedidosUsuario(idUser)

        elif opcion == 7:
            # Mostramos el historial de entradas
            entrada.mostrarEntradasUsuario(idUser)

        elif opcion == 8:  # Mostramos los monederos de usuario
            monedero.mostrarMonederoUser(idUser)