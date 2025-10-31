# Menu 1-3
#------------------
# Add expenses
# read file and load file (if there is no file create one)
# user input
# dump in file
#------------------
# View expenses
#------------------
# Remove expenses
#------------------
# Quit

import json

def add_expenses():
    expenses_list = []

    try:
        loop = int(input("How many items (with prices) would you like to add?: "))
    except:
        print("Enter a number.")

    for i in range(loop):
        item = input("Enter Item: ")
        try:
            price = float(input("Enter Price: £"))
        except:
            print("Use a number.")
        
        print(f"You have added {item}, which is £{price}")
        price_item = {"item": item, "price": price} 
        expenses_list.append(price_item)
        
# File Write
    try:
        with open("expenses_database.json", "r") as f:
            database = json.load(f)
            database["expenses"].extend(expenses_list)

        with open("expenses_database.json", "w") as f:
            json.dump(database, f, indent = 4 )
    except FileNotFoundError:
         with open("expenses_database.json", "w") as f:
            json.dump({"expenses": expenses_list}, f, indent = 4 )




def view_expenses():
    with open("expenses_database.json", "r") as f:
        database = json.load(f)
        amount = 0
        for expenses_data in database["expenses"]:
            print("Item: ",expenses_data["item"], "|| Price: £",expenses_data["price"])
            amount += expenses_data["price"]
        print(f"Total Amount: £{amount:.2f}") # Round to 2 decimal places



def remove_expenses():
    with open("expenses_database.json", "r") as f:
        expenses_data = json.load(f)
        counter = 0
        for expenses in expenses_data["expenses"]:
            counter += 1
            print(f"{counter}) Item: {expenses["item"]} || Price: £{expenses["price"]}")
        
        try:
            remove_data = int(input("Which one do you want to delete?: "))
            remove_data = remove_data - 1
        except:
            print("Use numbers")
        
        print(f"You have removed {expenses_data["expenses"][remove_data]["item"]}, which costs £{expenses_data["expenses"][remove_data]["price"]}")
        del expenses_data["expenses"][remove_data]
# Write file
        with open("expenses_database.json", "w") as f:
            json.dump(expenses_data, f, indent = 4)

    
             
def end_program():
    print("You have ended the program.")




print("**Expenses Tracker**")
print("1. Add Expenses")
print("2. View Expenses")
print("3. Remove Expenses")
print("4. Quit")

expenses_list = []

while True:
    menu_option = input("Select an option: ")

    if menu_option == "1":
        add_expenses()
    elif menu_option == "2":
        view_expenses()
    elif menu_option == "3":
        remove_expenses()
    elif menu_option == "4":
        end_program()
        break
    else:
        print("Invalid Option.")
    
    
