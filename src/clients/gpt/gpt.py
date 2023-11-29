from abc import ABC, abstractmethod
from typing import List, Tuple


class GPTClient(ABC):
    @abstractmethod
    def send_question_to_evaluation(self, text: str) -> Tuple[List[str], List[str]]:
        pass
