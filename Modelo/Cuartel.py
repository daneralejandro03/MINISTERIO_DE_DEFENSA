from Modelo import Cuerpo
from Modelo import Despliegue


class Cuartel:

    __idCuartel:str
    __nombre:str
    __ubicacion:str

    __cuerpo: Cuerpo
    __despliegues: list["Despliegue"]

    def __init__(self, idCuartel:str, nombre:str, ubicacion:str):

        self.__idCuartel = idCuartel
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__despliegues = []

    def getCuartel(self) -> str:
        return self.__idCuartel

    def setCuartel(self, idCuartel:str):
        self.__idCuartel = idCuartel

    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def getUbicacion(self) -> str:
        return self.__ubicacion

    def setUbicacion(self, ubicacion:str):
        self.__ubicacion = ubicacion

    def getCuerpo(self) -> Cuerpo:
        return self.__cuerpo

    def setCuerpo(self, cuerpo:Cuerpo):
        self.__cuerpo = cuerpo

    def getDespliegues(self) -> list["Despliegue"]:
        return self.__despliegues

    def setDespliegues(self, despliegues:list["Despliegue"]):
        self.__despliegues = despliegues

    def agregarDespliegue(self, despliegue:Despliegue):
        self.__despliegues.append(despliegue)

    def eliminarDespliegue(self, idDespliegue:str):
        for i in range(len(self.__despliegues)):
            if self.__despliegues[i].getDespliegue() == idDespliegue:
                self.__despliegues.pop(i)
                break

    def toStr(self) -> str:
        return f"Cuartel: {self.__idCuartel}, Nombre: {self.__nombre}, Ubicacion: {self.__ubicacion}"


    def to_dict(self) -> dict:
        return {
            "idCuartel": self.__idCuartel,
            "nombre": self.__nombre,
            "ubicacion": self.__ubicacion,
            "despliegues": [despliegue.to_dict() for despliegue in self.__despliegues]
        }

    @classmethod
    def from_dict(cls, dict: dict) -> 'object':
        cuartel = cls(
            idCuartel=dict["idCuartel"],
            nombre=dict["nombre"],
            ubicacion=dict["ubicacion"]
        )

        for despliegue_data in dict["despliegues"]:
            despliegue = Despliegue.Despliegue.from_dict(despliegue_data)
            cuartel.agregarDespliegue(despliegue)

        return cuartel



