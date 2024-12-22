"""
Title: Object Oriented Programming (OOP) In Python - Beginner Crash Course
Source: Patrick Loeber YouTube Channel
Author (Original Tutorial): Patrick Loeber
URL: https://www.youtube.com/watch?v=-pEs-Bss8Wc
Date of Implementation: 2024-12-22
Description:
    In this Beginner Object Oriented Programming (OOP) Tutorial
    I will be covering all the fundamentals about classes,
    objects, and inheritance in Python. This tutorial is
    designed for beginners and will give you a strong
    foundation in object oriented principles.
"""


# Create class
class SoftwareEngineer:

    # Class attribute
    alias = "Employee"

    def __init__(self, name, age, level, salary):
        # Instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # Instance methods
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    # special double under methods dunder
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # Class function
    # no self, only callable by class
    # in practice it will be decorated (static_method)
    # no tied to specific instance, therefore instance attributes
    # not excessable (e.g. self.age)
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# Create instance
se1 = SoftwareEngineer("Max", 21, "Junior", 4500)
se2 = SoftwareEngineer("Janna", 24, "Senior", 6700)
se3 = SoftwareEngineer("Janna", 24, "Senior", 6700)
print(se1.name, se1.age)
se1.code()
se1.code_in_language("Python")
print(se1)
print(se2)
print(se2 == se3)
SoftwareEngineer.entry_salary(26)
print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))
