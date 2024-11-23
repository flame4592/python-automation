while True:
    print ( "hello")
    name = input(" enter the name : ")
    if name == 'adarsh' :
        continue
        print ( "hello adarsh ")
        password = input( "enter the pass : ")
        if password != "fish":
            print ( " access granted ")
            break
        
    else:
        print ( "acess denied")