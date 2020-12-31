def squaretriangule():
    select = int(input("1) Square\n2) Triangle\n\nEnter a number: "))

    if select == 1:
        
        square = int(input("Enter the length of one of its sides: "))
        print("Square Area {0}".format(square**2))
        
    elif select == 2:
        
        base = int(input("Enter the base of triangle: "))
        height = int(input("Enter the height of triangle: \n\n"))

        print("Triangle Area {0}".format(base * height /2))
    else:

        print("Choose the correct answer")
        


squaretriangule()