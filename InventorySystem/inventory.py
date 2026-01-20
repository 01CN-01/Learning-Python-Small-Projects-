import csv
from error_handling import int_checker, input_checker, round_number

class ItemInfo:
    def __init__(self, quantity, item, price):
        self.quantity = quantity
        self.item = item
        self.price = price
        

class InventorySystem:
    def __init__(self):
        self.inventory_system_list = []
# Adds data to list if file is found. If not keeps list Empty.        
        try:
            with open("inventory_system_data.csv", "r") as csv_file:
                old_data = csv.DictReader(csv_file)
                self.inventory_system_list.extend(old_data)
        except FileNotFoundError:
            self.inventory_system_list = []
    
    def add_inventory_system(self):
        loop = int_checker("How different items would you like too add?: ")
        for i in range(loop):
            quantity = int_checker("Enter Quantity: ")
            item = input_checker("Enter Item: ")
            price = round_number("Enter Price: £")
            
            item_info = ItemInfo(quantity, item, price)
            
            if quantity > 1:
                print("-" * 40)
                print(f"You have added {item_info.quantity} {item_info.item}s, which is £{item_info.price:.2f}")
                print("-" * 40)
            else:
                print("-" * 40)
                print(f"You have added {item_info.quantity} {item_info.item}, which is £{item_info.price:.2f}")
                print("-" * 40)
# Turns into Raw Data          
            inventory_system_dict = {
                
                "Quantity": item_info.quantity,
                "Item": item_info.item,
                "Price": item_info.price
                
            }
 # Adds Dictionary Data into the List         
            self.inventory_system_list.append(inventory_system_dict)

# Adding the Data to the CSV file (newline stops it from creating any blank space.)
        with open("inventory_system_data.csv", "w", newline ="") as csv_file:
            fieldnames = ["Quantity", "Item", "Price"] # Assigns what the fieldnames are going too be
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames) # Tells DictWriter what the headers are going to be.
            writer.writeheader() # Writes the fieldnames at the top of CSV file
            writer.writerows(self.inventory_system_list)
    
    def view_inventory_system(self):
        counter = 0
        found = False
        grand_total = 0
        for iteminfo in self.inventory_system_list:
            counter += 1
            found = True
            print(f"--------{counter}--------")
            print(f"Quantity: {int(iteminfo['Quantity'])}")
            print(f"Item: {iteminfo['Item']}")
            print(f"Price: £{float(iteminfo['Price']):.2f}")
            
            price = float(iteminfo["Price"]) # Convert into Number
            quantity = int(iteminfo["Quantity"]) # Convert into Number
# Prints Total            
            total = price * quantity
            grand_total += total
        print("----------------")    
        print(f"|Total = £{grand_total:.2f}|")
        print("----------------")  
# Couldnt find Data so set       
        if found == False:
            print("No Data Found.")
    
    
    def remove_inventory_system(self):
        counter = 0
        found = False
        
        for iteminfo in self.inventory_system_list:
            counter += 1
            found = True
            print(f"--------{counter}--------")
            print(f"Quantity: {int(iteminfo['Quantity'])}")
            print(f"Item: {iteminfo['Item']}")
            print(f"Price: £{float(iteminfo['Price']):.2f}")
        
        while True:
            del_index = int_checker("Delete data corresponding to the number: ")
# Checks if the delete number is within range of the counter.
            if del_index == 0 or del_index > counter:
                print("Invalid Selection.")
            else:
                del_index -= 1
                specific_data = self.inventory_system_list[del_index]
                
                print("--------------- Successfully deleteted ---------------")
                print(f"Quantity: {specific_data["Quantity"]}")
                print(f"Item: {specific_data["Item"]}")
                print(f"Price: {float(specific_data["Price"]):.2f}")
                
                del self.inventory_system_list[del_index]
# Writes New Data                
                with open("inventory_system_data.csv", "w", newline ="") as csvfile:
                    fieldnames = ["Quantity", "Item", "Price"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.inventory_system_list)
                    break
    
    
    def filter_inventory_system(self):
        # Search Item
        # Search Price
        print("------- Filter -------")
        print("1) Search from Item")
        print("2) Search from Price")
        
        while True:
            filter_option_choice = int_checker("Choose an options: ")
            if filter_option_choice == 1:
                item_filter = input_checker("Enter an Item to search for: ")
                counter = 0
                found = False
                for iteminfo in self.inventory_system_list:
# Filter search to Search by Item
                    if item_filter == iteminfo["Item"]:
                        counter += 1
                        found = True 
                        print(f"--------{counter}--------")
                        print(f"Quantity: {iteminfo["Quantity"]}")
                        print(f"Item: {iteminfo["Item"]}")
                        print(f"Price: {float(iteminfo["Price"]):.2f}") 
# Checks if Item hasnt been found                
                if found == False:
                    print("Item Not Found.")                      
                break
################################################
            elif filter_option_choice == 2:
                price_filter = round_number("Enter a Price to search: £")
                counter = 0
                found = False
                for iteminfo in self.inventory_system_list:
# Filter search to Search by Item
                    if price_filter == float(iteminfo["Price"]):
                        counter += 1
                        found = True
                        print(f"--------{counter}--------")
                        print(f"Quantity: {iteminfo["Quantity"]}")
                        print(f"Item: {iteminfo["Item"]}")
                        print(f"Price: {float(iteminfo["Price"]):.2f}") 
# Checks if Item hasnt been found                
                if found == False:
                    print("Item Not Found.")                      
                break
            else:
                print("Choose from 1 and 2")
                    
            
            
            
            
            
            