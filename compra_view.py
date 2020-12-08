from pedido_logic import PedidoLogic
from entrada_logic import EntradaLogic
from monedero_logic import MonederoLogic
from card_logic import CardLogic
from prettytable import PrettyTable

# Creamos los objetos de las clases
pedidoLogic = PedidoLogic()
entradaLogic = EntradaLogic()
monederoLogic = MonederoLogic()
tarjeta = CardLogic()


class viewCompra:
    def compra(self, idUsuario, idEvento):  # método para comprar entradas
        listaTarjetas = tarjeta.checkIDCards(idUsuario)
        if listaTarjetas == []:
            print(
                "\n¡Oh no! No puedes comprar si no tienes una tajeta bancaria registrada.\nTranquilo, regresa a registrarla.\n\n"
            )
            print(
                "\n------------------------------------------------------------------------------------------------------------------"
            )
        else:
            print("\nEstas son tus tarjetas:")
            self.mostrarTarjetas(idUsuario)
            idTarjetaCompra = int(
                input("\nSelecciona el 'id' de la tarjeta con la que comprarás.\nID: ")
            )
            while True:
                if idTarjetaCompra in listaTarjetas:
                    break
                else:
                    idTarjetaCompra = int(
                        input(
                            "\n¡Oops! El 'id' no es válido, por favor ingrésalo de nuevo\nID: "
                        )
                    )
            self.procederCompra(idUsuario, idEvento, idTarjetaCompra)

    def getTotalAPagar(
        self, idEvento, cantEntradas
    ):  # Método para obtener el total a pagar
        # obtenemos el total que va a pagar el cliente
        valorEntrada = pedidoLogic.getTotal(idEvento, cantEntradas)
        total = (valorEntrada["valorEntrada"]) * (cantEntradas)
        return total

    def procederCompra(
        self, idUsuario, idEvento, idTarjeta
    ):  # Método para terminar la compra
        cantEntradas = int(input("¿Cuántas entradas deseas comprar? :"))
        total = self.getTotalAPagar(idEvento, cantEntradas)
        # registramos el pedido y obtenemos el ID
        pedidoID = pedidoLogic.addPedido(
            idEvento, idUsuario, idTarjeta, cantEntradas, total
        )
        # revisamos si logramos obtener el ID del pedido
        if pedidoID > 0:
            print("Processing transaction...")
            # revisamos si existen suficientes entradas a las solicitadas
            result = pedidoLogic.checkDisponibilidad(idEvento)
            # si hay suficientes entradas, el pedido queda registrado, registramos todas las entradas y cargamos el dinero al creador del evento
            if cantEntradas <= result:
                entradaLogic.registrarAllEntradas(
                    pedidoID, idEvento, cantEntradas, result
                )
                monederoLogic.cargarDineroCreador(idEvento, total)
                print("¡Felicidades! La transacción se completó con éxito")

            # Si el usuario ordenó más entradas de las existentes, borramos el pedido e informamos
            else:
                print(f"Lo sentimos, solo quedan {result} entradas disponibles")
                pedidoLogic.deletePedido(pedidoID)

        else:
            # por algún motivo algo ha fallado, pero nunca deberíamos llegar a esta parte
            print("Sth went wrong, pls try again")

    def mostrarTarjetas(self, idUsuario):  # mostramos las tarjetas del usuario
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