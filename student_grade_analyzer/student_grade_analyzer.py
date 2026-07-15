maths_marks = float(input("Enter maths_marks: "))
physics_marks = float(input("Enter physics marks: "))
chemistry_marks =float(input("Enter chemistry marks: "))

def calculate_average  (maths_marks , physics_marks , chemistry_marks):
    average= (maths_marks + physics_marks + chemistry_marks)/3
    return average
print("================")
average = calculate_average(maths_marks , physics_marks , chemistry_marks)
print ("Average marks: " , average)
if average>=90:
   print("Grade A+")
elif average>=80:
  print("Grade A")
elif average>=70:
  print("Grade B")
elif average>=60:
   print("Grade C")
elif average>=50:
   print("Grade D")
else:
   print("Grade F")

print("================")