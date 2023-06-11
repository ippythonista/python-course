print(' EXERCISE 4 '.center(50, '='))

name = input("What's your name? ")
age = input('How old are you? ')

if name and age:
    print(f'Your name is {name!r}')
    print(f'Your name in reverse is {name[::-1]!r}')
    if ' ' in name:
        print('Your name has spaces')
    else:
        print("Your name doesn't have spaces")
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is: {name[0]!r}')
    print(f'The last letter of your name is: {name[-1]!r}')
else:
    print('Sorry, no blank fields allowed!')
