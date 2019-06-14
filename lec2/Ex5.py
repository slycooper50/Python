print("Enter the number to sum the even numbers in between.")
x = int(input())
q=0
if x % 2 != 0:
    x = x-1
    
for s in range(x+1):
    if s %2 ==0:
        q = q+s
print ("The sum is: " + str(q)) 
