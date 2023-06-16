n1=1 
while n1 == 1: 
    print("\n Welcome to Karan's calculator") 
    print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n") 
    num=int(input("Select any one from the following: ")) 
    if num == 1: 
        x=int(input("Enter first number :")) 
        y=int(input("Enter second number:")) 
        print("Addition of following numbers is : ",(x+y)) 
    elif num==2: 
        x=int(input("Enter first number :")) 
        y=int(input("Enter second number :")) 
        print("Subtraction of following numbers is : ",(x-y)) 
    elif num==3 : 
        x=int(input("Enter first number :")) 
        y=int(input("Enter second number :")) 
        print("Multiplication of following numbers is : ",(x*y)) 
    elif num==4: 
        x=int(input("Enter first number :")) 
        y=int(input("Enter second number :")) 
        print("Division of following numbers is : ",(x/y)) 
    else: 
        print("Wrong Option") 
    n=input("If you want to proceed press 1 \n otherwise press any key ") 
    if n!="1": 
        exit()
    n1=int(n)