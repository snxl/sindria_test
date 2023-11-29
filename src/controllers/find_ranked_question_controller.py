from typing import Tuple

from flask import Request
from werkzeug.exceptions import BadRequest

from src.usecases.find_ranked_question.find_ranked_question_factory import FindRankedQuestionFactory


class FindRankedQuestionController:
    @classmethod
    def handle(cls, request: Request) -> Tuple[dict, int]:
        page, size = cls._validate(
            request.args.get('page'),
            request.args.get('size')
        )

        use_case = FindRankedQuestionFactory().create()
        questions = use_case.execute(dict(page=page, size=size))

        return {
            "questions": questions
        }, 200

    @classmethod
    def _validate(cls, page: str, size: str) -> Tuple[int, int]:
        try:
            return int(page), int(size)
        except Exception:
            raise BadRequest(
                description="Invalid parameter types. Page and size must be integers"
            )
