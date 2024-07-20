from openai import OpenAI
import os
from .utils import CHAT_COMPLETION_SYSTEM_PROMPT as SYSTEM_PROMPT


class OpenAIClient:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)

    def ask_question(self, question_text):
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
