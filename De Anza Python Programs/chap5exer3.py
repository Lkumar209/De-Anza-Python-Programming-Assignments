'''
Laxya Kumar
Computation program using 3 different fuctions
'''

import random

def get_input():
    while True:
        try:
            company_name = input("Enter your company name: ").strip()
            hours = float(input("Enter the hours: ").strip())
            rate = float(input("Enter the rate: ").strip())
            
            if hours <= 0 or rate <= 0:
                raise ValueError("Hours and rate must be positive numbers.")
            
            return company_name, hours, rate
        except ValueError as e:
            print("Invalid input:", e)

def compute_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

def print_output(company_name, hours, rate, pay):
    document_number = random.randint(1000, 2000)
    print("Company:", company_name)
    print("Hours:", round(hours, 2))
    print("Rate:", round(rate, 2))
    print("**********************************************")
    print("Your document number is:", document_number)
    print("Your", company_name, "gross pay is", round(pay, 2), "dollars.")

def main():
    company_name, hours, rate = get_input()
    pay = compute_pay(hours, rate)
    print_output(company_name, hours, rate, pay)

main()
