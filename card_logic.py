from eventbrite_logic import Logic
from card_obj import CardObj


class CardLogic(Logic):
    def __init__(self):
        super().__init__()

    def createCardObj(self, id, idUser, cardNum, secNum, endNum):  # crear card object
        userObj = CardObj(id, idUser, cardNum, secNum, endNum)
        return userObj

    def createCardObj(self, userDict):  # crear card object
        userObj = CardObj(
            userDict["id"],
            userDict["numeroTarjeta"],
            userDict["codigoSeguridad"],
            userDict["vencimiento"],
            userDict["idOwner"],
        )
        return userObj

    def insertCard(self, cardNum, secNum, endDate, email):  # Registrar tarjeta
        database = self.database
        # obtenemos el id del dueño
        sql = f"SELECT `id` FROM `eventbrite`.`usuarios` WHERE `correo` = '{email}'"
        output = database.executeQueryOneRow(sql)
        idOwner = output["id"]
        # insertamos la tarjeta
        sql = (
            f"INSERT INTO `eventbrite`.`tarjetadecredito` (`id`, `numeroTarjeta`, `codigoSeguridad`, `vencimiento`, `idOwner`) "
            + f"VALUES(0, '{cardNum}', '{secNum}', '{endDate}', '{idOwner}');"
        )
        database.executeNonQueryRows(sql)

    def deleteCard(self, idCard, idUser):  # Eliminar tarjeta
        database = self.database
        sql = (
            f"DELETE FROM `eventbrite`.`tarjetadecredito` "
            + f"WHERE id={idCard} and idOwner={idUser};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllCards(self, idUser):  # Obtener todas las tarjetas del usuario
        database = self.database
        sql = f"SELECT * FROM eventbrite.tarjetadecredito where idOwner={idUser};"
        rows = database.executeQueryRows(sql)
        cardList = []
        for element in rows:
            newEvent = self.createCardObj(element)
            cardList.append(newEvent)
        return cardList

    def getIDCards(self, idUser):  # Obtener todos los ID de las tarjetas del usuario
        database = self.database
        sql = f"SELECT `id` FROM eventbrite.tarjetadecredito WHERE idOwner = {idUser};"
        output = database.executeQueryRows(sql)
        idList = []
        for element in output:
            idList.append(element["id"])
        return idList

    def checkIDCards(
        self, idUser
    ):  # Revisar si existen tarjetas registradas para un usuario
        database = self.database
        idList = []
        sql = f"SELECT `id` FROM eventbrite.tarjetadecredito WHERE idOwner = {idUser};"
        output = database.executeQueryRows(sql)
        if output is None:
            return idList
        else:
            for element in output:
                idList.append(element["id"])
            return idList