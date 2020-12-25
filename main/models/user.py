from datetime import datetime

from main.db import db

from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):
    """
    User Model Class
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at=db.Column(db.DateTime(), default=datetime.utcnow())
    categories = db.relationship('Category', backref='users', lazy=True)
    items = db.relationship('Item', backref='users', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User(username={self.username!r})>".format(self=self)

    """
    Save user details in Database
    """
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    """
    Find user by username
    """
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    """
    generate hash from password by encryption using sha256
    """
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    """
    Verify hash and password
    """
    @staticmethod
    def verify_hash(password, hash_):

        return sha256.verify(password, hash_)