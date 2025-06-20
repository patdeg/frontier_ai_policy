# 🛡️  Transparency 4-A — tack on a one-sentence "why" to every answer
def explainable_chat(system_msg: str, user_msg: str) -> dict:
    """
    Return both the main answer and a tiny rationale.
    Keeps auditors—and curious customers—happy.
    """
    answer = chat(system_msg, user_msg)

    # Second call: ask the model to justify itself in one crisp sentence
    rationale_prompt = f"Q: {user_msg}\nA: {answer}\nExplain why in one sentence."
    reason  = chat("Provide a short rationale.", rationale_prompt)

    return {"answer": answer, "why": reason}

result = explainable_chat("", "Best grinder for small kitchen?")
assert "because" in result["why"].lower()    # sanity: rationale must exist
