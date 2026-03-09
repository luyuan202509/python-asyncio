

def main():
    pazza_size = ['large', 'medium', 'small']
    pazza = {
        'crust': 'thick',
        'toppings': ['mashrooms','extra cheese'],
        'size': pazza_size[0],
    }
    
    print(f'You ordered a {pazza_size[0]} pizza with {pazza["toppings"][0]} and {pazza["toppings"][1]}.')
    
    for topping in pazza['toppings']:
        print(f'\t{topping}')
if __name__ == '__main__':
    main()