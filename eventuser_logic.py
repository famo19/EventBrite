from eventbrite_logic import Logic
from eventuser_obj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAllUsers(self):  # crea una lista con todos los usuarios
        database = self.database
        data = database.executeQueryRows("select * from usuarios;")
        userList = []
        for element in data:
            newUser = self.createUserObj(element)
            userList.append(newUser)
        return userList

    def createUserObj(
        self, id, userName, password, mail, city, country
    ):  # crea un user object
        userObj = UserObj(id, userName, password, mail, city, country)
        return userObj

    def createUserObj(self, userDict):  # crea un user object
        userObj = UserObj(
            userDict["userName"],
            userDict["password"],
            userDict["mail"],
            userDict["id"],
            userDict["city"],
            userDict["country"],
        )
        return userObj

    def insertUser(
        self, country, city, userName, mail, password
    ):  # Registra un usuario
        database = self.database
        sql = (
            f"INSERT INTO `eventbrite`.`usuarios`(`id`,`pais`, `ciudad`, `userName`, `correo`, `contrasenna`) "
            + f"VALUES(0, '{country}', '{city}', '{userName}', '{mail}', '{password}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUserIDByUsername(
        self, userName
    ):  # Obtener el ID de un usuario por su UserName
        database = self.database
        sql = f"SELECT id FROM eventbrite.usuarios where userName='{userName}';"
        rows = database.executeQueryOneRow(sql)
        return rows["id"]

    def getUserName(self):  # obtener todos los UserName
        database = self.database
        sql = f"SELECT userName FROM eventbrite.usuarios;"
        rows = database.executeQueryRows(sql)
        return rows

    def getCorreo(self):  # obtener todos los correos
        database = self.database
        sql = f"SELECT correo FROM eventbrite.usuarios;"
        rows = database.executeQueryRows(sql)
        return rows

    def getPassword(self):  # obtener todas las contraseñas
        database = self.database
        sql = f"SELECT contrasenna FROM eventbrite.usuarios;"
        rows = database.executeQueryRows(sql)
        return rows

    def getUserIDByMail(self, mail):  # obtener el ID de un usuario por su correo
        database = self.database
        sql = f"SELECT id FROM eventbrite.usuarios where correo='{mail}';"
        rows = database.executeQueryOneRow(sql)
        return rows["id"]

    def getMails(self):  # obtener todos los correos
        database = self.database
        sql = f"SELECT `correo` FROM `eventbrite`.`usuarios`;"
        rows = database.executeQueryRows(sql)
        return rows

    def getTarjetas(self):  # obtener todas las tarjetas
        database = self.database
        sql = f"SELECT `numeroTarjeta` FROM `eventbrite`.`tarjetadecredito`;"
        rows = database.executeQueryRows(sql)
        return rows

    def getContraReal(self, email):  # obtener la contrseña ligada a un correo
        database = self.database
        sql = f"SELECT contrasenna FROM eventbrite.usuarios WHERE correo = '{email}'"
        rows = database.executeQueryOneRow(sql)
        if rows is None:
            rows = ""
            return rows
        else:
            return rows["contrasenna"]

    def getMailByID(self, idUser):  # obtener el correo dado un ID usuario
        database = self.database
        sql = f"SELECT correo FROM eventbrite.usuarios WHERE id = {idUser}"
        output = database.executeQueryOneRow(sql)
        email = output["correo"]
        return email