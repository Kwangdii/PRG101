print("----------------------------------------------------------------------------------------")
print("Welcome to SCE Library Management System")
print()

Student_name= input("Enter your name:")
print()

Book_Borrowed = float(input("Enter the number of days the book was borrowed: "))
print()

Book_Returned = float(input("Enter the number of days late #0 for same day return:"))
print()

print("----------------------------------------------------------------------------------------")
print("LIBRARY REPORT")
print("----------------------------------------------------------------------------------------")
print()

N= Student_name

print("Student Name: {}".format(N))
print()

B= Book_Borrowed
print(f"Days Borrowed: {B}")
print()

L= Book_Returned
print(f"Days Late: {L}")
print()

if (Book_Returned == 0):
    print("{N} have no fine".format(N=Student_name))
    print()

elif (Book_Returned <= 5):
    print ("Total Fine: Nu.{}".format(Book_Returned*5))
    print()

elif (Book_Returned <= 10):
    print("Total Fine: Nu.{}".format(Book_Returned*10))
    print()

elif (Book_Returned >= 10):
    print("Total Fine: Nu.{}".format(Book_Returned*20))
    print()

if (Book_Borrowed > 30):
    print("WARNING:Library privileges may be restricted")
    print()

print("----------------------------------------------------------------------------------------")