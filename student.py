# Creating and writing into the file
file = open("Dummy_students_namelist", "w")
file.write("STUDENT NAME OF BEd ICT I\n")
file.write("------------------------------\n")
file.write("karma wangdi,08250269\n") 
file.write("jetsun pema,08240342\n")
file.write("dorji tshering,08250266\n")
file.write("sonam tobgay,08250273\n")
file.write("arjun,08250290\n")
file.close()

print("------------------------------")
print("File created successfully")
print("------------------------------")

# Reading the file
file = open("Dummy_students_namelist", "r")
data = file.readlines()
file.close()

# Asking user to enter student name
name = input("Enter student name: ")
found = False

# Checking whether the student exists
for line in data:

    if name in line:
        print("------------------------------")
        print("Student Found")
        print("------------------------------")
        print("Name:", line.split(",")[0])
        print("Student ID:", line.split(",")[1])
        
        found = True

if found == False:
    print("------------------------------")
    print("Student not found")
    print("------------------------------")