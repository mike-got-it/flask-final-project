from main.db import db


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

    @classmethod
    def find_by_id(cls, category_id):
        return cls.query.filter_by(id=category_id).first()