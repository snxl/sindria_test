from flask import Flask

from src.routes.question_routes import question_routes


class Routes:
    @classmethod
    def load(cls, app: Flask):
        question_routes(app)
