from prettytable import PrettyTable
from event_logic import EventLogic
from categoriaEventos_logic import CategoriaEventLogic
from monedero_logic import MonederoLogic
import datetime

monedero = MonederoLogic()


class EventosView:
    def CrearEvento(self, idUser):  # Crear un evento
        print(
            "\nAcontinuación, vamos a crea un evento.\n\nPor favor ingresa los datos solicitados\n"
        )
        nombre = input("Nombre:\n")
        print(
            "\nAhora definiremos la categoría\nLista de categorías disponibles para eventos:\n"
        )
        catEventObj = CategoriaEventLogic()
        for element in catEventObj.getCat():
            print("(" + str(element["id"]) + ") " + element["nombre_categoria"])
        listaCat = []
        for element in catEventObj.getCat():
            listaCat.append(element["id"])

        idCategoria = int(
            input(
                "\nIngresa el número 'id' correspondiente a la categoría de tu evento:\n"
            )
        )
        while True:
            if idCategoria in listaCat:
                break
            else:
                idCategoria = int(
                    input(
                        "\n¡Oops!\n La categoría seleccionada no se encuentra en la lista.\nIngresa el número nuevamente.\n"
                    )
                )

        fecha1 = input("\nFecha del evento (YYYY-MM-DD):\n")
        fecha = datetime.datetime.strptime(fecha1, "%Y-%m-%d")
        hora1 = input("\nHora del evento (HH:MM):\n")
        hora = datetime.datetime.strptime(hora1, "%H:%M")
        descripcion = input("\nDescripcion del evento:\n")
        valorEntrada = float(input("\nValor de la entrada:\n$"))
        capacidad = int(input("\nCapacidad máxima del evento:\n"))
        disponibilidad = capacidad
        ciudad = input("\nCiudad donde se llevará a cabo:\n")
        pais = input("\nPais donde se llevará a cabo:\n")
        direccion = input("\nDireccion especifica del evento:\n")

        logic = EventLogic()
        rows = logic.insertEvent(
            idUser,
            nombre,
            idCategoria,
            fecha,
            hora,
            descripcion,
            valorEntrada,
            capacidad,
            disponibilidad,
            ciudad,
            pais,
            direccion,
        )
        monedero.createMonedero(idUser)
        print("\n¡Evento creado con éxito!\n")
        print(
            "\n-------------------------------------------------------------------------------------------------------"
        )

    def UpdateEvent(self, idUser):  # actualizar un evento
        eventosLogic = EventLogic()
        print("\nEstos son tus eventos:")
        self.SeeUserEvents(idUser)
        listaEventos = eventosLogic.getUserEventsList(idUser)

        idEvento = int(input("\nIngresa el 'id' del evento a actualizar:\n"))
        while True:
            if idEvento in listaEventos:
                break
            else:
                idEvento = int(
                    input(
                        "\n¡Oops! El 'id' ingresado no existe.\nPor favor ingresalo de nuevo:\n"
                    )
                )
        oldEvent = eventosLogic.getEventById(idEvento)

        print(f"\nNombre anterior: {oldEvent['nombre']}")
        nombre = input("Nombre nuevo:\n")

        print(f"\nCategoría antigua: {oldEvent['idCategoria']}")
        print("\nLista de categorías disponibles para eventos:\n")
        catEventObj = CategoriaEventLogic()
        for element in catEventObj.getCat():
            print("(" + str(element["id"]) + ")" + " " + element["nombre_categoria"])
        idCategoria = int(
            input("\nIngrese el número de la nueva categoria de su evento:\n")
        )
        listaCat = []
        for element in catEventObj.getCat():
            listaCat.append(element["id"])
        while True:
            if idCategoria in listaCat:
                break
            else:
                idCategoria = int(
                    input(
                        "\n¡Oops!\n La categoría seleccionada no se encuentra en la lista.\nIngresa el número nuevamente.\n"
                    )
                )

        print(f"\nFecha anterior: {oldEvent['fecha']}")
        fecha1 = input("\nNueva fecha (YYYY-MM-DD):\n")
        fecha = datetime.datetime.strptime(fecha1, "%Y-%m-%d")

        print(f"\nHora anterior: {oldEvent['hora']}")
        hora1 = input("\nNueva hora (HH:MM):\n")
        hora = datetime.datetime.strptime(hora1, "%H:%M")

        print(f"\nDescripcion anterior: {oldEvent['descripcion']}")
        descripcion = input("\nNueva descripcion:\n")

        print(f"\nValorEntrada anterior: {oldEvent['valorEntrada']}")
        valorEntrada = float(input("\nNuevo valor de entrada:\n"))

        print(f"\nCapacidad anterior: {oldEvent['capacidad']}")
        capacidad = int(input("\nNueva capacidad:\n"))

        disponibilidad = capacidad

        print(f"\nCiudad anterior: {oldEvent['ciudad']}")
        ciudad = input("\nNueva ciudad:\n")

        print(f"\nPaís anterior: {oldEvent['pais']}")
        pais = input("\nNuevo país:\n")

        print(f"\nDirección anterior: {oldEvent['direccion']}")
        direccion = input("\nNueva dirección:\n")

        rows = eventosLogic.updateEvent(
            idEvento,
            nombre,
            idCategoria,
            fecha,
            hora,
            descripcion,
            valorEntrada,
            capacidad,
            disponibilidad,
            ciudad,
            pais,
            direccion,
        )
        print("\n¡Actualización completada!")

    print(
        "\n---------------------------------------------------------------------------------------------------------------------------------\n"
    )

    def DeleteEvent(self, idUser):  # Eliminar un evento
        logic = EventLogic()
        print("\nEstos son tus eventos:")
        self.SeeUserEvents(idUser)
        listaEventos = logic.getUserEventsList(idUser)

        idEvento = int(input("\nIngresa el 'id' del evento a eliminar:\n"))
        while True:
            if idEvento in listaEventos:
                break
            else:
                idEvento = int(
                    input(
                        "\n¡Oops! El 'id' ingresado no existe.\nPor favor ingresalo de nuevo:\n"
                    )
                )
        logic.deleteMonedero(idEvento)
        logic.deleteEvent(idEvento)

    def SeeUserEvents(self, idUser):  # Mostrar los eventos creados por un usuario
        eventListObj = EventLogic()
        events = eventListObj.getUserEvents(idUser)

        table = PrettyTable()
        table.field_names = [
            "idEvento",
            "idCreador",
            "nombre",
            "categoria",
            "fecha",
            "hora",
            "descripcion",
            "valorEntrada",
            "capacidad",
            "disponibilidad",
            "ciudad",
            "pais",
            "direccion",
        ]

        for event in events:
            table.add_row(
                [
                    event.id,
                    event.idUsuario,
                    event.nombre,
                    event.idCategoria,
                    event.fecha,
                    event.hora,
                    event.descripcion,
                    event.valorEntrada,
                    event.capacidad,
                    event.disponibilidad,
                    event.ciudad,
                    event.pais,
                    event.direccion,
                ]
            )
        print(table)

    def SeeOneEvent(self):  # Ver un solo evento
        events = EventLogic()
        idEvento = int(input("idEvento: "))
        event = events.getEventById(idEvento)

        table = PrettyTable()
        table.field_names = [
            "idEvento",
            "idCreador",
            "nombre",
            "categoria",
            "fecha",
            "hora",
            "descripcion",
            "valorEntrada",
            "capacidad",
            "disponibilidad",
            "ciudad",
            "pais",
            "direccion",
            "tipo",
        ]
        table.add_row(
            [
                event["id"],
                event["idUsuario"],
                event["nombre"],
                event["idCategoria"],
                event["fecha"],
                event["hora"],
                event["descripcion"],
                event["valorEntrada"],
                event["capacidad"],
                event["disponibilidad"],
                event["ciudad"],
                event["pais"],
                event["direccion"],
            ]
        )
        print(table)