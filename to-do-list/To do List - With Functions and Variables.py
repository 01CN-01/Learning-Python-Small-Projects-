tasks = []

def add():
    add_list = input("What would you like to add to the list?: ")
    tasks.append(add_list) #adds variable to the list
    print("Your have successfully added it")

def view():
    print("Your lists")
    print(tasks)

def delete():
    print(tasks)
    delete_choice = input("What would you like to delete in your lists? ")
    delete_choice = int(delete_choice)
    del tasks[delete_choice - 1] #deletes that choice they have selected
    print("Your have successfully deleted it")

def exit_program():
    print("Goodbye")

while True:
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Delete Tasks")
    print("4) Quit")
    option = input("What would you like to do?: ")
    option = int(option)
    if option == 1:
        add()
    elif option == 2:
        view()
    elif option == 3:
        delete()
    elif option == 4:
        exit_program()
        break
    else:
        print("You have inputed a invalid option")

