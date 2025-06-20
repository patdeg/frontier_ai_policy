# 🛡️  Transparency 4-B — attach a simple saliency map to the answer
from chatty import Chatty

bot_safe = Chatty(safe=True)
bot_unsafe = Chatty(safe=False)

tokens = ["grinder", "noise", "size", "budget"]
weights = [0.30, 0.25, 0.25, 0.20]   # toy example; real values come from LLM tools

heatmap = dict(zip(tokens, weights))

# Basic sanity: weights should sum to 1
assert abs(sum(weights) - 1.0) < 1e-6

if __name__ == "__main__":
    question = "Recommend a quiet burr grinder under $100"
    print("UNSAFE:", bot_unsafe.chat(question))
    print("SAFE:  ", bot_safe.chat(question))
