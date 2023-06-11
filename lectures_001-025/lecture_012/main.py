print(' OPERATORS PRECEDENCE '.center(50, '='))
print('\n' + ' PRIORITY '.center(50, '~'))
print('()')
print('**')
print('* / // %')
print('+ -')

print('\n' + ' EXAMPLES '.center(50, '~'))
calculation = 1 + 1 ** 5 + 5
print(calculation)

calculation = (1 + 1) ** (5 + 5)
print(calculation)

calculation = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(calculation)
