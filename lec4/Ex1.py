def funct(a):
    mult = 1
    for i in a:
        mult = mult * float(i)
    return print(mult)

print("Enter the list of numbers to be multiplied.")
s = input()
list1 = s.split()
funct(list1)
