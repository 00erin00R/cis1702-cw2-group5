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

if __name__ == "__main__":

    inventory = load_inventory('inventory.json') # loads the json file stored as the varial inventory

    print("welcome to the product inventoty system.")
    print("What would you like to do: ")
    print("1 - Add item")
    print("2 - View stock")
    print("3 - Update item")
    print("4 - Search")
    print("5 - save")
    print("6 - exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                print("Add item selected")
                # call add_item()
            elif choice == 2:
                print("View stock selected")
                # call view_stock()
            elif choice == 3:
                print("Update item selected")
                # call update_item()
            elif choice == 4:
                print("Search selected")
                # call search_item()
            elif choice == 5:
                print("Save selected")
                # call save_inventory()
            elif choice == 6:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 6.")

        except ValueError:
            print("Invalid input. Please enter a number (1–6).")

        except Exception as e:
            print("An unexpected error occurred:", e)
