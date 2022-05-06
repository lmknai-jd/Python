# This is a guess the number game. :)

import random

print ('hello, what is your name?')
name = input ()

print ('lets play "Guess the Number." ' + name + ', I am thinking of a number between 0 and 50.')
secretNumber = random.randint (1, 50)

for guessesTaken in range (1,11):
    print ('take a guess.')
    guess = int(input () )

    if guess < secretNumber :
        print ('hmm...too low.')
    elif guess > secretNumber:
        print ('woah. too high.')
    else:
        break # this condition is for the correct answer.

if guess == secretNumber:
    print ('You got it,' + name +'!' + ' You guessed my number in ' + str(guessesTaken) + ' tries. Good job!')
else:
    print ('Aw man. You couldnt guess my number...')
    print ('The number I was thinking of was ' +  str(secretNumber))

           



