import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "its 1"
    elif answerNumber == 2:
        return "its 2"
    elif answerNumber ==3:
        return "its 3"
        
r = random.randint(1, 3)
fortune = getAnswer(r)
print (fortune)        

        
        
def helllo ():
    print ("hey")
    print ("ahoy")

def hello(name):
    print ( "hello " + name)
    
# hello ("alice")

