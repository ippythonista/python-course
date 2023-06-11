print(' F-STRING '.center(50, '='))

name = 'Paula'
height = 1.62
weight = 84.5
bmi = weight / height ** 2

print('\n' + ' EXAMPLES '.center(50, '~'))
print(f"{name}'s height is {height:.2f} meters,")
print(f'her weight is {weight:.2f} kg and her')
print(f'BMI is {bmi:.3f}')
print()

number = 12345678.90
print(f'NUMBER: {number:,.2f}')
