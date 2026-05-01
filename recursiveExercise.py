'''d'ef function(x,y):
    if x==0:
        return y
    else:
        return function(x-1,y+x)
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
print("The value of function({}, {}) is: {}".format(x,y,function(x,y)))
print()'''

def pattern(n):
    if n == 1:
        print("*")
        return
    pattern(n - 1) # n-1 means that the function will call itself with a smaller value of n until it reaches 1
    print("* "*n) #*n means that it will print n number of * with a space in between each *


# Take input from user
n = int(input("Enter a number: "))

# Call the function
pattern(n) #This will print the pattern of stars based on the input number n. For example, if n=3, it will print: 