from eventbrite_x import EventbriteX


class Logic:
    def __init__(self):
        self.database = None
        self.__createDatabase()

    def __createDatabase(self):
        if self.database is None:
            self.database = EventbriteX()

    def getAllRows(self, tableName):
        database = self.database
        sql = f"select * from `{database.database}`.`{tableName}`;"
        rowList = database.executeQueryRows(sql)
        return rowList

    def deleteRowById(self, id, tableName):
        database = self.database
        sql = f"DELETE FROM `{database.database}`.`{tableName}` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows