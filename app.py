
i = 0

while i < 3:
    guess = int(input('Guess: '))
    if guess == 9:
        print('You win!')
        break
    i += 1
else:
    print('Sorry you failed!')