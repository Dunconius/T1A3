from colored import fg, attr, bg
import random
import pandas as pd
from shopping_functions import add_item, remove_item, view_basket, checkout, inventory, create_menu, user_interaction

file_name = "high_scores.csv"

try:
    # open in read mode
    highscore = open(file_name, "r")
    highscore.close()
    # if throw error, means file doesn't exist
    # if no error, means file exists
except FileNotFoundError:
    # now we know file doesn't exist
    # create the file
    highscore = open(file_name, "w")
    # insert the first line into the file
    highscore.write("Name,Score\n")
    highscore.close()


# starting item variables
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
print(f"{fg('black')}{bg('35')}{attr('bold')}\nWelcome to Food ‘n’ Things. We sell all the food, and most of the things!{attr('reset')}")
print(f"The rules of the game are simple. Buy food to feed your family. \nYour score is determined by how close to 0 your final cash amount is,\nand how many nutrition points you earn from the food you bought.{attr('reset')}")
input("\nHit enter to get started.")
inventory(items_for_sale)
print(f"You have ${starting_cash} in your wallet. What would you like to buy today?{attr('reset')}")

# Call the user interaction function
user_interaction(items_to_buy, items_for_sale, starting_cash, file_name)

# End of game
print(f"\n{fg('0')}{bg('35')}Thank you for shopping at food 'n' things.{attr('reset')}\n")