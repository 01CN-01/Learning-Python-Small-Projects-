
def notes_program():
    print("---------- Notes ----------")
    print("1. Add to Notes (Add)")
    print("2. View Notes (View)")
    while True:
        option = input("Select an Option: ").lower()

        if option == "1" or option == "add":
            open_file = open("notes.txt","a")
            open_file.write(input("Add to notes: ")+ "\n")
            open_file.close()
            break

        elif option == "2" or option == "view":
            open_file = open("notes.txt","r")
            print(open_file.read())
            open_file.close()
            break
        else:
            print("Invalid Option")

#Notes
notes_program()

#Continue Program?
print("1. Yes")
print("2. No")
quit_program = input("Continue? ").lower()

if quit_program == "1" or quit_program == "yes":
    notes_program()
else:
    print("Goodbye")


    