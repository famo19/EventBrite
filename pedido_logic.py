from eventbrite_logic import Logic
from pedido_obj import PedidoObj
from prettytable import PrettyTable


class PedidoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "pedidos"

    def createPedidoObj(self, pedidoDict):
        pedidoObj = PedidoObj(
            pedidoDict["id"],
            pedidoDict["nombre"],
            pedidoDict["numeroTarjeta"],
            pedidoDict["cantidadEntradas"],
            pedidoDict["total"],
        )
        return pedidoObj

    # Método que registra el pedido en la tabla pedidos y regresa el id del mismo
    def addPedido(self, idEvento, idUsuario, idTarjeta, cantEntradas, total):
        database = self.database
        sql = (
            f"INSERT INTO `eventbrite`.`pedidos`(`id`,`id_evento`,`id_usuario`, `idBankTarjeta`,`cantidadEntradas`,`total`)"
            + f"VALUES(0,'{idEvento}','{idUsuario}', '{idTarjeta}','{cantEntradas}','{total}');"
        )
        database.executeNonQueryRows(sql)
        sql = (
            f"SELECT id from `eventbrite`.`pedidos` where id_evento = {idEvento} and id_usuario = {idUsuario} "
            + f"and idBankTarjeta = {idTarjeta} and cantidadEntradas = {cantEntradas} and total = {total} ORDER BY `id` DESC;"
        )
        idPedido = database.executeQueryOneRow(sql)
        return idPedido["id"]

    def deletePedido(self, idPedido):
        database = self.database
        super().deleteRowById(idPedido, self.tableName)

    # Método que calcula el monto total a pagar por el usuario dado un idEvento y unda cantidad de entradas
    def getTotal(self, idEvento, cantEntradas):
        database = self.database
        sql = (
            f"SELECT `valorEntrada` FROM `eventbrite`.`eventos` where id = {idEvento};"
        )
        costoEntrada = database.executeQueryOneRow(sql)
        return costoEntrada

    # Método que dado un idEvento devuelve los cupos disponibles
    def checkDisponibilidad(self, idEvento):
        database = self.database
        sql = f"SELECT `disponibilidad` FROM `eventbrite`.`eventos` where id = {idEvento};"
        cuposRestantes = database.executeQueryOneRow(sql)
        """
        if cuposRestantes["disponibilidad"] <= cantEntradas:
            disponibilidad = True
        else:
            disponibilidad = False
            """
        return cuposRestantes["disponibilidad"]

    def mostrarPedidosUsuario(
        self, idUser
    ):  # muestra el hitorial de de pedidos de un usuario
        database = self.database
        sql = (
            f"SELECT pedidos.id, nombre, numeroTarjeta, cantidadEntradas, total "
            + f"FROM eventbrite.pedidos inner join eventbrite.tarjetadecredito on pedidos.idBankTarjeta = tarjetadecredito.id INNER JOIN eventbrite.eventos on pedidos.id_evento = eventos.id "
            + f"WHERE id_usuario = {idUser};"
        )
        output = database.executeQueryRows(sql)
        print("\nEstos son tus pedidos:\n")
        listaPedidos = []
        for pedido in output:
            newPedido = self.createPedidoObj(pedido)
            listaPedidos.append(newPedido)

        table = PrettyTable()
        table.field_names = [
            "idPedido",
            "Nombre evento",
            "Num. Tarjeta",
            "Cantidad entradas",
            "Total ($)",
        ]
        for pedido in listaPedidos:
            table.add_row(
                [
                    pedido.id,
                    pedido.nombre,
                    pedido.numeroTarjeta,
                    pedido.cantidadEntradas,
                    pedido.total,
                ]
            )
        print(table)
        table.clear()
        print(
            "\n-------------------------------------------------------------------------------------------------------------------------------------------\n"
        )
