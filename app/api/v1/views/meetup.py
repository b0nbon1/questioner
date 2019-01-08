from flask import Flask, jsonify, make_response, request, Blueprint
from app.api.v1.models.model_meetups import meetups, Meetup


meetup = Blueprint('meetup', __name__, url_prefix='/api/v1/meetup')


@meetup.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    location = data['location']
    images = data['images']
    topic = data['topic']
    happeningOn = data['happeningOn']
    tags = data['tags']

    new_meetup = Meetup(location, images, topic, happeningOn, tags)
    add_meetup = new_meetup.create_meetup()

    return make_response(jsonify({"data": add_meetup,
                                  "message": "user successfull registered!",
                                  "status": 201})), 201

@meetup.route('/upcoming', methods=['GET'])
def get_upcoming():
    if len(meetups) == 0:
        return make_response(jsonify({"message": "no available questions right now",
                                        "status": 404})), 404
    return make_response(jsonify({"status": 200},
                                {"data":meetups})), 200
