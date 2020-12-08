import pymysql


class EventbriteX:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "12345"
        self.database = "eventbrite"
        self.cursorType = pymysql.cursors.DictCursor
        self.connection = self.createConnection()

    def createConnection(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.database,
            cursorclass=self.cursorType,
        )
        return connection

    # un metodo que nos ayude con las sentencias sql que no regresan informacion
    def executeNonQueryBool(self, sql):
        # Se refresca la connection para que se actualicen los datos
        self.endConnection()
        self.startConnection()
        currentCursor = self.connection.cursor()
        # print(sql)
        currentCursor.execute(sql)
        self.connection.commit()
        success = False
        if currentCursor.rowcount > 0:
            success = True
        return success

    def executeNonQueryRows(self, sql):
        # Se refresca la connection para que se actualicen los datos
        self.endConnection()
        self.startConnection()
        currentCursor = self.connection.cursor()
        # print(sql)
        currentCursor.execute(sql)
        self.connection.commit()
        return currentCursor.rowcount

    # otro metodo que nos ayude con las sentencias sql que si traigan informacion
    def executeQueryRows(self, sql):
        # Se refresca la connection para que se actualicen los datos
        self.endConnection()
        self.startConnection()
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        return currentCursor.fetchall()

    def executeQueryOneRow(self, sql):
        # Se refresca la connection para que se actualicen los datos
        self.endConnection()
        self.startConnection()
        currentCursor = self.connection.cursor()
        currentCursor.execute(sql)
        return currentCursor.fetchone()

    def endConnection(self):
        if self.connection.open:
            self.connection.close()

    def startConnection(self):
        if not self.connection.open:
            self.connection = self.createConnection()