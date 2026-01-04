def add_item(inventory):
    name = input("Enter item name: ")
    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid price or quantity.")
        return
    item = {
        "id": get_next_id(inventory),
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory.append(item)
    print("Item added successfully.")

