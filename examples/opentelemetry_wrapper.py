# 🛡️  Transparency 4-C — dual mandate: traceable *and* PII-safe
import hashlib, re
from opentelemetry import trace
tracer = trace.get_tracer(__name__)

def scrub(text: str) -> str:
    """Basic PII scrub: redact ages and phone numbers."""
    text = re.sub(r"\b\d{1,3}\s*years? old\b", "[AGE]", text, flags=re.I)
    text = re.sub(r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b", "[PHONE]", text)
    return text

user_prompt = "Hi, I'm 30 years old. What's the cheapest burr grinder?"

prompt_hash = hashlib.sha256(user_prompt.encode()).hexdigest()   # pointer only

with tracer.start_as_current_span("assistant_call") as span:
    # 🔹 Store the HASH so auditors can fetch the full prompt from the vault
    span.set_attribute("prompt.sha256", prompt_hash)

    # 🔹 Use a scrubbed prompt for the model call
    safe_prompt = scrub(user_prompt)
    answer = chat("", safe_prompt)                               # LLM call

    # 🔹 Scrub the answer before logging it
    span.set_attribute("ai.answer", scrub(answer))

    # 🔹 Only structural info about downstream queries
    span.set_attribute("db.query", "SELECT price FROM grinders LIMIT 1")
