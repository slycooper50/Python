print("Enter the statement to analyse.")
x = input()
s=0
r=0
o=0
inx = 0
t=0
for i in range(len(x)):
    if x[i] == " " : 
        s=s+1

list1 = list(x.split())
list2 = list(x)


for e in range(len(list1)):
    inx = inx + 1
    if list1[e].isdigit() : t = t+1
    if list1[e].isalpha() : r = r+1
length = len(list1)
print("The number of spaces is:" + str(s))
print("The number of words is:" + str(r))
print("The number of digits is:" + str(t))
print("The number of special characters is:" + str(len(list1)-r-t+s))
