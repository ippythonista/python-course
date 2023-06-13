print(' FUNCTION: ENUMERATE '.center(50, '='))

names = ['Mirilaine', 'Charles', 'Fernanda', 'Paula', 'Wagner']

enum_names = enumerate(names)
list_names = list(enumerate(names))

print('\n' + ' ENUMERATE '.center(50, '~'))

print(f'{enum_names=}')
print(f'{list_names=}')

print('\n' + ' FOR '.center(50, '~'))
print('\n' + ' DEFAULT '.center(50, '-'))
print('👇' * 8)
for item in enum_names:
    print(item)
print('👆' * 8)
print()

print('👇' * 8)
for item in enum_names:
    print(item)
print('👆' * 8)
print()

for item in enumerate(names):
    print(item)
print()

for item in enumerate(names, 1):
    print(item)

print('\n' + ' UNPACKING '.center(50, '-'))
for item in enumerate(names):
    index, name = item
    print(f'{index=} - {name=}')
print()

for index, name in enumerate(names):
    print(f'{index=} - {name=}')
