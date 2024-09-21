from abc import ABC, abstractmethod

class Persistencia(ABC):

    @abstractmethod
    def guardar(self, archivo: str):
        pass

    @abstractmethod
    def cargar(self, archivo: str):
        pass