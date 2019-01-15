from flask import Flask, abort, jsonify, make_response, request
from datetime import datetime


questions = []

votes = []
voters = []


class Questions():
    def __init__(self):
        self.questions = questions
        self.votes = votes

    def create_question(self, user, meetup, title, body):
        new_question = {
            "id": len(self.questions) + 1,
            "user": user,
            "meetup": meetup,
            "title": title,
            "body": body,
        }
        self.questions.append(new_question)
        return new_question

    def add_vote(self, question_id, user_id):
        try:
                meetup = [question for question in self.questions if
                          question['id'] == question_id][0]['meetup']
                title = [question for question in self.questions if
                         question['id'] == question_id][0]['title']
                body = [question for question in self.questions if
                        question['id'] == question_id][0]['body']
                self.voters(user_id, question_id)
        except:
                return False
        if len(self.votes) == 0:
            new_vote = {
                "question_id": question_id,
                "title": title,
                "meetup": meetup,
                "upvotes": 0,
                "downvotes": 0
            }
            self.votes.append(new_vote)
            return self.votes
        else:
            v = [v for v in self.votes if v['question_id'] == question_id]
            if len(v) == 0:
                new_vote = {
                        "question_id": question_id,
                        "title": title,
                        "meetup": meetup,
                        "upvotes": 0,
                        "downvotes": 0
                        }
                self.votes.append(new_vote)
                return votes
            else:
                return votes

    @classmethod
    def voters(cls, user_id, question_id):
        cls.voter = voters
        cls.user_id = user_id
        cls.question_id = question_id

        if len(cls.voter) != 0:
            question = [q for q in cls.voter if
                        q['question_id'] == cls.question_id]
            if len(question) != 0:
                user = [user for user in question if
                        user['id'] == cls.user_id]
                if len(user) != 0:
                    return False
        
        new_voter = {'user': cls.user_id,
                     'question_id': cls.question_id}
        cls.voter.append(new_voter)
