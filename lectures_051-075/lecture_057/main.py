import re
import sys

print(' EXERCISE 14 '.center(50, '='))

cpf = input('Enter a CPF: ')
clean_cpf = re.sub(r'\D', '', cpf)

invalid_size = len(clean_cpf) != 11
invalid_sequence = clean_cpf[0] * len(clean_cpf) == clean_cpf

if invalid_size or invalid_sequence:
    print(f'{cpf=} is an INVALID CPF!')
    sys.exit(0)

verify_cpf = clean_cpf[:9]

for start in range(10, 12):
    sum_digits = 0

    for i, factor in enumerate(range(start, 1, -1)):
        sum_digits += int(verify_cpf[i]) * factor

    mod11 = sum_digits * 10 % 11

    verify_cpf += str(mod11) if mod11 < 10 else '0'

if verify_cpf == clean_cpf:
    print(f'{cpf=} is a VALID CPF!')
else:
    print(f'{cpf=} is an INVALID CPF!')
