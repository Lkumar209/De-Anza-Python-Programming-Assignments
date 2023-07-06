'''
Laxya Kumar

Final Project

'''
from person import Staff, Student

import time
import datetime

class Order:
    def __init__(self):
        self._price_dict = {
            "De Anza Burger": 5.25,
            "Bacon Cheese": 5.75,
            "Mushroom Swiss": 5.95,
            "Western Burger": 5.95,
            "Don Cali Burger": 5.95
        }
        self._order_dict = {
            "De Anza Burger": 0,
            "Bacon Cheese": 0,
            "Mushroom Swiss": 0,
            "Western Burger": 0,
            "Don Cali Burger": 0
        }
        self._price_btax = 0
        self._price_atax = 0
        self._tax = 0.09

    def display_menu(self):
        print("\n----------- De Anza Food Court -----------")
        for i, (item, price) in enumerate(self._price_dict.items(), start=1):
            print(f"{i}. {item:15s} {price:8.2f}")
        print("6. Exit")

    def get_inputs(self):
        while True:
            choice = input("\nEnter the number of the item you want to order (1-6): ").strip()
            if choice == "6":
                break
            elif not choice.isdigit() or int(choice) < 1 or int(choice) > 6:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue

            item_index = int(choice) - 1
            quantity = input("Enter the quantity: ").strip()
            if not quantity.isdigit() or int(quantity) < 1:
                print("Invalid quantity. Please enter a positive whole number.")
                continue

            item = list(self._price_dict.keys())[item_index]
            self._order_dict[item] += int(quantity)
            print(f"{quantity}x {item} has been added to your order.")

    def calculate(self):
        self._price_btax = sum(
            self._order_dict[item] * self._price_dict[item] for item in self._price_dict
        )
        self._price_atax = self._price_btax + (self._price_btax * self._tax)

    def print_bill(self):
        print("\nYour bill:")
        for item, quantity in self._order_dict.items():
            price = self._price_dict[item]
            total = quantity * price
            print(f"{item:20s} Qty: {quantity:10d} Price: ${price:.2f} Total: ${total:.2f}")
        print("-" * 50)
        print("Price before tax:", self._price_btax)
        print("Price after tax:", self._price_atax)

    def save_to_file(self):
     

        timestamp = time.time()
        order_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H-%M-%S")
        filename = f"{order_timestamp}.txt"

        with open(filename, "w") as file:
            file.write("Order Summary:\n")
            for item, quantity in self._order_dict.items():
                price = self._price_dict[item]
                total = quantity * price
                file.write(f"{item:20s} Qty: {quantity:10d} Price: ${price:.2f} Total: ${total:.2f}\n")

            file.write(f"Order ID: {self.order_id}\n")
            file.write(f"Items: {', '.join(self.items)}\n")
            file.write(f"Total: ${self.total:.2f}\n")

        print("Order saved to file.")


    def place_order(self):
        self.display_menu()
        self.get_inputs()
        self.calculate()
        self.print_bill()
        self.save_to_file()

order = Order()
order.place_order()



'''
Output 1:



----------- De Anza Food Court -----------
1. De Anza Burger      5.25
2. Bacon Cheese        5.75
3. Mushroom Swiss      5.95
4. Western Burger      5.95
5. Don Cali Burger     5.95
6. Exit

Enter your choice (1-6): 1
Enter the item name: De Anza Burger
Enter the quantity: 2
2x De Anza Burger has been added to your order.

Enter your choice (1-6): 2

Current order:
De Anza Burger     Qty:          2

Enter your choice (1-6): 3
Enter the item name to update: De Anza Burger
Enter the new quantity: 3
Quantity for De Anza Burger has been updated to 3.

Enter your choice (1-6): 2

Current order:
De Anza Burger     Qty:          3

Enter your choice (1-6): 4
Enter the item name to delete: De Anza Burger
De Anza Burger has been removed from the order.

Enter your choice (1-6): 2

Current order:

Enter your choice (1-6): 5

Your bill:
--------------------------------------------------
Price before tax: 0
Price after tax: 0.00
Order saved to file.




Output 2:
----------- De Anza Food Court -----------
1. De Anza Burger      5.25
2. Bacon Cheese        5.75
3. Mushroom Swiss      5.95
4. Western Burger      5.95
5. Don Cali Burger     5.95
6. Exit

Enter your choice (1-6): 1
Enter the item name: De Anza Burger
Enter the quantity: 2
2x De Anza Burger has been added to your order.

Enter your choice (1-6): 2

Current order:
De Anza Burger     Qty:          2

Enter your choice (1-6): 1
Enter the item name: Bacon Cheese
Enter the quantity: 1
1x Bacon Cheese has been added to your order.

Enter your choice (1-6): 2

Current order:
De Anza Burger     Qty:          2
Bacon Cheese       Qty:          1

Enter your choice (1-6): 5

Your bill:
De Anza Burger            Qty:          2 Price: $5.25 Total: $10.50
Bacon Cheese              Qty:          1 Price: $5.75 Total: $5.75
--------------------------------------------------
Price before tax: 16.50
Price after tax: 17.97
Order saved to file.






'''