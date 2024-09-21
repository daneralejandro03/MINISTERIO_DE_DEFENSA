from Modelo import Servicio


class Guardia(Servicio.Servicio):

    __tipoGuardia: str
    __duracion:int

    def __init__(self, idServicio: str, descripcion: str, tipoGuardia: str, duracion:int):
        super().__init__(idServicio, descripcion)
        self.__tipoGuardia = tipoGuardia
        self.__duracion = duracion

    def getTipoGuardia(self) -> str:
        return self.__tipoGuardia

    def setTipoGuardia(self, tipoGuardia: str):
        self.__tipoGuardia = tipoGuardia

    def getDuracion(self) -> int:
        return self.__duracion

    def setDuracion(self, duracion: int):
        self.__duracion = duracion

    def toStr(self) -> str:
        return f"Guardia: {super().toStr()}, Tipo de Guardia: {self.__tipoGuardia}, Duracion: {self.__duracion}"

    def to_dict(self) -> dict:
        return {
            'type': 'Guardia',
            **super().to_dict(),
            'tipoGuardia': self.getTipoGuardia(),
            'duracion': self.getDuracion()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'object':
        return cls(
            idServicio=data['idServicio'],
            descripcion=data['descripcion'],
            tipoGuardia=data['tipoGuardia'],
            duracion=data['duracion']
        )