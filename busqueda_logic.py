from busqueda_obj import EventoObj, CategoriaObj
from eventbrite_logic import Logic


class EventoLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAllEventosFromSearch(
        self,
    ):  # Método para obtner todos los eventos existentes
        database = self.database
        data = database.executeQueryRows("SELECT * FROM `eventbrite`.`eventos`;")
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList

    def getEventosById(self, id):  # Método para obtener un event por su ID
        database = self.database
        sql = f"SELECT * FROM `eventbrite`.`eventos` where id = {id};"
        rows = database.executeQueryOneRow(sql)
        return rows

    def getEventosByCategoria(
        self, categoria
    ):  # Método para obtener un evento por su categoría
        database = self.database
        # obtenemos el id de la categoría
        eventoList = []
        sql = f"SELECT `id` FROM `eventbrite`.`categoria_eventos` WHERE `nombre_categoria` = '{categoria}'"
        output = database.executeQueryOneRow(sql)
        if output is None:
            return eventoList
        else:
            idCat = output["id"]

            # obtenemos la lista de eventos
            sql = f"SELECT * FROM `eventbrite`.`eventos` where `idCategoria` = {idCat}"
            data = database.executeQueryRows(sql)

            for element in data:
                newEvento = self.createEventoObj(element)
                eventoList.append(newEvento)
            return eventoList

    def getEventosByDate(self, date):  # Método para obtener eventos por su fecha
        database = self.database
        data = database.executeQueryRows(
            f"SELECT * FROM `eventbrite`.`eventos` where `fecha` = '{date}'"
        )
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList

    def getEventosByCity(self, city):  # Método para obtener eventos por su ciudad
        database = self.database
        data = database.executeQueryRows(
            f"SELECT * FROM `eventbrite`.`eventos` where `ciudad` = '{city}'"
        )
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList

    def getEventosByCountry(self, country):  # Método para obtener eventos por su país
        database = self.database
        data = database.executeQueryRows(
            f"SELECT * FROM `eventbrite`.`eventos` where `pais` = '{country}'"
        )
        eventoList = []
        for element in data:
            newEvento = self.createEventoObj(element)
            eventoList.append(newEvento)
        return eventoList

    def getCategoriasByEvent(self, id):  # Método para obtener el nombre de la categoría
        database = self.database
        # obtenemos el id de la categoria
        sql = f"SELECT `idCategoria` FROM `eventbrite`.`eventos` WHERE `id` = {id}"
        output = database.executeQueryOneRow(sql)
        idCategoria = output["idCategoria"]
        # obtenemos el nombre de la categoria
        sql = f"SELECT `nombre_categoria` FROM `eventbrite`.`categoria_eventos` WHERE `id` = {idCategoria}"
        categoriaName = database.executeQueryOneRow(sql)
        return categoriaName["nombre_categoria"]

    def getAllCategorias(self):  # Método para obtener todas las categorías
        database = self.database
        data = database.executeQueryRows(
            "SELECT * FROM `eventbrite`.`categoria_eventos`;"
        )
        categoriaList = []
        for element in data:
            newCat = self.createCategoriaObj(element)
            categoriaList.append(newCat)
        return categoriaList

    def getUserName(self, id):  # Método para obtener el userName del creador del evento
        database = self.database
        # obtenemos el id del creador
        sql = f"SELECT `idUsuario` FROM `eventbrite`.`eventos` WHERE `id` = {id}"
        output = database.executeQueryOneRow(sql)
        idCreador = output["idUsuario"]
        # obtenemos el username del creador
        sql = f"SELECT `userName` FROM `eventbrite`.`usuarios` WHERE `id` = {idCreador}"
        output = database.executeQueryOneRow(sql)
        userNameCreador = output["userName"]
        return userNameCreador

    def createEventoObj(
        self,
        id,
        idUsuario,
        nombre,
        fecha,
        hora,
        descripcion,
        valorEntrada,
        capacidad,
        disponibilidad,
        ciudad,
        pais,
        direccion,
        idCategoria,
    ):  # Método que crea el Evento Object
        eventoObj = EventoObj(
            id,
            idUsuario,
            nombre,
            fecha,
            hora,
            descripcion,
            valorEntrada,
            capacidad,
            disponibilidad,
            ciudad,
            pais,
            direccion,
            idCategoria,
        )
        return EventoObj

    def createEventoObj(self, eventoDict):  # Método que crea el Evento Object
        eventoObj = EventoObj(
            eventoDict["id"],
            eventoDict["idUsuario"],
            eventoDict["nombre"],
            eventoDict["fecha"],
            eventoDict["hora"],
            eventoDict["descripcion"],
            eventoDict["valorEntrada"],
            eventoDict["capacidad"],
            eventoDict["disponibilidad"],
            eventoDict["ciudad"],
            eventoDict["pais"],
            eventoDict["direccion"],
            eventoDict["idCategoria"],
        )
        return eventoObj

    def createCategoriaObj(
        self, idcategorias_eventos, nombreCat
    ):  # Método que crea el categoría object
        eventoObj = CategoriaObj(idcategorias_eventos, nombreCat)
        return CategoriaObj

    def createCategoriaObj(self, categoriaDict):  # Método que crea el categoría object
        categoriaObj = CategoriaObj(
            categoriaDict["id"], categoriaDict["nombre_categoria"]
        )
        return categoriaObj