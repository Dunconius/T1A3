from colored import fg, attr, bg
import pandas as pd
import random
from shopping_functions import inventory, user_interaction

file_name = "high_scores.csv"

try:
    # Check if the file exists
    with open(file_name, "r") as highscore:
        pass
except FileNotFoundError:
    # Create the file
    with open(file_name, "w") as highscore:
        highscore.write("Name,Score\n")

# Define inventory items_for_sale
items_for_sale = {
    "milk": (4, 5),
    "eggs": (8, 6),
    "bread": (2, 1),
    "meat": (17, 8)
    }

items_to_buy = {}

starting_cash = random.randint(87, 129)

total_cost = 0


# Main program
print(
    f"{fg('black')}{bg('35')}{attr('bold')}\nWelcome to Food ‘n’ Things. "
    f"We sell all the food, and most of the things!{attr('reset')}"
    )
print(
    f"The rules of the game are simple. Buy food to feed your family. \nYour "
    "score is determined by how close to 0 your final cash amount is,\nand how "
    f"many nutrition points you earn from the food you bought.{attr('reset')}"
    )
input("\nHit enter to get started.")
inventory(items_for_sale)
print(f"You have ${starting_cash} in your wallet. What would you like to buy "
      f"today?{attr('reset')}")

# Call the user interaction function
user_interaction(items_to_buy, items_for_sale, starting_cash, file_name)

# End of game
print(f"\n{fg('0')}{bg('35')}Thank you for shopping at Food 'n' Things."
      f"{attr('reset')}\n")