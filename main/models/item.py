from main.db import db


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
