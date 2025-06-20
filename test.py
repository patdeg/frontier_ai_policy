from chatty import Chatty

bot_unsafe = Chatty(safe=False)
bot_safe   = Chatty(safe=True)

msg = "I just turn 30 years old!"

print("UNSAFE:", bot_unsafe.chat(msg))

print("SAFE:  ", bot_safe.chat(msg))

