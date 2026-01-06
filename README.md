Project Brief 1: Command-Line Inventory Management
System

Project Goal: Create a command-line application to help a small business owner
track product inventory. The system must allow the user to add, view, update, and
remove stock items, and save the data between sessions.

Key Functional Requirements:

[x] The application must store inventory data in a file (e.g., inventory.json or
inventory.csv).

[x] On startup, the program must load existing data from the file.

[x] The user must be presented with a clear menu to perform actions (e.g., Add
Item, View Stock, Update Item, Search, Save & Exit).

[x] Add Item: Allow the user to add a new product with a unique ID, name, price,
and quantity.

[x] View Stock: Display a formatted table of all products in the inventory.

[x] Update Item: Allow the user to find an item by its ID and update its name,
price, or quantity.

[x] Search: Allow users to search for an item by name and display its details.

[x] The program must handle errors gracefully (e.g., invalid input, item not
found).

Possible Extensions:

[x] Generate a low-stock report for items with a quantity below a certain
threshold.

[] Add functionality to track sales, reducing the quantity of an item when sold.

[] Implement a more advanced search feature (e.g., by price range).

● Marking Focus Areas: Robust file handling for data persistence, effective use of data
structures (lists of dictionaries), clear user interface and input validation, and
comprehensive testing of all core CRUD (Create, Read, Update, Delete) operations.

