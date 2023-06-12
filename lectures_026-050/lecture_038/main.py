print('  LOOPS: WHILE (PART 2) '.center(50, '='))

print('\n' + ' CONTINUE '.center(50, '~'))
counter = 0
while counter < 10:
    counter = counter + 1
    if counter % 2 == 0:
        continue
    print(counter, end=' ')
print()

print('\n' + ' NESTED LOOPS '.center(50, '~'))
rows = 7
columns = 4

i = 0
while i < rows:
    j = 0
    while j < columns:
        print(f'[{i=}][{j=}]', end=' ')
        j += 1
    i += 1

    print()
