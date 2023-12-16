import random
# this is the counter function import
from collections import Counter
# from shopping_functions import *

items_for_sale = {
    "milk": 4,
    "eggs": 8,
    "bread": 2,
    "meat":17
}

user_input_dict = {}
total_cost = 0
cash = random.randint(87, 129)

def add_item():
    # user_input_dict = {}

    while True:
        item = input("Enter name of item (type 'done' to finish): ")
        if item.lower() == 'done':
            break

        try:
            qty = int(input("Enter the quantity: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    
        user_input_dict[item] = qty
    return user_input_dict
    
        
def remove_item():
    pass

def view_basket():
    print("\nUser Shopping List:")
    for item, quantity, price in user_input_dict:
        print(f"Item: {item}, Quantity: {quantity}, Price per item: ${price}")

    print(f"\nTotal Cost of Selected Items: ${total_cost}")

def checkout():
    pass

def test_function():
    print("test function!!!!")

print("Welcome to Food ‘n’ Things. We sell all the food, and most of the things.")
print(f"You have ${cash} in your wallet.")
print("What would you like to buy today?")

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
        add_item()
    elif (user_choice == "remove"):
        remove_item()
    elif (user_choice == "view"):
        view_basket()
    elif (user_choice == "checkout"):
        checkout()
    elif (user_choice == "exit"):
        print("Goodbye!")
    else:
        print("Invalid Input")