from abc import ABC, abstractmethod

from src.models.question import QuestionModel


class QuestionRepository(ABC):
    @abstractmethod
    def insert_question(self, model: QuestionModel) -> None:
        pass

    @abstractmethod
    def find_ranked_by_requisites(self, page: int, size: int) -> list[dict]:
        pass
