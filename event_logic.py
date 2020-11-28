from eventbrite_logic import Logic
from event_obj import EventObj

class EventLogic(Logic):
    def __init__(self):
        super().__init__()

    def createEventObj(self, id, idUsuarios, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo):
        eventObj = EventObj(id, idUsuarios, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo)
        return eventObj

    def createEventObj(self, eventDict):
        eventObj = EventObj(
            eventDict["idEventos"],
            eventDict["idUsuarios"],
            eventDict["nombre"],
            eventDict["categoria"],
            eventDict["fecha"],
            eventDict["hora"],
            eventDict["descripcion"],
            eventDict["valorEntrada"],
            eventDict["capacidad"],
            eventDict["disponibilidad"],
            eventDict["ciudad"],
            eventDict["pais"],
            eventDict["direccion"],
            eventDict["tipo"]
        )
        return eventObj

    def insertEvent(self, idUsuarios, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo):
        database = self.database
        sql = (
            f"INSERT INTO `eventbrite`.`eventos`(`idEventos`,`idUsuarios`,`nombre`,`categoria`,`fecha`,`hora`,`descripcion`,`valorEntrada`,`capacidad`,`disponibilidad`,`ciudad`,`pais`,`direccion`,`tipo`) "
            + f"VALUES(0,{idUsuarios},'{nombre}','{categoria}','{fecha}','{hora}','{descripcion}',{valorEntrada},{capacidad},{disponibilidad},'{ciudad}','{pais}','{direccion}','{tipo}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateEvent(self, idEventos, nombre, categoria, fecha, hora, descripcion, valorEntrada, capacidad, disponibilidad, ciudad, pais, direccion, tipo):
        database = self.database
        sql = (
            "UPDATE `eventbrite`.`eventos` "
            + f"SET `nombre` = '{nombre}',`categoria` = {categoria},`fecha` = '{fecha}',`hora` = '{hora}',`descripcion` = '{descripcion}',`valorEntrada` = {valorEntrada},`capacidad` = {capacidad},`disponibilidad` = {disponibilidad},`ciudad` = '{ciudad}',`pais` = '{pais}',`direccion` = '{direccion}',`tipo` = {tipo} "
            + f"WHERE `idEventos` = {idEventos};"
        )
        rows = database.executeNonQueryBool(sql)
        return rows

    def deleteEvent(self, idEventos):
        database = self.database
        sql = f"DELETE FROM `eventbrite`.`eventos` WHERE idEventos={idEventos};"
        rows = database.executeNonQueryBool(sql)
        return rows

    def getEventById(self, idEventos):
        database = self.database
        sql = f"SELECT * FROM eventbrite.eventos where idEventos={idEventos};"
        rows = database.executeQueryOneRow(sql)
        return rows 

    def getAllEvents(self):
        database = self.database
        data = database.executeQueryRows("SELECT * FROM eventbrite.eventos;")
        eventList = []
        for element in data:
            newEvent = self.createEventObj(element)
            eventList.append(newEvent)
        return eventList


    