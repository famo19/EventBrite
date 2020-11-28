from eventbrite_logic import Logic
from card_obj import CardObj


class CardLogic(Logic):
    def __init__(self):
        super().__init__()


    # polimorfismo
    def createCardObj(self, id, idUser, cardNum, secNum, endNum):
        userObj = CardObj(id, idUser, cardNum, secNum, endNum)
        return userObj

    def createCardObj(self, userDict):
        userObj = CardObj(
            userDict["idTarjetaDeCredito"],
            userDict["numeroTarjeta"],
            userDict["codigoSeguridad"],
            userDict["vencimiento"],
            userDict["idUsuarios"]
            
        )
        return userObj

    def insertCard(self, cardNum,secNum, endDate, idUser):
        database = self.database
        sql = (
            f"INSERT INTO `eventbrite`.`tarjetadecredito` (`idTarjetaDeCredito`, `numeroTarjeta`, `codigoSeguridad`, `vencimiento`, `idUsuarios`) "
            +f"VALUES(0, '{cardNum}', {secNum}, '{endDate}', {idUser});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCard(self, idCard, idUser):
        database = self.database
        sql = (
            f"DELETE FROM `eventbrite`.`tarjetadecredito` "
            + f"WHERE idTarjetaDeCredito={idCard} and idUsuarios={idUser};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllCards(self, idUser):
        database = self.database
        sql = (
            f"SELECT * FROM eventbrite.tarjetadecredito where idUsuarios={idUser};"
        )
        rows = database.executeQueryRows(sql)
        cardList = []
        for element in rows:
            newEvent = self.createCardObj(element)
            cardList.append(newEvent)
        return cardList


