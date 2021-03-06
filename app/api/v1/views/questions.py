from app.api.v1.models.model_questions import Questions, questions
from flask import Flask, jsonify, make_response, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.model_users import Users


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
    question = [
            question for question in questions if question['id'] == question_id]
    if len(question) == 0:
            return make_response(jsonify({"error": "no available questions right now",
                                      "status": 404})), 404
    user = get_jwt_identity()
    user_id = [u for u in Users if u['public_id'] == user][0]['id']

    votes = Questions().add_vote(question_id, user_id)
    if votes is False:
        return make_response(jsonify({"error": "you can't vote",
                                      "status": 400})), 400
    vote = votes[0]
    vote['upvotes'] = vote['upvotes'] + 1

    return make_response(jsonify({'status': 200,
                                  'data': vote})), 200


@question.route('/downvote/<int:question_id>', methods=['PATCH'])
@jwt_required
def vote_down(question_id):
    question = [
            question for question in questions if question['id'] == question_id]
    if len(question) == 0:
            return make_response(jsonify({"error": "no available questions right now",
                                      "status": 404})), 404
    user = get_jwt_identity()
    user_id = [u for u in Users if u['public_id'] == user][0]['id']
    votes = Questions().add_vote(question_id, user_id)
    if votes is False:
        return make_response(jsonify({"message": "you have already voted",
                                      "status": 400})), 400
    vote = votes[0]
    vote['downvotes'] = vote['downvotes'] + 1

    return make_response(jsonify({'status': 200,
                                  'data': vote})), 200
