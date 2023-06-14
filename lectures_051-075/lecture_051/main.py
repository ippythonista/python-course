from decimal import Decimal

print(' FLOAT IMPRECISION '.center(50, '='))

print('\n' + ' FLOAT '.center(50, '~'))
n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print(f'{n3=}')
print(f'{n3=:.2f}')

print('\n' + ' ROUND '.center(50, '~'))
r1 = round(n3, 1)
r2 = round(n3, 2)
r3 = round(n3, 3)

print(f'{r1=} - {type(r1)=}')
print(f'{r2=} - {type(r2)=}')
print(f'{r3=} - {type(r3)=}')

print('\n' + ' DECIMAL '.center(50, '~'))
d1 = Decimal('0.1')
d2 = Decimal('0.7')
d3 = d1 + d2
print(f'{d3} - {d3=} - {type(d3)=}')
