from src.models.graph import GraphModel
from src.repositories.graph.graph_repository import GraphRepository


class FakeGraphRepository(GraphRepository):
    def insert_graph(self, model: GraphModel):
        pass
