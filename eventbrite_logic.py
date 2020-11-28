from eventbrite_x import EventbriteX


class Logic:
    def __init__(self):
        self.database = None
        self.__createDatabase()

    def __createDatabase(self):
        if self.database is None:
            self.database = EventbriteX()
