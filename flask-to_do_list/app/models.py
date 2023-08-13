from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # to_do_list = db.relationship("List")

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)


    def to_dict(self):
        return{
            'id':self.id,
            'username':self.username,
            'password':self.password
        }

    # def add_to_list(self, product):
    #     p = List(self.id, product)
    #     db.session.add(p)
    #     db.session.commit()

    # def remove_from_list(self, product):
    #     p = List.query.filter_by(user_id=self.id).filter_by(item_id=item.id).first()
    #     db.session.delete(p)
    #     db.session.commit()

    # def get_list(self):
    #     p = List.query.filter_by(user_id=self.id).all()
    #     list = [List.query.get(obj.item_id) for obj in p]
    #     return list
    


# class List(db.Model):
    # id = db.Column(db.Integer, primary_key=True, unique=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # product_id = db.Column(db.Integer, db.ForeignKey("product.id"))

    # def __init__(self, user_id, product_id):
    #     self.user_id = user_id
    #     self.product_id = product_id












