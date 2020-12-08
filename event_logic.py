from eventbrite_logic import Logic
from event_obj import EventObj


class EventLogic(Logic):
    def __init__(self):
        super().__init__()

    def createEventObj(
        self,
        id,
        idUsuarios,
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
    ):  # Crea un evento object
        eventObj = EventObj(
            id,
            idUsuarios,
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
        return eventObj

    def createEventObj(self, eventDict):  # Crea un evento object
        eventObj = EventObj(
            eventDict["id"],
            eventDict["idUsuario"],
            eventDict["nombre"],
            eventDict["idCategoria"],
            eventDict["fecha"],
            eventDict["hora"],
            eventDict["descripcion"],
            eventDict["valorEntrada"],
            eventDict["capacidad"],
            eventDict["disponibilidad"],
            eventDict["ciudad"],
            eventDict["pais"],
            eventDict["direccion"],
        )
        return eventObj

    def insertEvent(
        self,
        idCreador,
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
    ):  # Registra un evento
        database = self.database
        sql = (
            f"INSERT INTO `eventbrite`.`eventos`(`id`,`idUsuario`,`nombre`,`idCategoria`,`fecha`,`hora`,`descripcion`,`valorEntrada`,`capacidad`,`disponibilidad`,`ciudad`,`pais`,`direccion`) "
            + f"VALUES(0,{idCreador},'{nombre}','{idCategoria}','{fecha}','{hora}','{descripcion}',{valorEntrada},{capacidad},{disponibilidad},'{ciudad}','{pais}','{direccion}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateEvent(
        self,
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
    ):  # Actualiza un evento
        database = self.database
        sql = (
            "UPDATE `eventbrite`.`eventos` "
            + f"SET `nombre` = '{nombre}',`idCategoria` = {idCategoria},`fecha` = '{fecha}',`hora` = '{hora}',`descripcion` = '{descripcion}',`valorEntrada` = {valorEntrada},`capacidad` = {capacidad},`disponibilidad` = {disponibilidad},`ciudad` = '{ciudad}',`pais` = '{pais}',`direccion` = '{direccion}'"
            + f"WHERE `id` = {idEvento};"
        )
        rows = database.executeNonQueryBool(sql)
        return rows

    def deleteEvent(self, idEvento):  # Elimina un evento
        database = self.database
        sql = f"DELETE FROM `eventbrite`.`eventos` WHERE id={idEvento};"
        rows = database.executeNonQueryBool(sql)
        return rows

    def getEventById(self, idEvento):  # Obtiene un evento por su ID
        database = self.database
        sql = f"SELECT * FROM eventbrite.eventos where id={idEvento};"
        rows = database.executeQueryOneRow(sql)
        return rows

    def getAllEvents(self):  # Obtiene todos los eventos existentes
        database = self.database
        data = database.executeQueryRows("SELECT * FROM eventbrite.eventos;")
        eventList = []
        for element in data:
            newEvent = self.createEventObj(element)
            eventList.append(newEvent)
        return eventList

    def getUserEvents(self, idUser):  # Obtiene los eventos creados por un usuario
        database = self.database
        sql = f"SELECT * FROM eventbrite.eventos WHERE idUsuario = {idUser}"
        eventos = database.executeQueryRows(sql)
        userEventList = []
        for element in eventos:
            newEvent = self.createEventObj(element)
            userEventList.append(newEvent)
        return userEventList

    def getUserEventsID(
        self, idUser
    ):  # Crea un lista con los id de los eventos creados por un usuario
        database = self.database
        sql = f"SELECT id FROM eventbrite.eventos WHERE idUsuario = {idUser}"
        eventos = database.executeQueryRows(sql)
        userEventList = []
        for element in eventos:
            userEventList.append(element["id"])
        return userEventList

    def getUserEventsList(self, idUser):  # Obtiene los eventos creados por un usuario
        listaeventos = self.getUserEventsID(idUser)
        return listaeventos

    def deleteMonedero(self, idEvento):  # Elimina un monedero asociado a un evento
        database = self.database
        sql = f"DELETE FROM eventbrite.monedero WHERE idEvent = {idEvento}"
        database.executeNonQueryBool(sql)
