# import the json file so the programme can read, write and work with json file
import json

#function to load the inventory.json file
def load_inventory(filename):

    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError: # if not found the programme returns an error message
        print(f"Error: '{filename}' file not found.")
        return []
    except json.JSONDecodeError: # if the json file is brocken programme returns a different error
        print(f"Error: Failed to decode JSON from '{filename}'.")
        return []

#function to generate a reort based on contents of the json file   
def generate_report(data):

    if not data: # handles empty file
        return 0, None, []

    total_items = sum(item.get("stock", 0) for item in data) # finds the total amount of items in stock using sum
    # finds the highest priced item from the file and creates a small anonymous function to look through the dictionary
    highest_price = max(data, key=lambda item: item.get("price",0)) 
    out_stock = [item for item in data if item.get("stock", 0)== 0] # searches dictionary for any items that are out of stock

    # returns data found
    return total_items, highest_price, out_stock

# function to restock items with given product id
def restock_item(data, product_id, amount):

    for item in data: # goes through items in the dictionary
        if item.get("id")==product_id: # if user input matches an id in the json file
            item["stock"] += amount # add users inputted stock amount
            print(f"Restocked {item['name']}. New stock: {item['stock']}") # print new stock levels
            return True
    
    print(f"Error: Product with ID {product_id} not found.") # prints error if id not found
    return False

# function to save new retocked inventory list
def save_inventory(filename, data):
    
    try:
        with open(filename,"w") as f: # makes new json file that can have data written to it
            json.dump(data, f, indent=1)
    except Exception as e:
        print("error saving file: ", e)

#---------------------------------------------main program------------------------------------------------#

# checks if the file is being run directly by the user, or is it being imported to another file
# if false the code does not run 
if __name__ == "__main__":

    inventory = load_inventory('inventory.json') # loads the json file stored as the varial inventory

    # generates the report using the function generate report on inventory
    total_items, highest_price, out_stock = generate_report(inventory)

    print("\n--- Inventory Report ---")
    print("Your total stock is: ", total_items) # prints total amount of items
    print("Your highest priced item is: ", highest_price.get("name"), "at £", highest_price.get("price")) # displays name and price of the most expensive item
    print("The items out of stock are: ") # prints what items are out of stock

    # gets the name of item if it is out of stock 
    if out_stock:
        for item in out_stock:
            print("-", item.get("name"))
    else:
        print("None")


    #loops to make sure user inputs a number and keeps asking till user enters correct 
    while True:
        try:
            product_id = int(input("Enter the product ID to be restocked: ")) # asks user to input product id
            if any(item.get("id") == product_id for item in inventory): # checks if user input is a ID in the json file
                break # if valid. loop ends
            else:
                print(f"Product ID {product_id} not found. Please try again.") # asks user to try again
        except ValueError:
            print("Invalid ID. Must be a number.") # if input isnt a number error message is displayed

    while True:
        try:
            amount = int(input("Enter the amount to restock: ")) # ask user to enter amount
            if amount < 0: # check if input is more than 0
                print("Amount cannot be negative. Please enter a positive number") # if not error is given and user is asked again
                continue
            break
        except ValueError:
            print("Invalid ID. Must be a number.") # if input isnt a number error message is displayed


    # checks if id is a part of inventory and if its not, save inventory doesnt happen
    if restock_item(inventory, product_id, amount):
        save_inventory("updated_inventory.json",inventory)