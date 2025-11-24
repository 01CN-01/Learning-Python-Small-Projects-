# --------Course--------
# Subject
# Teacher 
# Student List

# Computer Science → Mr. Neizer
# Math → Mrs. Patel
# English → Ms. Parker
# Geography → Mr. Luvaluka
# Art → Mrs. Patel

# --------Student--------
# Name
# Age
# Gender
# Course

# --------Program--------
# Add student
# Remove student
# Add student to courses
# Remove students from courses


print("Student Course Tracker")
print("1. Add student")
print("2. Remove Student")
print("3. Add student to course")
print("4. Remove student from course")
print("5. Exit")
student_list = []
class Student:
    def add_student():
        try:
            loop_students = int(input("How many students would you like to add?: "))
        for i in range(loop_students):
            student_name = input("Name:")
            student.name = student_name

            student_age = input("Age: ")
            student.age = student_age

            student_gender = input("Gender: ")
            student.gender = student_gender


while True:
    option = int(input("Choose an option: "))
    if option == 1:
        add_student()
    elif option == 2:
        remove_student()
    elif option == 3:
        student_add_course()
    elif option == 4:
        student_remove_course()
    elif option == 5:
        end_program()
        break
    else:
        print("Invalid Option...")
