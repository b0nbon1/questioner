from flask import Flask, abort, jsonify, make_response, request, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from app.api.v1.models.model_users import Users, User


auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    PhoneNumber = data['PhoneNumber']
    email = data['email']
    password = data['password']
    confirm_password = data['confirm_password']

    if password == confirm_password:
        '''Add user to the data structure'''
        password = generate_password_hash(password)
        new_user = User(firstname, lastname, othername, PhoneNumber, username, email, password)
        add_user = new_user.register_user()

        return make_response(jsonify(add_user,
                                     {"message": "user successfull registered!"})), 200
    else:
        return make_response(
            jsonify({"message": "Passwords don't match"})), 400
