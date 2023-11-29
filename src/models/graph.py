class GraphModel:
    def __init__(self, question_id: str, node_type: str, text: str):
        self.question_id = question_id
        self.node_type = node_type
        self.text = text

    def to_dict(self):
        return {
            'question_id': self.question_id,
            'type': self.node_type,
            'text': self.text
        }
