# 🛡️  Reliability 5-C — latency & fallback stress test
from chaoslib import network        # faux helper for demo
from timeit   import default_timer as now
from chatty import Chatty

bot_safe = Chatty(safe=True)
bot_unsafe = Chatty(safe=False)

def time_call(fn):
    """Return wall-clock seconds for a function call."""
    start = now()
    _ = fn()
    return now() - start

with network.block("api.weather.com"):          # ❶ sever weather API
    latencies = [time_call(lambda: bot_safe.chat("Rain tomorrow?"))
                 for _ in range(1000)]          # ❷ 1 000 parallel calls

# ❸ At least 99 % under two seconds
good = sum(t < 2 for t in latencies) / len(latencies)

# ❹ No "unavailable" filler text allowed
clean = all("unavailable" not in bot_safe.chat("") for _ in latencies)
assert good >= 0.99 and clean

if __name__ == "__main__":
    print("UNSAFE latency sample:", time_call(lambda: bot_unsafe.chat("Rain tomorrow?")))
