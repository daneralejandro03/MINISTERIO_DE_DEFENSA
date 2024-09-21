from abc import ABC, abstractmethod
from typing import List, Dict

from Modelo import Ministerio, Cuartel, Soldado


# Importaciones tardías para evitar problemas de importación circular
def import_classes():
    from Modelo.Artilleria import Artilleria
    from Modelo.Infanteria import Infanteria
    from Modelo.Armada import Armada
    return Artilleria, Infanteria, Armada


class Cuerpo(ABC):
    _idCuerpo: str
    _nombre: str
    _informacion: str

    __ministerio: 'Ministerio'
    __cuarteles: List['Cuartel']
    __soldados: List['Soldado']

    def __init__(self, idCuerpo: str, nombre: str, informacion: str):
        self._idCuerpo = idCuerpo
        self._nombre = nombre
        self._informacion = informacion
        self.__cuarteles = []
        self.__soldados = []

    def getCuerpo(self) -> str:
        return self._idCuerpo

    def setCuerpo(self, idCuerpo: str):
        self._idCuerpo = idCuerpo

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getInformacion(self) -> str:
        return self._informacion

    def setInformacion(self, informacion: str):
        self._informacion = informacion

    def getMinisterio(self) -> 'Ministerio':
        return self.__ministerio

    def setMinisterio(self, ministerio: 'Ministerio'):
        self.__ministerio = ministerio

    def getCuarteles(self) -> List['Cuartel']:
        return self.__cuarteles

    def setCuarteles(self, cuarteles: List['Cuartel']):
        self.__cuarteles = cuarteles

    def getSoldados(self) -> List['Soldado']:
        return self.__soldados

    def setSoldados(self, soldados: List['Soldado']):
        self.__soldados = soldados

    @abstractmethod
    def toStr(self) -> str:
        return f"Cuerpo: {self._idCuerpo}, Nombre: {self._nombre}, Informacion: {self._informacion}"
        pass


    def agregarCuartel(self, cuartel: 'Cuartel'):
        self.__cuarteles.append(cuartel)

    def agregarSoldado(self, soldado: 'Soldado'):
        self.__soldados.append(soldado)

    def eliminarCuartel(self, idCuartel: str):
        for i in range(len(self.__cuarteles)):
            if self.__cuarteles[i].getCuartel() == idCuartel:
                self.__cuarteles.pop(i)
                break
        return self.__cuarteles

    def eliminarSoldado(self, idSoldado: str):
        for i in range(len(self.__soldados)):
            if self.__soldados[i].getSoldado() == idSoldado:
                self.__soldados.pop(i)
                break
        return self.__soldados

    def saberlosdesplieguesdeloscuerpos(self):
        for cuartel in self.__cuarteles:
            print()
            print(f"Nombre del Cuartel: {cuartel.getNombre()}")
            for despliegue in cuartel.getDespliegues():
                print("DESPLIEGUES DEL CUARTEL")
                print(f"Nombre del Despliegue: {despliegue.toStr()}")

    def to_dict(self) -> Dict[str, any]:
        return {
            'type': self.__class__.__name__,  # Añadir el tipo de clase
            'id': self.getCuerpo(),
            'nombre': self.getNombre(),
            'informacion': self.getInformacion(),
            'cuarteles': [cuartel.to_dict() for cuartel in self.getCuarteles()],
            'soldados': [soldado.to_dict() for soldado in self.getSoldados()]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, any]) -> 'Cuerpo':
        Artilleria, Infanteria, Armada = import_classes()

        cuerpo_type = data.get('type')

        # Mapear el tipo del cuerpo a la clase concreta correspondiente
        if cuerpo_type == 'Artilleria':
            return Artilleria.from_dict(data)
        elif cuerpo_type == 'Infanteria':
            return Infanteria.from_dict(data)
        elif cuerpo_type == 'Armada':
            return Armada.from_dict(data)
        else:
            raise ValueError(f"Tipo de cuerpo desconocido: {cuerpo_type}")
