# 🛡️  Reliability 5-C — latency & fallback stress test
from chaoslib import network        # faux helper for demo
from timeit   import default_timer as now

def time_call(fn):
    """Return wall-clock seconds for a function call."""
    start = now()
    _ = fn()
    return now() - start

with network.block("api.weather.com"):          # ❶ sever weather API
    latencies = [time_call(lambda: chatty("Rain tomorrow?"))
                 for _ in range(1000)]          # ❷ 1 000 parallel calls

# ❸ At least 99 % under two seconds
good = sum(t < 2 for t in latencies) / len(latencies)

# ❹ No "unavailable" filler text allowed
clean = all("unavailable" not in chatty("") for _ in latencies)
assert good >= 0.99 and clean
