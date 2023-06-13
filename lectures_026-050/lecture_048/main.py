print(' DATA TYPE: TUPLE '.center(50, '='))

print('\n' + ' TUPLE '.center(50, '~'))
names = ('Paula', 'Wagner')
numbers = tuple(range(3))
ages = (26, 26)

print(f'{names=} - {type(names)=}')
print(f'{ages=} - {type(ages)=}')
print(f'{numbers=} - {type(numbers)=}')

print('\n' + ' INDEXING '.center(50, '~'))

print(f'{names[0]=}')
print(f'{names[-1]=}')

# TypeError
# numbers[0] = -1
