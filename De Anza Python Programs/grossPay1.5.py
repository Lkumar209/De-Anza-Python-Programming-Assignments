''' 
Laxya Kumar
Prompting User for Hours and Rate and Calculating Gross Pay with Overtime
'''
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Calculating gross pay
if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * (rate * 1.5)

print("Pay:", pay)

'''
Result 1:
Hours: 30
Rate: 8
Pay: 240.0

Result 2:
Hours: 60
Rate: 25
Pay: 1750.0

'''