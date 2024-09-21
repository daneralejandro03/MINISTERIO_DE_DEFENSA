import os
import json

from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import Soldado


class ControladorSoldado(Repositorio, Persistencia):

    soldados: list["Soldado"]

    def __init__(self):
        self.soldados = []

    def create(self, soldado:object) -> None:
        return self.soldados.append(soldado)


    def get(self, id: str) -> object:

        encontrado: Soldado = None
        i:int = 0

        while i < len(self.soldados) and encontrado == None:
            if self.soldados[i].getSoldado() == id:
                encontrado = self.soldados[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for soldado in self.soldados:
            respuesta.append(soldado)

        return respuesta


    def update(self, soldado: object) -> object:
        soldado_nuevo = soldado
        soldado_actual = self.get(soldado_nuevo.getSoldado())
        if soldado_actual is not None:
            indice_actual = self.soldados.index(soldado_actual)
            self.soldados[indice_actual] = soldado_nuevo
            return soldado_nuevo
        return None

    def delete(self, id: str) -> bool:
        soldado_buscado = self.get(id)
        if soldado_buscado is not None:
            self.soldados.remove(soldado_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        """Guarda todos los ministerios en un archivo JSON"""
        data = [soldado.to_dict() for soldado in self.soldados]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Soldados guardados en {archivo}")

    def cargar(self, archivo: str) -> None:
        """Carga ministerios desde un archivo JSON"""
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.soldados.clear()
            for soldado_data in data:
                soldado = Soldado.Soldado.from_dict(soldado_data)
                self.create(soldado)
            print(f"Soldados cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")
