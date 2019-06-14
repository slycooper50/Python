print("Enter the total electricity units to find the bill.")
x = float(input())
if x >= 0 and x <= 50:
    y =  x*0.5
    print("The bill is: " + str(y + 0.2*y))
elif x > 50 and x <= 150:
    y = 25+(x-50)*0.75
    print("The bill is: " + str(y + 0.2*y))
elif x > 150 and x <= 250:
    y = 100+(x-150)*1.2
    print("The bill is: " + str(y + 0.2*y))
elif x > 250:
    y = 220+(x-250)*1.5
    print("The bill is: " + str(y + 0.2*y))
else:
    print("Enter a valid number.")
