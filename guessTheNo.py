import random, sys

randNo = random.randint(1, 10)
print ( " guess a number between 1 to 10 ")


while True:
    guess = int(input())
    
    if guess == randNo:
        print ( " you guessed it right")
        sys.exit()
    
    elif guess > randNo:
            print ( " your guess is higher, try again ")
    else:
            print ( " your guess is lower, try again " )
            
            
# # This is a guess the number game.
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')

# # Ask the player to guess 6 times.
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())

#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break    # This condition is the correct guess!

# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + '
# guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))