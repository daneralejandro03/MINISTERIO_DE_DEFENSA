from Modelo.Cuerpo import Cuerpo


class Infanteria(Cuerpo):

    __tipoInfanteria: str
    __equipoEspecializado: str

    def __init__(self, idCuerpo: str, nombre: str, informacion: str, tipoInfanteria: str, equipoEspecializado: str):
        super().__init__(idCuerpo, nombre, informacion)
        self.__tipoInfanteria = tipoInfanteria
        self.__equipoEspecializado = equipoEspecializado

    def getTipoInfanteria(self) -> str:
        return self.__tipoInfanteria

    def setTipoInfanteria(self, tipoInfanteria: str):
        self.__tipoInfanteria = tipoInfanteria

    def getEquipoEspecializado(self) -> str:
        return self.__equipoEspecializado

    def setEquipoEspecializado(self, equipoEspecializado: str):
        self.__equipoEspecializado = equipoEspecializado

    def toStr(self) -> str:
        return f"Infanteria: {super().toStr()}, Tipo de Infanteria: {self.__tipoInfanteria}, Equipo Especializado: {self.__equipoEspecializado}"

    def to_dict(self) -> dict:
        return {
            'type': 'Infanteria',
            **super().to_dict(),
            'tipoInfanteria': self.getTipoInfanteria(),
            'equipoEspecializado': self.getEquipoEspecializado()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Infanteria':
        return cls(
            idCuerpo=data['id'],
            nombre=data['nombre'],
            informacion=data['informacion'],
            tipoInfanteria=data['tipoInfanteria'],
            equipoEspecializado=data['equipoEspecializado']
        )