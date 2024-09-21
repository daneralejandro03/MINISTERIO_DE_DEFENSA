from Modelo.Servicio import Servicio


class Imaginaria(Servicio):

    __frecuencia: str
    __tipo: str

    def __init__(self, idServicio: str, descripcion: str, frecuencia: str, tipo: str):
        super().__init__(idServicio, descripcion)
        self.__frecuencia = frecuencia
        self.__tipo = tipo

    def getFrecuencia(self) -> str:
        return self.__frecuencia

    def setFrecuencia(self, frecuencia: str):
        self.__frecuencia = frecuencia

    def getTipo(self) -> str:
        return self.__tipo

    def setTipo(self, tipo: str):
        self.__tipo = tipo

    def toStr(self) -> str:
        return f"Imaginaria: {super().toStr()}, Frecuencia: {self.__frecuencia}, Tipo: {self.__tipo}"

    def to_dict(self) -> dict:
        return {
            'type': 'Imaginaria',
            **super().to_dict(),
            'frecuencia': self.getFrecuencia(),
            'tipo': self.getTipo()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'object':
        return cls(
            idServicio=data['idServicio'],
            descripcion=data['descripcion'],
            frecuencia=data['frecuencia'],
            tipo=data['tipo']
        )