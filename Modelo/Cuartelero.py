from Modelo.Servicio import Servicio


class Cuartelero(Servicio):

    __turno: str
    __ubicacion: str

    def __init__(self, idServicio: str, descripcion: str, turno: str, ubicacion: str):
        super().__init__(idServicio, descripcion)
        self.__turno = turno
        self.__ubicacion = ubicacion

    def getTurno(self) -> str:
        return self.__turno

    def setTurno(self, turno: str):
        self.__turno = turno

    def getUbicacion(self) -> str:
        return self.__ubicacion

    def setUbicacion(self, ubicacion: str):
        self.__ubicacion = ubicacion

    def toStr(self) -> str:
        return f"Cuartelero: {super().toStr()}, Turno: {self.__turno}, Ubicacion: {self.__ubicacion}"

    def to_dict(self) -> dict:
        return {
            'type': 'Cuartelero',
            **super().to_dict(),
            'turno': self.getTurno(),
            'ubicacion': self.getUbicacion()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'object':
        return cls(
            idServicio=data['idServicio'],
            descripcion=data['descripcion'],
            turno=data['turno'],
            ubicacion=data['ubicacion']
        )