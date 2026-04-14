for i in range(1,4): #outer loop to iterate from 1 to 3
    for j in range(i):
        print(f"Outer Loop iteration {i}, inner loop iteration {j+1}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(4): #it represents the number of rows in the pattern, and it iterates from 0 to 3 (inclusive)
    for j in range(i):#it represents the number of columns in each row, and it iterates from 0 to i-1 (inclusive)
        print("*", end=" ") #end-"" is used for printing the output in the same line without a new line after each print statement
    print() #print a new line after each iteration of the outer loop
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ") #end-"" is used for printing the output in the same line without a new line after each print statement
    print() #print a new line after each iteration of the outer loop

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      
for i in range(6,0,-1):
    for j in range(1,i):
        print("❤️", end=" ") #end-"" is used for printing the output in the same line without a new line after each print statement
    print() #print a new line after each iteration of the outer loop

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
