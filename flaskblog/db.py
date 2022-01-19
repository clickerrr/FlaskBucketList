from flaskblog import database, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# User class for the databases
class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password_hash = database.Column(database.String(128))

    def hashPassword(self, password):
        self.password_hash = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=16)

    def checkPasswordHash(self, password):
        return check_password_hash(pwhash=self.password_hash, password=password)

    def __repr__(self):
        return "[" + str(self.username) + ", " + str(self.email) + ", " + str(self.password_hash) + "]"

# so when you set a relationship you set this to a one to many, with the many part having the relationship
# since a user can have many posts, the relationship is between the MANY posts for one user

# when you query the database and ask for first() or all(), first() returns a string based off the toString in the class
# and all() returns a list with all the toStrings
# Posts class for the database
class Posts(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(80), unique=False, nullable=False)
    content = database.Column(database.String(240), unique=False, nullable=False)

    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    user_rel = database.relationship('User', backref=database.backref('user', lazy=True))

    def __repr__(self):
        return "[" + str(self.title) + "]"

@login.user_loader
def load_user(id):
    return User.query.get(int(id))