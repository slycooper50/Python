print("Enter the number to find how many digits in it and print the sum of digits.")
x = str(input())
r=x[::-1]
count = 0
q = 0
for s in x:
    q = q + int(x[count])
    count = count + 1
print("The number of digits is: " + str(count))
print("The sum of the digits is: " + str(q))
print(r)
