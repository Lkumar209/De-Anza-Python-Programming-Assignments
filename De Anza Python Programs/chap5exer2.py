'''
Laxya Kumar
Computation program using 3 different fuctions
'''

def get_input():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    return hours, rate

def compute_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

def print_output(pay):
    print("Pay:", pay)

def main():
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay)

main()
