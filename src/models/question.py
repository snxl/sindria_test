class QuestionModel:
    def __init__(
            self,
            question_id: str,
            focus: list[str],
            image: str,
            text: str,
            alternatives: list[str],
            answer: str,
            video: str,
            discipline: str,
            theme: str
    ):
        self.question_id = question_id
        self.focus = focus
        self.image = image
        self.text = text
        self.alternatives = alternatives
        self.answer = answer
        self.video = video
        self.discipline = discipline
        self.theme = theme

    def to_dict(self) -> dict[str, str | list[str]]:
        return {
            'question_id': self.question_id,
            'focus': self.focus,
            'image': self.image,
            'text': self.text,
            'alternatives': self.alternatives,
            'answer': self.answer,
            'video': self.video,
            'discipline': self.discipline,
            'theme': self.theme
        }
