import pytest
from unittest.mock import patch, MagicMock
from app import create_app, db
from app.models import Question
from app.config import TestConfig


@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.

    This fixture sets up an application context with an in-memory SQLite database
    and yields the app instance. After the test, the database is dropped.
    """
    app = create_app(config_class=TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """
    Create a test client for the app.

    This fixture provides a test client that can be used to make requests to the app.
    """
    return app.test_client()


@patch('app.routes.OpenAIClient')
def test_ask(MockOpenAIClient, client, app):
    """
    Test the /ask endpoint.

    This test patches the OpenAIClient's ask_question method to return a mock response.
    It then sends a POST request to the /ask endpoint with a sample question and checks
    the response status code and content. Finally, it verifies that the question and answer
    were correctly stored in the database.
    """
    mock_ask_question = MagicMock(return_value="Roger Federer")
    MockOpenAIClient.return_value.ask_question = mock_ask_question

    response = client.post('/ask', json={'question': "Who won the most Wimbledon titles in the open era?"})

    # Check the response status code
    assert response.status_code == 200
    data = response.get_json()

    # Verify the response content
    assert data['question'] == "Who won the most Wimbledon titles in the open era?"
    assert data['answer'] == "Roger Federer"

    # Verify the question and answer were stored in the database
    with app.app_context():
        row = Question.query.filter_by(question="Who won the most Wimbledon titles in the open era?").first()
        assert row is not None
        assert row.answer == "Roger Federer"
