print(' TYPE CASTING '.center(50, '='))

print('\n' + ' INT '.center(50, '~'))
print('\n' + ' STR -> INT '.center(50, '-'))
print(repr('1'), type('1'))
print(int('1'), type(int('1')))

print('\n' + ' FLOAT -> INT '.center(50, '-'))
print(1.9, type(1.9))
print(int(1.9), type(int(1.9)))

print('\n' + ' BOOL -> INT '.center(50, '-'))
print(True, type(True))
print(int(True), type(int(True)))
print()

print(False, type(False))
print(int(False), type(int(False)))

print('\n' + ' FLOAT '.center(50, '~'))
print('\n' + ' STR -> FLOAT '.center(50, '-'))
print(repr('1.8'), type('1.8'))
print(float('1.8'), type(float('1.8')))

print('\n' + ' INT -> FLOAT '.center(50, '-'))
print(1, type(1))
print(float(1), type(float(1)))

print('\n' + ' BOOL -> FLOAT '.center(50, '-'))
print(True, type(True))
print(float(True), type(float(True)))
print()

print(False, type(False))
print(float(False), type(float(False)))

print('\n' + ' BOOL '.center(50, '~'))
print('\n' + ' STR -> BOOL '.center(50, '-'))
print(repr(' '), type(' '))
print(bool(' '), type(bool(' ')))
print()

print(repr(''), type(''))
print(bool(''), type(bool('')))

print('\n' + ' INT -> BOOL '.center(50, '-'))
print(-21, type(-21))
print(bool(-21), type(bool(-21)))
print()

print(0, type(0))
print(bool(0), type(bool(0)))

print('\n' + ' FLOAT -> BOOL '.center(50, '-'))
print(-2.1, type(-2.1))
print(bool(-2.1), type(bool(-2.1)))
print()

print(.0, type(.0))
print(bool(.0), type(bool(.0)))

print('\n' + ' STR '.center(50, '~'))
print('\n' + ' INT -> STR '.center(50, '-'))
print(123, type(123))
print(repr(str(123)), type(str(123)))

print('\n' + ' FLOAT -> STR '.center(50, '-'))
print(-3.21, type(-3.21))
print(repr(str(-3.21)), type(str(-3.21)))

print('\n' + ' BOOL -> STR '.center(50, '-'))
print(True, type(True))
print(repr(str(True)), type(str(True)))
