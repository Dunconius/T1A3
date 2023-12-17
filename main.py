import random
from shopping_functions import add_item, remove_item, view_basket, checkout, inventory

# starting item definitions -----------------------------------------------
items_for_sale = {
    "milk": 4,
    "eggs": 8,
    "bread": 2,
    "meat":17
}

items_to_buy = {}

starting_cash = random.randint(87, 129)
total_cost = 0

# user menu -----------------------------------------------
print("Welcome to Food ‘n’ Things. We sell all the food, and most of the things.")
inventory(items_for_sale)
print(f"You have ${starting_cash} in your wallet. What would you like to buy today?")

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
        add_item(items_to_buy)
    elif (user_choice == "remove"):
        remove_item(items_to_buy)
    elif (user_choice == "view"):
        view_basket(items_for_sale, items_to_buy, starting_cash)
    elif (user_choice == "checkout"):
        checkout(items_for_sale, items_to_buy, starting_cash)
    elif (user_choice == "exit"):
        print("Thanks for shopping at Food ‘n’ Things!")
    else:
        print("Invalid Input")