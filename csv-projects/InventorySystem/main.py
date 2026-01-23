from inventory import InventorySystem
from error_handling import int_checker

inventory_system = InventorySystem()

def menu():

    while True:
        inventory_system = InventorySystem()
        print("================= Menu =================")
        print("1) Add to Inventory System")
        print("2) View Inventory System")
        print("3) Remove from Inventory System")
        print("4) Filter from Inventory System")
        print("5) End Program")
        
        menu_choice = int_checker("Choose an option: ")
        if menu_choice == 1:
            inventory_system.add_inventory_system()
        elif menu_choice == 2:
            inventory_system.view_inventory_system()
        elif menu_choice == 3:
            inventory_system.remove_inventory_system()
        elif menu_choice == 4:
            inventory_system.filter_inventory_system()
        elif menu_choice == 5:
            print("Program has ended.")
            break
        else:
            print("Invalid Option Choice.")

menu()