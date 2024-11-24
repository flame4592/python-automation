import random, sys
for i in range(5):
    print( random.randint(1, 10))
    
while True:
    response= input( "enter exit to exit ")
    if response == "exit":
        sys.exit()
            
print (" exited ")
    
    
    