from flask import Flask, abort, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import uuid


Users = []


class User(object):

    def __init__(self, *args):
        self.firstname = args[0]
        self.lastname = args[1]
        self.othername = args[2]
        self.PhoneNumber = args[3]
        self.username = args[4]
        self.email = args[5]
        self.password = args[6]

    def register_user(self):
        new_user = {
            "id": len(Users) + 1,
            "public_id": str(uuid.uuid4()),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othername': self.othername,
            'PhoneNumber': self.PhoneNumber,
            'isAdmin': False,
            "username": self.username,
            'registered': datetime.now(),
            "email": self.email,
            "password": self.password
        }
        Users.append(new_user)
        return new_user

    def get_user(username):
        user = [
            user for user in Users if user['username'] == username]
        return user
