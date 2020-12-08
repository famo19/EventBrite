class EventObj:
    def __init__(
        self,
        id,
        idUsuario,
        nombre,
        idCategoria,
        fecha,
        hora,
        descripcion,
        valorEntrada,
        capacidad,
        disponibilidad,
        ciudad,
        pais,
        direccion,
    ):
        self.id = id
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.idCategoria = idCategoria
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.valorEntrada = valorEntrada
        self.capacidad = capacidad
        self.disponibilidad = disponibilidad
        self.ciudad = ciudad
        self.pais = pais
        self.direccion = direccion
