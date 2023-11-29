from typing import Tuple, List

from src.clients.gpt.gpt import GPTClient


class FakeGPTClient(GPTClient):
    def send_question_to_evaluation(self, text: str) -> Tuple[List[str], List[str]]:
        return list(), list()
