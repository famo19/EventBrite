from eventbrite_logic import Logic
from entrada_obj import EntradaObj
from prettytable import PrettyTable


class EntradaLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "entradas"

    def createEntradaObj(self, entradaDict):  # Crea un entrada object
        entradaObj = EntradaObj(
            entradaDict["id"],
            entradaDict["pedidos.id"],
            entradaDict["nombre"],
            entradaDict["valorEntrada"],
            entradaDict["numEntrada"],
        )
        return entradaObj

    def registrarAllEntradas(
        self, idPedido, idEvento, cantEntradas, disponibilidad
    ):  # registra todas la entradas compradas por un usuario
        database = self.database
        # Obtener la capacidad del evento
        sql = f"SELECT `capacidad` FROM `eventbrite`.`eventos` WHERE id = {idEvento}"
        result = database.executeQueryOneRow(sql)
        capacidad = result["capacidad"]
        estado = "No canjeado"
        numEntrada = 0

        i = 1
        if capacidad == disponibilidad:
            while i <= cantEntradas:
                numEntrada = i
                sql = (
                    f"INSERT INTO `eventbrite`.`entradas`(`id`,`idEvento`, `idPedido`,`estado`,`numEntrada`)"
                    f"VALUES (0, '{idEvento}', '{idPedido}','{estado}','{numEntrada}');"
                )
                database.executeNonQueryRows(sql)
                i += 1
        else:
            while i <= cantEntradas:
                numEntrada = (capacidad - disponibilidad) + i
                sql = (
                    f"INSERT INTO `eventbrite`.`entradas`(`id`,`idEvento`, `idPedido`,`estado`,`numEntrada`)"
                    f"VALUES (0, '{idEvento}', '{idPedido}','{estado}','{numEntrada}');"
                )
                database.executeNonQueryRows(sql)
                i += 1
        self.actualizarDisponibilidad(idEvento, cantEntradas, disponibilidad)

    def actualizarDisponibilidad(
        self, idEvento, cantEntradas, oldDisponibilidad
    ):  # actualiza la disponibilidad del evento después de comprar entradas
        database = self.database
        newDisponibilidad = oldDisponibilidad - cantEntradas
        sql = f"UPDATE `eventbrite`.`eventos` SET `disponibilidad` = {newDisponibilidad} where id = {idEvento};"
        database.executeNonQueryBool(sql)

    def mostrarEntradasUsuario(
        self, idUser
    ):  # muestra todas las entradas adquiridas por un usuario
        database = self.database
        sql = (
            f"SELECT entradas.id, pedidos.id, nombre, valorEntrada, numEntrada "
            + f"FROM eventbrite.entradas INNER JOIN eventbrite.eventos on entradas.idEvento = eventos.id INNER JOIN eventbrite.pedidos ON entradas.idPedido = pedidos.id "
            + f"WHERE id_usuario = {idUser};"
        )
        output = database.executeQueryRows(sql)
        print("\nEstas son tus entradas adquiridas:\n")
        listaEntradas = []
        for entrada in output:
            newEntrada = self.createEntradaObj(entrada)
            listaEntradas.append(newEntrada)
        table = PrettyTable()
        table.field_names = [
            "idEntrada",
            "idPedido",
            "Nombre evento",
            "Valor entrada ($)",
            "Número de entrada",
        ]
        for pedido in listaEntradas:
            table.add_row(
                [
                    pedido.id,
                    pedido.idPedido,
                    pedido.nombre,
                    pedido.valorEntrada,
                    pedido.numEntrada,
                ]
            )
        print(table)
        table.clear()
        print(
            "\n-------------------------------------------------------------------------------------------------------------------------------------------\n"
        )
