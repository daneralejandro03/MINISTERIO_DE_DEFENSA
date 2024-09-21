from Modelo import Despliegue
from Modelo import Soldado


class Compania:

    __idCompania:str
    __nombre:str
    __actividad:str

    __soldados: list["Soldado"]
    __despliegues: list["Despliegue"]

    def __init__(self, idCompania:str, nombre:str, actividad:str):

            self.__idCompania = idCompania
            self.__nombre = nombre
            self.__actividad = actividad

            self.__soldados = []
            self.__despliegues = []

    def getCompania(self) -> str:
        return self.__idCompania

    def setCompania(self, idCompania:str):
        self.__idCompania = idCompania

    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def getActividad(self) -> str:
        return self.__actividad

    def setActividad(self, actividad:str):
        self.__actividad = actividad

    def getSoldados(self) -> list["Soldado"]:
        return self.__soldados

    def setSoldados(self, soldados: list["Soldado"]):
        self.__soldados = soldados

    def getDespliegues(self) -> list["Despliegue"]:
        return self.__despliegues

    def setDespliegues(self, despliegues: list["Despliegue"]):
        self.__despliegues = despliegues

    def toStr(self) -> str:
        return f"Compania: {self.__idCompania}, Nombre: {self.__nombre}, Actividad: {self.__actividad}"

    def agregarSoldado(self, soldado: Soldado):
        self.__soldados.append(soldado)

    def eliminarSoldado(self, idSoldado: str):
        for i in range(len(self.__soldados)):
            if self.__soldados[i].getSoldado() == idSoldado:
                self.__soldados.pop(i)
                break
        return self.__soldados

    def buscarSoldado(self, idSoldado: str):
        for soldado in self.__soldados:
            if soldado.getSoldado() == idSoldado:
                return soldado
        return None

    def agregarDespliegue(self, despliegue: "Despliegue"):
        if despliegue not in self.__despliegues:
            self.__despliegues.append(despliegue)

    def eliminarDespliegue(self, idDespliegue: str):
        for i in range(len(self.__despliegues)):
            if self.__despliegues[i].getDespliegue() == idDespliegue:
                self.__despliegues.pop(i)
                break
        return self.__despliegues

    def to_dict(self) -> dict:
        return {
            "idCompania": self.__idCompania,
            "nombre": self.__nombre,
            "actividad": self.__actividad,
            "soldados": [soldado.to_dict() for soldado in self.__soldados],
            "despliegues": [despliegue.to_dict() for despliegue in self.__despliegues]
        }

    @classmethod
    def from_dict(cls, compania_dict: dict):
        compania = cls(compania_dict["idCompania"],
                       compania_dict["nombre"],
                       compania_dict["actividad"])
        compania.setSoldados([Soldado.Soldado.from_dict(soldado) for soldado in compania_dict["soldados"]])
        compania.setDespliegues([Despliegue.Despliegue.from_dict(despliegue) for despliegue in compania_dict["despliegues"]])

        return compania