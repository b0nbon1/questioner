from flask import Flask, jsonify
from datetime import datetime

meetups = [
        {
            'id': 1,
            'location': 'Nairobi',
            'createdOn': '3rd jan 2019',
            'images': ['https://www.gsd.harvard.edu/wp-content/uploads/2017/08/Lib-Lab.jpg'],
            'topic': 'machine learning',
            'happeningOn': '7th jan 2019',
            'tags': ['machines', 'data']
        },
        {
            'id': 2,
            'location': 'Thika',
            'createdOn': '5th jan 2019',
            'images': ['https://www.gsd.harvard.edu/wp-content/uploads/2017/08/Lib-Lab.jpg'],
            'topic': 'web development',
            'happeningOn': '17th jan 2019',
            'tags': ['html', 'css']
        },
        {
            'id': 3,
            'location': 'Nairobi',
            'createdOn': '9th jan 2019',
            'images': ['https://www.gsd.harvard.edu/wp-content/uploads/2017/08/Lib-Lab.jpg'],
            'topic': 'ethical hacking',
            'happeningOn': '22nd jan 2019',
            'tags': ['hacking', 'data']
        }
]


class Meetup(object):

    def __init__(self, location, images, topic, happeningOn, tags):
        self.meetup_id = len(meetups) + 1
        self.location = location
        self.createdOn = datetime.now()
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags

    def create_meetup(self):
        new_user = {
            "id": self.meetup_id,
            'location': self.location,
            'createdOn': self.createdOn,
            'images': self.images,
            'topic': self.topic,
            'happeningOn': self.happeningOn,
            "tags": self.tags,
        }
       
        return new_user

    def get_meetup(meetup_id):
        meetup = [
            meetup for meetup in meetups if meetup['id'] == meetup_id]
        return user

    def del_user(meetup_id):
        for meetup in meetups:
            if (meetup['id'] == meetup_id):
                meetups.remove(meetup)
                return meetups
            return jsonify({'message': 'meetup not found'}), 404