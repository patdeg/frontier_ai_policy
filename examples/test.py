from chatty import Chatty


def run_demo() -> None:
    """Show difference between safe and unsafe modes."""
    bot_unsafe = Chatty(safe=False)
    bot_safe = Chatty(safe=True)

    msg = "I just turn 30 years old!"

    print("UNSAFE:", bot_unsafe.chat(msg))
    print("SAFE:  ", bot_safe.chat(msg))


if __name__ == "__main__":
    run_demo()

