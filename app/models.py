from . import db


class Question(db.Model):
    """
    Model representing a question and its answer.

    Attributes:
        id (int): Primary key.
        question (str): The question text.
        answer (str): The answer text.
    """
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
