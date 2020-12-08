from eventbrite_x import EventbriteX
from eventuser_logic import UserLogic
from card_logic import CardLogic
from prettytable import PrettyTable
from event_main import menuEventos
import datetime


eventbrite = EventbriteX()
user = UserLogic()
card = CardLogic()
tarjeta = CardLogic()


class Tabla:
    def viewAllCards(self, idUser):  # Mostrar todas las tarjetas de un usuario
        cardList = tarjeta.getAllCards(idUser)

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


tabla = Tabla()


class Views:
    def Registro(self):  # Registrar un nuevo usuario
        print(
            "\n\n-------------------------------------------------------------------------------------------------------------------------------"
        )
        print("\n\t\t\t\t\t!Bienvenido al registro! Por favor ingresa tus datos\n")
        country = input("Introduzca su país:\n")
        city = input("\nIngrese el nombre de su ciudad:\n")
        userName = input("\nIntroduzca el usuario que desea tener:\n")
        # Revisamos que el usuario esté disponible
        lista = []  # Creo una lista con solo los usuarios, sin diccionarios
        for element in user.getUserName():
            lista.append(element["userName"])

        while True:
            if userName not in lista:
                break
            else:
                userName = input(
                    "\n¡Oops!\nEl usuario ingresado ya no está disponible.\nPor favor ingresa otro: \n"
                )

        mail = input("\nEscriba su correo electrónico:\n")
        # Revisamos que el correo no esté registrado
        lista = []  # lista con solo correos sin diccionarios
        for element in user.getMails():
            lista.append(element["correo"])

        while True:
            if mail not in lista:
                break
            else:
                mail = input(
                    "\n¡Oops!\nEl correo ingresado ya ha sido registrado.\nPor favor ingresa otro: \n"
                )

        password = input("\nDigite una contraseña (¡Solo usted debe saberla!):\n")
        response = int(
            input(
                "\n¡Excelente! Ya casi terminamos.\n¿Deseas añadir tarjeta bancaria a tu registro?\n(1) Sí\n(2) No\nTu Opción: "
            )
        )
        if response == 1:
            user.insertUser(
                country, city, userName, mail, password
            )  # Registramos usuario
            self.RegistroTarjeta(mail)  # registramos tarjeta
            print("¡Excelente! Ya puedes iniciar sesión con tus datos.")
            print(
                "\n-------------------------------------------------------------------------------------------------------------------------------"
            )
        else:
            user.insertUser(
                country, city, userName, mail, password
            )  # Registramos usuario
            print("\n\n¡Registro completado! Ya puedes iniciar sesión con tus datos.\n")
            print(
                "\n-------------------------------------------------------------------------------------------------------------------------------"
            )

    def RegistroTarjeta(self, email):  # Registrar un tarjeta
        print(
            "-------------------------------------------------------------------------------------\n"
        )
        print("A continuación, registraremos los datos de tu tarjeta bancaria.\n")
        cardNum = input("\nIngrese el número de su tarjeta(12 digitos)\n")
        while len(cardNum) != 12:
            cardNum = input(
                "\n¡Número de tarjeta inválido!\nPor favor ingresarlo de nuevo:\n"
            )

        lista = []
        for element in user.getTarjetas():
            lista.append(element["numeroTarjeta"])

        while True:
            if cardNum in lista:
                cardNum = input(
                    "\n¡Oops!\nEl número de tarjeta ya ha sido registrado\nPor favor ingrese otro:\n"
                )
            else:
                break

        secNum = input("\nIngrese el código de seguridad de su tarjeta:\n")
        endDate1 = input("\nIngrese el mes de vencimiento de su tarjeta:\n")
        endDate2 = input("\nIngrese el año de vencimiento de su tarjeta:\n")
        finalDate = endDate2 + "-" + endDate1 + "-1"
        fecha2 = datetime.datetime.strptime(finalDate, "%Y-%m-%d")
        card.insertCard(cardNum, secNum, finalDate, email)
        print("\n¡Registro completado!")
        print(
            "\n-------------------------------------------------------------------------------------------------------------------------------"
        )

    def InicioSesion(self):  # iniciar sesión
        print(
            "-------------------------------------------------------------------------------------------------------------------------------"
        )
        print(
            "\n\t\t\t\t\t¡Bienvenido al inicio de sesión! Por favor ingresa tus datos.\n"
        )
        email = input("\nEmail: ")  # Solicitamos el correo al usuario
        password = input("\nPassword: ")  # Solicitamos la contraseña
        print(
            "\n-----------------------------------------------------------------------------------------------------------------------------"
        )

        # Creamos una lista de todos los correos existentes
        lista = []
        for element in user.getCorreo():
            lista.append(element["correo"])
        # Creamos una lista de todas las contraseñas existentes
        lista2 = []
        for element in user.getPassword():
            lista2.append(element["contrasenna"])
        # Obtenemos la contraseña ligada al correo
        contraReal = user.getContraReal(email)

        # VALIDACIÓN DE DATOS
        if (email in lista) and (password in lista2) and (password == contraReal):
            while True:
                # Menú de usuario
                print(
                    "\n\n¡Buen día! ¿Qué deseas hacer?\n(0) Salir\n(1) Agregar una tarjeta a tu cuenta\n(2) Borrar una tarjeta de tu cuenta\n(3) Mostrar tus tarjetas registradas\n(4) Ir al menú de eventos "
                )
                opcion = int(input("\nTu opción: "))
                while True:  # Bloqueamos opciones no disponibles
                    if opcion < 0 or opcion > 4:
                        opcion = int(
                            input(
                                "\n¡Oops! Opción inválida, intenta nuevamente.\nTu opción: "
                            )
                        )
                    else:
                        break

                idUser = user.getUserIDByMail(email)  # Obtengo su ID
                if opcion == 1:  # Registrar nueva tarjeta
                    self.RegistroTarjeta(email)
                elif opcion == 2:  # Borrar tarjeta
                    print("\n\nEstas son tus tarjetas:")
                    tabla.viewAllCards(idUser)

                    delete = int(
                        input("Ingresa el número 'id' de la Tarjeta a borrar: ")
                    )
                    # Obtenemos lista con id de tarjetas del usuario
                    listaIDCard = card.getIDCards(idUser)
                    # Impedimos que el usuario seleccione una tarjeta que no le pertenece
                    while True:
                        if delete in listaIDCard:
                            break
                        else:
                            delete = int(
                                input(
                                    "\n¡Oops! El 'id' es inválido.\nPor favor ingrésalo nuevamente: "
                                )
                            )
                    # Borramos tarjeta
                    card.deleteCard(delete, idUser)
                    print(
                        "\n¡Excelente! La tarjeta se ha eliminado.\n\nAhora estas son tus tarjetas:"
                    )
                    tabla.viewAllCards(idUser)
                elif opcion == 3:  # Mostrar todas las tarjetas
                    print("\nEstas son tus tajetas:")
                    tabla.viewAllCards(idUser)
                elif opcion == 0:  # Salir del login
                    break
                elif opcion == 4:  # Ir al menú de eventos
                    menuEventos(idUser)
        else:  # Error en la validación
            print(
                "\n!Oops!\nEmail o contraseña erroneo\n\nIngrese los datos nuevamente."
            )
            self.InicioSesion()