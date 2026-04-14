student_list = [] #store student names
student_age = set() #store student ages
student_grade = set() #store student grades
student_dict = {} #store student details with name as key and a tuple of age and grade as value

#Student 1
student_list.append ("Karma Wangdi")
student_age.add (22)
student_grade.add ("A")
student_dict ["Karma Wangdi"] = (22, "A")

#Student 2
student_list.append ("Dorji")
student_age.add (21)
student_grade.add ("A")
student_dict ["Pholang"] = (21, "A")

#Student 3
student_list.append ("Jetsun Pema")
student_age.add (19)
student_grade.add ("A")
student_dict ["Jetsun Pema"] = (19, "A")

#Student 4
student_list.append ("Yesel Delsey")
student_age.add (25)
student_grade.add ("A")
student_dict ["Body"] = (25, "A")

#Search for a student
search_name = input("Enter the name of the student to search: ")
if search_name in student_list:
    print(f"Student found! The age of the '{search_name}' is '{student_dict[search_name][0]}' and the grade is '{student_dict[search_name][1]}'")
else:
    print("Student not found!")


