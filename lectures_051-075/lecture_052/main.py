print(' METHODS: SPLIT & STRIP & JOIN '.center(50, '='))

quote = "I would love to change the world but they don't give me the source code"

print('\n' + ' SPLIT '.center(50, '~'))

print(f'{quote.split()=}')
print(f'{quote.split("e")=}')

print('\n' + ' STRIP '.center(50, '~'))
word = '      Paula Rodrigues      '
print(f'{word.strip()=}')
print(f'{word.lstrip()=}')
print(f'{word.rstrip()=}')

print('\n' + ' JOIN '.center(50, '~'))
username = 'pullynnhah'
print(f'{"_".join(username)=}')
print(f'{" - ".join(username)=}')
