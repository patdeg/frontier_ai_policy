# 🛡️  Privacy 1-A — strip ages before they echo
import re

def scrub_age(text: str) -> str:
    """Turn 'I am 30 years old' into 'I am [REDACTED]'."""
    AGE_PATTERN = r"\b\d{1,3}\s*years? old\b"      # catches 5–120-ish
    return re.sub(AGE_PATTERN, "[REDACTED]", text, flags=re.I)

# quick smoke test so CI yells if we regress
assert "30 years old" not in scrub_age("I am 30 years old.")
