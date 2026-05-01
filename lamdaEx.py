#to check a number is positive, negative or zero
number= float(input("Enter a number:"))
check= lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(check(number))    