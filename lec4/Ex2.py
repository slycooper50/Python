def funct(x):
    print("Enter a number to test whether it is a perfect number.")
    list1=[]
    for i in range(x):
        if x % (i+1)== 0:
            list1.append(i+1) 
    del list1[-1]   
    if x == sum(list1):
        print("It is a perfect number.")
    else:
        print("No")
