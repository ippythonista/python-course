print(' LOOPS: WHILE (PART 1) '.center(50, '='))

print('\n' + ' INFINITE LOOP '.center(50, '~'))
# while True:
#     name = input("What's your name? ")
#     print(f'Hello, {name}!')

print('\n' + ' BREAK '.center(50, '~'))
while True:
    name = input("What's your name? ")
    if name == 'exit':
        break
    print(f'Hello, {name}!')

print('Bye!')

print('\n' + ' WHILE '.center(50, '~'))
counter = 0
while counter < 10:
    counter = counter + 1
    print(counter, end=' ')
print()
