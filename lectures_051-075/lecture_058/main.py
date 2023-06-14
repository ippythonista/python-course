import random

print(' EXERCISE 15 '.center(50, '='))

cpf = None
while cpf is None or cpf[0] * len(cpf) == cpf:
    cpf = f'{random.randrange(0, 10 ** 9):09d}'

for start in range(10, 12):
    sum_digits = 0

    for i, factor in enumerate(range(start, 1, -1)):
        sum_digits += int(cpf[i]) * factor

    mod11 = sum_digits * 10 % 11

    cpf += str(mod11) if mod11 < 10 else '0'

format_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
print(f'CPF: {format_cpf!r}')
