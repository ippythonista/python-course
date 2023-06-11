print(' EXERCISE 3'.center(50, '='))

first = input("First: ")
last = input("Last: ")

if first > last:
    print(f'{first=} is greater than {last=}')
elif last > first:
    print(f'{last=} is greater than {first=}')
else:
    print(f'{first=} is equal to {last=}')
