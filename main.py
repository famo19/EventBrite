from eventbrite_x import EventbriteX
from eventuser_logic import UserLogic
from card_logic import  CardLogic
from login_views import Tabla, Views
from prettytable import PrettyTable

#NOMBRAR A LA BASE DE DATOS COMO "eventbrite"
viewObj = Views()
while True:
    
    print("Bienvenido a Eventbrite")
    opcion = int(input("Inserte '1' para registrarte | '2' para iniciar sesión | '0' para salir del programa "))

    if opcion == 1:#REGISTRO
        viewObj.Registro()

    elif opcion ==2:#INIICIO DE SESIÓN
        viewObj.InicioSesion()

    elif opcion ==0 :
        print("Pase feliz día")
        break

    else:
        print("Opción inválida, intente de nuevo")




  