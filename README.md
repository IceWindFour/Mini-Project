# Mini Project Cafe CLI 
- A simple CLI application to track customer orders in a busy cafe.
## Project Background
- My client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders

## Client requirements
The client has given me these requirements for the app. 

- I want to maintain a collection of products and couriers.

- When a customer makes a new order, I need to create this on the
  system.

- I need to be able to update the status of an order i.e: preparing,
  out-for-delivery, delivered.

- When I exit my app, I need all data to be persisted and not lost.

- When I start my app, I need to load all persisted data.

- I need to be sure my app has been tested and proven to work well.

- I need to receive regular software updates

## Current Features
- Data persistence using SQlite3
- Unit and integration testing with pytest
- Implemented CRUD operations
• Create
• Read
• Update
• Delete

## Project Design
The project design was lead by the requirements of the client

```

├── data
│   ├── __init__.py
│   ├── couriers.csv
│   ├── data.db
│   ├── database.py
│   ├── orders.py
│   └── products.csv
├── src
│   ├── __init__.py
│   ├── dbfunctions.py
│   └── functions.py
├── tests
│   ├── __init__.py
│   ├── test_db_courier.py
│   ├── test_db_order.py
│   ├── test_db_product.py
│   └── test_menu.py
├── app.py
└── README.md

```

### Demo update order

```python

def add_new_order(connection):
    customer_name = input("New Customer Name? ")
    customer_address = input("New Customer Address? ")
    customer_phone = input("New Customer Phone number? ")
    display_products_with_id(connection)
    items = input("items? ")
    display_couriers(connection)
    couriers = input("Courier index? ")
    status = 1
    if customer_name and customer_address and customer_phone:
        database.add_order(
            connection,
            customer_name.title(),
            customer_address,
            customer_phone,
            couriers,
            status,
            items,
        )
    display_orders(connection)

```
```python 

INSERT_ORDER = """INSERT INTO orders
(customer_name,customer_address,customer_phone,courier,status,items)
VALUES (?,?,?,?,?,?);"""

def add_order(
    connection, customer_name, customer_address, customer_phone, courier, status, items
):
    with connection:
        connection.execute(
            INSERT_ORDER,
            (customer_name, customer_address, customer_phone, courier, status, items),
        )
```

### Test demo update order

```python 

@patch("src.dbfunctions.display_couriers")
@patch("src.dbfunctions.display_products_with_id")
@patch("builtins.input", side_effect = ["1","Patrick","75 patty street","0712348238","3,1,2",4])
def test_update_orders(mock_input, mock_display_products_with_id, mock_display_courier, setup_database):
    cursor = setup_database
    
    Johns_order = (1, 'John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 1, '1,2,3')
    Patricks_order = (1, 'Patrick', '75 patty street', '0712348238', 4, 1, '3,1,2')

    assert Johns_order in cursor.execute(ALL_ORDERS)
    assert Patricks_order not in cursor.execute(ALL_ORDERS)
    
    update_order(cursor)

    assert Johns_order not in cursor.execute(ALL_ORDERS)
    assert Patricks_order in cursor.execute(ALL_ORDERS)

```

## Meeting project requirements
- I used pytest to ensure core functionality
### Testing 
![image](https://user-images.githubusercontent.com/115299269/203525193-3c08d915-d96d-4443-9ae7-096042994297.png)
