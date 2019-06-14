import sys
def funct(x):
    for i in range(2,x-1):
        if x % i != 0 and x != 1 and x != 2:
            continue
        elif x == 1 or x == 2: print("Yes.")
        else : 
            print("No.")
            sys.exit()
    print("Yes.")
