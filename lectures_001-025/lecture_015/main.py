print(' METHOD: FORMAT '.center(50, '='))

a = 'AAA'
b = 'BBB'
c = 1.23

print('\n' + ' DEFAULT '.center(50, '~'))
string = 'a={} b={} c={}'
print(string.format(a, b, c))

string = 'a={} b={} c={:.3f}'
print(string.format(a, b, c))

# IndexError
# print(string.format(a, b))

print('\n' + ' INDEX '.center(50, '~'))
string = 'a={1} b={2} c={0:.3f}'
print(string.format(c, a, b))

print('\n' + ' KEYWORD '.center(50, '~'))
string = 'a={a} b={b} c={c:.3f}'
print(string.format(c=c, a=a, b=b))
print()

string = 'a={} b={b} c={c:.3f}'
print(string.format(a, c=c, b=b))
