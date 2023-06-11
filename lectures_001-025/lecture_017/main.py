print(' CONDITIONAL STATEMENTS '.center(50, '='))

entry = input('Do you wanna "enter" or "exit"? ')

print('\n' + ' NO CONDITION '.center(50, '~'))

print("You're IN!")
print("You're OUT!")

print('\n' + ' CONDITIONALS '.center(50, '~'))
print('\n' + ' IF/ELIF/ELSE '.center(50, '-'))
if entry == 'enter':
    print("You're IN!")
elif entry == 'exit':
    print("You're OUT!")
else:
    print("INVALID")

print('\n' + ' IF '.center(50, '-'))
if entry == 'enter':
    print("You're IN!")

print('\n' + ' IF/ELSE '.center(50, '-'))
if entry == 'enter':
    print("You're IN!")
else:
    print("INVALID")

print('\n' + ' IF/ELIF '.center(50, '-'))
if entry == 'enter':
    print("You're IN!")
elif entry == 'exit':
    print("You're OUT!")

print('\n' + ' CONTROL FLOW '.center(50, '~'))
letter = input('Enter a lowercase vowel: ')

if letter == 'a':
    print('A')
elif letter == 'e':
    print('E')
elif letter == 'i':
    print('I')
elif letter == 'o':
    print('O')
elif letter == 'u':
    print('U')
else:
    print("NOT a lowercase vowel!")
