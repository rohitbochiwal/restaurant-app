import re
from datetime import datetime
class Customer:
    def __init__(self, name, mobile_number, password, dob, address=""):
        self.name = name
        self.mobile_number = mobile_number
        self.password = password
        self.dob = dob
        self.address = address

class User:
    def __init__(self):
        self.customer_data = []

    def signUp(self):
        name= input("Please enter your name:")
        address= input("Please enter your address or press enter to skip:")
        while True:    
            mobile_number=input("Enter your mobile number(11 digits starting with 0):")
            if not re.match(r'^0\d{10}$', mobile_number):
                print("Invalid mobile number.")
                continue
            
            password = input("Enter your password (Starting with alphabet, followed by @,$ or & and then number):")
            if not re.match(r'^[a-zA-Z][a-zA-Z@#&]+\d$', password):
                print("Inavalid password format. Please use alphabets, special symbols like @,$ or & ,followed by number.")
                continue
            
            confirm_password = input("Confirm your password:")
            
            if password != confirm_password:
                print("Password did not match. Please insert valid password.")
                continue
            
            dob = input("Enter your date of birth in DD/MM/YYYY format: ")
            if not self.dob_validation(dob):
                print("Invalid date format. Please enter in DD/MM/YYYY format.")
                continue
            
            user = Customer(name, mobile_number, password, dob, address)
            self.customer_data.append(user) 
            print("Signup process is completed Successfully!")
    
            break
    def dob_validation(self, dob):
        try:
            format = "%d/%m/%Y"
            dob_date = datetime.strptime(dob, format)
            age = datetime.now().year - dob_date.year
            return age >= 21
        except ValueError:
            return False 

    def logIn(self):
        print("\n")
        print("Enter your details to login:")
        while True:
            mobile_number = input("Enter your mobile number: ")
            password = input("Enter your password: ")

            # Check if user exists
            user_exists = False
            for user in self.customer_data:
                if user.mobile_number == mobile_number and user.password == password:
                    user_exists = True 
                    break
            
            if user_exists:
                print("Login successful.")
                break
                
            else:
                print("Invalid mobile number or password. Please try again.")

class Order:
    def __init__(self):
        self.menu_items1 = {
            "1": {"name": "Sandwich", "price": 40},
            "2": {"name": "Noodles", "price": 60},
            "3": {"name": "Burger", "price": 60},
            "4": {"name": "Pizza", "price": 100},
            "5": {"name": "Roll", "price": 80},
            "6": {"name": "Chicken", "price": 120},

        }
        self.menu_items2 = {
            "8": {"name": "Cold Coffee", "price": 50},
            "9": {"name": "Virgin Mojito", "price": 60},
            "10": {"name": "Iced Tea", "price": 70},
        }
        self.selected_items = []
        self.selected_items2 = []
        self.selected_items3 = []
        self.customer_transaction=[]
        self.customer= Customer("", "", "", "")
    def home_page(self):
        while True:
                    print("\nWelcome to the Home Page!")
                    print("1. Ordering (Dine in, Self-Pickup, Delivery)")
                    print("2. Summary of Transactions")
                    print("3. Logout")
                    option = input("Enter your choice: ")

                    if option == "1":
                        print("Redirecting to Ordering...")
                        self.proceed_ordering()
                        # Implement Ordering functionality
                    elif option == "2":
                        print("Redirecting to Summary of Transactions...")
                        self.display_order_history()
                        # Implement Summary of Transactions functionality
                    elif option == "3":
                        print("Logging out...")
                        break  # Exit the function to log out
                    else:
                        print("Invalid option. Please select a valid option.")
    def proceed_ordering(self):
        while True:
            mode = input("Enter your selected ordering mode (1 for Dine in, 2 for online ordering, 3 for home page): ")
            if mode == "1":
                service_charge = 15
                if service_charge is not None:
                    print(f"Additional 15% service charge will be added.")
                
                self.dine_in_menu()    
                break
            elif mode == "2":
                self.order_online_page()
                print("No additional charges for pick up.")
                break
            elif mode == "3":
                self.home_page()
                # delivery_charge = delivery_mode()
                # if delivery_charge is not None:
                #     print(f"Delivery charge: AUD {delivery_charge}")
                break
            else:
                print("Invalid option. Please select a valid ordering mode.")
    def order_online_page(self):
        while True:
            print("\nOrder Online Page:")
            print("1. Self-Pickup")
            print("2. Home Delivery")
            print("3. Go to Previous Menu")
            option = input("Enter your choice: ")

            if option == "1":
                print("Redirecting to Self-Pickup...")
                self.order_pickup_menu()
                # Implement Self-Pickup functionality
            elif option == "2":
                print("Redirecting to Home Delivery...")
                self.order_online_menu()
                # Implement Home Delivery functionality
            elif option == "3":
                print("Returning to Previous Menu...")
                self.proceed_ordering()
                return  # Exit the function to go back to the previous menu
            else:
                print("Invalid option. Please select a valid option.")


    def dine_in_menu(self):
        order_id = 3333 
        num_persons = int(input("Enter the number of persons: "))
        date_of_visit = input("Enter the date of visit (DD/MM/YYYY): ")
        time_of_visit = input("Enter the time of visit (HH:MM): ")
        type= "Dine in"
        
        # Display food menu
        print("\nFood Menu:")
        print("ID   Name           Price")
        for item_id, item_info in self.menu_items1.items():
            print(f"{item_id}    {item_info['name']}       AUD {item_info['price']}")
        
        # Initialize an empty list to store selected items
        while True:
            choice = input("Enter your choice (ID) or 7 to proceed to Drinks: ")
            
            if choice == "7":
                print("Redirecting to Drinks Menu...")
                break
            elif choice.isdigit() and 1 <= int(choice) <= 6:
                self.selected_items.append(choice)
                print(f"Item {choice} added to your order.")
            else:
                print("Invalid choice. Please enter a valid ID or 7 to proceed to Drinks.")
        
        # Display drinks menu
        print("\nDrinks Menu:")
        print("ID   Name           Price")
        for item_id, item_info in self.menu_items2.items():
            print(f"{item_id}    {item_info['name']}       AUD {item_info['price']}")
        
        while True:
            choice = input("Enter your choice (ID) or 4 to proceed to Checkout: ")
            
            if choice == "4":
                print("Redirecting to Checkout...")
                break
            elif choice.isdigit() and 8 <= int(choice) <= 10:
                self.selected_items.append(choice)
                print(f"Item {choice} added to your order.")
            else:
                print("Invalid choice. Please enter a valid ID or 4 to proceed to Checkout.")
        item_prices = {
        "1": 60,
        "2": 40,
        "3": 60,
        "4": 100,
        "5": 80,
        "6": 120,
        "7": 0,  # Proceed to Drinks
        "8": 50,  # Cold Coffee
        "9": 60,  # Virgin Mohito
        "10": 70, # Iced Tea
    }
        # Calculate total amount
        Food_total = sum(item_prices[item_id] for item_id in self.selected_items)
        if Food_total == 0:
            print("You didn't selected any item.Please order again")
            self.order_online_page()
        else:    
            total_amount = Food_total + (Food_total*0.15)
            print(f"Total amount to be paid: INR {total_amount:.2f} including 15% service charges.")
        
        # Offer payment options
        while True:
            print("\nPlease press 1 to checkout or 2 to cancel your booking:")
            print("1. Checkout..")
            print("2. Cancel order")
            option = input("Enter your choice: ")

            if option == "1":
                print("Your booking is confirmed. Your order id is :",order_id)
                order_id += 1
                order = {
                "total_amount": total_amount,
                "order_id": order_id,
                #"time_of visit": time_of_visit,
                "date":date_of_visit,
                "type":type
            }
                self.customer_transaction.append(order)
                break
            elif option == "2":
                print("Order cancelled.")
                break
            else:
                print("Invalid option. Please select a valid option.")

    def order_online_menu(self):
        order_id = 2222
        date_of_visit = input("Enter the date of order delivery (DD/MM/YYYY): ")
        time_of_visit = input("Enter the time of delivery (HH:MM): ")
        type = "Delivery"
        # Display food menu
        print("\nFood Menu:")
        print("ID   Name           Price")
        for item_id, item_info in self.menu_items1.items():
            print(f"{item_id}    {item_info['name']}       AUD {item_info['price']}")
        
        # Initialize an empty list to store selected items
        while True:
            choice = input("Enter your choice (ID) or 7 to proceed to checkout: ")
            
            if choice == "7":
                print("Redirecting to checkout...")
                break
            elif choice.isdigit() and 1 <= int(choice) <= 6:
                self.selected_items2.append(choice)
                print(f"Item {choice} added to your order.")
            else:
                print("Invalid choice. Please enter a valid ID or 7 to proceed to checkout.")
        

        # Define dictionary for item prices
        item_prices = {
            "1": 60,
            "2": 40,
            "3": 60,
            "4": 100,
            "5": 80,
            "6": 120,
        }
        
        # Calculate total amount
        food_order_amount = sum(item_prices[item_id] for item_id in self.selected_items2)
        if food_order_amount == 0:
            print("You didn't selected any item.Please order again")
            self.order_online_page()
            return 

        delivery_charges = self.delivery_mode()

        if delivery_charges is None:
            print("No delivery available for this distance. Please select another mode.")
            self.proceed_ordering()
            return

        total_amount = food_order_amount+ delivery_charges
        
        
        print(f"Total amount to be paid: INR {total_amount:.2f} including delivery charges.")
        
        #date_of_delivery = input("Enter the date of delivery (DD/MM/YYYY): ")
        time_of_delivery = input("Enter the time of delivery (HH:MM): ")        
            
        #Offer payment options
        while True:
            print("\nPayment Options:")
            print("1. Proceed to checkout.")
            print("2. Cancel order")
            option = input("Enter your choice: ")

            if option == "1":
                print("Your Order is successfully placed. Your order id is :",order_id)
                order_id += 1
                order = {
                "total_amount": total_amount,
                "order_id": order_id,
                #"time_of visit": time_of_visit,
                "date":date_of_visit,
                "type":type
            }
                self.customer_transaction.append(order)
                break
            elif option == "2":
                print("Order cancelled.")
                break
            else:
                print("Invalid option. Please select a valid option.")

    def order_pickup_menu(self):
        order_id = 1111
        date_of_visit = input("Enter the date of order pickup (DD/MM/YYYY): ")
        time_of_visit = input("Enter the time of order pickup (HH:MM): ")
        type = "Pickup"
        # Display food menu
        print("\nFood Menu:")
        print("ID   Name           Price")
        for item_id, item_info in self.menu_items1.items():
            print(f"{item_id}    {item_info['name']}       AUD {item_info['price']}")
        
        while True:
            choice = input("Enter your choice (ID) or 7 to proceed to checkout: ")
            
            if choice == "7":
                print("Redirecting to checkout...")
                break
            elif choice.isdigit() and 1 <= int(choice) <= 6:
                self.selected_items3.append(choice)
                print(f"Item {choice} added to your order.")
            else:
                print("Invalid choice. Please enter a valid ID or 7 to proceed to checkout.")
        

        # Define dictionary for item prices
        item_prices = {
            "1": 60,
            "2": 40,
            "3": 60,
            "4": 100,
            "5": 80,
            "6": 120,
        }
        
        # Calculate total amount
        total_amount = sum(item_prices[item_id] for item_id in self.selected_items3) 
        if total_amount == 0:
            print("You didn't selected any item. Please order again.")
            self.order_online_page()
        else:    
            print(f"Total amount to be paid: INR {total_amount:.2f}")
            name_of_person_picking_up = input("Enter the name of person picking up: ")
        # Offer payment options
        while True:
            print("\nPayment Options:")
            print("1. Proceed to checkout.")
            print("2. Cancel order")
            option = input("Enter your choice: ")

            if option == "1":
                print("Thank you for your Order, Your Order has been confirmed.Your order id is :",order_id)
                order_id+=1
                order = {
                "total_amount": total_amount,
                "order_id": order_id,
                #"time_of visit": time_of_visit,
                "date":date_of_visit,
                "type":type
            }
                self.customer_transaction.append(order)
                
                break
            elif option == "2":
                print("Order cancelled.")
                break
            else:
                print("Invalid option. Please select a valid option.")

    def display_order_history(self):
        print("\nOrder History:")
        print("Option 1: All Dine in orders")
        print("Option 2: All Pickup Orders")
        print("Option 3: All Deliveries")
        print("Option 4: All Orders in Ascending order (based on amount)")
        print("Option 5: Total Amount Spent (All Type of Orders i.e., Dine in, Deliveries and Pickups)")
        print("Option 6: Go to Previous Menu")

        option = input("Enter your choice: ")
        if option == "1":
            print("\nAll Dine in orders:")
            print("Order ID    Date           Total Amount Paid   Type of Order")
            for order in self.customer_transaction:
                if order["type"] == "Dine in":
                    print(f"{order['order_id']}    {order['date']}     {order['total_amount']}                  {order['type']}")
        elif option == "2":
            print("\nAll Pickup Orders:")
            print("Order ID    Date           Total Amount Paid   Type of Order")
            for order in self.customer_transaction:
                if order["type"] == "Pickup":
                    print(f"{order['order_id']}    {order['date']}     {order['total_amount']}                  {order['type']}")
        elif option == "3":
            print("\nAll Deliveries:")
            print("Order ID    Date           Total Amount Paid   Type of Order")
            for order in self.customer_transaction:
                if order["type"] == "Delivery":
                    print(f"{order['order_id']}    {order['date']}     {order['total_amount']}                  {order['type']}")
        elif option == "4":
            print("\nAll Orders in Ascending order (based on amount):")
            sorted_orders = sorted(self.customer_transaction, key=lambda x: x["total_amount"])
            print("Order ID    Date           Total Amount Paid   Type of Order")
            for order in sorted_orders:
                print(f"{order['order_id']}    {order['date']}     {order['total_amount']}                  {order['type']}")
        elif option == "5":
            total_spent = sum(order["total_amount"] for order in self.customer_transaction)
            print(f"\nTotal Amount Spent (All Types of Orders): {total_spent}")
        elif option == "6":
            return
        else:
            print("Invalid option. Please select a valid option.") 

    def delivery_mode(self):
    
        if not self.customer.address:
            print("Delivery address is required for delivery mode.")
            input("Please enter your delivery address: ")
            #address = input("Please enter your delivery address: ")
        distance = float(input("Enter the distance from the restaurant in kilometers: "))
        #distance_from_restaurant = float(input("Enter the distance from the restaurant in kilometers: "))
        if distance > 12:
            print("Distance exceeds delivery limit. Please select another mode.")
            self.proceed_ordering()
        delivery_charge = self.calculate_delivery_charge(distance)
        if delivery_charge is None:
            print("No delivery available for this distance.")
            return None
        else:
            return delivery_charge

    def calculate_delivery_charge(self,distance):
        if distance > 0 and distance <= 4:
            return 3
        elif distance > 4 and distance <= 8:
            return 6
        elif distance > 8 and distance <= 12:
            return 10
        else:
            return None

      



def main():
    user=User()
    user.signUp()
    user.logIn()
    order=Order()
    order.home_page()

if __name__ == "__main__":
    main()