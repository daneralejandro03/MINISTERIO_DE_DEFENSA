from datetime import datetime

from Modelo import Servicio
from Modelo import Soldado


class ServicioRealizado:

    __idServicioRealizado: str
    __actividad: str
    __fecha: datetime

    __soldado:Soldado = None
    __servicio:Servicio = None

    def __init__(self, idServicioRealizado: str, actividad: str, fecha: datetime):
        self.__idServicioRealizado = idServicioRealizado
        self.__actividad = actividad
        self.__fecha = fecha

    def getServicioRealizado(self) -> str:
        return self.__idServicioRealizado

    def setServicioRealizado(self, idServicioRealizado: str):
        self.__idServicioRealizado = idServicioRealizado

    def getActividad(self) -> str:
        return self.__actividad

    def setActividad(self, actividad: str):
        self.__actividad = actividad

    def getFecha(self) -> datetime:
        return self.__fecha

    def setFecha(self, fecha: datetime):
        self.__fecha = fecha

    def getSoldado(self) -> Soldado:
        return self.__soldado

    def setSoldado(self, soldado: Soldado):
        self.__soldado = soldado

    def getServicio(self) -> Servicio:
        return self.__servicio

    def setServicio(self, servicio: Servicio):
        self.__servicio = servicio

    def toStr(self) -> str:
        return f"Servicio Realizado: {self.__idServicioRealizado}, Actividad: {self.__actividad}, Fecha: {self.__fecha}"

    def to_dict(self) -> dict:
        return {
            "idServicioRealizado": self.__idServicioRealizado,
            "actividad": self.__actividad,
            "fecha": self.__fecha.isoformat(),  # Convertir fecha a string
            "soldado": self.__soldado.to_dict() if self.__soldado else None,  # Verifica si __soldado es None
            "servicio": self.__servicio.to_dict() if self.__servicio else None  # Verifica si __servicio es None
        }

    @classmethod
    def from_dict(cls, despliegue_dict: dict):
        fecha = datetime.fromisoformat(despliegue_dict["fecha"])  # Convertir de string a datetime
        despliegue = cls(
            despliegue_dict["idServicioRealizado"],
            despliegue_dict["actividad"],
            fecha
        )
        # Asignar soldado y servicio después de la inicialización
        soldado_data = despliegue_dict.get("soldado")
        servicio_data = despliegue_dict.get("servicio")

        if soldado_data:
            despliegue.setSoldado(Soldado.Soldado.from_dict(soldado_data))  # Asume que Soldado tiene un método from_dict
        if servicio_data:
            despliegue.setServicio(Servicio.Servicio.from_dict(servicio_data))  # Asume que Servicio tiene un método from_dict

        return despliegue
