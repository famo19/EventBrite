from eventbrite_bd import getConnection ,getCorreo, getPassword, getConnection, insertUser, getUserName, getUserID, insertCard
from prettytable import PrettyTable
import datetime


def registro():
    #Registro de usuario
    print("Welcome, sign up")
    country= input("Insert yout country\n")
    city= input("Insert the city where you live\n")
    userName= input("Insert your username\n")
    mail= input("insert your mail\n")
    password= input("Insert your password\n")
    
    print("-------------------------------------------------------------------------------------\n")

    lista=[]#Creo una lista con solo los usuarios, sin diccionarios
    for element in getUserName():
        lista.append(element["userName"])

    if userName in lista:#validación de datos
        print("Usuario ya existente, por favor ingrese otro\n\n")
    else:
        insertUser(country, city, userName, mail, password)#Meto registro
    #Registro de tarjeta
        idUser=getUserID(userName)#Obtengo su ID
        print("-------------------------------------------------------------------------------------\n")
        print("A continuación, registraremos sus datos de la tarjeta:\n")
        cardNum = input("Ingrese el número de su tarjeta(12 digitos)\n")
        secNum = input("Ingrese el código de seguridad de su tarjeta\n")
        endDate1 = input("Ingrese el mes de vencimiento de su tarjeta\n")
        endDate2 = input("Ingrese el año de vencimiento de su tarjeta\n")
        finalDate = endDate2+"-"+endDate1+"-1"#
        fecha2= datetime.datetime.strptime(finalDate, "%Y-%m-%d")
        if len(cardNum)<12:
            print("Número de tarjeta inválida")
        else:
            insertCard(cardNum,secNum,finalDate,idUser)
        
def inicioSesion():
    print("Digita tus datos para iniciar sesión")
    email = input("email:")
    password = input("password:")
    print("--------------------------------------------------------------")
    
    lista=[]
    for element in getCorreo():
        lista.append(element["correoElectronico"])
   
    lista2=[]
    for element in getPassword():
        lista2.append(element["contrasenna"])
    
    if ((email in lista) and (password in lista2) and(lista.index(email) == lista2.index(password))):
        print("Iniciando sesión")
    else:
        print("Ingrese los datos nuevamente")

while True:
    print("Bienvenido a Eventbrite")
    opcion = int(input("Inserte '1' para registrarte o '2' para iniciar sesión"))

    if opcion == 1:
        registro()       

    elif opcion ==2:
        inicioSesion()
    
    else:
        print("Opción iválida, intente de nuevo")




    