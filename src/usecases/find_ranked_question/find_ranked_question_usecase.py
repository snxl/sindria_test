from typing import TypedDict

from src.repositories.question.question_repository import QuestionRepository

Input = TypedDict('Input', {'page': int, 'size': int})


class FindRankedQuestionUseCase:
    def __init__(self, question_repository: QuestionRepository):
        self.question_repository = question_repository

    def execute(self, input_param: Input) -> list[dict]:
        return self.question_repository.find_ranked_by_requisites(
            input_param.get('page', 1),
            input_param.get('size', 50)
        )
