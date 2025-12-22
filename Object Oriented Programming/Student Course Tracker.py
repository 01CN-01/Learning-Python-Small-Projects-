# --------Student--------
# Name
# Age
# Gender
# Course

# --------Program--------
# Add student
# Remove student
# View Students
# End Program


print("Student Course Tracker")
print("1. Add student")
print("2. Remove Student")
print("3. Add student to course")
print("4. Remove student from course")
print("5. Exit")

def add_student():
    print("---------- Add Student ----------")
    try:
        create_students = int(input("How many students would you like to add? "))
    except:
        print("Enter a number...")
        
    for i in range(create_students):
         first_name = input("Enter First Name: ")
         last_name = input("Enter Last Name: ")
         age = input("Enter Age: ")
         gender = input("Enter Gender: ")
         
         if create_students > 1:
             print("------Enter Other Student------")
         else:
             print("")
         
         student_info = Student(first_name, last_name, age, gender)
         
         student_list.append(student_info)
        
        
def remove_student():
    print("---------- Remove Student ----------")
    counter = 0
    for students_info in student_list:
        counter += 1
        print(counter, ")", students_info)
    
    try: 
        delete_index = int(input("Choose the number corresponding to the student to delete: "))
    except:
        print("Use a number...")
    
    delete_index = delete_index - 1
    print("Data deleted ------->", student_list[delete_index])
    del student_list[delete_index]

def view_students():
    for students in student_list:
        print(students)
    
    print("-------------------")
    

def end_program():
    print("Goodbye.")
    
########################################################################

student_list = []

class Student:
    def __init__(self, firstName, lastName, age, gender):
        self.FirstName = firstName
        self.LastName = lastName
        self.Age = age
        self.Gender = gender
# Takes all values and "stores it"
    def __str__(self):
        return f"{self.FirstName} {self.LastName}, Age: {self.Age}, Gender: {self.Gender}"

while True:
    option = int(input("Choose an option: "))
    if option == 1:
        add_student()
    elif option == 2:
        remove_student()
    elif option == 3:
        view_students()
    elif option == 4:
        end_program()
        break
    else:
        print("Invalid Option...")
