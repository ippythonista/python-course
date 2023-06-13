print(' EXERCISE 11 '.center(50, '='))

SECRET = 'paula'
ABC = 'abcdefghijklmnopqrstuvwxyz'
guessed_letters = ''
guesses = 0
word = '*' * len(SECRET)

while word != SECRET:
    print(word.upper())
    guess = input('Guess a letter: ').lower()
    guesses += 1
    if len(guess) != 1:
        print('Enter one letter')
        continue
    if guess not in ABC:
        print('Enter a letter from the alphabet')
        continue
    if guess in guessed_letters:
        print(f'You already guessed {guess!r}')
        continue
    guessed_letters += guess
    if guess not in SECRET:
        print(f'Sorry no letter {guess!r} found')
        continue

    word = ''
    for letter in SECRET:
        if letter in guessed_letters:
            word += letter
        else:
            word += '*'
else:
    print(f'\nYou guessed {SECRET=} with {guesses} guesses')
