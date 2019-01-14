from flask import Flask, jsonify
from datetime import datetime

# damps data for meetups
meetups = []

rsvps = []


class Meetup(object):

    def __init__(self, *args):
        self.meetup_id = len(meetups) + 1
        self.location = args[0]
        self.createdOn = datetime.now()
        self.images = args[1]
        self.topic = args[2]
        self.happeningOn = args[3]
        self.tags = args[4]

    def create_meetup(self):
        new_meetup = {
            "id": self.meetup_id,
            'location': self.location,
            'createdOn': self.createdOn,
            'images': self.images,
            'topic': self.topic,
            'happeningOn': self.happeningOn,
            "tags": self.tags,
        }
        meetups.append(new_meetup)
        return new_meetup

    def get_meetup(meetup_id):
        meetup = [
            meetup for meetup in meetups if meetup['id'] == meetup_id]
        return meetup

    def create_rsvp(topic, meetup, status):

        rsvp = {
            "topic": topic,
            "meetup": meetup,
            "status": status
        }

        return rsvp
