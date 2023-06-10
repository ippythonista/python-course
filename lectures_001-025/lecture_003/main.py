print(' FUNCTION: PRINT '.center(50, '='))

print('\n' + ' DEFAULT '.center(50, '~'))
print(1, 2, 3)
print(4, 5, 6)

print('\n' + ' SEP '.center(50, '~'))
print(1, 2, 3, sep=' ')
print(1, 2, 3, sep=" ")
print()

print(4, 5, 6, sep='-')
print(4, 5, 6, sep=' and ')

print('\n' + ' END '.center(50, '~'))

# CRLF => \r\n
# LF => \n
print(1, 2, 3, end='\r\n')
print(4, 5, 6, end='\n')
print()

print(1, 2, 3, end=' and ')
print(4, 5, 6, end=".\n")
print(123, 456)

print('\n' + ' SEP & END '.center(50, '~'))
print(1, 2, 3, sep=' * ', end=' = ')
print(6)

print(1, 2, 3, end=' = ', sep=' * ')
print(6)

# NameError
# Print()
