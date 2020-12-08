class EventoObj:
    def __init__(
        self,
        id,
        idUsuario,
        nombre,
        fecha,
        hora,
        descripcion,
        valorEntrada,
        capacidad,
        disponibilidad,
        pais,
        ciudad,
        direccion,
        idCategoria,
    ):
        self.id = id
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.valorEntrada = valorEntrada
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.pais = pais
        self.ciudad = ciudad
        self.direccion = direccion
        self.idCategoria = idCategoria


class CategoriaObj:
    def __init__(self, id, nombre_categoria):
        self.id = id
        self.nombre_categoria = nombre_categoria