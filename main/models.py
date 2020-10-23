from datetime import datetime

from main import db

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


class Category(db.Model):
    """
    Category Model Class
    """

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    """
    Save category details in Database
    """
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Item(db.Model):
    """
    Item Model Class
    """

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    """
    Save item details in Database
    """
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class CategoryItem(db.Model):
    """
    CategoryItem Model Class
    """

    __tablename__ = 'category_items'

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False, primary_key=True)

    """
    Save category_item details in Database
    """
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class RevokedToken(db.Model):
    """
    Revoked Token Model Class
    """

    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    """
    Saving Token in DB
    """
    def add(self):
        db.session.add(self)
        db.session.commit()

    """
    Checking if the token is blacklisted
    """
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)