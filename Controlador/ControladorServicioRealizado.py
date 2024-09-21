import os
import json

from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import ServicioRealizado


class ControladorServicioRealizado(Repositorio, Persistencia):

    serviciosRealizados: list["ServicioRealizado"]

    def __init__(self):
        self.serviciosRealizados = []

    def create(self, servicioRealizado:object) -> None:
        return self.serviciosRealizados.append(servicioRealizado)


    def get(self, id: str) -> object:

        encontrado: ServicioRealizado = None
        i:int = 0

        while i < len(self.serviciosRealizados) and encontrado == None:
            if self.serviciosRealizados[i].getServicioRealizado() == id:
                encontrado = self.serviciosRealizados[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for servicioRealizado in self.serviciosRealizados:
            respuesta.append(servicioRealizado)

        return respuesta


    def update(self, servicioRealizado: object) -> object:
        servicioRealizado_nuevo = servicioRealizado
        servicioRealizado_actual = self.get(servicioRealizado_nuevo.getServicioRealizado())
        if servicioRealizado_actual is not None:
            indice_actual = self.serviciosRealizados.index(servicioRealizado_actual)
            self.serviciosRealizados[indice_actual] = servicioRealizado_nuevo
            return servicioRealizado_nuevo
        return None

    def delete(self, id: str) -> bool:

        servicioRealizado_buscado = self.get(id)
        if servicioRealizado_buscado is not None:
            self.serviciosRealizados.remove(servicioRealizado_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        """Guarda todos los ministerios en un archivo JSON"""
        data = [servicioRealizado.to_dict() for servicioRealizado in self.serviciosRealizados]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"ServiciosRealizados guardados en {archivo}")

    def cargar(self, archivo: str) -> None:
        """Carga ministerios desde un archivo JSON"""
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.serviciosRealizados.clear()
            for despliegue_data in data:
                despliegue = ServicioRealizado.ServicioRealizado.from_dict(despliegue_data)
                self.create(despliegue)
            print(f"ServiciosRealizados cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")
