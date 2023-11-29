from abc import ABC, abstractmethod

from src.models.graph import GraphModel


class GraphRepository(ABC):
    @abstractmethod
    def insert_graph(self, model: GraphModel):
        pass
