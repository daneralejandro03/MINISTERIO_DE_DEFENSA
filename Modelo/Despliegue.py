from datetime import datetime

from Modelo import Compania
from Modelo import Cuartel


class Despliegue:

    __idDespliegue: str
    __informacion: str
    __fecha: datetime

    __cuartel: Cuartel = None
    __compania: Compania = None

    def __init__(self, idDespliegue: str, informacion: str, fecha: datetime):
        self.__idDespliegue = idDespliegue
        self.__informacion = informacion
        self.__fecha = fecha


    def getDespliegue(self) -> str:
        return self.__idDespliegue

    def setDespliegue(self, idDespliegue: str):
        self.__idDespliegue = idDespliegue

    def getInformacion(self) -> str:
        return self.__informacion

    def setInformacion(self, informacion: str):
        self.__informacion = informacion

    def getFecha(self) -> datetime:
        return self.__fecha

    def setFecha(self, fecha: datetime):
        self.__fecha = fecha

    def getCuartel(self) -> Cuartel:
        return self.__cuartel

    def setCuartel(self, cuartel: Cuartel):
        self.__cuartel = cuartel

    def getCompania(self) -> Compania:
        return self.__compania

    def setCompania(self, compania: Compania):
        self.__compania = compania

    def toStr(self) -> str:
        return f"Despliegue: {self.__idDespliegue}, Informacion: {self.__informacion}, Fecha: {self.__fecha}"

    def to_dict(self) -> dict:
        return {
            "idDespliegue": self.__idDespliegue,
            "informacion": self.__informacion,
            "fecha": self.__fecha.isoformat(),  # Convertir fecha a string
            "cuartel": self.__cuartel.to_dict(),
            "compania": self.__compania.to_dict()
        }

    @classmethod
    def from_dict(cls, despliegue_dict: dict):
        fecha = datetime.fromisoformat(despliegue_dict["fecha"])  # Convertir de string a datetime
        despliegue = cls(
            despliegue_dict["idDespliegue"],
            despliegue_dict["informacion"],
            fecha
        )
        # Asignar cuartel y compania después de la inicialización
        despliegue.setCuartel(despliegue_dict.get("cuartel"))
        despliegue.setCompania(despliegue_dict.get("compania"))
        return despliegue

    #RELACIÓN DE MUCHOS A MUCHOS ENTRE DESPLIEGUE Y CUARTEL Y COMPAÑÍA ! NO FUNCIONA FALTA
    #ARRELGAR

    def agregarCuartel(self, cuartel: Cuartel):
        self.__cuartel = cuartel
        cuartel.agregarDespliegue(self)  # Agregar despliegue al cuartel

    def agregarCompania(self, compania: Compania):
        self.__compania = compania
        compania.agregarDespliegue(self)  # Agregar despliegue a la compañía

    def agregarCuartelCompania(self, cuartel: Cuartel, compania: Compania):
        self.agregarCuartel(cuartel)
        self.agregarCompania(compania)
        cuartel.agregarDespliegue(self)
        compania.agregarDespliegue(self)

    def eliminarCuartelCompania(self):
        if self.__cuartel:
            self.__cuartel.eliminarDespliegue(self.__idDespliegue)
        if self.__compania:
            self.__compania.eliminarDespliegue(self.__idDespliegue)
        self.__cuartel = None
        self.__compania = None


