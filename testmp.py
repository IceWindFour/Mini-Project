from unittest.mock import patch
from unittest import mock
from functions import products, orders, couriers
from functions import Menu, new_product, product_print, order_print, courier_print, read_file

def test_main_menu_inputs():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().main_menu()
    assert result == "1"

def test_products_menu_inputs():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().products_menu()
    assert result == "1"

def test_order_menu_inputs():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().order_menu()
    assert result == "1"

def test_courier_menu_input():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().courier_menu()
    assert result == "1"

read_file()

@patch("builtins.print")
def test_product_print(mock_print):
    product_print()
    for product in products:
        last_product = f'{product["Name"]}: ${product["Price"]}'
    mock_print.assert_called_with(last_product)

@patch("builtins.print")
def test_order_print(mock_print):
    order_print()
    mock_print.assert_called_with(orders[-1])

@patch("builtins.print")
def test_courier_print(mock_print):
    courier_print()
    mock_print.assert_called_with(couriers[-1])    

# @patch("builtins.input")
# def test_new_product(mock_input):
#     # mock_args = ["1"]
#     # with mock.patch("builtins.input") as mock_input:
#     #     mock_input.side_effect = mock_args
#     #     result = new_product()
#     result = new_product()
#     assert result == mock_input
#     # assert result == products[-1]

# def test_couea_menu_input():
#     arg1 = "Spoon"
#     arg2 = "5"
#     mock_args = arg1 + arg2
#     with mock.patch("builtins.input") as mock_input:
#         mock_input.side_effect = mock_args
#         result = new_product()
#     assert result == products[-1]