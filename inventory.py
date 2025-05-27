def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for idx, item in enumerate(inventory, 1):
        print(f"{idx}. {item['name']} - Quantity: {item['quantity']}")

def update_inventory(inventory):
    name = input("Enter item name to add/update: ")
    quantity = int(input("Enter quantity: "))
    for item in inventory:
        if item['name'].lower() == name.lower():
            item['quantity'] += quantity
            print(f"Updated {name} quantity to {item['quantity']}.")
            return
    inventory.append({'name': name, 'quantity': quantity})
    print(f"Added new item: {name} with quantity {quantity}.")

if __name__ == "__main__":
    inventory = [
        {'name': 'Apples', 'quantity': 10},
        {'name': 'Bananas', 'quantity': 20},
        {'name': 'Oranges', 'quantity': 15}
    ]
    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Add/Update Item")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            update_inventory(inventory)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")