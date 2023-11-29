from flask import Flask, request, jsonify

from src.controllers.find_ranked_question_controller import FindRankedQuestionController
from src.controllers.process_file_controller import ProcessFileController


def question_routes(app: Flask):
    @app.route('/question/process-file', methods=['GET'])
    def process_file():
        result, code = ProcessFileController().handle(request)
        return jsonify(result), code

    @app.route('/question/find-ranked', methods=['GET'])
    def find_ranked_question():
        result, code = FindRankedQuestionController().handle(request)
        return jsonify(result), code
