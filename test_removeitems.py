import pytest
from shopping_functions import remove_item

# this test tests if user input is correctly stored in the items_to_buy dictionary
@pytest.mark.parametrize("user_input, expected_result", [
    # this one tests for correct user input
    (['milk', '2', 'done'], {'milk': 3, "eggs": 8}),
    (['milk', '2', 'eggs', '4', 'done'], {'milk': 3, "eggs": 4}),
    # this one tests that invalid input is not saved to the dictionary.
    (['invalid_item', 'done'], {"milk": 5, "eggs": 8}),
])

def test_remove_item_valid_input(user_input, expected_result, monkeypatch):
    items_to_buy = {"milk": 5, "eggs": 8}

    # Monkeypatch the input function to return values from user_input
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))

    result = remove_item(items_to_buy)

    assert result == expected_result

