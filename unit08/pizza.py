"""任意数量实参"""

def make_pizza(size,*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
