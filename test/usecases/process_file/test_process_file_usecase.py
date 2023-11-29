import json
import os.path
from unittest.mock import MagicMock

import pytest
from werkzeug.exceptions import NotFound, BadRequest

from src.usecases.process_file.process_file_usecase import ProcessFileUseCase
from test.factories.json_of_questions import get_single_question
from test.fakes.clients.fake_gpt_client import FakeGPTClient
from test.fakes.repositories.fake_graph_repository import FakeGraphRepository
from test.fakes.repositories.fake_question_repository import FakeQuestionRepository


class TestProcessFileUseCase:
    def test_execute_without_file(self):
        fake_gpt_client = FakeGPTClient()
        fake_question_repository = FakeQuestionRepository()
        fake_graph_repository = FakeGraphRepository()

        use_case = ProcessFileUseCase(
            fake_gpt_client,
            fake_question_repository,
            fake_graph_repository
        )
        use_case._load_json_file = MagicMock(return_value=None)

        with pytest.raises(NotFound) as exec_info:
            use_case.execute(dict(file_name="nonexistent_file.json"))

        assert "File does not exist" in str(exec_info.value)

    def test_empty_file(self):
        fake_gpt_client = FakeGPTClient()
        fake_question_repository = FakeQuestionRepository()
        fake_graph_repository = FakeGraphRepository()

        use_case = ProcessFileUseCase(
            fake_gpt_client,
            fake_question_repository,
            fake_graph_repository
        )

        empty_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..', '..', '..', 'tmp',
            'empty_file.json'
        )
        with open(empty_file_path, 'w') as empty_file:
            empty_file.write('[]')

        with pytest.raises(BadRequest) as exc_info:
            use_case.execute(dict(file_name="empty_file.json"))

        assert "The file is empty" in str(exc_info.value)

        os.remove(empty_file_path)

    def test_count_call_of_gpt(self):
        fake_gpt_client = FakeGPTClient()
        fake_question_repository = FakeQuestionRepository()
        fake_graph_repository = FakeGraphRepository()

        use_case = ProcessFileUseCase(
            fake_gpt_client,
            fake_question_repository,
            fake_graph_repository
        )

        fake_gpt_client.send_question_to_evaluation = MagicMock(return_value=(list(), list()))

        empty_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..', '..', '..', 'tmp',
            'valid_file.json'
        )
        with open(empty_file_path, 'w') as empty_file:
            empty_file.write(json.dumps(get_single_question()))

        use_case.execute(dict(file_name='valid_file.json'))

        assert fake_gpt_client.send_question_to_evaluation.call_count == 1

        os.remove(empty_file_path)

    def test_count_call_of_insert_question(self):
        fake_gpt_client = FakeGPTClient()
        fake_question_repository = FakeQuestionRepository()
        fake_graph_repository = FakeGraphRepository()

        use_case = ProcessFileUseCase(
            fake_gpt_client,
            fake_question_repository,
            fake_graph_repository
        )

        fake_question_repository.insert_question = MagicMock()

        empty_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..', '..', '..', 'tmp',
            'valid_file.json'
        )
        with open(empty_file_path, 'w') as empty_file:
            empty_file.write(json.dumps(get_single_question()))

        use_case.execute(dict(file_name='valid_file.json'))

        assert fake_question_repository.insert_question.call_count == 1

        os.remove(empty_file_path)

    def test_count_call_of_insert_graph(self):
        fake_gpt_client = FakeGPTClient()
        fake_question_repository = FakeQuestionRepository()
        fake_graph_repository = FakeGraphRepository()

        use_case = ProcessFileUseCase(
            fake_gpt_client,
            fake_question_repository,
            fake_graph_repository
        )

        fake_gpt_client.send_question_to_evaluation = MagicMock(return_value=(['requisite'], ['concept']))
        fake_graph_repository.insert_graph = MagicMock()

        empty_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..', '..', '..', 'tmp',
            'valid_file.json'
        )
        with open(empty_file_path, 'w') as empty_file:
            empty_file.write(json.dumps(get_single_question()))

        use_case.execute(dict(file_name='valid_file.json'))

        assert fake_graph_repository.insert_graph.call_count == 2

        os.remove(empty_file_path)
