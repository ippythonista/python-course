print('\n' + ' EXCEPTION HANDLING: TRY/CATCH '.center(50, '~'))

number = input("Enter a number: ")

print('\n' + ' IF/ELSE '.center(50, '~'))
if number.isdigit():
    integer = int(number)
    print(f'{integer=}')
else:
    print(f'{number=} CANNOT be converted to INT.')

print('\n' + ' TRY/CATCH '.center(50, '~'))
try:
    print(f'{number=}')
    integer = int(number)
    print(f'{integer=}')
    priint(f'{number=}')
except:
    print(f'{number=} CANNOT be converted to INT.')
