# Laxya Kumar
''' Description: The program validates user inputs for company name, rate, and hours, 
calculates pay with overtime if applicable, and prints the pay stub, all using modularized functions.
'''




COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]

def getInputs():
    while True:
        company_name = input("Enter your company name: ")
        if company_name in COMPANYLIST:
            break
        print("Invalid company name. Please try again.")

    while True:
        try:
            rate = float(input("Enter the rate: "))
            if rate <= 0:
                raise ValueError("Rate must be a positive value.")
            break
        except ValueError:
            print("Invalid rate. Please enter a numeric and positive value.")

    while True:
        try:
            hours = float(input("Enter the hours: "))
            if hours <= 0:
                raise ValueError("Hours must be a positive value.")
            break
        except ValueError:
            print("Invalid hours. Please enter a numeric and positive value.")

    return {
        "company_name": company_name,
        "rate": rate,
        "hours": hours
    }

def computePay(theDict):
    rate = theDict["rate"]
    hours = theDict["hours"]

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate

    theDict["total_pay"] = total_pay
    return theDict

def printPay(theDict):
    print("Pay Stub:")
    print("Company Name:", theDict["company_name"])
    print("Rate:", theDict["rate"])
    print("Hours:", theDict["hours"])
    print("Total Pay:", theDict["total_pay"])


def payProcess():
  
    theDict = getInputs()
    theDict = computePay(theDict)
    printPay(theDict)

if __name__ == '__main__':
    payProcess()


'''
Result 1:

Enter your company name: Google
Enter the rate: 10
Enter the hours: 45
Pay Stub:
Company Name: Google
Rate: 10.0
Hours: 45.0
Total Pay: 475.0


Result 2:

Enter your company name: Microsoft
Invalid company name. Please try again.
Enter your company name: Facebook
Enter the rate: -5
Invalid rate. Please enter a numeric and positive value.
Enter the rate: 15
Enter the hours: abc
Invalid hours. Please enter a numeric and positive value.
Enter the hours: 40
Pay
'''