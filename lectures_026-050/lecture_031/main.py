print(' IDENTITY OPERATORS '.center(50, '='))

something = input("Enter something: ")

print('\n' + ' NONE '.center(50, '~'))
is_valid = something or False
flagged = None
print(f'{is_valid=}')
print(f'{flagged=}')

print('\n' + ' FLAG '.center(50, '~'))

if is_valid:
    flagged = True
    print(f'{something=}')
else:
    print("You didn't enter something!")

if flagged:
    print("You're FLAGGED!")
else:
    print("You're NOT flagged!")

print('\n' + ' IS/NOT IS '.center(50, '~'))
print(f'{flagged=} is None? {flagged is None}')
print(f'{flagged=} is not None? {flagged is not None}')
