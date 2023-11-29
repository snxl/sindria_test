import json

from bson import json_util

from src.config.pymongo import mongodb
from src.models.question import QuestionModel
from src.repositories.question.question_repository import QuestionRepository


class PymongoQuestionRepository(QuestionRepository):
    def insert_question(self, model: QuestionModel) -> None:
        question_dict = model.to_dict()
        mongodb.questions.insert_one(question_dict)

    def find_ranked_by_requisites(self, page: int, size: int) -> list[dict]:
        cursor = mongodb.questions.aggregate(
            [
                {
                    '$lookup': {
                        'from': 'graphs',
                        'localField': 'question_id',
                        'foreignField': 'question_id',
                        'as': 'graphs'
                    }
                },
                {
                    '$addFields': {
                        'requisite_graphs_count': {
                            '$size': {
                                '$filter': {
                                    'input': '$graphs',
                                    'as': 'graph',
                                    'cond': {
                                        '$eq': ['$$graph.type', 'requisite']
                                    }
                                }
                            }
                        },
                        'concept_graphs_count': {
                            '$size': {
                                '$filter': {
                                    'input': '$graphs',
                                    'as': 'graph',
                                    'cond': {
                                        '$eq': ['$$graph.type', 'concept']
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    '$match': {
                        'requisite_graphs_count': {'$gt': 0}
                    }
                },
                {
                    '$sort': {
                        'requisite_graphs_count': -1
                    }
                },
                {
                    '$skip': (page - 1) * size
                },
                {
                    '$limit': size
                }
            ]
        )

        return list(json.loads(json_util.dumps(cursor)))
