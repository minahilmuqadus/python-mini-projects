maths_marks = float(input("Enter maths_marks: "))
physics_marks = float(input("Enter physics marks: "))
chemistry_marks =float(input("Enter chemistry marks: "))

def calculate_average  (maths_marks , physics_marks , chemistry_marks):
    average= (maths_marks + physics_marks + chemistry_marks)/3
    return average

average = calculate_average(maths_marks , physics_marks , chemistry_marks)
print ("Average marks: " , average)