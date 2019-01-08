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

    return make_response(jsonify(add_meetup,
                                 {"message": "user successfull registered!"})), 201
