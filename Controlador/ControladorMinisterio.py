import os
import json

from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import Ministerio


class ControladorMinisterio(Repositorio, Persistencia):

    ministerios: list["Ministerio"]

    def __init__(self):
        self.ministerios = []

    def create(self, ministerio:object) -> None:
        return self.ministerios.append(ministerio)


    def get(self, id: str) -> object:

        encontrado: Ministerio = None
        i:int = 0

        while i < len(self.ministerios) and encontrado == None:
            if self.ministerios[i].getMinisterio() == id:
                encontrado = self.ministerios[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for ministerio in self.ministerios:
            respuesta.append(ministerio)

        return respuesta


    def update(self, ministerio: object) -> object:
        ministerio_nuevo = ministerio
        ministerio_actual = self.get(ministerio_nuevo.getMinisterio())
        if ministerio_actual is not None:
            indice_actual = self.ministerios.index(ministerio_actual)
            self.ministerios[indice_actual] = ministerio_nuevo
            return ministerio_nuevo
        return None

    def delete(self, id: str) -> bool:

        ministerio_buscado = self.get(id)
        if ministerio_buscado is not None:
            self.ministerios.remove(ministerio_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        """Guarda todos los ministerios en un archivo JSON"""
        data = [ministerio.to_dict() for ministerio in self.ministerios]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Ministerios guardados en {archivo}")

    def cargar(self, archivo: str) -> None:
        """Carga ministerios desde un archivo JSON"""
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.ministerios.clear()
            for ministerio_data in data:
                ministerio = Ministerio.Ministerio.from_dict(ministerio_data)
                self.create(ministerio)
            print(f"Ministerios cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")
