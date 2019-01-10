from flask import Flask, jsonify, make_response, request, Blueprint
from app.api.v1.models.model_meetups import meetups, Meetup, rsvps


meetup = Blueprint('meetup', __name__, url_prefix='/api/v1/meetup')


# create a meetup
@meetup.route('/', methods=['POST'])
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


# get a upcoming meetups
@meetup.route('/upcoming', methods=['GET'])
def get_upcoming():
    upcoming_meetups = meetups[::-1]
    if len(upcoming_meetups) == 0:
        return make_response(jsonify({"message": "no available questions right now",
                                      "status": 404})), 404
    return make_response(jsonify({"status": 200},
                                 {"data": upcoming_meetups})), 200


# get specific meetup
@meetup.route('/<int:meetup_id>', methods=['GET'])
def get_meetup(meetup_id):
    meetup = [
        meetup for meetup in meetups if meetup['id'] == meetup_id]
    if len(meetup) == 0:
        return make_response(jsonify({"error": "no such available meetup right now",
                                      "status": 404})), 404
    return make_response(jsonify({"status": 200},
                                 {"data": meetup})), 200


# deletes a meetup
@meetup.route('/<int:meetup_id>', methods=['DELETE'])
def delete_question(meetup_id):
    for meetup in meetups:
        if (meetup_id) == meetup["id"]:
            meetups.remove(meetup)
            return make_response(jsonify({"status": 200},
                                         {"message": "meetup deleted successful"})), 200
    return make_response(jsonify({"error": "no such available meetup right now",
                                  "status": 404})), 404


# creates rsvp to a meetup
@meetup.route('/<int:meetup_id>/rsvps', methods=['POST'])
def create_rsvp(meetup_id):
    # checks if there is such a meetup
    try:
        meetup = [meetup for meetup in meetups if
                  meetup['id'] == meetup_id][0]['id']
        topic = [meetup for meetup in meetups if
                 meetup['id'] == meetup_id][0]['topic']

    # if either the meetup or value is not found
    except IndexError:
        return make_response(jsonify(
            {
                "status": 500,
                "error": "error retrieving meetup data"
            })), 500

    data = request.get_json()
    status = data['status']
    status = status.lower()
    if status == 'yes' or status == 'maybe' or status == 'no':
        rsvp = Meetup.create_rsvp(topic, meetup, status)
        rsvps.append(rsvp)

        return make_response(jsonify({
            "status": 201,
            "data": rsvps
        })), 201

    return make_response(jsonify(
        {
            "status": 406,
            "error": "there is no such status"
        })), 406
