
def main():
    motorsycle = ['honda', 'yamaha_old', 'suzuki']
    print(motorsycle)
    motorsycle[0] = 'ducati'
    print(motorsycle)
    motorsycle.append('honda')
    print(motorsycle)
    motorsycle.insert(0,'yamaha_new')
    print(motorsycle)
    motorsycle.pop(2)
    print(motorsycle)

if __name__ == '__main__':
    main()
