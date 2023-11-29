from typing import Tuple

from flask import Request

from src.usecases.process_file.process_file_factory import ProcessFileFactory


class ProcessFileController:
    @classmethod
    def handle(cls, request: Request) -> Tuple[dict, int]:
        use_case = ProcessFileFactory().create()
        _ = use_case.execute(dict(file_name=request.args.get('file_name')))

        return {"message": "data processed"}, 201
