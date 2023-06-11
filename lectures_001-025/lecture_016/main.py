print(' FUNCTION: INPUT '.center(50, '='))

print('\n' + ' EXAMPLES '.center(50, '~'))
name = input("What's your name? ")
print(f'Your name is: {name}')

print('\n' + ' DISPLAYING VARIABLE '.center(50, '-'))
print(f'{name=}')
print('\n' + ''.center(50, '-') + '\n')

num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
result = num1 + num2
print(f'{repr(num1)} + {repr(num2)} = {repr(result)}')

int1 = int(num1)
int2 = int(num2)
result = int1 + int2
print(f'{int1} + {int2} = {result}')
print()

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
result = num1 + num2
print(f'{num1} + {num2} = {result}')
