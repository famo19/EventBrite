from busqueda_logic import EventoLogic
from compra_view import viewCompra
from card_logic import CardLogic
from prettytable import PrettyTable


logic = EventoLogic()
buy = viewCompra()
cardLogic = CardLogic()

# Búsqueda general
class busquedaView:
    def detallesEventos(self, idUser):  # Método que regresa los detalles de un evento

        id = int(input("¿Cuál es el id del evento que desea ver más detalles?  "))

        eventoElegido = logic.getEventosById(id)
        while eventoElegido == None:
            id = int(input("\n¡Oops! El 'id' es inválido.\nIngréselo nuevamente: "))
            eventoElegido = logic.getEventosById(id)

        catEventoElegido = logic.getCategoriasByEvent(id)
        userEventoElegido = logic.getUserName(id)

        print(
            "----------------------------------------------------------------------------------------------"
        )
        print("La información adicional de este evento es: ")
        print("\n")
        print("El creador del evento es: " + str(userEventoElegido))
        print("La categoría del evento es: " + str(catEventoElegido))
        print("Descripción: " + eventoElegido["descripcion"])
        print("El valor de la entrada es: ($) " + str(eventoElegido["valorEntrada"]))
        print(
            "La máxima capacidad de asistentes es: "
            + str(eventoElegido["capacidad"])
            + " (personas)"
        )
        print(
            "La cantidad de entradas disponibles es: "
            + str(eventoElegido["disponibilidad"])
        )
        print(
            "La dirección detallada de la ubicación del evento es: "
            + eventoElegido["direccion"]
        )

        # Preguntamos si desea efectuar una compra
        print("\n¿Deseas comprar entradas para este evento? \n")
        print("(1) Sí")
        print("(2) No")
        option = int(input("Tu opción: "))

        while option != 1 and option != 2:
            print("Opción incorrecta, elija nuevamente")
            option = int(input())

        if option == 1:
            # mandamos al usuario a comprar
            buy.compra(idUser, id)
        else:
            pass  # de regreso al menu de busquedas

    def tablaEventos(
        self, eventoList, idUser
    ):  # Método que imprime una tabla con los eventos en una lista dada
        if eventoList == []:
            print("**No hay eventos existentes**\n")
        else:
            table = PrettyTable()
            table.field_names = [
                "IdEvento",
                "nombre",
                "fecha",
                "hora",
                "valorEntrada",
                "disponibilidad",
                "pais",
                "ciudad",
            ]
            for eventoObj in eventoList:
                table.add_row(
                    [
                        eventoObj.id,
                        eventoObj.nombre,
                        eventoObj.fecha,
                        eventoObj.hora,
                        eventoObj.valorEntrada,
                        eventoObj.disponibilidad,
                        eventoObj.ciudad,
                        eventoObj.pais,
                    ]
                )
            print(table)
            response = int(
                input(
                    "\n¿Desea saber más sobre algún evento?\n\n(1) Sí\n(2) No\nTu opción: "
                )
            )
            while response != 1 and response != 2:
                response = int(
                    input("¡Oops! Opción incorrecta, seleccione una nuevamente:\n")
                )

            if response == 1:
                self.detallesEventos(idUser)
            else:
                pass

    def buscar(self, idUser):  # Menú principal del evento
        while True:
            print("\n Elija de qué manera desea realizar la búsqueda de eventos\n")
            print("(0) Salir de la búsqueda")
            print("(1) General")
            print("(2) Por categoría")
            print("(3) Por fecha")
            print("(4) Por ciudad")
            print("(5) Por país\n")
            option = int(input("Tu opción: "))

            if option == 0:  # Salir de la búsqueda
                break
            elif option == 1:  # Buscar todos los eventos existentes
                eventoList = logic.getAllEventosFromSearch()
                self.tablaEventos(eventoList, idUser)

            elif option == 2:  # Buscar por categoría
                categoriaList = logic.getAllCategorias()
                table = PrettyTable()
                table.field_names = ["Categorías"]
                for categoriaObj in categoriaList:
                    table.add_row([categoriaObj.nombre_categoria])
                print(table)

                categoria = input(
                    "Escriba el nombre de la categoria en la que quiere buscar eventos: "
                )

                eventoList = logic.getEventosByCategoria(categoria)

                self.tablaEventos(eventoList, idUser)

            elif option == 3:  # Buscar por fecha
                date = str(
                    input(
                        "Escriba la fecha (YYYY-MM-DD) en la que desea buscar eventos: "
                    )
                )
                eventoList = logic.getEventosByDate(date)
                self.tablaEventos(eventoList, idUser)

            elif option == 4:  # Buscar por fecha
                city = input("Escriba la ciudad en la que quiere buscar los eventos: ")
                eventoList = logic.getEventosByCity(city)
                self.tablaEventos(eventoList, idUser)

            elif option == 5:  # Buscar por país
                country = input("Escriba el país en el que quiere buscar los eventos: ")
                eventoList = logic.getEventosByCountry(country)
                self.tablaEventos(eventoList, idUser)

            else:
                print("Opción incorrecta")