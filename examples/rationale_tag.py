# 🛡️  Transparency 4-A — tack on a one-sentence "why" to every answer
from chatty import Chatty

bot_safe = Chatty(safe=True)
bot_unsafe = Chatty(safe=False)

def explainable_chat(system_msg: str, user_msg: str) -> dict:
    """
    Return both the main answer and a tiny rationale.
    Keeps auditors—and curious customers—happy.
    """
    answer = bot_safe.chat(user_msg, system_msg=system_msg)

    # Second call: ask the model to justify itself in one crisp sentence
    rationale_prompt = f"Q: {user_msg}\nA: {answer}\nExplain why in one sentence."
    reason = bot_safe.chat(
        rationale_prompt,
        system_msg="Provide a short rationale."
    )

    return {"answer": answer, "why": reason}

result = explainable_chat("", "Best grinder for small kitchen?")
assert "because" in result["why"].lower()    # sanity: rationale must exist

if __name__ == "__main__":
    print("UNSAFE:", bot_unsafe.chat("Best grinder for small kitchen?"))
    print("SAFE:  ", result["answer"])
