from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerializeMixin

db = SQLAlchemy()


class Question(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True)
    wording = db.Column(db.Text, nullable=False)
    code = db.Column(db.Text,
                     nullable=False,
                     unique=True)

    def __repr__(self):
        return f'<Question {self.wording}'


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer,
                            db.ForeignKey('question.id'))
    question = db.relationship('Question',
                               backref=db.backref('items'),
                               lazy=True)

    def __repr__(self):
        return f'Item {self.text}'
