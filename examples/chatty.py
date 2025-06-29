from dotenv import load_dotenv
import os
import openai

load_dotenv()

RAW_MODEL = "llama3-8b-8192"

class Chatty:
    """Minimal interface for Groq's API with optional safety."""

    def __init__(self, safe: bool = True):
        self.safe = safe
        self.client = openai.OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
        )
        if safe:
            self.system_prompt = (
                "You are Chatty, a helpful assistant following the California policy on frontier AI."
            )
        else:
            self.system_prompt = "You are Chatty, a helpful assistant."

    def chat(self, text: str, system_msg: str | None = None) -> str:
        """Send a prompt with an optional override for the system message."""
        prompt = system_msg if system_msg else self.system_prompt
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ]
        if self.safe and self._triggers(text):
            return "I'm sorry, but I can't help with that."
        response = self.client.chat.completions.create(
            model=RAW_MODEL,
            messages=messages,
        )
        return response.choices[0].message.content

    def _triggers(self, text: str) -> bool:
        """Basic content filter for the safe mode."""
        flagged = ["hack", "bomb", "kill", "malware", "illegal"]
        lowered = text.lower()
        return any(t in lowered for t in flagged)
