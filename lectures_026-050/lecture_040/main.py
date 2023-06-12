print(' EXERCISE 9 '.center(50, '='))

terminate = False
while not terminate:
    float1 = float2 = None
    while float1 is None or float2 is None:
        try:
            float1 = float(input('Number 1: '))
            float2 = float(input('Number 2: '))
        except ValueError:
            print('Enter numbers!\n')
            continue

    operator = input('Operator: ')
    while not (len(operator) == 1 and operator in '+-*/'):
        operator = input('Invalid operator!\nOperator: ')

    if operator == '+':
        print(f'{float1} + {float2} = {float1 + float2:.2f}')
    elif operator == '-':
        print(f'{float1} - {float2} = {float1 - float2:.2f}')
    elif operator == '*':
        print(f'{float1} * {float2} = {float1 * float2:.2f}')
    else:
        if float2 == 0:
            print('Division by ZERO is not allowed!')
        else:
            print(f'{float1} / {float2} = {float1 / float2:.2f}')

    terminate = input('Press [e] to exit anything else to continue: ').lower() == 'e'
    print()
