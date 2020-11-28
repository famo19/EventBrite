from eventbrite_logic import Logic
from tipoEventos_obj import TipoEventosObj

class TipoEventLogic(Logic):
    def __init__(self):
        super().__init__()

    def getTipo(self):
        database = self.database
        sql = (f"SELECT * FROM eventbrite.`tipo-eventos`;")
        rows = database.executeQueryRows(sql)
        return rows
        