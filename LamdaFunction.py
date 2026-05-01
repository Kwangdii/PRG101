
name= input("Enter your name:")
greet= lambda x: print("Hello, " + x)
greet(name)

even_odd= lambda x: "Even" if x%2 == 0 else "odd"
num=int(input("Enter a number:"))
print(even_odd(num))

arith= lambda x,y: (x+y, x-y, x*y, x/y)
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
result= arith(num1,num2)

mylist=[1,2,3,4,5,6]
even= filter(lambda x: x%2==0, mylist)
print(list(even))

mylist=[1,2,3,4,5,6]
double = map(lambda x: x*2, mylist)
mynewlist=list(double)
print(mynewlist)
division= map(lambda x: x//2, mynewlist)
print(list(division))

from functools import reduce
mylist=[1,2,3,4]
multiply= reduce(lambda x,y: x*y, mylist)
print(multiply)





