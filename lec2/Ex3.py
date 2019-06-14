print("Enter the year to test whether it is a leap year.")
x = float(input())
if x % 4 == 0 and x % 100 != 0:
    print("The year is a leap year.")
elif x % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
