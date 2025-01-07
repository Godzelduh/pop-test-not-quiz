def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    place_order = True
    while place_order:
        # Loop through the menu dictionary, extracting the food category and
        # the options for each category
        menu_selection_number = 1
        for category, items in menu.items():
            print(f"{category}:")
            # Loop through the options for each food category, extracting the
            # meal and the price
            for meal, price in items.items():
                # Print the menu item number, food category, meal, and price
                print(f"{menu_selection_number}. {meal} - ${price:.2f}")
                # Update the menu selection number
                menu_selection_number += 1

        # Ask customer to input menu item number
        menu_selection = input("Type menu number: ")

        # Update the order list using the update_order function
        # Send the order list, menu selection, and menu items as arguments
        order = update_order(order, menu_selection, menu_items)

        # Ask the customer if they would like to order anything else
        # Let the customer know if they should type 'n' or 'N' to quit
        keep_ordering = input("Would you like to keep ordering? (N) to quit: ")

        # Write a conditional statement that checks if the customer types
        # 'n' or 'N'
        if keep_ordering.lower() == 'n':
            # Since the customer decided to stop ordering, thank them for
            # their order
            print("Thank you for your order.")

            # Use a list comprehension to create a list called prices_list,
            # which contains the total prices for each item in the order list:
            # The total price for each item should multiply the price by quantity
            prices_list = [item["Price"] * item["Quantity"] for item in order]

            # Create an order_total from the prices list using sum()
            # and round the prices to 2 decimal places.
            order_total = round(sum(prices_list), 2)

            # Write a break statement or set the condition to False to exit
            # the ordering loop
            place_order = False

    # Return the order list and the order total
    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # Check if the customer's input string can be converted 
    # to an integer and prints an error message if it does not
    if not menu_selection.isdigit():
        print("Invalid selection. Please enter a valid menu number.")
        return order

    # Convert the menu selection to an integer
    menu_selection = int(menu_selection)

    # Write a conditional statement that checks if the customer's input is 
    # an item on the menu and prints an error message if it is not
    if menu_selection not in menu_items:
        print("Invalid selection. Please enter a valid menu number.")
        return order

    # Store the item name as a variable
    item_name = menu_items[menu_selection]["Item name"]

    # A prompt (input) to the customer that prints the name of the 
    # menu item to the user and asks the quantity they would like to order.
    # Store the return in a quantity variable
    quantity = input(f"How many {item_name} would you like to order? ")

    # Write a conditional statement that checks if the input quantity 
    # can be converted to an integer, then converts it to an integer. 
    # Have it default to 1 if it does not.
    if not quantity.isdigit():
        quantity = 1
    else:
        quantity = int(quantity)

    # Add a dictionary with the item name, price, and quantity to the 
    # order list. Use the following names for the dictionary keys:
    # "Item name", "Price", "Quantity"
    order.append({
        "Item name": item_name,
        "Price": menu_items[menu_selection]["Price"],
        "Quantity": quantity
    })

    # Return the updated order
    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt
    #print(receipt)

    # Loop through the items in the customer's receipt
    for item in receipt:
        # Store the dictionary items ("Item name", "Price", "Quantity") as variables
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # Print the receipt line using the print_receipt_line function
        # send the item name, price, and quantity as separate arguments
        print_receipt_line(item_name, price, quantity)