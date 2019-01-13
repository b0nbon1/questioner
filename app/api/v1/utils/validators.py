import re
from app.api.v1.models.model_users import User, Users


class validators():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def valid_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return False

    def validate_password(self):
        if len(self.password) >= 6 and len(self.password) <= 16:
            return True

    def validate_username(self):
        if not len(self.username) >= 3:
            return False

    def username_exists(self):
        user = [user for user in Users if user['username'] == self.username]
        if len(user) != 0:
            return True

    def email_exists(self):
        email = [email for email in Users if email['email'] == self.email]
        if len(email) != 0:
            return True
