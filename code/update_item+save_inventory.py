#update_item function for updating items selected by the user
def update_item(inventory):
    try:
        item_id = int(input("Enter the ID of the item to update: "))
        for item in inventory:
            if item["id"] == item_id:
                print("Item found:")
                print(f"the selected item is {item["name"]}")

                print("\nWhat would you like to update?")
                print("1 - Item name")
                print("2 - Item price")
                print("3 - Item stock")

                choice = int(input("Enter your choice (1-3)- "))

                if choice == 1:
                    new_name = input("Please enter the updated name - ")
                    item["name"] = new_name
                elif choice == 2:
                    new_price = float(input("Please enter the upadted price - "))
                    item["price"] = new_price
                elif choice == 3:
                    new_stock = int(input("Please enter the updated stock amount - "))
                    item["stock"] = new_stock
                else:
                    print("Invalid option.")
                    return
                print("Item updated successfully.")
                print("Updated item:", item)
                return
            
        print("Item with that ID was not found.")
        
    except ValueError:
        print("Invalid input. Please enter numbers only.")


#save_inventory function to save updates made to the inventory on a updated file
def save_inventory(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Updated inventory saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving inventory to '{filename}': {e}")
