from eventbrite_logic import Logic
from eventuser_obj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAllUsers(self):
        database = self.database
        data = database.executeQueryRows("select * from usuarios;")
        userList = []
        for element in data:
            newUser = self.createUserObj(element)
            userList.append(newUser)
        return userList

    # polimorfismo
    def createUserObj(self, id, userName, password, mail, city, country):
        userObj = UserObj(id, userName, password, mail, city, country)
        return userObj

    def createUserObj(self, userDict):
        userObj = UserObj(
            userDict["userName"],
            userDict["password"],
            userDict["mail"],
            userDict["id"],
            userDict["city"],
            userDict["country"],
        )
        return userObj

    def insertUser(self, country, city, userName, mail, password):
        database = self.database
        sql = (
            f"INSERT INTO `eventbrite`.`usuarios`(`idUsuarios`,`pais`, `ciudad`, `userName`, `correoElectronico`, `contrasenna`) "
            +f"VALUES(0, '{country}', '{city}', '{userName}', '{mail}', '{password}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUserIDByUsername(self, userName):
        database = self.database
        sql = (
            f"SELECT idUsuarios FROM eventbrite.usuarios where userName='{userName}';"
        )
        rows = database.executeQueryOneRow(sql)
        return rows["idUsuarios"]

    def getUserName(self):
        database = self.database
        sql = (f"SELECT userName FROM eventbrite.usuarios;")
        rows = database.executeQueryRows(sql)
        return rows
    
    def getCorreo(self):
        database = self.database
        sql = (f"SELECT correoElectronico FROM eventbrite.usuarios;")
        rows = database.executeQueryRows(sql)
        return rows

    def getPassword(self):
        database = self.database
        sql = (f"SELECT contrasenna FROM eventbrite.usuarios;")
        rows = database.executeQueryRows(sql)
        return rows

    def getUserIDByMail(self, mail):
        database = self.database
        sql = (
            f"SELECT idUsuarios FROM eventbrite.usuarios where correoElectronico='{mail}';"
        )
        rows = database.executeQueryOneRow(sql)
        return rows["idUsuarios"]




    
    
    
    


    
    




