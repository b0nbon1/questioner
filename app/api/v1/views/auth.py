from flask import Flask, abort, jsonify, make_response, request, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from ..models.model_users import Users, User
from ..utils.validators import validators


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

    '''validations'''
    data1 = [username, firstname, lastname, othername,
             PhoneNumber, email, password, confirm_password]
    for data in data1:
        if not data:
            return make_response(jsonify({"error": "all fields required"}), 400)

    validator = validators(username, email, password)
    check_username = validator.validate_username()
    username_exist = validator.username_exists()
    email_exist = validator.email_exists()
    check_email = validator.valid_email()
    check_password = validator.validate_password()

    if username_exist is True:
        return make_response(jsonify({"error": "username exists",
                                      "status": 409}), 409)

    if email_exist is True:
        return make_response(jsonify({"error": "email exists",
                                      "status": 409}), 409)

    if check_username is False:
        return make_response(jsonify({"error": "invalid username"}), 400)

    if check_email is False:
        return make_response(jsonify({"error": "invalid email",
                                      "status": 400}), 400)

    if not check_password:
        return make_response(jsonify({"error": "invalid password"})), 400

    if password == confirm_password:
        '''Add user to the data structure'''
        password = generate_password_hash(password)
        new_user = User(firstname, lastname, othername,
                        PhoneNumber, username, email, password)
        add_user = new_user.register_user()
        return make_response(jsonify(add_user,
                                     {"message": "user successfull registered!",
                                      "status": 201})), 201
    else:
        return make_response(
            jsonify({"error": "Passwords don't match"})), 400


@auth.route('/login', methods=['POST'])
def login():
    '''login a user to the platform'''
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.get_user(username)
    if len(user) == 0:
        return make_response(jsonify({'message': 'user not found'}), 404)
    else:
        if check_password_hash(user[0]['password'], password):
            public_id = user[0]['public_id']
            access_token = create_access_token(identity=public_id)
            return make_response(jsonify({"access_token": access_token,
                                          "message": "Successfully Logged In",
                                          "status": 200}), 200)
        else:
            return make_response(jsonify({"error": "wrong password",
                                          "status": 401})), 401


@auth.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [
        user for user in Users if user['id'] == user_id]
    if len(user) == 0:
        return make_response(jsonify({'error': 'user cannot be updated'}), 404)
    isAdmin = user[0]['isAdmin']
    isAdmin = True

    return make_response(jsonify(user,
                                 {"message": "user successfull updated!",
                                  "status": 201})), 201
