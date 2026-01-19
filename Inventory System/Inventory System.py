import csv

# Error Handeling Functions.
def int_checker(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Use Number.")

def round_checker(prompt):
    while True:
        try:
            answer = float(input(prompt)) 
            answer = round(answer, 2)
            return answer
        except:
            print("Enter Number") 
            

def input_checker(prompt):
    while True:
        answer = input(prompt)
        if answer != "":
            return answer
        else:
            print("Cannot leave blank.")  
                      
# Class
class Item:
    def __init__(self, quantity, item, price):
        self.quantity = quantity
        self.item = item
        self.price = price

class InventorySystem:
    def __init__(self):
        self.inventory_system_list = []
# Load CSV if there and add data too list. If not keep list empty
        try:
            with open("InventorySystemData.csv", "r") as f:
                old_data = csv.DictReader(f)
                self.inventory_system_list.extend(old_data)
        except FileNotFoundError:
            inventory_system_list = []
        
    def add_inventory(self):
        many_items = int_checker("How many items would you like to add?: ")
        
        for i in range(many_items):
            quantity = int_checker("Enter Quantity: ")
            item = input_checker("Enter Item: ")
            price = round_checker("Enter Price: £")
#  Turn Class into Raw Data            
            class_item = Item(quantity, item, price)
            class_item_dict = {
                
                "quantity": class_item.quantity,
                "item": class_item.item,
                "price": class_item.price
            }
            self.inventory_system_list.append(class_item_dict)
            
            if quantity > 1:
                print("----------------------------------------------------------------")
                print(f"You have added {quantity} {item}s, which is £{price} per {item}")
                print("----------------------------------------------------------------")
            else:
                print("----------------------------------------------------------------")
                print(f"You have added {quantity} {item}, which is £{price} per {item}")
                print("----------------------------------------------------------------")
# FINSIHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH                
        with open("InventorySystemData.csv", "w") as f:
            csv.DictReader
        
        #     menu()
    def view_inventory(self):
        for line in self.inventory_system_list:
            quantity = line["quantity"]
            item = line["item"]
            price = line["price"]
            
            print(f"Quantity: {quantity} | Item: {item} | Price: £{int(price)}")
            
            

inventory_system = InventorySystem()

inventory_system.add_inventory()

