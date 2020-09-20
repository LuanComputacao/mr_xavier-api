from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerializeMixin

db = SQLAlchemy()

FlaskSerializeMixin.db = db


class Question(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True)
    wording = db.Column(db.Text, nullable=False)
    code = db.Column(db.Text, nullable=False, unique=True)
    type = db.Column(db.Integer, nullable=False, server_default='1', default=1)
    created_at = db.Column(db.DateTime, onupdate=db.func.now(), server_default=db.func.now(), default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), default=db.func.now())

    create_fields = update_fields = ['wording', 'code']

    def __repr__(self):
        return f'<Question: {self.wording}>'


class Item(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = db.relationship('Question',
                               backref=db.backref('items'),
                               lazy=True)
    created_at = db.Column(db.DateTime, onupdate=db.func.now(), server_default=db.func.now(), default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), default=db.func.now())

    create_fields = update_fields = ['text', 'question_id']

    def __repr__(self):
        return f'<Item: {self.text}>'


quiz_questions = db.Table(
    'quiz_questions',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True)
)


class Quiz(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    questions = db.relationship(
        'Question',
        backref=db.backref('quizs', lazy=True),
        lazy='subquery',
        secondary=quiz_questions
    )
    created_at = db.Column(db.DateTime, onupdate=db.func.now(), server_default=db.func.now(), default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), default=db.func.now())

    def __repr__(self):
        return f'<Quiz: {self.title}> '
