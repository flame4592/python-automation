import random

randNo = random.randint(1, 10)
print ( " guess a number between 1 to 10 ")


while True:
    guess = int(input())
    
    if guess == randNo:
        print ( " you guessed it right")
        break
    
    elif guess > randNo:
            print ( " your guess is higher, try again ")
    else:
            print ( " your guess is lower, try again " )