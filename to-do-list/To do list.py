print("------To Do List------")
print("1. Add to List")
print("2. Delete List")
print("3. View list")
print("4. Quit")

while True:
    option = input("Select an option: ")
    open_file = None
    if option == "1":
        open_file = open("to_do_list.txt", "a")
        open_file.write(input("What would you like to add to your to do list: ")+ "\n")
        open_file.close()
    elif option == "2":
        open_file = open("to_do_list.txt", "r")
        lines = open_file.readlines()
        
        list_number = 0
        for list in open_file:
            list_number += 1
            print(list_number,")", list.rstrip("\n") ) #prints list and removes the indent at the end of the list

        remove_line = input("What would you like to remove from the list?: ")
        remove_line = int(remove_line)
        
        del lines[remove_line - 1]
        open_file.close()

    elif option == "3":
        open_file = open("to_do_list.txt", "r")
        lines = open_file.readlines()
        for line in lines:
            print(line)

        





