print(' EXERCISE 7 '.center(50, '='))

name = input("What's your first name? ")
size = len(name)

if size < 5:
    print('Your name is short')
elif size < 7:
    print('Your name is normal')
else:
    print('Your name is very long')
