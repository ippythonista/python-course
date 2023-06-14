print(' NESTED LISTS '.center(50, '='))

print('\n' + ' 2D LISTS '.center(50, '~'))
students_grades = [
    ['A+', 'A-', 'A'],
    ['B-', 'B', 'B+'],
    ['F', 'C+', 'C'],
]

print('\n' + ' INDEXING '.center(50, '-'))
print(f'{students_grades[0]=}')
print(f'{students_grades[0][0]=}')
print()

print(f'{students_grades[1]=}')
print(f'{students_grades[1][2]=}')
print()

print(f'{students_grades[2]=}')
print(f'{students_grades[2][1]=}')

print('\n' + ' FOR '.center(50, '-'))
for i, student_grades in enumerate(students_grades, 1):
    print(f'Student {i}:')
    for grade in student_grades:
        print(f'\tGrade: {grade!r}')
