
def raw_method():
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    compiled_designs = []

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        compiled_designs.append(current_design)
    
    print("\nThe following models have been printed:")
    for compiled_design in compiled_designs:
        print(compiled_design)


def print_models(unprinted_designs,compiled_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        compiled_designs.append(current_design)

def show_compiled_designs(compiled_designs):
    print("\nThe following models have been printed:")
    for compiled_design in compiled_designs:
        print(compiled_design)

if __name__ == '__main__':
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    compiled_designs = []
    print_models(unprinted_designs,compiled_designs)
    show_compiled_designs(compiled_designs)