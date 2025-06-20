from chatty import Chatty

if __name__ == "__main__":
    agent = Chatty(safe=True)
    print(agent.chat("tell me a joke?"))
