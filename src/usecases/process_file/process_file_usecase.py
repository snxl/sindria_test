import json
import os.path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TypedDict

from werkzeug.exceptions import NotFound, BadRequest

from src.clients.gpt.gpt import GPTClient
from src.models.graph import GraphModel
from src.models.question import QuestionModel
from src.repositories.graph.graph_repository import GraphRepository
from src.repositories.question.question_repository import QuestionRepository

Input = TypedDict('Input', {'file_name': str})


class ProcessFileUseCase:
    def __init__(
            self,
            gpt_client: GPTClient,
            question_repository: QuestionRepository,
            graph_repository: GraphRepository
    ):
        self.gpt_client = gpt_client
        self.question_repository = question_repository
        self.graph_repository = graph_repository

    def execute(self, input_param: Input):
        file_name = input_param.get('file_name', None)
        actual_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(actual_dir, '..', '..', '..', 'tmp', file_name)
        if not os.path.exists(file_path):
            raise NotFound(f"File does not exist: {file_path}")

        loaded_json = self._load_json_file(file_path)
        if not loaded_json:
            raise BadRequest("The file is empty")

        futures = []

        with ThreadPoolExecutor(max_workers=3) as executor:
            for question_data in loaded_json:
                question_model = self._create_question_model(question_data)
                self.question_repository.insert_question(question_model)

                if question_model.text is not None:
                    future = executor.submit(self.gpt_client.send_question_to_evaluation, question_model.text)
                    futures.append((question_model, future))

            for completed_future in as_completed([future for _, future in futures]):
                question, future = next((item for item in futures if item[1] == completed_future))
                requisites, concepts = completed_future.result()

                if question.question_id is not None:
                    for concept in concepts:
                        graph = self._create_graph_model(question.question_id, 'concept', concept)
                        self.graph_repository.insert_graph(graph)

                    for requisite in requisites:
                        graph = self._create_graph_model(question.question_id, 'requisite', requisite)
                        self.graph_repository.insert_graph(graph)

    @classmethod
    def _load_json_file(cls, file_path: str) -> list[dict]:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @classmethod
    def _create_question_model(cls, question_data: dict) -> QuestionModel:
        return QuestionModel(
            question_id=question_data.get('_id', {}).get('$oid', None),
            focus=question_data.get('focos', []),
            image=question_data.get('imagem', None),
            text=question_data.get('texto', None),
            alternatives=question_data.get('alternativas', []),
            answer=question_data.get('resposta', None),
            video=question_data.get('resposta', None),
            discipline=question_data.get('disciplina', None),
            theme=question_data.get('tematica', None)
        )

    @classmethod
    def _create_graph_model(cls, question_id: str, node_type: str, text: str) -> GraphModel:
        return GraphModel(
            question_id=question_id,
            node_type=node_type,
            text=text
        )
