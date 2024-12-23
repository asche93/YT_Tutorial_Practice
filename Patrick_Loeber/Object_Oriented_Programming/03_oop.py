"""
Title: Object Oriented Programming (OOP) In Python - Beginner Crash Course
Source: Patrick Loeber YouTube Channel
Author (Original Tutorial): Patrick Loeber
URL: https://www.youtube.com/watch?v=-pEs-Bss8Wc
Date of Implementation: 2024-12-22
Description:
    - Inheritance: ChildClass(BaseClass)
    - inherit, extend, overwrite
    - super().__init__()
    - Polymorphism
"""


# Parent class
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


# Child class
# Inharits, extend, override
class SoftwareEngineer(Employee):

    # Call initalizer of parent class
    # Overwritten, always call super init in here
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        # Extend functionality
        self.level = level

    # Overwritten parent method
    def work(self):
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debugging...")


class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")


se = SoftwareEngineer("Max", 23, 7000, "Junior")
# se.work()

d = Designer("Philipp", 28, 6000)
# d.work()

"""
Polymorphism (many shapes)
- write code that works on the super-class but also 
with any subtype-class aswell
- use a class exactly as its parent, but still each child class keeps
its own methods as they are
"""


# Collection of employees, just treat them as employees
employees = [
    SoftwareEngineer("Max", 23, 7000, "Junior"),
    SoftwareEngineer("Lisa", 21, 7500, "Senior"),
    Designer("Philipp", 28, 6000),
]


def motivate_employees(employees):
    for employee in employees:
        # Will work on all employees
        # Get specific implementation of the child class
        # Capable of taking different shapes
        employee.work()


motivate_employees(employees)
