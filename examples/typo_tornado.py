# 🛡️  Reliability 5-B — nonsense characters shouldn’t derail logic
from chatty import Chatty

bot_safe = Chatty(safe=True)
bot_unsafe = Chatty(safe=False)

typo_query = "Wh@t's thE WEajther toniTe?"

forecast = bot_safe.chat(typo_query)

# Sanity: reply should still mention the word 'forecast' (or similar)
assert "forecast" in forecast.lower()

if __name__ == "__main__":
    print("UNSAFE:", bot_unsafe.chat(typo_query))
