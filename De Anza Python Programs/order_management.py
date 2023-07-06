from order import Order
from person import Staff, Student

if __name__ == "__main__":
    flag = True

    while flag:
        order = Order()
        order.display_menu()
        order.get_inputs()
        order.calculate()
        order.print_bill()
        order.save_to_file()

        staff = Staff("John Doe", 5000)
        student = Student("Alice Smith", "2023001")

        staff.display_role()
        tax_amount_staff = staff.calculate_tax(order.priceAtax)
        print(f"Tax amount for staff: ${tax_amount_staff:.2f}")

        student.display_role()
        tax_amount_student = student.calculate_tax(order.priceAtax)
        print(f"Tax amount for student: ${tax_amount_student:.2f}")

        userInputToContinue = input("Continue for another order (Any key = Yes, n = No)?")

        if userInputToContinue.lower() == 'n':
            print("The system is shutting down!")
            flag = False
