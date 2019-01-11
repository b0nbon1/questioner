from flask import Flask, abort, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import uuid


Users = [
        {
            "id": 1,
            "public_id": 'hwfuqkeirhc4253redsf',
            'firstname': 'testlogin',
            'lastname': 'login',
            'othername': 'log',
            'PhoneNumber': '2547logintest',
            'email': 'test1@login.com',
            'username': 'pytest',
            'registered': 'jan 2018',
            'isAdmin': True,
            'password': generate_password_hash("testpytest")
        },
        {
            "id": 1,
            "public_id": 'hwfuqkeirhc4253redsf',
            'firstname': 'testlogin2',
            'lastname': 'login2',
            'othername': 'log2',
            'PhoneNumber': '2547logintest2',
            'email': 'test2@login.com',
            'username': 'pytest2',
            'registered': 'jan 2019',
            'isAdmin': False,
            'password': generate_password_hash("test2guy")
        }
    ]


class User(object):

    def __init__(self, firstname, lastname, othername, PhoneNumber, username, email, password):
        self.user_id = len(Users) + 1
        self.public_id = str(uuid.uuid4())
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.PhoneNumber = PhoneNumber
        self.username = username
        self.registered = datetime.now()
        self.password = password

    def register_user(self):
        new_user = {
            "id": self.user_id,
            "public_id": self.public_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othername': self.othername,
            'PhoneNumber': self.PhoneNumber,
            'isAdmin': False,
            "username": self.username,
            'registered': self.registered,
            "email": self.email,
            "password": self.password
        }       
        return new_user

    def get_user(username):
        user = [
            user for user in Users if user['username'] == username]
        return user
