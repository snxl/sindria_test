from src.models.question import QuestionModel
from src.repositories.question.question_repository import QuestionRepository


class FakeQuestionRepository(QuestionRepository):
    def insert_question(self, model: QuestionModel) -> None:
        return

    def find_ranked_by_requisites(self, page: int, size: int) -> list[dict]:
        return list()
