def add_item():
    user_input_dict = {}

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