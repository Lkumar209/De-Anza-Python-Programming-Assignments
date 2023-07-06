class Person:
    def __init__(self, name):
        self.name = name

    def display_role(self):
        pass

    def calculate_tax(self, amount):
        pass


class Staff(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display_role(self):
        print(f"Staff: {self.name}")

    def calculate_tax(self, amount):
        tax_rate = 0.2
        tax_amount = amount * tax_rate
        return tax_amount


class Student(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def display_role(self):
        print(f"Student: {self.name}")

    def calculate_tax(self, amount):
        tax_rate = 0.1
        tax_amount = amount * tax_rate
        return tax_amount
