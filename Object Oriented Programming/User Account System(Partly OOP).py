# ---- Menu ----
# 1. Save a Password
    # Ask what the user passwords for (Facebook / Instagram)
    # Ask Username / Email
    # Ask Password
    # Stores in Json file
# 2. View all Passwords
    # Prints all password saved
# 3. Delete Password
    #  Select what they want to delete
# 4 .Exit Program

import json
    


def save_password():
    try:
        loops = int(input("How many accounts you wanna save: "))
    except:
        print("Enter number...")
        
    new_account = []
    
    for i in range(loops):
        social = input("Social: ")
        username_email = input("Username / Email: ")
        password = input("Password: ")
# Stores Class in variable and Appends to list
        account = UserAccountSystem(social, username_email, password)
# Put data in dictionary to turn into raw data (to store in json)        
        account_dict = {
            "social": account.social,
            "username_email": account.username_email,
            "password": password
            }
        
        new_account.append(account_dict)
# Json File
    try:
        with open("UserAccountSystem.json", "r") as json_file:
          old_data = json.load(json_file) 
          old_data["account"].extend(new_account)
        
        with open("UserAccountSystem.json", "w") as json_file:
          json.dump(old_data, json_file, indent = 4) 
          
    except FileNotFoundError:
        with open("UserAccountSystem.json", "w") as json_file:
            json.dump({"account": new_account}, json_file, indent = 4)
        
                  
def view_password():
# Read file / store in variable
    with open("UserAccountSystem.json", "r") as json_file:
        UserAccountSystem_data = json.load(json_file)
    
    counter = 0
# loops through each line
    for account in UserAccountSystem_data["account"]:
        counter += 1
        print(f"{counter}) Social: {account['social']} || Username / Email: {account['username_email']} || Password: {account['password']}")


def delete_password():
       with open("UserAccountSystem.json", "r") as json_file:
        UserAccountSystem_data = json.load(json_file)
    
        counter = 0
# loops through each line
        for account in UserAccountSystem_data["account"]:
            counter += 1
            print(f"{counter}) Social: {account['social']} || Username / Email: {account['username_email']} || Password: {account['password']}")
# Getting option from user
        index = int(input("Delete the data to the corresponding number: "))
        index = index - 1
        
        print(f"You have deleted: ---- {UserAccountSystem_data["account"][index]} ----")
        del UserAccountSystem_data["account"][index]
        
        with open("UserAccountSystem.json", "w") as json_file:
            json.dump(UserAccountSystem_data, json_file, indent = 4)
            
            
def end_program():
    print("Goodbye...")
    
class UserAccountSystem:
    def __init__(self, social, username_email, password):
        self.social = social
        self.username_email = username_email
        self.password = password

##############################################################################   
userAccountSystemList_view = []

print("------ Menu ------")
print("1. Save Password")
print("2. View All Passwords")
print("3. Delete Password")
print("4. Exit")

while True:
    print("---------------------------")
    menu_choice = int(input("Select an Option: "))
    if menu_choice == 1:
        save_password()
    elif menu_choice == 2:
        view_password()
    elif menu_choice == 3:
        delete_password()
    elif menu_choice == 4:
        end_program()
        break
    else:
        print("You have inputted Invalid Choice")

