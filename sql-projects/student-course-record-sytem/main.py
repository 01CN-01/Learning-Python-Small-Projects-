from student_course_record_system import StudentRecordSystem
from error_handling import int_checker

student_record_system = StudentRecordSystem()

print("---------- Student Record System ----------")
print("             1) Add Student")
print("            2) Remove Students")
print("            3) View Students")
print("            4) Exit Program")
print("-------------------------------------------")

while True:
    menu_option = int_checker("Choose an option: ")

    if menu_option == 1:
        student_record_system.add_students()
    elif menu_option == 2:
        student_record_system.remove_students()
    elif menu_option == 3:
        student_record_system.view_students()
    elif menu_option == 4:
        print("Program ended.")
        break