import os
import json

from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import Cuartel


class ControladorCuartel(Repositorio, Persistencia):

    cuarteles: list["Cuartel"]

    def __init__(self):
        self.cuarteles = []

    def create(self, cuartel:object) -> None:
        return self.cuarteles.append(cuartel)


    def get(self, id: str) -> object:

        encontrado: Cuartel = None
        i:int = 0

        while i < len(self.cuarteles) and encontrado == None:
            if self.cuarteles[i].getCuartel() == id:
                encontrado = self.cuarteles[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for cuartel in self.cuarteles:
            respuesta.append(cuartel)

        return respuesta


    def update(self, cuartel: object) -> object:
        cuartel_nuevo = cuartel
        cuartel_actual = self.get(cuartel_nuevo.getCuartel())
        if cuartel_actual is not None:
            indice_actual = self.cuarteles.index(cuartel_actual)
            self.cuarteles[indice_actual] = cuartel_nuevo
            return cuartel_nuevo
        return None

    def delete(self, id: str) -> bool:

        cuartel_buscado = self.get(id)
        if cuartel_buscado is not None:
            self.cuarteles.remove(cuartel_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        """Guarda todos los ministerios en un archivo JSON"""
        data = [cuartel.to_dict() for cuartel in self.cuarteles]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Cuarteles guardrooms en {archivo}")

    def cargar(self, archivo: str) -> None:
        """Carga ministerios desde un archivo JSON"""
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.cuarteles.clear()
            for cuartel_data in data:
                cuartel = Cuartel.Cuartel.from_dict(cuartel_data)
                self.create(cuartel)
            print(f"Cuarteles cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")
