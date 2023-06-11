print(' EXERCISE 3'.center(50, '='))

number1 = input("Number 1: ")
number2 = input("Number 2: ")

if number1 > number2:
    print(f'{number1=} is greater than {number2=}')
elif number2 > number1:
    print(f'{number2=} is greater than {number1=}')
else:
    print(f'{number1=} is equal to {number2=}')
