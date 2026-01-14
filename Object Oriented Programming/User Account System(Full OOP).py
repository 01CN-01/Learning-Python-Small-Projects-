import json


def int_checker(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid. Use a Number")


def input_checker(prompt):
    while True:
        answer = input(prompt)
        if answer != "":
            return answer
        else:
            print("Cannot Leave Blank.")


def email_format(prompt):
    while True:
# E.g  "hello@gmail.com" = "hello", "gmail.com"
        email_check = input(prompt)
        part = email_check.split("@")   
# After splitting "@" should be 2 parts before and after "@"
        if len(part) != 2:
            print("Invalid.")
        elif part[0] == "" or part[1] == "":
            print("Invalid.")
        else:
            return email_check
            
def menu():
    print("-----------Menu-----------")
    print("1) Add Account")
    print("2) Remove Account")
    print("3) View All Accounts")
    print("4) Search filter")
    print("5) Exit")

    while True:
        option_menu = int_checker("Choose an Option: ")
        if option_menu == 1:
            my_useraccountsystem.add_account()
            break
        elif option_menu == 2:
            my_useraccountsystem.remove_account()
            break
        elif option_menu == 3:
            my_useraccountsystem.view_all_accounts()
            break
        elif option_menu == 4:
            my_useraccountsystem.search_filter()
            break
        elif option_menu == 5:
            my_useraccountsystem.end_program()
            break
        else:
            print("Choose out of 1, 2, 3, 4, 5")
            
###########################################################################
class User:
    def __init__(self, social, firstname, lastname, email, password,):
        self.social = social
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

class UserAccountSystem:
    def __init__(self):
        self.account_list = []
# Load data start of program
        try:
            with open("User_Accounts.json", "r") as f:
                    old_data = json.load(f)
                    self.account_list.extend(old_data["user_account"])
        except FileNotFoundError:
            self.account_list = []
            
            
    
    
    def add_account(self):
        loop = int_checker("How many users do you want to add?: ")
        for i in range(loop):
            social = input_checker("Enter social name(e.g. Instagram, Facebook): ")
            firstname = input_checker("Enter First Name: ")
            lastname = input_checker("Enter Last Name: ")
            email = email_format("Enter Email Address: ")
# Confirm Password       
            while True:   
                password = input_checker("Enter Password: ")
                password_confirmation = input("Confirm Password: ")
                if password != password_confirmation:
                    print("Password does not match. Re-enter.")
                else:
                    print("You have added an Account.")
                    break
# Assign Variables as Objects.
            user_accounts = User(social, firstname, lastname, email, password)
# Put objects into dictionary so turns into raw data.       
            user_dict ={
                "social": user_accounts.social,
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "password": password
            }
            self.account_list.append(user_dict)
# Write data into Json
            with open("User_Accounts.json", "w") as f:
                json.dump({"user_account": self.account_list}, f, indent = 4)
# Callng Menu            
        while True:
            continue_program = input_checker("Would you like to continue? (Y/N): ").upper()
            if continue_program == "Y":
                menu()
                break
            elif continue_program == "N":
                end_program()
                break
            else:
                print("Invalid option.")
                    
 
    def remove_account(self):
        if len(self.account_list) == 0:
            print("No Account to remove...") 
        else:
            counter = 0
            for account in self.account_list:
                counter += 1
                print(f"{counter})")
                print(f"Social: {account["social"]}")
                print(f"Name: {account["firstname"]} {account["lastname"]}")
                print(f"Email: {account["email"]}")
                print(f"Password: {account["password"]}")
                print("-" * 30)

            while True:
                del_index = int_checker("Select a number corresponding to the User you want to delete: ")
                if del_index <= counter:
                    del_index = del_index - 1
                    del self.account_list[del_index]     
# Write Data in Json
                    with open("User_Accounts.json", "w") as f:
                        json.dump({"user_account": self.account_list}, f, indent = 4)
                    break
                else:
                    print("Outside of Account List Range... ")
# Callng Menu            
            menu()
    
    
    def view_all_accounts(self):
        counter = 0
        
        if len(self.account_list) != 0:
            for account in self.account_list:
                counter += 1
                print(f"{counter})")
                print(f"Social: {account["social"]}")
                print(f"Name: {account["firstname"]} {account["lastname"]}")
                print(f"Email: {account["email"]}")
                print(f"Password: {account["password"]}")
                print("-" * 30)
        else:
            print("No Accounts Found in Database.")
            
        while True:
            continue_program = input_checker("Would you like to continue? (Y/N): ").upper()
            if continue_program == "Y":
                menu()
                break
            elif continue_program == "N":
                end_program()
                break
            else:
                print("Invalid option.")
                           
    
    def search_filter(self):
        print("1) Search from Social")
        print("2) Search from Name")
        
        while True:
            option = int_checker("Select one of the Options: ")
# Filtered Search for SOCIAL
            if option == 1:
                counter = 0
                social_input = input_checker("Enter a name to search by: ")
                
                for account in self.account_list:
                    if account["social"] == social_input:
                        counter += 1
                        print(f"{counter})")
                        print(f"Social: {account["social"]}")
                        print(f"Name: {account["firstname"]} {account["lastname"]}")
                        print(f"Email: {account["email"]}")
                        print(f"Password: {account["password"]}")
                        print("-" * 30)
                    elif counter == 0:
                        print("No Accounts Found.")
# Filtered Search for NAME                        
            elif option == 2:
                counter = 0
                name_input = input_checker("Enter a name to search by: ")
                
                for account in self.account_list:
                    if account["name"] == name_input:
                        counter += 1
                        print(f"{counter})")
                        print(f"Social: {account["social"]}")
                        print(f"Name: {account["firstname"]} {account["lastname"]}")
                        print(f"Email: {account["email"]}")
                        print(f"Password: {account["password"]}")
                        print("-" * 30)
                    else:
                        print("No Accounts Found.")
                        
            while True:
                continue_program = input_checker("Would you like to continue? (Y/N): ").upper()
                if continue_program == "Y":
                    menu()
                    break
                elif continue_program == "N":
                    end_program()
                    break
                else:
                    print("Invalid option.")
        
                
def end_program():
    print("Goodbye")
                
###############################################################
my_useraccountsystem = UserAccountSystem()

menu()

