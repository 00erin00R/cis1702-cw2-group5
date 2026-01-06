# import the json file so the program can read, write and work with json file
import json

#function to load the inventory.json file
def load_inventory(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError: # if not found the program returns an error message
        print(f"Error: '{filename}' file not found.")
        return []
    except json.JSONDecodeError: # if the json file is broken program returns a different error
        print(f"Error: Failed to decode JSON from '{filename}'.")
        return []

def get_next_id(inventory):
    if not inventory:
        return 1
    return inventory[-1]['id'] + 1
#1
def add_item(inventory):

    while True:
        name = input("Enter item name: ")
        try:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Invalid price or quantity.")

    item = {
        "id": get_next_id(inventory),
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory.append(item)
    print("Item added successfully.")

#2
#view stock by printing all info using for loop in inventory
def view_stock(inventory):
    print("Overall stock: ")
    print("ID\tName\tPrice\tQuantity")
    print("--------------------------------")
    for item in inventory: #uses for loop to search through the quantity value in inventory
        print(item["id"], "\t", item['name'], "\t", item['price'], "\t", item['quantity'])
        if item["quantity"] == 0:
            print(f"Out of stock: {item['name']}")

#3
#changes data for a specific item by searching through by ID,
def update_item(inventory, product_id):
    print(f"Updating item {product_id}:")
    for item in inventory:
        max = len(inventory) #determines how long the data is to find an end point to loop
        counter = 0
        if item["id"] == product_id: #uses if statements to prevent user overwriting data by mistake
            print("Item found:")
            print(f"the selected item is {item['name']}.")

            selection = input("Do you want to update this item's name? Y or N: ")
            if selection == "Y":
                newName = input("Please enter the item's new name: ")
                item["name"] = newName #replaces data with input 
                print(f"the selected item is {item['name']}.")

            selection = input("Do you want to update this item's price? Y or N: ")
            if selection == "Y":
                newPrice = float(input("Please enter new price: "))
                item["price"] = newPrice
                print(f"Changed {item['name']}s price to {item['price']}.")

            selection = input("Do you want to update this item's amount of stock? Y or N: ")
            if selection == "Y":
                amount = int(input("Please enter an amount to update stock by: "))
                item["quantity"] += amount #replates data with input plus initial amount rather than overwriting
                print(f"Restocked {item['name']}. New amount: {item['quantity']}")

        else:
            counter=+1
        if counter == max: #if looped through all data items without finding a match...
            print("This product ID is not valid.")


#4
def search_item(inventory):
    name_search = input("Please enter the name of the item to begin searching: ") # finds item in file

    found = False

    for item in inventory:
        if item["name"].lower() == name_search.lower(): # turns input into lowercase characters to remove errors

            # prints item details to user but only if its found in inventory
            print("Item found:")
            print("(ID)\tName\t\tPrice\tQuantity")
            print("--------------------------------------------")
            print(item["id"], "\t", item["name"], "\t\t", item["price"], "\t", item["quantity"])
            found = True
            break

    if found == False: # if theres no item a message is displayed to the user
        print("There is no item with this name, please try again.")


#5
#save_inventory function to save updates made to the inventory on an updated file (e.g updated_inventory.json)
def save_inventory(filename, inventory):
    try:
        #saves new list
        #uses .w as new file or overwrite
        with open(f"{filename}", "w") as f:
            json.dump(inventory, f, indent=4)
        print(f"Updated inventory saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving inventory to '{filename}': {e}")

#7

#allows input of a value and outputs the related data of all items that are less than provided value
def low_stock_report(inventory):
    try:
        threshold = int(input("Enter low stock threshold: "))
    except ValueError:
        print("Invalid threshold.")
        return
    
    found = False
    print("\nLow Stock Items:")
    print("ID\tName\tPrice\tQuantity")
    print("--------------------------------")

    for item in inventory: #uses for loop to search through the quantity value in inventory
        if item["quantity"] < threshold:
            print(item["id"], "\t", item["name"], "\t", item["price"], "\t", item["quantity"])
            found = True
    if not found:
        print("No items are below the threshold.")


if __name__ == "__main__":

    inventory = load_inventory('inventory.json') #loads the json file and stores as the variable "inventory"

    print("Welcome to the product inventory system.")
    print("What would you like to do: ")
    print("1 - Add item")
    print("2 - View stock")
    print("3 - Update item")
    print("4 - Search")
    print("5 - Save")
    print("6 - Low stock report")
    print("7 - Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))

            if choice == 1:
                print("Add item selected")
                add_item(inventory)
            elif choice == 2:
                print("View stock selected")
                view_stock(inventory)
            elif choice == 3:
                print("Update item selected")
                product_id = int(input("Enter product ID to update: "))
                update_item(inventory, product_id)
            elif choice == 4:
                print("Search selected")
                search_item(inventory)
            elif choice == 5:
                print("Save selected")
                save_inventory("inventory.json", inventory)
            elif choice == 6:
                low_stock_report(inventory)
            elif choice == 7:
                print("Exiting program. Goodbye!")
                break
                
            else:
                print("Invalid option. Please choose a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a number (1-7).")

        except Exception as e:
            print("An unexpected error occurred:", e)
