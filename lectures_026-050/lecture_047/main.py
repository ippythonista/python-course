print(' UNPACKING (PART 1) '.center(50, '='))

print('\n' + ' DEFAULT '.center(50, '~'))
numbers = list(range(0, 3))

# ValueError
# n1, n2, n3, n4 = numbers

n1, n2, n3 = numbers
print(f'{numbers=}')
print(f'{n1=}')
print(f'{n2=}')
print(f'{n3=}')

print('\n' + ' ASTERISK (*) '.center(50, '~'))
numbers = list(range(10))

# ValueError
# n1, n2, n3 = numbers

n1, n2, n3, *others = numbers
print(f'{numbers=}')
print(f'{n1=}')
print(f'{n2=}')
print(f'{n3=}')
print(f'{others=}')
print()

numbers = list(range(7))
_, n, *_ = numbers
print(f'{numbers=}')
print(f'{n=}')
print()

numbers = list(range(2))
_, n, *others = numbers
print(f'{numbers=}')
print(f'{n=}')
print(f'{others=}')
