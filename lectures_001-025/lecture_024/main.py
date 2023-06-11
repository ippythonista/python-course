print(' F-STRING: ADVANCED '.center(50, '='))

abc = 'ABC'
goal = 12345.6789
birth_year = 1996
emoji = '🐍'

print('\n' + ' ALIGNMENT '.center(50, '~'))
print('\n' + ' SPACE '.center(50, '-'))
print(repr(f'{abc:>11}'))
print(repr(f'{abc:<11}'))
print(repr(f'{abc:^11}'))

print('\n' + ' OTHERS '.center(50, '-'))
print(repr(f'{abc:=>11}'))
print(repr(f'{abc:-<11}'))
print(repr(f'{abc:_^11}'))

print('\n' + ' NUMBERS '.center(50, '~'))
print('\n' + ' DEFAULT '.center(50, '-'))
print(f'{goal:.3f}')
print(f'{goal:,.3f}')
print(f'{goal:+,.3f}')
print(f'{goal:0>+16,.3f}')
print(f'{goal:0=+16,.3f}')

print('\n' + ' HEXADECIMAL '.center(50, '-'))
print(f'{birth_year} in hexadecimal is:')
print(f'{birth_year:x} | {birth_year:X} |  '
      f'{birth_year:04x} | {birth_year:08X}')

print('\n' + ' CONVERSION FLAGS '.center(50, '~'))
print(f'repr: {emoji!r}')
print(f'str: {emoji!s}')
print(f'ascii: {emoji!a}')
