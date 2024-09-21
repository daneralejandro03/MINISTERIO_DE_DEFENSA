from Modelo.Cuerpo import Cuerpo

class Ministerio():

    _idMinisterio: str
    _nombre: str
    _informacion: str

    __cuerpos: list[Cuerpo]

    def __init__(self, idMinisterio: str, nombre: str, informacion: str):
        self._idMinisterio = idMinisterio
        self._nombre = nombre
        self._informacion = informacion

        self.__cuerpos = []

    def getMinisterio(self) -> str:
        return self._idMinisterio

    def setMinisterio(self, idMinisterio: str):
        self._idMinisterio = idMinisterio

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getInformacion(self) -> str:
        return self._informacion

    def setInformacion(self, informacion: str):
        self._informacion = informacion

    def getCuerpos(self) -> list[Cuerpo]:
        return self.__cuerpos

    def setCuerpos(self, cuerpos: list[Cuerpo]):
        self.__cuerpos = cuerpos

    def toStr(self) -> str:
        return f"Ministerio: {self._idMinisterio}, Nombre: {self._nombre}, Informacion: {self._informacion}"

    def agregarCuerpo(self, cuerpo: Cuerpo):
        self.__cuerpos.append(cuerpo)

    def eliminarCuerpo(self, idCuerpo: str):
        for i in range(len(self.__cuerpos)):
            if self.__cuerpos[i].getCuerpo() == idCuerpo:
                self.__cuerpos.pop(i)
                break
        return self.__cuerpos

    def obtenerSoldadosCuerpo(self):

        print(f"Ministerio: {self._nombre}")
        print("")
        for curpo in self.__cuerpos:
            print(f"Nombre del Cuerpo: {curpo.getNombre()}")
            for soldado in curpo.getSoldados():
                print(f"{soldado.getNombre()}")
            print("")

    def to_dict(self) -> dict:
        cuerpos_dict = [cuerpo.to_dict() for cuerpo in self.getCuerpos() if cuerpo is not None]  # Generamos la lista de cuerpos antes
        print(cuerpos_dict)
        return {
            'id': self.getMinisterio(),
            'nombre': self.getNombre(),
            'informacion': self.getInformacion(),
            'cuerpos': cuerpos_dict  # Usamos la lista generada
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'object':
        ministerio = cls(
            idMinisterio=data['id'],
            nombre=data['nombre'],
            informacion=data['informacion']
        )
        for cuerpo_data in data['cuerpos']:
            cuerpo = Cuerpo.from_dict(cuerpo_data)
            ministerio.agregarCuerpo(cuerpo)
        return ministerio