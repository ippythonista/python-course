print(' STRING METHODS '.center(50, '='))
string1 = 'blablabla'
string2 = 'bla BLA bLa'
string3 = '1234'
print('\n' + ' IMMUTABLE '.center(50, '~'))

# TypeError
# string[3:6] = '...'

string4 = f'{string1[:3]}...{string1[6:]}'
print(string1, string4)

print('\n' + ' METHODS '.center(50, '~'))
print(string2.capitalize())
print(string3.zfill(10))
