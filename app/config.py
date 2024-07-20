import os


class Config:
    """
    Base configuration class.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to track modifications in SQLAlchemy.
        OPENAI_API_KEY (str): API key for OpenAI.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


class TestConfig(Config):
    """
    Testing configuration class.

    Inherits from Config and overrides settings for testing.

    Attributes:
        TESTING (bool): Flag to enable testing mode.
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy using in-memory SQLite for testing.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
