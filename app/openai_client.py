from openai import OpenAI
import os
from .utils import CHAT_COMPLETION_SYSTEM_PROMPT as SYSTEM_PROMPT


class OpenAIClient:
    """
    Wrapper class for interacting with the OpenAI API.

    Attributes:
        api_key (str): API key for OpenAI.
        client (OpenAI): Instance of the OpenAI client.
    """

    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)

    def ask_question(self, question_text):
        """
        Ask a question to the OpenAI API and get an answer.

        Args:
            question_text (str): The question text to send to the OpenAI API.

        Returns:
            str: The answer text from the OpenAI API.
        """
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question_text},
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        answer_text = response.choices[0].message.content.strip()
        return answer_text
