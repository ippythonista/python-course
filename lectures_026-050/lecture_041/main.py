print(' LOOPS: WHILE (PART 3) '.center(50, '='))

print('\n' + ' ELSE '.center(50, '~'))

name = input('Name: ')
search = input('Search: ')

size_name = len(name)
size_search = len(search)

i = 0
while i < size_name:
    if name[i:i + size_search] == search:
        print(f'FOUND {search!r} at: {i}')
        break
    i += 1
else:
    print(f'{search!r} was NOT found in {name!r}')
