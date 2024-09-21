from abc import ABC, abstractmethod
from typing import Dict

from Modelo import ServicioRealizado

def import_classes():
    from Modelo.Guardia import Guardia
    from Modelo.Imaginaria import Imaginaria
    from Modelo.Cuartelero import Cuartelero
    return Guardia, Imaginaria, Cuartelero

class Servicio(ABC):

    _idServicio: str #_ -> protected
    _descripcion: str

    __serviciosRealizados: list["ServicioRealizado"]

    def __init__(self, idServicio: str, descripcion: str):
        self._idServicio = idServicio
        self._descripcion = descripcion

        self.__serviciosRealizados = []

    def getServicio(self) -> str:
        return self._idServicio

    def setServicio(self, idServicio: str):
        self._idServicio = idServicio

    def getDescripcion(self) -> str:
        return self._descripcion

    def setDescripcion(self, descripcion: str):
        self._descripcion = descripcion

    def getServiciosRealizados(self) -> list["ServicioRealizado"]:
        return self.__serviciosRealizados

    def setServiciosRealizados(self, serviciosRealizados: list["ServicioRealizado"]):
        self.__serviciosRealizados = serviciosRealizados

    @abstractmethod
    def toStr(self) -> str:
        return f"Servicio: {self._idServicio}, Descripcion: {self._descripcion}"
        pass

    def to_dict(self) -> Dict[str, any]:
        return {
            "type": self.__class__.__name__,
            "idServicio": self.getServicio(),
            "descripcion": self.getDescripcion(),
            "serviciosRealizados": [servicio.to_dict() for servicio in self.getServiciosRealizados()]
        }

    @classmethod
    def from_dict(self, data: Dict[str, any]) -> 'Servicio':
        Guardia, Imaginaria, Cuartelero = import_classes()
        servicio_type = data.get('type')

        if servicio_type == 'Guardia':
            return Guardia.from_dict(data)
        elif servicio_type == 'Imaginaria':
            return Imaginaria.from_dict(data)
        elif servicio_type == 'Cuartelero':
            return Cuartelero.from_dict(data)
        else:
            raise ValueError(f"Tipo de servicio desconocido: {servicio_type}")
