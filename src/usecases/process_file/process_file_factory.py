from src.clients.gpt.openai_gpt_4_turbo_client import OpenaiGPT4TurboClient
from src.repositories.graph.pymongo_graph_repository import PymongoGraphRepository
from src.repositories.question.pymongo_question_repository import PymongoQuestionRepository
from src.usecases.process_file.process_file_usecase import ProcessFileUseCase


class ProcessFileFactory:
    @staticmethod
    def create() -> ProcessFileUseCase:
        return ProcessFileUseCase(
            OpenaiGPT4TurboClient(),
            PymongoQuestionRepository(),
            PymongoGraphRepository()
        )
