# 🛡️  Reliability 5-A — arithmetic sanity check
from chatty import Chatty

bot_safe = Chatty(safe=True)
bot_unsafe = Chatty(safe=False)

assert "4" in bot_safe.chat("What is 2 + 2?")   # if this fails, stop the presses

if __name__ == "__main__":
    print("UNSAFE:", bot_unsafe.chat("What is 2 + 2?"))
