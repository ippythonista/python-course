print(' EXERCISE 6 '.center(50, '='))

time = input('Enter the current time: ')

if time.isdigit():
    current_time = int(time)
    if current_time < 0 or current_time >= 24:
        print(f'{current_time=} is out of RANGE')
    elif current_time < 12:
        print('Good Morning!')
    elif current_time < 18:
        print('Good Afternoon!')
    else:
        print('Good Night!')
else:
    print(f'{time=} is a  INVALID time format')
