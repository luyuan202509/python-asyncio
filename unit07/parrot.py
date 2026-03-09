
def main():
    messate = input('Tell me something, and I will repeat it back to you: ')
    print(messate)

def auto_quit():
    prompt = "\n Tell me something, and I will repeat it back to you: "
    prompt1 = "\n Enter 'quit' to end the program. "
    message = ""

    while message != 'quit':
        message = input(prompt)
       # print(message)
        if message != 'quit':
            print(message)
            print(prompt1)

def auto_quit2():
    prompt = "\n Tell me something, and I will repeat it back to you: "
    prompt1 = "\n Enter 'quit' to end the program. "
    active = True
    while active:
        message = input(prompt)
       # print(message)
        if message == 'quit' | message == 'exit' :
            active = False
        else:
            print(message)
            print(prompt1)
                 


if __name__ == '__main__':
    auto_quit2()