from prettytable import PrettyTable
from event_logic import EventLogic
from categoriaEventos_logic import CategoriaEventLogic
from tipoEventos_logic import TipoEventLogic
import datetime

class EventosView:
    def CrearEvento(self, idUser):
        print("Puede comenzar a ingresar datos:\n")
        nombre = input("Nombre: ")
        print("Lista de categorías disponibles para eventos: ")
        catEventObj = CategoriaEventLogic()
        for element in catEventObj.getCat():
            print(str(element["idCategorias-eventos"])+"-"+element["nombreCat"])
        categoria = (input("Seleccione la categoria a la que pertenece su evento según el número correspondiente: "))
        fecha1 = input("fecha (YYYY-MM-DD): ")
        fecha = datetime.datetime.strptime(fecha1, "%Y-%m-%d")
        hora1 = input("Hora (HH:MM): ")
        hora = datetime.datetime.strptime(hora1, "%H:%M")
        descripcion = input("Descripcion: ")
        valorEntrada = float(input("Valor entrada: "))
        capacidad = int(input("Capacidad: "))
        disponibilidad = int(input("Disponibilidad: "))
        ciudad = input("Ciudad: ")
        pais = input("Pais: ")
        direccion = input("Direccion: ")
        print("Lista de tipos de evento disponibles: ")
        tipoEventObj = TipoEventLogic()
        for element in tipoEventObj.getTipo():
            print(str(element["idtipo-eventos"])+"-"+element["nombreTipo"])
        tipo = (input("Seleccione el tipo de evento según el número correspondiente: "))

        logic = EventLogic()
        rows = logic.insertEvent(idUser, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo)
        
    def UpdateEvent(self):
        eventosLogic = EventLogic()
        idEventos = int(input("idEventos: "))
        oldEvent = eventosLogic.getEventById(idEventos)

        print(f"old nombre: {oldEvent['nombre']}")
        nombre = input("Nuevo nombre: ")

        print(f"old categoria: {oldEvent['categoria']}")
        print("Lista de categorías disponibles para eventos: ")
        catEventObj = CategoriaEventLogic()
        for element in catEventObj.getCat():
            print(str(element["idCategorias-eventos"])+"-"+element["nombreCat"])
        categoria = (int(input("Seleccione la nueva categoria a la que pertenece su evento según el número correspondiente: ")))

        print(f"old fecha: {oldEvent['fecha']}")
        fecha1 = input("Nueva fecha (YYYY-MM-DD): ")
        fecha = datetime.datetime.strptime(fecha1, "%Y-%m-%d")

        print(f"old hora: {oldEvent['hora']}")
        hora1 = input("Nueva hora (HH:MM): ")
        hora = datetime.datetime.strptime(hora1, "%H:%M")

        print(f"old descripcion: {oldEvent['descripcion']}")
        descripcion = input("Nueva descripcion: ")

        print(f"old valorEntrada: {oldEvent['valorEntrada']}")
        valorEntrada = float(input("Nuevo valor de entrada: "))

        print(f"old capacidad: {oldEvent['capacidad']}")
        capacidad = int(input("Nueva capacidad: "))

        print(f"old disponibilidad: {oldEvent['disponibilidad']}")
        disponibilidad = int(input("Nueva disponibilidad: "))

        print(f"old ciudad: {oldEvent['ciudad']}")
        ciudad = input("Nueva ciudad: ")

        print(f"old pais: {oldEvent['pais']}")
        pais = input("Nuevo pais: ")

        print(f"old direccion: {oldEvent['direccion']}")
        direccion = input("Nueva direccion: ")

        print(f"old tipo: {oldEvent['tipo']}")
        print("Lista de tipos de evento disponibles: ")
        tipoEventObj = TipoEventLogic()
        for element in tipoEventObj.getTipo():
            print(str(element["idtipo-eventos"])+"-"+element["nombreTipo"])
        tipo = (int(input("Seleccione el nuevo tipo de evento según el número correspondiente: ")))

        rows = eventosLogic.updateEvent(idEventos, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo)

    def DeleteEvent(self):
        logic = EventLogic()
        idEventos = int(input("idEventos: "))
        rows = logic.deleteEvent(idEventos)

    def SeeAllEvents(self):
        eventListObj = EventLogic()
        events = eventListObj.getAllEvents()

        table = PrettyTable()
        table.field_names = ["idEventos", "idUsuarios", "nombre", "categoria", "fecha", "hora", "descripcion", "valorEntrada", "capacidad", "disponibilidad", "ciudad", "pais", "direccion", "tipo"]

        for event in events:
            table.add_row(
                [event.idEventos, event.idUsuarios, event.nombre, event.categoria, event.fecha, event.hora, event.descripcion, event.valorEntrada, event.capacidad, event.disponibilidad, event.ciudad, event.pais, event.direccion, event.tipo]
            )
        print(table)        

    def SeeOneEvent(self):
        events = EventLogic()
        idEventos = int(input("idEventos: "))
        event = events.getEventById(idEventos)

        table = PrettyTable()
        table.field_names = ["idEventos", "idUsuarios", "nombre", "categoria", "fecha", "hora", "descripcion", "valorEntrada", "capacidad", "disponibilidad", "ciudad", "pais", "direccion", "tipo"]
        table.add_row(
            [event["idEventos"], event["idUsuarios"], event["nombre"], event["categoria"], event["fecha"], event["hora"], event["descripcion"], event["valorEntrada"], event["capacidad"], event["disponibilidad"], event["ciudad"], event["pais"], event["direccion"], event["tipo"]]
        )
        print(table)