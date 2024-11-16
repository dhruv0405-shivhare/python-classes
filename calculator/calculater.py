while True:
    print ("1.add\n  2.sub\n  3.div\n  4.multi\n 5.off")
    n = int(input("enter what you want"))
    x = [1,2,3,4,5]
    if n in x:
        x = int(input("enter 1st value"))
        y = int(input("enter 2nd value"))

        if n==1:
            print ("addition = " , x + y)  

        elif n==2:
            print ("subtract = " , x - y) 

        elif  n==3:
            print ("division = " , x / y) 

        elif n==4:
            print ("multipication = " , x * y) 

    elif n==5: 
        break
    else:
        print("enter right no.")