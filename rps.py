import random , sys 
print ( " Rock , Paper , Scissor game")

wins = 0 
loss = 0 
tie = 0 

while True:
    print ( "%s Wins, %s Losses, %s Ties " % ( wins , loss  , tie ))
    
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerInput = input()
        if playerInput == "q":
            sys.exit()
        if playerInput not in ("r", "p", "s"):
            print ( "enter a valid input")
            continue
        break
        
    if playerInput  == "r":
        print ("rock versus ")
    if playerInput  == "p":
        print ("paper versus ")
    if playerInput  == "s":
        print ("scissor versus ")
        
    randomNumber = random.randint(1 , 3)
    if randomNumber == 1:
        computerMove = 'r'
        print ( "Rock")
    elif randomNumber == 2:
        computerMove = 'p'
        print ( "Paper")
    elif randomNumber == 3:
        computerMove = 's'
        print ( "Scissor")
        
    