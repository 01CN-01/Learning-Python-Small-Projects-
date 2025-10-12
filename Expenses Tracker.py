print("--------Expenses Tracker--------")
print("1. Add new expense")
print("2. View all expenses")
print("3. See the total")
print("4. Quit")

def expense_tracker():

    open_file_expenses = open("expenses.txt", "a")
    total = 0

    while True:
        option = input("Select an option: ")
        if option == "1":
            food = input("Add an food: ")
            price = input("Add a price: : ")
            food_price = food + "-" + price + "\n"
            open_file_expenses = open("expenses.txt", "a")
            open_file_expenses.write(food_price)
            open_file_expenses.close()
        elif option == "2":
            open_file_expenses = open("expenses.txt", "r")
            for line in open_file_expenses:
                line = line.strip()
                food, price = line.split("-")
                print("Food: ", food, "Price: ", price)
        elif option == "3":
            open_file_expenses = open("expenses.txt", "r")
            for i in open_file_expenses:
                i = i.strip().replace("£","")
                food, price = i.split("-")
                total += float(price)
            print("Total: £", round(total, 2))
        elif option == "4":
            print("Goodbye")
            break
        else:
            print("Invalid Option")

        again = input("Would you like to continue? (yes / no): ").lower()
        if again == "no":
            print("goodbye")
            break


expense_tracker()




        





        

