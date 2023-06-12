print(' EXERCISE 5 '.center(50, '='))

number = input('Enter an integer: ')
try:
    integer = int(number)
    print(f'{integer=} is:', end=' ')
    if integer % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
except:
    print(f'Sorry {number=} is NOT an int.')
