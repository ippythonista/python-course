print(' TERNARY OPERATOR '.center(50, '='))

number = int(input('Number: '))

print('\n' + ' EXAMPLE '.center(50, '~'))
status = 'EVEN' if number % 2 == 0 else 'ODD'
print(f'{number} is {status}')
