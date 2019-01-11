from app.api.v1.models.model_questions import Questions, questions
from flask import Flask, jsonify, make_response, request, Blueprint
from flask_jwt_extended import jwt_required


question = Blueprint('questions', __name__, url_prefix='/api/v1/question')


@question.route('/', methods=['POST'])
@jwt_required
def ask_question():
    data = request.get_json()

    user = data["user"]
    meetup = data["meetup"]
    title = data["title"]
    body = data["body"]

    ask = Questions().create_question(user, meetup, title, body)
    return make_response(jsonify({"status": 201,
                                  "data": ask})), 201


@question.route('/upvote/<int:question_id>', methods=['PATCH'])
@jwt_required
def vote_up(question_id):
    try:
        meetup = [question for question in questions if
                  question['id'] == question_id][0]['meetup']
        title = [question for question in questions if
                 question['id'] == question_id][0]['title']
        body = [question for question in questions if
                question['id'] == question_id][0]['body']
    except IndexError:
        return make_response(jsonify(
            {
                "status": 404,
                "error": "error can't find meetup data"
            })), 404

    vote = Questions().add_upvote(meetup, title, body, question_id)

    vote['upvotes'] = vote['upvotes'] + 1

    return make_response(jsonify({'status': 200,
                                  'data': vote})), 200


@question.route('/downvote/<int:question_id>', methods=['PATCH'])
@jwt_required
def vote_down(question_id):
    try:
        meetup = [question for question in questions if
                  question['id'] == question_id][0]['meetup']
        title = [question for question in questions if
                 question['id'] == question_id][0]['title']
        body = [question for question in questions if
                question['id'] == question_id][0]['body']

    except IndexError:
        return make_response(jsonify(
            {
                "status": 404,
                "error": "error can't find meetup data"
            })), 404

    vote = Questions().add_downvote(meetup, title, body, question_id)

    vote['downvotes'] = vote['downvotes'] + 1

    return make_response(jsonify({'status': 200,
                                  'data': vote})), 200
