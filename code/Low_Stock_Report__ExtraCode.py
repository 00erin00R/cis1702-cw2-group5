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

    for item in inventory:
        if item["quantity"] < threshold:
            print(item["id"], "\t", item["name"], "\t", item["price"], "\t", item["quantity"])
            found = True
    if not found:
        print("No items are below the threshold.")