print(' EXERCISE 8 '.center(50, '='))
name = 'paula'

fancy_name = '*'
size = len(name)
i = 0

while i < size:
    fancy_name += f'{name[i]}*'
    i += 1

print(fancy_name)  # *p*a*u*l*a*
