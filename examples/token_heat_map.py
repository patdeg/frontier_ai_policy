# 🛡️  Transparency 4-B — attach a simple saliency map to the answer
tokens   = ["grinder", "noise", "size", "budget"]
weights  = [0.30, 0.25, 0.25, 0.20]   # toy example; real values come from LLM tools

heatmap = dict(zip(tokens, weights))

# Basic sanity: weights should sum to 1
assert abs(sum(weights) - 1.0) < 1e-6
