
import json

def program():

    user = []

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

    try:
# If file Exist, merge old and new data and write it.
        with open("user_database.json", "r") as f:
            old_user_data = json.load(f)
            old_user_data["user"].extend(user)

        with open("user_database.json", "w") as f:
            json.dump(old_user_data, f, indent = 4)
# If file doesn't exist write file.
    except FileNotFoundError:
        with open("user_database.json", "w") as f:
            json.dump({"user": user} , f, indent = 4)



def end_program():
    while True:
        yes_no = input("Would you like to continue? (Y/N): ").lower()
        if yes_no == "y":
            program()
        elif yes_no == "n":
            print("Goodbye.")
            break
        else:
            print("Invalid Option") 
    

program()
end_program()





 
        
