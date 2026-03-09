
def main():
    prompt = "If you tell us who you are, we can personalize the message you see."
    prompt += "\nWhat is your first name?: "

    name = input(prompt)
    print(f"\nHello, {name.title()}!")

def age_check():
    prompt = "How old are you?: "
    age = input(prompt)
    age = int(age)
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you registered to vote yet?")
    else:
        print("Sorry, you are too young to vote.")
        print("Please register to vote as soon as you turn 18!")

if __name__ == '__main__':
    age_check()


