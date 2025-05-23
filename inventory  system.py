inventory = {
    "Guns": 10,
    "Swords": 15,
    "Knives": 8
}

def display_inventory():
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_inventory():
    item = input("Enter the item name to update: ")
    if item in inventory:
        try:
            new_quantity = int(input(f"Enter new quantity for {item}: "))
            inventory[item] = new_quantity
            print(f"{item} updated to {new_quantity}.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"{item} not found in inventory.")

while True:
    print("\nArsenal Menu")
    print("1. Display Arsenal")
    print("2. Update Arsenal")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        print("Exiting .")
        break
    else:
        print("Invalid choice. Please try again.")