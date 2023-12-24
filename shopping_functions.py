import pandas as pd
from colored import fg, attr, bg

def create_menu():
    """Prints the menu for user interaction."""
    print("\nEnter 'add' to add items to basket.")
    print("Enter 'remove' to remove items from basket.")
    print("Enter 'view' to view basket contents.")
    print("Enter 'stock' to see today's inventory.")
    print("Enter 'checkout' to checkout.")
    print("Enter 'exit' to exit game.\n")

def user_interaction(items_to_buy, items_for_sale, starting_cash, file_name):
    """Takes user input for the main menu."""
    while True:
        create_menu()
        user_choice = input("Enter your selection: ")
        if user_choice == "add":
            add_item(items_to_buy, items_for_sale)
        elif user_choice == "remove":
            remove_item(items_to_buy)
        elif user_choice == "view":
            view_basket(items_for_sale, items_to_buy, starting_cash)
        elif user_choice == "stock":
            inventory(items_for_sale)
        elif user_choice == "checkout":
            checkout(items_for_sale, items_to_buy, starting_cash, file_name)
            break
        elif user_choice == "exit":
            break
        else:
            print("Invalid Input")

def add_item(items_to_buy, items_for_sale):
    """Adds items to the users basket. Items are saved to the variable 
    'items_to_buy'. Items are compared to the variable 'items_for_sale' 
    to check that they exist.
    """
    while True:
        item = input("Enter an item to add (or 'done' to finish): ")
        
        if item.lower() == 'done':
            break
        
        # Check if user input is valid from items_for_sale
        if item not in items_for_sale:
            # If not, throw error and ask for input again
            print("Invalid item. Please enter a valid item from the list.")
            continue
        
        # Check that user is inputting positive, whole numbers
        while True:
            try:
                quantity = int(input(f"Enter the quantity for {item}: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be a valid number.")
                break # break out of loop if input is valid number
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")

        # Check if the item already exists in the dictionary
        if item in items_to_buy:
            # If it does, update the quantity
            items_to_buy[item] += quantity
        else:
            # If it doesn't, add a new entry
            items_to_buy[item] = quantity

    return list(items_to_buy.items())

def remove_item(items_to_buy):
    """Takes user input to remove items from users basket."""
    # Prints the contents of the users basket in item - quantity format.
    print(
        f"""Your basket contains: {' | '.join(f'{key} x {value}' 
        for key, value in items_to_buy.items())}"""
        )
    
    while True:
        # Asks user input for item to be removed
        item_to_remove = input("Enter an item to remove (or 'done' to finish): ")

        if item_to_remove.lower() == 'done':
            break

        # Compares user input with current basket to check if the item is 
        # in the basket
        if item_to_remove in items_to_buy:
            while True:
                try:
                    # Takes user input for quantity of items to remove
                    quantity_to_remove = int(input(
                        f"Enter the quantity to remove for {item_to_remove}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Check if the entered quantity is less than or equal to the 
            # existing quantity.
            if quantity_to_remove <= items_to_buy[item_to_remove]:
                # If quantity is valid then removed that number of items from
                # the users basket and prints successful message to screen
                items_to_buy[item_to_remove] -= quantity_to_remove
                print(f"Removed {quantity_to_remove} {item_to_remove}(s).")
                # If resulting quantity = 0 then item is removed from the list
                if items_to_buy[item_to_remove] == 0:
                    del items_to_buy[item_to_remove]
            else:
                # If user input is greater than current quantity then error
                # message is displayed and asks for user input again
                print(
                    f"Cannot remove more than {items_to_buy[item_to_remove]} "
                    f"{item_to_remove}(s)."
                    )
        else:
            # If user input doesn't match items in the list then prints an
            # error message and asks for input again.
            print(
                f"{item_to_remove} is not in the list. "
                f"Please enter a valid item."
                )

    return items_to_buy

def view_basket(items_for_sale, items_to_buy, starting_cash):
    """Prints the current basket contents to screen along with the users
    remaining cash.
    """
    total_cost = calculate_cost(items_for_sale, items_to_buy)
    # Print the user shopping list and total cost
    print("\nYour basket contains:")
    for item, quantity in items_to_buy.items():
        print(f"{item} x {quantity}")
    print(f"Total Cost: ${total_cost}")
    remaining_cash = (starting_cash - total_cost)
    if remaining_cash < 0:
        print(
            f"""{fg('black')}{bg('red')}Warning: Total cost (${total_cost}) 
            exceeds your budget of ${starting_cash}. Please adjust your 
            shopping list.{attr('reset')}"""
            )
        print(
            f"{fg('black')}{bg('red')}Remaining cash: "
            f"${remaining_cash}{attr('reset')}\n"
            )
    else:
        print(
            f"{fg('black')}{bg('35')}Remaining cash: "
            f"${remaining_cash}{attr('reset')}\n")


def calculate_cost(items_for_sale, items_to_buy):
    """Calculates the cost of items in the basket."""
    total_cost = 0
    user_shopping_list = []

    # Iterates through the list of items in basket, compares the items with
    # the matching items in items_for_sale, multiplies the qty by the price
    # and then sums the total cost
    for item, quantity in items_to_buy.items():
        if item in items_for_sale:
            price, _ = items_for_sale[item]
            total_cost += price * quantity
            user_shopping_list.append((item, quantity, price))
        else:
            # if there are any invalid items in basket they are ignored
            continue 
    return total_cost


def checkout(items_for_sale, items_to_buy, starting_cash,file_name):
    """Runs the calculate_cost and _nutrition_score functions, then calculates
    the remaining cash score to return the users final score for this game.
    """
    total_cost = calculate_cost(items_for_sale, items_to_buy)
    nutrition_score = (nutrition_points(items_for_sale, items_to_buy))
    remaining_cash = (starting_cash - total_cost)
    # remaining cash calculation
    dollar_score = (100 - remaining_cash)
    final_score = (nutrition_score + dollar_score)
    # checks if user has enough cash to proceed to checkout
    if remaining_cash < 0:
        print(
            f"Total cost ${total_cost} exceeds your budget of ${starting_cash}."
            f" Remove some items from your cart.")
        return
    else:
        print(f"Your final score is {final_score}pts")
    # runs the high_scores function
    high_scores(file_name, final_score)
    

def high_scores(file_name, final_score):
    """ Takes the users final score and compares it to the high scores file to
    determine if user makes it into the high scores.
    """
    # Checks that the file exists and loads it into a DataFrame
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'Score'])

    # Check if the user's score is higher than the lowest score in the CSV file
    if len(df) < 5 or df.empty or final_score > df['Score'].min():
        print(
            f"{fg('black')}{bg('cyan')}Congratulations! You made it to the high"
            f" score!{attr('reset')}"
            )
        # Prompts the user for their name
        user_name = input("Enter your name: ")

        # Add the new score to the DataFrame
        new_score = pd.DataFrame({'Name': [user_name], 'Score': [final_score]})
        df = pd.concat([df, new_score], ignore_index=True)

        # Sorts the DataFrame by scores in descending order
        df = df.sort_values(by='Score', ascending=False)

        # Keeps only the top 5 scores
        df = df.head(5)

        # Writes the updated high scores back to the CSV file
        df.to_csv(file_name, index=False)
        print("High scores updated!")
    else:
        print(
            f"{fg('black')}{bg('red')}Sorry, you didn't make the high scores."
            f"{attr('reset')}"
            )
    print("\nHigh Scores:")
    print(df.to_string(index=False))


def inventory(items_for_sale):
    """Prints the availaible inventory to screen."""
    print(f"\n{fg('black')}{bg('35')}Today our stock is:{attr('reset')}")
    for item, (price, nutrition) in items_for_sale.items():
        print(
            f"{fg('black')}{bg('35')}{item} ${price} N:{nutrition}"
            f"{attr('reset')}"
            )


def nutrition_points(items_for_sale, items_to_buy):
    """Calculation for nutrition points."""
    total_points = 0
    user_shopping_list = []

    # Iterates through items_to_buy and compares them to items_for_sale
    for item, quantity in items_to_buy.items():
        if item in items_for_sale:
            # Access the second element of the tuple (points)
            _, points = items_for_sale[item] 
            total_points += points * quantity
            user_shopping_list.append((item, quantity, points))
        else:
            # Continues if any false values are found in the list
            continue 
    return total_points

