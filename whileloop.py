no_of_student=int(input("Enter the number of students: "))
i=1
student_name={}
while i<=no_of_student:
    name=input("Enter the name of student: ")
    print("The name of the student {} is {}".format(i,name))
    i+=1
    student_name[i]=name
print(student_name)
    
#testing infinite loop
while True:
    print("This is an infinite loop. Press Ctrl+C to stop it.")



#break and continue statement in while loop
for i in range(10):
    if i==5:
        break
    print(i)
print("Loop ended") 

for i in range(4):
    if i==2:
        continue 
    print(i)
print("Loop ended") 
#here the output will be 0,1,3 and the loop will end after that.also the number 2 will be skipped because of the continue statement.
