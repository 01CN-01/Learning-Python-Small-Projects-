students = {}

#Adding students to list
def add_students():
    name = input("Who would you like to add in the tracker? ").lower()
    students[name] = [] #Adds "name" to list
    print(f"You have added {name} to the tracker.")

def add_grade():
    while True:
        name = input("Whos grades would you like to add on? ").lower()
        if name in students:
            print(f"----Sucessfully found {name}----.")
            many_grades = input(f"How many grades for {name} would you like to add? ")
            many_grades = int(many_grades)
            for i in range(many_grades):
                grade = input("Add their grade into the system: ")
                grade = int(grade)
                students[name].append(grade) #assign grade to specific person
                print(students[name])
                print(f"Added grade {grade} to {name}")
            break
        else:
            print(f"Theres no one who goes by {name} in the database")

def view_grade():
    print("--------------")
    print("1. View everyones grades")
    print("2. View specific persons grade")

    try:
        option = int(input("What option would you like to pick? "))
    except ValueError:
        print("Enter a valid number.")
    
    while True:
        if option == 1:
            print(students)
            break
        elif option == 2:
            name = input("Who's grades would you like to see? ").lower()
            print(f"{name}'s grades: ",students[name])
            break
        else:
            print("Invalid option.")

def calculate_average():
#calculating average
    while True:
        name = input("Who would you like to calculate the average from? ")
        if name in students:
            students_average = sum(students[name]) / len(students[name])
            print(f"{name}'s average is ",students_average) #Total of score / How many scores are there
#Passed or Fail
            if students_average < 50:
                print(f"{name} has failed.")
            else:
                print(f"{name} has passed.")

            break
        else:
            print("Invalid choice.")

def end_program():
    print("Goodbye!")


while True:
    print("---------------------------------")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Grades")
    print("4. Calculate Average")
    print("5. Quit")
    option = input("What option would you like to pick? ")
    option = int(option)
    if option == 1:
        add_students()
    elif option == 2:
        add_grade()
    elif option == 3:
        view_grade()
    elif option == 4:
        calculate_average()
    elif option == 5:
        end_program()
        break
    else:
        print("You have inputted a invalid option")
        break


