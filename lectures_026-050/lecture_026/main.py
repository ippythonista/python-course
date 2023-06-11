print(' STRING SLICING '.center(50, '='))

abc = 'abcdefghijklmnopqrstuvwxyz'

print('\n' + ' [START:STOP] '.center(50, '~'))
print(abc[0:len(abc)])
print(abc[1:-1])

print('\n' + ' [START:] '.center(50, '~'))
print(abc[20:])
print(abc[-6:])

print('\n' + ' [:STOP] '.center(50, '~'))
print(abc[:5])

print('\n' + ' [START:STOP:STEP] '.center(50, '~'))
print(abc[3:16:4])
print(abc[15:2:-4])

print('\n' + ' [::STEP] '.center(50, '~'))
print(abc[::3])
print(abc[::-1])
