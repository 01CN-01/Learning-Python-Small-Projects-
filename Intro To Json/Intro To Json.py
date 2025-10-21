
import json

user = []

def program():
    try:
        loop = int(input("How many users do you want to add?: "))
    except ValueError:
        print("Use numbers...")

    for i in range(loop):
        name = input("Enter name: ")
        age = input("Enter age: ")
        print(f"You have added {name}, who is {age} years old.")
        user_dict = {"name": name, "age": age}
        user.append(user_dict)
# Creates file and dumps user in file
    with open("user_database.json", "w") as f:
        json.dump({"user":user}, f, indent = 4 )

def end_program():
    while True:
        yes_no = input("Would you like to continue? (Y/N): ").lower()
        if yes_no == "yes":
            program()
        elif yes_no == "no":
            print("Goodbye.")
            break
        else:
            print("Invalid Option") 
    

program()
end_program()





 
        
