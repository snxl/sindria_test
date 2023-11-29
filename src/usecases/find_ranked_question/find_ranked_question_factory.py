from src.repositories.question.pymongo_question_repository import PymongoQuestionRepository
from src.usecases.find_ranked_question.find_ranked_question_usecase import FindRankedQuestionUseCase


class FindRankedQuestionFactory:
    @staticmethod
    def create() -> FindRankedQuestionUseCase:
        return FindRankedQuestionUseCase(
            PymongoQuestionRepository()
        )
