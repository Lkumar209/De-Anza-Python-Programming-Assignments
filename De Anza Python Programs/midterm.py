'''
Laxya Kumar
Midterm program: This program implements a menu-driven system for the De Anza College Food Court,
allowing users to place orders, calculate the bill, and apply tax based on their customer type.
'''
def display_menu():
    """
    Displays the menu options for the De Anza College Food Court.
    """
    print("Welcome to De Anza College Food Court!")
    print("Menu:")
    print("1. De Anza Burger: $5.25")
    print("2. Bacon Cheese: $5.75")
    print("3. Mushroom Swiss: $5.95")
    print("4. Western Burger: $5.95")
    print("5. Don Cali Burger: $5.95")
    print("6. Exit")

def calculate_total_price(quantity, price):
    """
    Calculates the total price for a given quantity and price.

    Args:
        quantity (int): The quantity of items.
        price (float): The price of a single item.

    Returns:
        float: The total price.
    """
    return quantity * price

def calculate_tax(total_price, is_staff):
    """
    Calculates the tax amount based on the total price and customer type.

    Args:
        total_price (float): The total price before tax.
        is_student (bool): True if the customer is a student, False if staff.

    Returns:
        float: The tax amount.
    """
    if is_staff:
        return total_price * 0.09
    else:
        return 0

def display_bill(items, quantities, prices, total_before_tax, tax_amount, total_price):
    """
    Displays the bill summary.

    Args:
        items (list): List of food items.
        quantities (list): List of quantities for each item.
        prices (list): List of prices for each item.
        total_before_tax (float): The total price before tax.
        tax_amount (float): The tax amount.
        total_price (float): The total price after tax.
    """
    print("\nOrder Summary:")
    for i in range(len(items)):
        print(f"{quantities[i]}x {items[i]}: ${prices[i]:.2f}")
    print(f"\nTotal before tax: ${total_before_tax:.2f}")
    print(f"Tax amount: ${tax_amount:.2f}")
    print(f"Total price after tax: ${total_price:.2f}")

def main():
    """
    Main function to run the De Anza College Food Court program.
    """ 
    items = ["De Anza Burger", "Bacon Cheese", "Mushroom Swiss", "Western Burger", "Don Cali Burger"]
    prices = [5.25, 5.75, 5.95, 5.95, 5.95]
    quantities = [0] * len(items)

    display_menu()

    while True:
        choice = input("\nEnter the number of the item you want to order (1-6): ").strip()

        if choice == '6':
            print("Thank you, hope to see you again!")
            if sum(quantities) > 0:
                customer_type = input("Are you a student or a staff? Enter 'student' or 'staff': ").strip().lower()
                total_before_tax = sum(calculate_total_price(quantities[i], prices[i]) for i in range(len(items)))
                tax_amount = calculate_tax(total_before_tax, customer_type == 'staff')
                total_price = total_before_tax + tax_amount
                display_bill(items, quantities, prices, total_before_tax, tax_amount, total_price)
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 5:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        item_index = int(choice) - 1
        quantity = input("Enter the quantity: ").strip()

        if not quantity.isdigit() or int(quantity) < 1:
            print("Invalid quantity. Please enter a positive whole number.")
            continue

        quantities[item_index] += int(quantity)
        print(f"{quantity}x {items[item_index]} has been added to your order.")

if __name__ == "__main__":
    main()



'''
Result 1:

Welcome to De Anza College Food Court!
Menu:
1. De Anza Burger: $5.25
2. Bacon Cheese: $5.75
3. Mushroom Swiss: $5.95
4. Western Burger: $5.95
5. Don Cali Burger: $5.95
6. Exit

Enter the number of the item you want to order (1-6): 2
Enter the quantity: 3
3x Bacon Cheese has been added to your order.

Enter the number of the item you want to order (1-6): 4
Enter the quantity: 2
2x Western Burger has been added to your order.

Enter the number of the item you want to order (1-6): 6
Thank you, hope to see you again!
Are you a student or a staff? Enter 'student' or 'staff': student

Order Summary:
0x De Anza Burger: $5.25
3x Bacon Cheese: $5.75
0x Mushroom Swiss: $5.95
2x Western Burger: $5.95
0x Don Cali Burger: $5.95

Total before tax: $29.15
Tax amount: $0.00
Total price after tax: $29.15


Result 2:

Welcome to De Anza College Food Court!
Menu:
1. De Anza Burger: $5.25
2. Bacon Cheese: $5.75
3. Mushroom Swiss: $5.95
4. Western Burger: $5.95
5. Don Cali Burger: $5.95
6. Exit

Enter the number of the item you want to order (1-6): 3
Enter the quantity: 2
2x Mushroom Swiss has been added to your order.

Enter the number of the item you want to order (1-6): 5
Enter the quantity: 3
3x Don Cali Burger has been added to your order.

Enter the number of the item you want to order (1-6): 6
Thank you, hope to see you again!
Are you a student or a staff? Enter 'student' or 'staff': staff

Order Summary:
0x De Anza Burger: $5.25
0x Bacon Cheese: $5.75
2x Mushroom Swiss: $5.95
0x Western Burger: $5.95
3x Don Cali Burger: $5.95

Total before tax: $29.75
Tax amount: $2.68
Total price after tax: $32.43


Result 3:

Welcome to De Anza College Food Court!
Menu:
1. De Anza Burger: $5.25
2. Bacon Cheese: $5.75
3. Mushroom Swiss: $5.95
4. Western Burger: $5.95
5. Don Cali Burger: $5.95
6. Exit

Enter the number of the item you want to order (1-6): 4983357
Invalid choice. Please enter a number between 1 and 6.

Enter the number of the item you want to order (1-6): 6
Thank you, hope to see you again!

'''
