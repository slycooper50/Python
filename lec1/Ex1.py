import datetime
print ("What is your date of birth? DD/MM/YYYY\n")
dob = input ()
year = dob[6:]
currentDT = datetime.datetime.now()
print ("You are " + str(currentDT.year - int(year)) + " years old.")


