from Modelo import Cuerpo
from Modelo import Compania
from Modelo import ServicioRealizado


class Soldado:

    __idSoldado:str
    __nombre:str
    __ubicacion:str

    __cuerpo: Cuerpo
    __compania: Compania
    __serviciosRealizados: list["ServicioRealizado"]

    def __init__(self, idSoldado:str, nombre:str, ubicacion:str):

        self.__idSoldado = idSoldado
        self.__nombre = nombre
        self.__ubicacion = ubicacion

        self.__serviciosRealizados = []

    def getSoldado(self) -> str:
        return self.__idSoldado

    def setSoldado(self, idSoldado:str):
        self.__idSoldado = idSoldado

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

    def getServiciosRealizados(self) -> list["ServicioRealizado"]:
        return self.__serviciosRealizados

    def setServiciosRealizados(self, serviciosRealizados: list["ServicioRealizado"]):
        self.__serviciosRealizados = serviciosRealizados

    def getCompania(self) -> Compania:
        return self.__compania

    def setCompania(self, compania:Compania):
        self.__compania = compania

    def toStr(self) -> str:
        return f"Soldado: {self.__idSoldado}, Nombre: {self.__nombre}, Ubicacion: {self.__ubicacion}"

    def agregarServicioRealizado(self, servicioRealizado: "ServicioRealizado"):
        self.__serviciosRealizados.append(servicioRealizado)

    def eliminarServicioRealizado(self, idServicioRealizado: str):
        for i in range(len(self.__serviciosRealizados)):
            if self.__serviciosRealizados[i].getServicioRealizado() == idServicioRealizado:
                self.__serviciosRealizados.pop(i)
                break
        return self.__serviciosRealizados

    def to_dict(self) -> dict:
        return {
            "idSoldado": self.__idSoldado,
            "nombre": self.__nombre,
            "ubicacion": self.__ubicacion,
            "serviciosRealizados": [servicio.to_dict() for servicio in self.__serviciosRealizados]
        }

    @classmethod
    def from_dict(cls, dict) -> "object":
        soldado = cls(
            idSoldado=dict["idSoldado"],
            nombre=dict["nombre"],
            ubicacion=dict["ubicacion"]
        )

        for servicioRealizado_data in dict["serviciosRealizados"]:
            servicioRealizado = ServicioRealizado.ServicioRealizado.from_dict(servicioRealizado_data)
            soldado.agregarServicioRealizado(servicioRealizado)

        return soldado


