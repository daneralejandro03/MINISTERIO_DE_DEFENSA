from abc import ABC, abstractmethod
from typing import List, Optional


class Repositorio(ABC):

    @abstractmethod
    def create(self, el_objeto: object) -> bool:
        pass

    @abstractmethod
    def get(self, id: str) -> Optional[object]:
        pass

    @abstractmethod
    def index(self) -> List[object]:
        pass

    @abstractmethod
    def update(self, el_objeto: object) -> Optional[object]:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
