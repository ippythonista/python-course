print(' RELATIONAL OPERATORS '.center(50, '='))

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

str1 = input('String 1: ')
str2 = input('String 2: ')

print('\n' + ' GREATER (>) '.center(50, '~'))
print(f'{num1} > {num2}? {num1 > num2}')
print(f'{num2} > {num1}? {num2 > num1}')
print()

print(f'{str1} > {str2}? {str1 > str2}')
print(f'{str2} > {str1}? {str2 > str1}')

print('\n' + ' GREATER THAN OR EQUAL (>=) '.center(50, '~'))
print(f'{num1} >= {num2}? {num1 >= num2}')
print(f'{num2} >= {num1}? {num2 >= num1}')
print()

print(f'{str1} >= {str2}? {str1 >= str2}')
print(f'{str2} >= {str1}? {str2 >= str1}')

print('\n' + ' LESS (>) '.center(50, '~'))
print(f'{num1} < {num2}? {num1 < num2}')
print(f'{num2} < {num1}? {num2 < num1}')
print()

print(f'{str1} < {str2}? {str1 < str2}')
print(f'{str2} < {str1}? {str2 < str1}')

print('\n' + ' LESS THAN OR EQUAL (<=) '.center(50, '~'))
print(f'{num1} <= {num2}? {num1 <= num2}')
print(f'{num2} <= {num1}? {num2 <= num1}')
print()

print(f'{str1} <= {str2}? {str1 <= str2}')
print(f'{str2} <= {str1}? {str2 <= str1}')

print('\n' + ' EQUAL (==) '.center(50, '~'))
print(f'{num1} == {num2}? {num1 == num2}')
print(f'{str1} == {str2}? {str1 == str2}')

print('\n' + ' NOT EQUAL (!=) '.center(50, '~'))
print(f'{num1} != {num2}? {num1 != num2}')
print(f'{str1} != {str2}? {str1 != str2}')
