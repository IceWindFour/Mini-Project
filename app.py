import functions as pf
from functions import Menu

pf.read_file()
main_menu_input = Menu().main_menu()

while True:
    if main_menu_input == "1":
        products_menu_input = Menu().products_menu()
    
        if products_menu_input == "0":
            print("Returning to Main Menu")
            main_menu_input = Menu().main_menu()

        elif products_menu_input == "1":
            pf.product_print()

        elif products_menu_input == "2":
            pf.new_product()

        elif products_menu_input == "3":
            pf.updating_product()

        elif products_menu_input == "4":
            pf.delete_product()
      

    elif main_menu_input == "2":
        order_menu_input = Menu().order_menu()

        if order_menu_input == "0":
            print("Returning to Main Menu")
            main_menu_input = Menu().main_menu()

        elif order_menu_input == "1":
            for i in pf.orders:
                print(i)
    
        elif order_menu_input == "2":
            pf.customer_inputs()
            # still need to improve the function

        elif order_menu_input == "3":
            pf.update_status()

        elif order_menu_input == "4":
            pf.update_order()
            # doesn't meet the spec yet

        elif order_menu_input == "5":
            pf.delete_order()
    
    elif main_menu_input == "3":
        courier_menu_input = Menu().courier_menu()
        
        if courier_menu_input == "0":
            print("Returning to Main Menu")
            main_menu_input = Menu().main_menu()
        
        elif courier_menu_input == "1":
            for courier in pf.couriers:
                print(courier)
        
        elif courier_menu_input == "2":
            pf.new_courier()
        
        elif courier_menu_input == "3":
            pf.updating_courier()
        
        elif courier_menu_input == "4":
            pf.delete_courier()

    elif main_menu_input == "0":
        pf.write_file()
        print("bye")
        exit()

    else:
        print("Not a vaild input")
        main_menu_input = Menu().main_menu()