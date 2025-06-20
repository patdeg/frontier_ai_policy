from dotenv import load_dotenv
import os
import openai

load_dotenv()

class Chatty:
    """Minimal interface for GPT-4o-mini with optional safety."""

    def __init__(self, safe: bool = True):
        self.safe = safe
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if safe:
            self.system_prompt = (
                "You are Chatty, a helpful assistant following the California policy on frontier AI."
            )
        else:
            self.system_prompt = "You are Chatty, a helpful assistant."

    def chat(self, text: str) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text},
        ]
        if self.safe and self._triggers(text):
            return "I'm sorry, but I can't help with that."
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        return response.choices[0].message.content

    def _triggers(self, text: str) -> bool:
        """Basic content filter for the safe mode."""
        flagged = ["hack", "bomb", "kill", "malware", "illegal"]
        lowered = text.lower()
        return any(t in lowered for t in flagged)
