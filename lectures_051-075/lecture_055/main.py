print(' UNPACKING (PART 2) '.center(50, '='))

numbers = [1, 2, 3, 4, 5, 6]
username = 'pullynnhah'
info = ('Paula', 26, 'lilac')
students_grades = [
    ['A+', 'A-', 'A'],
    ['B-', 'B', 'B+'],
    ['F', 'C+', 'C'],
]

print('\n' + ' PRINT '.center(50, '~'))
print(*numbers)
print(*username)
print(*info)
print()

print(*students_grades, sep='\n')
