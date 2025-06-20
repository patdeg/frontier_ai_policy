# 🛡️  Reliability 5-B — nonsense characters shouldn’t derail logic
typo_query = "Wh@t's thE WEajther toniTe?"

forecast = chat("", typo_query)

# Sanity: reply should still mention the word 'forecast' (or similar)
assert "forecast" in forecast.lower()
