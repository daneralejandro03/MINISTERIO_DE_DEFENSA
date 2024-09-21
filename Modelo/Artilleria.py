from Modelo.Cuerpo import Cuerpo


class Artilleria(Cuerpo):

    __tipoArtilleria: str
    __alcanceMaximo: str

    def __init__(self, idCuerpo: str, nombre: str, informacion: str, tipoArtilleria: str, alcanceMaximo: str):
        super().__init__(idCuerpo, nombre, informacion)
        self.__tipoArtilleria = tipoArtilleria
        self.__alcanceMaximo = alcanceMaximo

    def getTipoArtilleria(self) -> str:
        return self.__tipoArtilleria

    def setTipoArtilleria(self, tipoArtilleria: str):
        self.__tipoArtilleria = tipoArtilleria

    def getAlcanceMaximo(self) -> str:
        return self.__alcanceMaximo

    def setAlcanceMaximo(self, alcanceMaximo: str):
        self.__alcanceMaximo = alcanceMaximo

    def toStr(self) -> str:
        return f"Artilleria: {super().toStr()}, Tipo de Artilleria: {self.__tipoArtilleria}, Alcance Maximo: {self.__alcanceMaximo}"

    def to_dict(self) -> dict:
        return {
            'type': 'Artilleria',
            **super().to_dict(),
            'tipoArtilleria': self.getTipoArtilleria(),
            'alcanceMaximo': self.getAlcanceMaximo()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'object':
        return cls(
            idCuerpo=data['id'],
            nombre=data['nombre'],
            informacion=data['informacion'],
            tipoArtilleria=data['tipoArtilleria'],
            alcanceMaximo=data['alcanceMaximo']
        )