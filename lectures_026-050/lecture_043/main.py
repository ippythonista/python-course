print(' LOOPS: FOR '.center(50, '='))

lang = 'python'
lang_backwards = ''

print('\n' + ' FOR IN '.center(50, '~'))
for letter in lang:
    lang_backwards = letter + lang_backwards
    print(lang_backwards)

print('\n' + ' RANGE '.center(50, '~'))
print('\n' + ' RANGE(STOP) '.center(50, '-'))
for i in range(10):
    print(i, end=' ')
print()

print('\n' + ' RANGE(START, STOP) '.center(50, '-'))
for i in range(1, 11):
    print(i, end=' ')
print()

print('\n' + ' RANGE(START, STOP, STEP) '.center(50, '-'))
for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(0, -10, -1):
    print(i, end=' ')
print()

print('\n' + ' ITER/NEXT '.center(50, '~'))
iterator = iter(lang)
print(iterator)

print(next(iterator), end=' ')
print(next(iterator), end=' ')
print(next(iterator), end=' ')
print(next(iterator), end=' ')
print(next(iterator), end=' ')
print(next(iterator))

# StopIteration
# print(next(iterator))

iterator = iter(lang)
while True:
    try:
        print(next(iterator), end=' ')
    except StopIteration:
        break

print('\n' + ' FOR '.center(50, '~'))
limit = int(input('Enter a number [1-10]: '))
for i in range(limit):
    if i == 3:
        print(f'{i=}! Continuing...')
        continue

    if i == 10:
        print(f'{i=}. Breaking...')
        break
    for j in range(3):
        print(f'({i=}, {j=})', end=' ')
    print()
else:
    print('Bye!!!')
