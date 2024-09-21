from Modelo.Cuerpo import Cuerpo


class Armada(Cuerpo):

    __tipoNave: str
    __areaOperativa: str

    def __init__(self, idCuerpo: str, nombre: str, informacion: str, tipoNave: str, areaOperativa: str):
        super().__init__(idCuerpo, nombre, informacion)
        self.__tipoNave = tipoNave
        self.__areaOperativa = areaOperativa

    def getTipoNave(self) -> str:
        return self.__tipoNave

    def setTipoNave(self, tipoNave: str):
        self.__tipoNave = tipoNave

    def getAreaOperativa(self) -> str:
        return self.__areaOperativa

    def setAreaOperativa(self, areaOperativa: str):
        self.__areaOperativa = areaOperativa

    def toStr(self) -> str:
        return f"Armada: {super().toStr()}, Tipo de Nave: {self.__tipoNave}, Area Operativa: {self.__areaOperativa}"

    def to_dict(self) -> dict:
        return {
            'type': 'Armada',
            **super().to_dict(),
            'tipoNave': self.getTipoNave(),
            'areaOperativa': self.getAreaOperativa()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'object':
        return cls(
            idCuerpo=data['id'],
            nombre=data['nombre'],
            informacion=data['informacion'],
            tipoNave=data['tipoNave'],
            areaOperativa=data['areaOperativa']
        )