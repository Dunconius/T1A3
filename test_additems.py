import pytest
from shopping_functions import add_item

# this test tests if user input is correctly stored in the items_to_buy dictionary
@pytest.mark.parametrize("user_input, expected_result", [
    # this one tests that valid user input is saved into the dictionary items_to_buy
    (['milk', '4', 'meat', '5', 'done'], [('milk', 4), ('meat', 5)]),
    # this one tests that invalid input is not saved to the dictionary
    (['invalid_item', 'done'], []),
])

def test_add_item_valid_input(user_input, expected_result, monkeypatch):
    items_to_buy = {}
    items_for_sale = {
        "milk": (4, 5),
        "eggs": (8, 6),
        "bread": (2, 1),
        "meat": (17, 8)
    }

    # Monkeypatch the input function to return values from user_input
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))

    result = add_item(items_to_buy, items_for_sale)

    assert result == expected_result

