import random

# starting item definitions -----------------------------------------------
items_for_sale = {
    "milk": 4,
    "eggs": 8,
    "bread": 2,
    "meat":17
}

items_with_quantities = {}

cash = random.randint(87, 129)

# function that gets user to input list items -----------------------------------------------
def add_item(items_with_quantities):

    while True:
        item = input("Enter an item to add (or 'done' to finish): ")
        
        if item.lower() == 'done':
            break
        
        try:
            quantity = int(input(f"Enter the quantity for {item}: "))
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
            continue

        # Check if the item already exists in the dictionary
        if item in items_with_quantities:
            # If it does, update the quantity
            items_with_quantities[item] += quantity
        else:
            # If it doesn't, add a new entry
            items_with_quantities[item] = quantity

    return list(items_with_quantities.items())


# function that gets user to remove list items -----------------------------------------------
def remove_item(items_with_quantities):
    print("Current items with quantities:", items_with_quantities)

    while True:
        item_to_remove = input("Enter an item to remove (or 'done' to finish): ")

        if item_to_remove.lower() == 'done':
            break

        # Check if the item is in the dictionary
        if item_to_remove in items_with_quantities:
            while True:
                try:
                    quantity_to_remove = int(input(f"Enter the quantity to remove for {item_to_remove}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Check if the entered quantity is less than or equal to the existing quantity
            if quantity_to_remove <= items_with_quantities[item_to_remove]:
                items_with_quantities[item_to_remove] -= quantity_to_remove
                print(f"Removed {quantity_to_remove} {item_to_remove}(s).")
                if items_with_quantities[item_to_remove] == 0:
                    del items_with_quantities[item_to_remove]
            else:
                print(f"Cannot remove more than {items_with_quantities[item_to_remove]} {item_to_remove}(s).")
        else:
            print(f"{item_to_remove} is not in the list. Please enter a valid item.")

    return items_with_quantities


def view_basket(items_with_quantities):
    print("Your basket contains the following:")
    for item, quantity in items_with_quantities.items():
        print(f"{quantity} {item}.")
    

# user menu -----------------------------------------------
# print("Welcome to Food ‘n’ Things. We sell all the food, and most of the things.")
# print(f"You have ${cash} in your wallet.")
# print("What would you like to buy today?")

def create_menu():
    print("\nEnter 'add' to add items to basket")
    print("Enter 'remove' to remove items from basket")
    print("Enter 'view' to view basket contents")
    print("Enter 'checkout' to checkout")
    print("Enter 'exit' to exit")
    # choice = input("Enter your selection: ")
    # return choice

user_choice = ""
# create_menu()
while user_choice != "exit":
    user_choice = create_menu()
    user_choice = input("Enter your selection: ")
    if (user_choice == "add"):
        add_item(items_with_quantities)
    elif (user_choice == "remove"):
        remove_item(items_with_quantities)
    elif (user_choice == "view"):
        view_basket(items_with_quantities)
    elif (user_choice == "checkout"):
        checkout()
    elif (user_choice == "exit"):
        print("Goodbye!")
    else:
        print("Invalid Input")