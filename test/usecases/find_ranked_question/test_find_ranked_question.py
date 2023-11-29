from unittest.mock import MagicMock

from src.usecases.find_ranked_question.find_ranked_question_usecase import FindRankedQuestionUseCase
from test.fakes.repositories.fake_question_repository import FakeQuestionRepository


class TestFindRankedQuestionUseCase:
    def test_execute(self):
        fake_question_repository = FakeQuestionRepository()
        fake_question_repository.find_ranked_by_requisites = MagicMock(return_value=list())

        use_case = FindRankedQuestionUseCase(
            fake_question_repository,
        )

        use_case.execute(dict(page=1, size=50))

        assert fake_question_repository.find_ranked_by_requisites.call_count == 1
