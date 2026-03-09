
def main():
    #print('hello world')
    message = 'hello world'
    print(message)
    name = "ada lovelace" 
    print(name.title())

def full_name():
    first_name = 'jimmy'
    last_name = 'chen'
    #full_name = first_name + ' ' + last_name
    full_name = f"{first_name} {last_name}"
    print(full_name)
    print(f'hello,{full_name.title()}')
    

def my_str():
    name = "Ada Lovelace"
    print(name.upper())
    print(name.lower())

    print("\nPython")
    print("\n=tPython")
    print("="*10)

    print("Languages:\n\tPython\n\tC\n\tJavaScript")

def remove_space():
    name = '  Ada Lovelace  '
    print(name)
    print(name.rstrip())
    print(name.lstrip())
    print(name.strip())
    
    nostarch_url = 'https://nostarch.com'
    print(nostarch_url.removeprefix('https://'))


if __name__ == '__main__':
    remove_space()
