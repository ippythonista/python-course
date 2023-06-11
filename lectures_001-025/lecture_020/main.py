print(' LOGICAL OPERATORS '.center(50, '='))

print('\n' + ' OPERATORS '.center(50, '~'))
print('\n' + ' AND '.center(50, '-'))
print('True and True ->', True and True)
print('True and False ->', True and False)
print('False and True ->', False and True)
print('False and False ->', False and False)

print('\n' + ' OR '.center(50, '-'))
print('True or True ->', True or True)
print('True or False ->', True or False)
print('False or True ->', False or True)
print('False or False ->', False or False)

print('\n' + ' NOT '.center(50, '-'))
print('not True ->', not True)
print('not False ->', not False)

print('\n' + ' SHORT CIRCUIT '.center(50, '~'))
something = input('Enter something: ')
print(0.0 and something)
print(something or 'Default Value')
print(not something)
