from Interface.Persistencia import Persistencia
from Interface.Repositorio import Repositorio
from Modelo import Cuerpo
import json
import os


class ControladorCuerpo(Repositorio, Persistencia):

    cuerpos: list["Cuerpo"]

    def __init__(self):
        self.cuerpos = []

    def create(self, cuerpo:object) -> None:
        return self.cuerpos.append(cuerpo)


    def get(self, id: str) -> object:

        encontrado: Cuerpo = None
        i:int = 0

        while i < len(self.cuerpos) and encontrado == None:
            if self.cuerpos[i].getCuerpo() == id:
                encontrado = self.cuerpos[i]
            i += 1

        return encontrado


    def index(self) -> list:

        respuesta:list["object"] = []

        for cuerpo in self.cuerpos:
            respuesta.append(cuerpo)

        return respuesta


    def update(self, cuerpo: object) -> object:
        cuerpo_nuevo = cuerpo
        cuerpo_actual = self.get(cuerpo_nuevo.getCuerpo())
        if cuerpo_actual is not None:
            indice_actual = self.cuerpos.index(cuerpo_actual)
            self.cuerpos[indice_actual] = cuerpo_nuevo
            return cuerpo_nuevo
        return None

    def delete(self, id: str) -> bool:

        cuerpo_buscado = self.get(id)
        if cuerpo_buscado is not None:
            self.cuerpos.remove(cuerpo_buscado)
            return True

        return False

    def guardar(self, archivo: str) -> None:
        data = [cuerpo.to_dict() for cuerpo in self.cuerpos]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Cuerpos guardados en {archivo}")

    def cargar(self, archivo: str) -> None:
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                data = json.load(f)
            self.cuerpos.clear()
            for cuerpo_data in data:
                cuerpo = Cuerpo.Cuerpo.from_dict(cuerpo_data)
                self.create(cuerpo)
            print(f"Cuerpos cargados desde {archivo}")
        else:
            print(f"El archivo {archivo} no existe.")
