students = [] 
choice = 0
while choice !=3 : 
 print ("--------Welcome-------")
 print ("Select the number for your action type.")
 print ("Press 1 for Adding a new student.")
 print ("Press 2 for Viewing student details.")
 print ("Press 3 to EXIT.")
 choice = int (input("choice?"))
 if choice ==1:
  print ("Enter Student Details.")
  student_id = int (input("Enter student id:")) 
  student_name =  (input("Enter student Name:")) 
  student_age = int (input("Enter student Age:")) 
  student_department = (input("Enter student Department:")) 
  student_cgpa = float (input("Enter student cgpa:")) 


  student = {
    "id": student_id,
    "name" : student_name,
    "age" : student_age,
    "department" : student_department,
    "cgpa" : student_cgpa,
 }
  students.append(student)
  print (student)
 elif choice == 2:
   for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Department:", student["department"])
    print("CGPA:", student["cgpa"])
    print("------------------------")
 elif choice == 3:
    print("Thank you for using Student Management System!")