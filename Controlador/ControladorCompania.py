import os
import json

from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import Compania


class ControladorCompania(Repositorio, Persistencia):

    companias: list["Compania"]

    def __init__(self):
        self.companias = []

    def create(self, compania:object) -> None:
        return self.companias.append(compania)


    def get(self, id: str) -> object:

        encontrado: Compania = None
        i:int = 0

        while i < len(self.companias) and encontrado == None:
            if self.companias[i].getCompania() == id:
                encontrado = self.companias[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for compania in self.companias:
            respuesta.append(compania)

        return respuesta


    def update(self, compania: object) -> object:
        compania_nuevo = compania
        compania_actual = self.get(compania_nuevo.getCompania())
        if compania_actual is not None:
            indice_actual = self.companias.index(compania_actual)
            self.companias[indice_actual] = compania_nuevo
            return compania_nuevo
        return None

    def delete(self, id: str) -> bool:

        compania_buscado = self.get(id)
        if compania_buscado is not None:
            self.companias.remove(compania_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        """Guarda todos los ministerios en un archivo JSON"""
        data = [compania.to_dict() for compania in self.companias]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Compañias guardados en {archivo}")

    def cargar(self, archivo: str) -> None:
        """Carga ministerios desde un archivo JSON"""
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.companias.clear()
            for compania_data in data:
                compania = Compania.Compania.from_dict(compania_data)
                self.create(compania)
            print(f"Compañias cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")
