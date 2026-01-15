#Python program to allow a user to guess a number untill the guess is right.
import random
print ('Lets Play a Game')
print ('Guess a number between 1 and 10. You win if you guess in 6 attempts!')
secretNumber = random.randint(1,10)

# ask the player to guess 6 times!
for guess in range(6):
    guessedNumber = input()
    if int(guessedNumber) < secretNumber:
        print ('Well, its too low. Try again.')
    elif int(guessedNumber) > secretNumber:
        print ('Well, its too high. Try again.')
    else:
        print ('You win! Guessed number is correct.')
        break

#while int(number) != secretNumber:
#    print ('Nope. Try again!')
#print ('Wohooo!! You guess it right.')

#if int(number) == secretNumber:
#    print ('You guess it right. You Win !!')
#elif int(number) < secretNumber:
#    print ('Well, its too low. Try again.')
#elif int(number) > secretNumber:
#    print ('Well, its too high. Try again.')