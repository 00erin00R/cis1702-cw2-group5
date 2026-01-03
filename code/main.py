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
    