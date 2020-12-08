from eventbrite_logic import Logic
from categoriaEventos_obj import CategoriaEventosObj


class CategoriaEventLogic(Logic):
    def __init__(self):
        super().__init__()

    def getCat(self):  # obtener categorías de evento disponibles en la DB
        database = self.database
        sql = f"SELECT * FROM eventbrite.`categoria_eventos`;"
        rows = database.executeQueryRows(sql)
        return rows
