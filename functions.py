import csv
products = []
couriers = []
orders = []
ORDER_STATUS = ("preparing","complete","canceled","delivered","waiting for pickup")

class Menu():
    def main_menu(self):
        main_menu_input = input("""
Main Menu
        
0: Exit
1: Product Menu
2: Order Menu
3: Courier Menu
>>>""")
        return main_menu_input
    
    def products_menu(self):
        products_menu_input = input("""
Products Menu

0: Return To Main Menu
1: Display Products
2: Add New Product
3: Change Product
4: Remove Product
>>>""")
        return products_menu_input

    def order_menu(self):
        order_menu_input = input("""
Order Menu

0: Return To Main Menu
1: Display Orders
2: New Order
3: Order Status
4: Update Order
5: Remove Order 
>>>""")
        return order_menu_input
    
    def courier_menu(self):
        courier_menu_input = input("""
Courier Menu

0: Return To Main Menu
1: Display Couriers
2: Add New Courier
3: Update Courier
4: Remove Courier 
>>>""")
        return courier_menu_input

# main_menu_input = Menu().main_menu
# products_menu_input = Menu()
# order_menu_input = Menu()
# courier_menu_input = Menu()

def read_file():
    with open("couriers.csv","r") as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            couriers.append(row)

    with open("products.csv","r") as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            products.append(row)
    
    with open("orders.csv") as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            orders.append(row)

def write_file():
    with open("couriers.csv", 'w') as file:
        fieldnames = ["Name","Phone"]
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        writer.writeheader()
        for data in couriers:
            writer.writerow(data)
    
    with open("products.csv", 'w') as file:
        fieldnames = ["Name","Price"]
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        writer.writeheader()
        for data in products:
            writer.writerow(data)
    
    with open("orders.csv", 'w') as file:
        fieldnames = ["customer_name","customer_address","customer_phone","courier","status","items"]
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        writer.writeheader()
        for data in orders:
            writer.writerow(data)


def product_print():
    print("Products: Price\n")
    for product in products:
        print(f'{product["Name"]}: ${product["Price"]}')

def new_product():
    new_product = input("New Product Name? ")
    new_product_price = input("New Product Price? ")
    if new_product and new_product_price:
        confirm = int(input(f'Would you like to add {new_product.title()} ${new_product_price}\n1: Yes\n2: No\n'))
        if confirm == 1:
            products.append({
            "Name": new_product.title(),
            "Price": new_product_price,
            })
    print("Products: Price\n")
    for product in products:
        print(f'{product["Name"]}: ${product["Price"]}')

def updating_product():
    for index,product in enumerate(products):
        print(index, product)
    update_product = input("Which product would you like to update? \nUse Index Number")
    if update_product:
        updated_product = input("Product Name? ")
        updated_price = input("Product Price? ")
        if updated_product and updated_price:
            confirm = int(input(f"Updated Product: {updated_product.title()}: ${updated_price}\n1: Yes\n2: No\n"))
            if confirm == 1:
                products[int(update_product)] = {
                'Name': updated_product.title(),
                'Price': updated_price,
                }
    print("Products: Price\n")
    for product in products:
        print(f'{product["Name"]}: ${product["Price"]}')

def delete_product():
    for index,product in enumerate(products):
        print(f'{index}: {product}')
    delete_product = input("Which Product would you like to delete? \nUse Index Number ")
    if delete_product:
        confirm = int(input(f'Would you like to delete {products[int(delete_product)]}\n1: Yes\n2: No\n'))
        if confirm == 1:
            products.pop(int(delete_product))

# dosen't meet spec fully
def customer_inputs():
    customer_name = input("New Customer Name? ")
    customer_address = input("New Customers Address? ")
    customer_phone = input("New Customers Phone Number? ")
    for index,product in enumerate(products):
        print(index, product)
    user_input = int(input("Add Products?\nUse Index Numbers "))
    product_list = []
    product_string = ''
    for i in str(user_input):
        product_list.append(i)
    for _ in product_list:
        product_string = ','.join(product_list)
    for index, courier in enumerate(couriers):
        print(index, courier)
    courier = input("Pick a courier ")
    if customer_name and customer_address and customer_phone and product_string:
        orders.append({
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": couriers[int(courier)]['Name'],
        "status": "preparing",
        "items": product_string,
        })
    for order in orders:
        print(order)

def update_status():
    for index,order in enumerate(orders):
        print(f'{index}: {order}')
    update_order_status = input("\nWhich order status would you like to update?\nUse Index Number ")
    if update_order_status:
        for index,order in enumerate(ORDER_STATUS):
            print(f'{index}: {order}')
        new_status = int(input("New Status?\nUse Index Number "))
        orders[int(update_order_status)]['status'] = ORDER_STATUS[new_status]
    for order in orders:
        print(order)
        
# dosen't meet spec yet
def update_order():
    for index,order in enumerate(orders):
        print(f'{index}: {order}')
    update_order = input("What order would you like to update?\nUse Index Number ")
    if update_order:
        customer_name = input("New Customer Name? ")
        customer_address = input("New Customers Address? ")
        customer_phone = input("New Customers Phone Number? ")
        for index, courier in enumerate(couriers):
            print(index, courier)
        courier = input("Pick a courier ")
        for index,product in enumerate(products):
            print(index, product)
        user_input = int(input("Add Products?\nUse Index Numbers "))
        product_list = []
        product_string = ''
        for i in str(user_input):
            product_list.append(i)
        for _ in product_list:
            product_string = ','.join(product_list)
        if customer_name and customer_address and customer_phone and product_string:
            orders[int(update_order)] = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": couriers[int(courier)]["Name"],
        "status": "preparing",
        "items": product_string}

def delete_order():
    for index,order in enumerate(orders):
        print(f'{index}: {order}')
    delete_order = input("What order would you like to delete?\nUse Index Number ")
    if delete_order:
        confirm = int(input(f'Would you like to delete {orders[int(delete_order)]}\n1: Yes\n2: No\n'))
        if confirm == 1:
            del orders[int(delete_order)]

def new_courier():
    new_courier = input("New Courier? ")
    new_courier_number = input("New Courier Phone Number? ")
    if new_courier and new_courier_number:
        confirm = int(input(f'Would you like to add {new_courier.title()}: {new_courier_number} as a Courier\n1: Yes\n2: No\n'))
        if confirm == 1:
            couriers.append({
            "Name": new_courier.title(),
            "Phone": new_courier_number,
            })
    for courier in couriers:
        print(courier)

def updating_courier():
    # print(couriers)
    for index,courier in enumerate(couriers):
        print(index, courier)
    # for courier in couriers:
    #     print(courier)
    update_courier = input("Which courier would you like to update? \nUse Index Number ")
    if update_courier:
        updated_courier = input("Change courier name? ")
        updated_phone = input("Change Courier Phone Number? ")
        if updated_courier and updated_phone:
            confirm = int(input(f"Updated Courier: {updated_courier.title()}\nUpdated Phone Number: {updated_phone}\n1: Yes\n2: No\n"))
            if confirm == 1:
                couriers[int(update_courier)] = {
                    'Name': updated_courier.title(),
                    'Price': updated_phone,
                }
    for courier in couriers:
        print(courier)

def delete_courier():
    for index,courier in enumerate(couriers):
        print(index, courier)
    delete_courier = input("Which courier would you like to delete? \nUse Index Number ")
    if delete_courier:
        confirm = int(input(f'Would you like to delete {couriers[int(delete_courier)]}\n1: Yes\n2: No\n'))
        if confirm == 1:
            couriers.pop(int(delete_courier))
    for courier in couriers:
        print(courier)