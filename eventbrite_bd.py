import pymysql

def getConnection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="12345",
        db="eventbrite",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection

def getCorreo():
    try:
        connection= getConnection()
        with connection.cursor() as mycursor:
            sql = (f"SELECT correoElectronico FROM eventbrite.usuarios;")
            mycursor.execute(sql)
            correo = mycursor.fetchall()
    finally:
        connection.close()
    return correo


def getPassword():
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (f"SELECT contrasenna FROM eventbrite.usuarios;")
            mycursor.execute(sql)
            password = mycursor.fetchall()
    finally:
        connection.close()
    return password

""" 
Partes del login
    -Creación de usuario
        *Rellenar todos los campos necesarios
    -Registro de tarjeta
        *Rellenar todos los campos necesarios
    -Inicio de sesión
        *Validar que las credenciales esten en MySQL
"""

def insertUser(country, city, userName, mail, password):#Se inserta el registro nuevo a la BD
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql=(f"INSERT INTO `eventbrite`.`usuarios` (`idUsuarios`, `pais`, `ciudad`, `userName`, `correoElectronico`, `contrasenna`) "
                +f"VALUES(0, '{country}', '{city}', '{userName}', '{mail}', '{password}');")
            print(sql)
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()

def getUserName():#Obtengo lista de diccionarios de userNames
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (f"SELECT userName FROM eventbrite.usuarios;")
            mycursor.execute(sql)
            user = mycursor.fetchall()
    finally:
        connection.close()
    return user

def getUserID(userName):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql = (f"SELECT idUsuarios FROM eventbrite.usuarios where userName='{userName}';")
            mycursor.execute(sql)
            user = mycursor.fetchone()
    finally:
        connection.close()
    return user["idUsuarios"]

def insertCard(cardNum, secNum, endDate, idUser):
    try:
        connection = getConnection()
        with connection.cursor() as mycursor:
            sql=(f"INSERT INTO `eventbrite`.`tarjetadecredito` (`idTarjetaDeCredito`, `numeroTarjeta`, `codigoSeguridad`, `vencimiento`, `idUsuarios`) "
                +f"VALUES(0, '{cardNum}', {secNum}, '{endDate}', {idUser});")
            print(sql)
            mycursor.execute(sql)
            connection.commit()
    finally:
        connection.close()

    
    


