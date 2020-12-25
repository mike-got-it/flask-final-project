from main.db import db


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