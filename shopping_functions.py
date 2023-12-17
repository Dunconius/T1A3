# function that gets user to input list items 

def add_item(items_to_buy):

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
        if item in items_to_buy:
            # If it does, update the quantity
            items_to_buy[item] += quantity
        else:
            # If it doesn't, add a new entry
            items_to_buy[item] = quantity

    return list(items_to_buy.items())

# function that gets user to remove list items 
def remove_item(items_to_buy):
    print("Current items with quantities:", items_to_buy)

    while True:
        item_to_remove = input("Enter an item to remove (or 'done' to finish): ")

        if item_to_remove.lower() == 'done':
            break

        # Check if the item is in the dictionary
        if item_to_remove in items_to_buy:
            while True:
                try:
                    quantity_to_remove = int(input(f"Enter the quantity to remove for {item_to_remove}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Check if the entered quantity is less than or equal to the existing quantity
            if quantity_to_remove <= items_to_buy[item_to_remove]:
                items_to_buy[item_to_remove] -= quantity_to_remove
                print(f"Removed {quantity_to_remove} {item_to_remove}(s).")
                if items_to_buy[item_to_remove] == 0:
                    del items_to_buy[item_to_remove]
            else:
                print(f"Cannot remove more than {items_to_buy[item_to_remove]} {item_to_remove}(s).")
        else:
            print(f"{item_to_remove} is not in the list. Please enter a valid item.")

    return items_to_buy

# function to view items in basket 
def view_basket(items_for_sale, items_to_buy, starting_cash):
    total_cost = calculate_cost(items_for_sale, items_to_buy)
    # Print the user shopping list and total cost
    print("\nUser Shopping List:")
    for item, quantity in items_to_buy.items():
        print(f"{item}: {quantity} units")
    print(f"Total Cost: ${total_cost}")
    remaining_cash = (starting_cash - total_cost)
    if remaining_cash < 0:
        print(f"Warning: Total cost (${total_cost}) exceeds your budget of ${starting_cash}. Please adjust your shopping list.")
    print(f"Remaining cash: ${remaining_cash}\n")


def calculate_cost(items_for_sale, items_to_buy):
    total_cost = 0
    user_shopping_list = []

    for item, quantity in items_to_buy.items():
        if item in items_for_sale:
            price = items_for_sale[item]
            total_cost += price * quantity
            user_shopping_list.append((item, quantity, price))
        else:
            continue # add to basket should deny any false values being added
    return total_cost  # Return the total cost

def checkout(items_for_sale, items_to_buy):
    total_cost = 0
    user_shopping_list = []

    for item, quantity in items_to_buy.items():
        if item in items_for_sale:
            price = items_for_sale[item]
            total_cost += price * quantity
            user_shopping_list.append((item, quantity, price))
        else:
            print(f"Item '{item}' not found in the list of items for sale.")

    return user_shopping_list, total_cost

def inventory(items_for_sale):
    print("Today our stock is:")
    for item, price in items_for_sale.items():
        print(f"{item} ${price}")