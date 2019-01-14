from flask import Flask, abort, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import uuid


Users = []


class User(object):

    def __init__(self, firstname, lastname, othername, PhoneNumber, username, email, password):
        self.public_id = str(uuid.uuid4())
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.PhoneNumber = PhoneNumber
        self.username = username
        self.password = password

    def register_user(self):
        new_user = {
            "id": len(Users) + 1,
            "public_id": self.public_id,
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
