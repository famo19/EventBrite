from eventbrite_x import EventbriteX
from eventuser_logic import UserLogic
from card_logic import CardLogic
from login_views import Tabla, Views
from prettytable import PrettyTable

viewObj = Views()
while True:

    print("\n\t\t\t\t\t¡Bienvenido a Eventbrite!")
    opcion = int(
        input(
            "\n¿Qué deseas hacer?\n\n(1) Registrarme\n(2) Iniciar sesión\n\nTu opción: "
        )
    )

    if opcion == 1:  # REGISTRO
        viewObj.Registro()

    elif opcion == 2:  # INICIO DE SESIÓN
        viewObj.InicioSesion()

    else:
        print("\n\n¡Oops! Opción inválida, intente de nuevo.\n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------"
        )
