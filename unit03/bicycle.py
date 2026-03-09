"""列表"""

def main():
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles)
    print(bicycles[0])
    print(bicycles[0].title())
    print("="*10)
    message = f"My first bicycle was a {bicycles[0].title()}."
    print(message)

def print_names():
    names = ['alice', 'bob', 'carol', 'dave']
    head = "Nice to meet you,"
    for name in names:
        print(head + " " + name.title() + "!")


if __name__ == '__main__':
    #main() 
    print_names()