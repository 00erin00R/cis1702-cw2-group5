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
