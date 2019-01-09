from app.api.v1.models.model_questions import Questions
from flask import Flask, jsonify, make_response, request, Blueprint


question = Blueprint('questions', __name__, url_prefix='/api/v1/question')


@question.route('/new_question', methods=['POST'])
def ask_question():
    data = request.get_json()

    user = data["user"]
    meetup = data["meetup"]
    title = data["title"]
    body = data["body"]

    ask = Questions().create_question(user, meetup, title, body)
    return make_response(jsonify({"status": 201,
                                  "data": ask})), 201
