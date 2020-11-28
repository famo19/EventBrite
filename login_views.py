from eventbrite_x import EventbriteX
from eventuser_logic import UserLogic
from card_logic import  CardLogic
from prettytable import PrettyTable
from event_main import menuEventos
import datetime


eventbrite = EventbriteX()
user = UserLogic()
card = CardLogic()
tarjeta = CardLogic()
class Tabla:

    def viewAllCards(self, idUser):
        cardList = tarjeta.getAllCards(idUser)

        table = PrettyTable()
        table.field_names = ["id", "iduser", "Num. Tarjeta", "Codigo", "Fecha de Vencimiento"]

        for card in cardList:
            table.add_row(
                [card.id, card.idUser, card.cardNum, card.secNum,card.endDate]
            )
        print(table)   
        table.clear() 
        return table

tabla = Tabla()
class Views:
    def Registro(self):
        print("Bienvenido, ingrese los datos siguientes")
        country= input("Introduzca su país\n")
        city= input("Ciudad donde reside\n")
        userName= input("Introduzca su usuario\n")
        mail= input("Escriba su correo electrónico\n")
        password= input("Inserte su contraseña\n")
        
        print("-------------------------------------------------------------------------------------\n")

        lista=[]#Creo una lista con solo los usuarios, sin diccionarios
        for element in user.getUserName():
            lista.append(element["userName"])

        if userName in lista:#validación de datos
            print("Usuario ya existente, por favor ingrese otro\n\n")
        else:   
            user.insertUser(country, city, userName, mail, password)#Meto registro
            self.RegistroTarjeta(mail)    

    def RegistroTarjeta(self, email):
        idUser= user.getUserIDByMail(email)#Obtengo su ID
        print("-------------------------------------------------------------------------------------\n")
        print("A continuación, registraremos sus datos de la tarjeta:\n")
        cardNum = input("Ingrese el número de su tarjeta(12 digitos)\n")
        secNum = input("Ingrese el código de seguridad de su tarjeta\n")
        endDate1 = input("Ingrese el mes de vencimiento de su tarjeta\n")
        endDate2 = input("Ingrese el año de vencimiento de su tarjeta\n")
        finalDate = endDate2+"-"+endDate1+"-1"
        fecha2= datetime.datetime.strptime(finalDate, "%Y-%m-%d")
        if len(cardNum)<12:
            print("Número de tarjeta inválida")
        else:
            card.insertCard(cardNum,secNum,finalDate,idUser)

    def InicioSesion(self):
        print("Digita tus datos para iniciar sesión")
        email = input("email:")
        password = input("password:")
        print("--------------------------------------------------------------")
        
        lista=[]
        for element in user.getCorreo():
            lista.append(element["correoElectronico"])

        lista2=[]
        for element in user.getPassword():
            lista2.append(element["contrasenna"])
        
        #VALIDACIÓN DE DATOS
        if ((email in lista) and (password in lista2) and(lista.index(email) == lista2.index(password))):
            while True:
                #Menú de usuario
                print("Bienvenido, ¿Qué desea hacer?\n 0-Salir \n 1-Agregar tarjeta \n 2-Borrar tarjeta \n 3-Mostrar tarjetas \n 4-Ir al menú de eventos ")
                opcion= int(input("Seleccione el número de la opción \n"))
                idUser= user.getUserIDByMail(email)#Obtengo su ID
                if opcion==1:  #registrar nueva tarjeta  
                    self.RegistroTarjeta(email)
                elif opcion==2:#Borrar tarjeta
                    tabla.viewAllCards(idUser)
                    delete = int(input("Seleccione el id de la Tarjeta a borrar"))
                    card.deleteCard(delete, idUser)
                    tabla.viewAllCards(idUser)
                elif opcion==3:#Mostrar todas las tarjetas
                    tabla.viewAllCards(idUser)  
                elif opcion==0:#Salir del login
                    break
                elif opcion==4:
                    menuEventos(idUser)
        else:
            print("Ingrese los datos nuevamente")
    
    