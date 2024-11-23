name = input("Enter the username : ")
if name == "adarsh":
    print (" hi adarsh enter pass ")
    attempts = 0
    while attempts < 3 :           
            password = input("enter the password : ")
            if password == "flame":
                print ( "welcome")
                break
            else:
                attempts +=1
                print ( " wrong pass ")
                if attempts == 3:
                    print( "Too many wrong passa")
                    
else:
    print ("who are you")