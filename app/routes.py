from flask import Blueprint, request, jsonify
from .models import db, Question
from .openai_client import OpenAIClient

main = Blueprint('main', __name__)


@main.route('/ask', methods=['POST'])
def ask():
    """
    Endpoint to ask a question and get an answer.

    This endpoint receives a JSON payload with a 'question' key, sends the question to the OpenAI API,
    stores the question and answer in the database, and returns the question and answer in a JSON response.

    Returns:
        Response: JSON response containing the question and answer.
    """
    data = request.get_json()
    question_text = data.get('question')

    openai_client = OpenAIClient()
    answer_text = openai_client.ask_question(question_text)

    question = Question(question=question_text, answer=answer_text)
    db.session.add(question)
    db.session.commit()

    return jsonify({'question': question_text, 'answer': answer_text})
