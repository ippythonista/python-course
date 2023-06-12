print(' CODE COMPLEXITY '.center(50, '='))

speed = int(input('Speed (km/h): '))
position = int(input('Position (km): '))

MAX_SPEED = 60
RADAR_POSITION = 110
RADAR_RANGE = 10

print('\n' + ' EXAMPLE '.center(50, '~'))
above_speed_limit = speed > MAX_SPEED
passed_radar = abs(RADAR_POSITION - position) <= RADAR_RANGE
is_fined = above_speed_limit and passed_radar

if above_speed_limit:
    print('Your speed is OVER the limit!')

if passed_radar:
    print('You passed the radar!')

if is_fined:
    print("You're FINED!")
