import json

INVENTORY_FILE = "inventory.json"
SALES_FILE = "sales.json"

def load_inventory(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError: 
        print(f"Error: '{filename}' file not found.")
        return []
    except json.JSONDecodeError: 
        print(f"Error: Failed to decode JSON from '{filename}'.")
        return []


def save_inventory(filename, inventory):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)


def load_sales(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(filename, "w") as file:
            json.dump([], file, indent=4)
        return []
    except json.JSONDecodeError: 
        print(f"Error: Failed to decode JSON from '{filename}'.")
        return []

def save_sales(filename, sales):
    with open(filename, "w") as file:
        json.dump(sales, file, indent=4)
        print(f"Sales data saved to '{SALES_FILE}'.")


def display_inventory(inventory):
    print("\nAvailable Items:")
    for item in inventory:
        print(
            f"ID: {item['id']} | "
            f"Name: {item['name']} | "
            f"Price: ${item['price']} | "
            f"Quantity: {item['quantity']}"
        )


def purchase_item(inventory):
    inventory = load_inventory(INVENTORY_FILE)
    sales = load_sales(SALES_FILE)

    display_inventory(inventory)

    try:
        item_id = int(input("\nPlease enter the ID of the item you want to purchase: "))
        amount = int(input("What is the ammount you want to purchase?: "))
    except ValueError:
        print("Invalid input, numbers only.")
        return

    if amount <= 0:
        print("The ammount of the item you want to buy must be greater than zero.")
        return

    for item in inventory:
        if item["id"] == item_id:
            if item["quantity"] < amount:
                print("Not enough in stock.")
                return
            
            elif item["quantity"] == 0:
                print(f"Sorry, {item["name"]} is out of stock. ")
                return

            item["quantity"] -= amount

            sale = {
                "ID": item["id"],
                "Name": item["name"],
                "Quantity": amount,
                "Total_price": item["price"] * amount
            }

            sales.append(sale)

            save_inventory(INVENTORY_FILE, inventory)
            save_sales(SALES_FILE, sales)

            print("Purchase successful!")
            return

    print("Item not found, try again.")


if __name__ == "__main__":

    inventory = INVENTORY_FILE
    sales = SALES_FILE

    while True:
        purchase_item(inventory)

        while True:
            repeat = input("\nPurchase another item? (y/n): ")
            if repeat == "y":
                print("Ok, What else would you like to buy?")
                break
            elif repeat == "n":
                print("Alright, goodbye.")
                exit()
            else:
                print("'y' or 'n' only, try again.")