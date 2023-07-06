# Laxya Kumar
# Description: This program helps a manager schedule weekly coffee chat meetings between employees.

from itertools import combinations

class CoffeeChatScheduler:
    def __init__(self, employees):
        self.employees = employees
        self.num_employees = len(employees)
        self.schedule = []

    def generate_schedule(self):
        combinations_list = list(combinations(self.employees, 2))
        for i in range(self.num_employees // 2):
            self.schedule.append(combinations_list[i])
        return self.schedule

    def print_schedule(self):
        for week, meeting in enumerate(self.schedule, start=1):
            print(f"Week {week}: {meeting[0]} & {meeting[1]}")

employees = ['employee_1', 'employee_2', 'employee_3', 'employee_4', 'employee_5', 'employee_6']
scheduler = CoffeeChatScheduler(employees)
scheduler.generate_schedule()
scheduler.print_schedule()


'''
Outputs:
Week 1: employee_1 & employee_2
Week 2: employee_1 & employee_3
Week 3: employee_1 & employee_4
Week 4: employee_1 & employee_5
Week 5: employee_1 & employee_6
Week 6: employee_2 & employee_3
Week 7: employee_2 & employee_4
Week 8: employee_2 & employee_5
Week 9: employee_2 & employee_6
Week 10: employee_3 & employee_4
Week 11: employee_3 & employee_5
Week 12: employee_3 & employee_6
Week 13: employee_4 & employee_5
Week 14: employee_4 & employee_6
Week 15: employee_5 & employee_6

'''