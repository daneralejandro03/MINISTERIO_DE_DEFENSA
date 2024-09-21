from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import Servicio
import json
import os


class ControladorServicio(Repositorio,Persistencia):

    servicios: list["Servicio"]

    def __init__(self):
        self.servicios = []

    def create(self, servicio:object) -> None:
        return self.servicios.append(servicio)


    def get(self, id: str) -> object:

        encontrado: Servicio = None
        i:int = 0

        while i < len(self.servicios) and encontrado == None:
            if self.servicios[i].getServicio() == id:
                encontrado = self.servicios[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for servicio in self.servicios:
            respuesta.append(servicio)

        return respuesta


    def update(self, servicio: object) -> object:
        servicio_nuevo = servicio
        servicio_actual = self.get(servicio_nuevo.getServicio())
        if servicio_actual is not None:
            indice_actual = self.servicios.index(servicio_actual)
            self.servicios[indice_actual] = servicio_nuevo
            return servicio_nuevo
        return None

    def delete(self, id: str) -> bool:

        servicio_buscado = self.get(id)
        if servicio_buscado is not None:
            self.servicios.remove(servicio_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        data = [servicio.to_dict() for servicio in self.servicios]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Servicios guardados en {archivo}")

    def cargar(self, archivo: str) -> None:
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.servicios.clear()
            for servicio_data in data:
                servicio = Servicio.Servicio.from_dict(servicio_data)
                self.create(servicio)
            print(f"Cuerpos cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")