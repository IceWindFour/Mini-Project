from unittest.mock import patch
from unittest import mock
from functions import products, orders, couriers
from functions import Menu, updating_courier, update_order,updating_product, new_courier, customer_inputs, new_product, product_print, order_print, courier_print, read_file

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

@patch("builtins.input", side_effect = ["Fanta","4.0","1"])
def test_new_product(mock_input):
    new_product()
    assert products[-1] == {'Name': 'Fanta', 'Price': '4.0'}

@patch("builtins.input", side_effect = ["1","Iron Brew","0.75","1"])
def test_update_product(mock_input):
    updating_product()
    assert products[1] == {'Name': 'Iron Brew', 'Price': '0.75'}

@patch("builtins.input", side_effect = ["Sheikh","The White House","911","234","3"])
def test_new_order(mock_input):
    customer_inputs()
    assert orders[-1] == {'customer_name': 'Sheikh', 'customer_address': 'The White House', 'customer_phone': '911', 'courier': 'Jenna', 'status': 'preparing', 'items': '2,3,4'}

@patch("builtins.input", side_effect = ["1","Matty","Mattys house","074848382","2","562"])
def test_update_order(mock_input):
    update_order()
    assert orders[1] == {'customer_name': 'Matty', 'customer_address': 'Mattys house', 'customer_phone': '074848382', 'courier': 'Patrick', 'status': 'preparing', 'items': '5,6,2'}

@patch("builtins.input", side_effect = ["Nayan","0792131233","1"])
def test_new_courier(mock_input):
    new_courier()
    assert couriers[-1] == {'Name': 'Nayan', 'Phone': '0792131233'}

@patch("builtins.input", side_effect = ["1","Numan","079696969","1"])
def test_update_courier(mock_input):
    updating_courier()
    assert couriers[1] == {'Name': 'Numan', 'Price': '079696969'}

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