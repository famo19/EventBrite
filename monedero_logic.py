from eventbrite_logic import Logic
from monedero_obj import MonederoObj
from card_logic import CardLogic
from prettytable import PrettyTable

tarjeta = CardLogic()


class MonederoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "monedero"

    def createMonederoObj(self, monederoDict):  # crear un monedero object
        monederoObj = MonederoObj(
            monederoDict["id"],
            monederoDict["nombre"],
            monederoDict["monto"],
            monederoDict["descontado"],
        )
        return monederoObj

    def cargarDineroCreador(
        self, idEvento, total
    ):  # añadir el dinero de una compra a su respectivo monedero
        database = self.database
        # obetener el id del creador del evento
        idCreador = self.getIDCreador(idEvento)
        idMonedero = self.getIDMonedero(idEvento)
        descontado = self.getDescontado(total)
        monto = total - descontado
        sql = f"UPDATE `eventbrite`.`monedero` SET `monto` = {monto} WHERE id = {idMonedero}"
        database.executeNonQueryBool(sql)
        sql = f"UPDATE `eventbrite`.`monedero` SET `descontado` = {descontado} WHERE id = {idMonedero}"
        database.executeNonQueryBool(sql)

    def getDescontado(
        self, totalPagado
    ):  # obtener el monto a descontar por el uso de este servicio
        descontado = totalPagado * 0.1
        return descontado

    def getIDCreador(self, idEvento):  # obtener el id del creador seún un evento
        database = self.database
        sql = f"SELECT `idUsuario` FROM `eventbrite`.`eventos` where id = {idEvento};"
        idCreador = database.executeQueryOneRow(sql)
        return idCreador["idUsuario"]

    def getIDMonedero(
        self, idEvento
    ):  # obtener el id de un monedero según el ID del evento
        database = self.database
        sql = f"SELECT `id` FROM `eventbrite`.`monedero` where idEvent = {idEvento};"
        idMonedero = database.executeQueryOneRow(sql)
        return idMonedero["id"]

    def createMonedero(self, idUser):  # crear un monedero para un evento
        database = self.database
        sql = "SELECT `id` FROM `eventbrite`.`eventos` ORDER BY `id` DESC limit 1;"
        output = database.executeQueryOneRow(sql)
        idEvento = output["id"]
        sql = (
            f"INSERT INTO eventbrite.monedero (id, idEvent, idUser, monto, descontado)"
            + f"VALUES (0, {idEvento}, {idUser}, 0.00, 0.00)"
        )
        database.executeNonQueryBool(sql)

    def mostrarMonederoUser(
        self, idUser
    ):  # mostrar los monederos de un usuario y retirar o conservar el dinero en los mismos
        database = self.database
        # Contar registros
        sql = f"SELECT count(*) FROM eventbrite.monedero where idUser = {idUser};"
        output = database.executeQueryRows(sql)
        if len(output) <= 0:
            print(
                "\n¡Oops! No tienes eventos creados.\nCrea un evento para poder ganar dinero con las entradas vendidas.\n\n"
            )
        else:
            # Mostrar tabla
            sql = (
                f"SELECT monedero.id, idUser, nombre, monto, descontado "
                + f"FROM eventbrite.monedero INNER JOIN eventbrite.eventos ON monedero.idEvent = eventos.id "
                + f"WHERE idUser = {idUser}"
            )
            output = database.executeQueryRows(sql)
            print("\nEstos son tus monederos:\n")
            listaMonedero = []

            for monedero in output:
                newMonedero = self.createMonederoObj(monedero)
                listaMonedero.append(newMonedero)

            table = PrettyTable()
            table.field_names = [
                "idMonedero",
                "Nombre del evento",
                "Monto ganado ($)",
                "Monto descontado ($)",
            ]
            for monedero in listaMonedero:
                table.add_row(
                    [
                        monedero.id,
                        monedero.nombre,
                        monedero.monto,
                        monedero.descontado,
                    ]
                )
            print(table)
            table.clear()

            # Quieres retirar el dinero? Y/N
            respuesta = int(
                input(
                    "\n¿Quieres retirar todo el dinero de algún monedero?\n(1) Sí\n(2) No\n\nTu opción: "
                )
            )
            while respuesta != 1 and respuesta != 2:
                respuesta = int(
                    input("\n¡Oops! Opción incorrecta, intenta de nuevo.\nTu opción: ")
                )
            if respuesta == 1:
                listaIDMonedero = []
                sql = f"SELECT id FROM eventbrite.monedero WHERE idUser = {idUser}"
                output = database.executeQueryRows(sql)
                for element in output:
                    listaIDMonedero.append(element["id"])
                # Selecciona el id del monedero
                idMon = int(
                    input("\nIngresa el 'id' del monedero para retirar su dinero: ")
                )
                while True:
                    if idMon not in listaIDMonedero:
                        idMon = int(
                            input(
                                "\n¡Oops! 'id' inválido\nPor favor intenta de nuevo: "
                            )
                        )
                    else:
                        break
                # Mostrar tarjetas
                print("\nEstas son tus tarjetas:")
                self.mostrarTarjetas(idUser)
                # Selecciona el id de la tarjeta (Validate)
                idTarjetaCompra = int(
                    input(
                        "\nSelecciona el 'id' de la tarjeta cuya cuenta bancaria recibirá el dinero\nID: "
                    )
                )
                listaTarjetas = tarjeta.checkIDCards(idUser)
                while True:
                    if idTarjetaCompra in listaTarjetas:
                        break
                    else:
                        idTarjetaCompra = int(
                            input(
                                "\n¡Oops! El 'id' no es válido, por favor ingrésalo de nuevo\nID: "
                            )
                        )
                # Set monto y descontado a cero
                self.clearMonedero(
                    idMon
                )  # Por aquí iría un código para realizar transacciones bancarias
                print(
                    "\nSolicitando N° de cuenta bancaria...\n\nRealizando transacción..\n\n¡Completado! Ya puedes revisar tu dinero en tu cuenta bancaria.\n\n¡Gracias por usar nuestros servicios!"
                )
            else:
                pass

    def mostrarTarjetas(self, idUsuario):  # Muestra las tarjetas de un usuario
        cardList = tarjeta.getAllCards(idUsuario)

        table = PrettyTable()
        table.field_names = [
            "id",
            "iduser",
            "Num. Tarjeta",
            "Codigo",
            "Fecha de Vencimiento",
        ]

        for card in cardList:
            table.add_row(
                [card.id, card.idUser, card.cardNum, card.secNum, card.endDate]
            )
        print(table)
        table.clear()
        return table

    def clearMonedero(self, idMonedero):  # Elimina el dinero de un monedero
        database = self.database
        sql = f"UPDATE eventbrite.monedero SET monto = 0.00 WHERE id = {idMonedero}"
        database.executeNonQueryBool(sql)
        sql = (
            f"UPDATE eventbrite.monedero SET descontado = 0.00 WHERE id = {idMonedero}"
        )
        database.executeNonQueryBool(sql)