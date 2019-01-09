from flask import Flask, abort, jsonify, make_response, request
from datetime import datetime


questions = [
    {"id": 1,
     "user": 1,
     "meetup": 1,
     "title": "sql and c#",
     "body": "How to Validate Where Expression in MS SQL Stored Procedure(Identify SQL Injection) or from C#"
     },
    {"id": 2,
     "user": 2,
     "meetup": 2,
     "title": "javascript",
     "body": "How to Validate Where Expression in MS SQL Stored Procedure(Identify SQL Injection)"
     }
]

upvotes = []

downvotes = []


class Questions():
    def __init__(self):
        self.questions = questions
        self.upvote = upvotes
        self.downvote = downvotes

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

    def add_upvote(self, meetup, title, body, question_id):
        if len(self.upvote) == 0:
            upvote = {
                "question_id": question_id,
                "title": title,
                "meetup": meetup,
                "upvotes": 0
            }
            upvote
            return upvote
        else:
            upvote = [upvote for upvote in upvotes if
                      upvote['question_id'] == question_id]

            return upvote
