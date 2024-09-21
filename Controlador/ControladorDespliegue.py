import os
import json

from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import Despliegue


class ControladorDespliegue(Repositorio, Persistencia):

    despliegues: list["Despliegue"]

    def __init__(self):
        self.despliegues = []

    def create(self, despliegue:object) -> None:
        return self.despliegues.append(despliegue)


    def get(self, id: str) -> object:

        encontrado: Despliegue = None
        i:int = 0

        while i < len(self.despliegues) and encontrado == None:
            if self.despliegues[i].getDespliegue() == id:
                encontrado = self.despliegues[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for despliegue in self.despliegues:
            respuesta.append(despliegue)

        return respuesta


    def update(self, despliegue: object) -> object:
        despliegue_nuevo = despliegue
        despliegue_actual = self.get(despliegue_nuevo.getDespliegue())
        if despliegue_actual is not None:
            indice_actual = self.despliegues.index(despliegue_actual)
            self.despliegues[indice_actual] = despliegue_nuevo
            return despliegue_nuevo
        return None

    def delete(self, id: str) -> bool:

        despliegue_buscado = self.get(id)
        if despliegue_buscado is not None:
            self.despliegues.remove(despliegue_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        """Guarda todos los ministerios en un archivo JSON"""
        data = [despliegue.to_dict() for despliegue in self.despliegues]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Compañias guardados en {archivo}")

    def cargar(self, archivo: str) -> None:
        """Carga ministerios desde un archivo JSON"""
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.despliegues.clear()
            for despliegue_data in data:
                despliegue = Despliegue.Despliegue.from_dict(despliegue_data)
                self.create(despliegue)
            print(f"Despliegues cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")
