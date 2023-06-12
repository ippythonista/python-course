print(' FUNCTION: ID '.center(50, '='))

print('\n' + ' ID(INT) '.center(50, '~'))
int1 = 2
int2 = 2
int3 = 10 ** 100
int4 = 10 ** 100
print(f'{id(int1)=}')
print(f'{id(int2)=}')
print(f'{id(int3)=}')
print(f'{id(int4)=}')

print('\n' + ' ID(STR) '.center(50, '~'))
str1 = 'paula'
str2 = 'paula'
str3 = 'paul'
print(f'{id(str1)=}')
print(f'{id(str2)=}')
print(f'{id(str3)=}')
