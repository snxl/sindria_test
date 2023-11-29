from src.config.pymongo import mongodb
from src.models.graph import GraphModel
from src.repositories.graph.graph_repository import GraphRepository


class PymongoGraphRepository(GraphRepository):
    def insert_graph(self, model: GraphModel):
        question_dict = model.to_dict()
        mongodb.graphs.insert_one(question_dict)
