print(' STRING INTERPOLATION '.center(50, '='))

name = 'Paula'
pi = 3.14159265358979
year = 2023

print('\n' + ' EXAMPLES '.center(50, '~'))
print('My name is %s' % name)
print("%s's favorite number is: %.5f" % (name, pi))
print('%d in hexadecimal is:' % year)
print('%x | %X |  %04x | %08X' % (year, year, year, year))
