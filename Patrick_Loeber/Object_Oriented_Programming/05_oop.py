"""
Property
Pythonic way of getter and setter application
Only way to access private attribute is through
methods defined by getter setter decorator

Recap:
encapsulation
abstraction
public, private
_foo(), _x
getter/setter
getter -> @property
setter -> @x.setter
"""


class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    def code(self):
        self._num_bugs_solved += 1

    # Getter
    @property
    def salary(self):
        # Checks, constrains, calculation
        return self._salary

    # Setter
    @salary.setter
    def salary(self, value):
        self._salary = value

    ## Deleter
    # @salary.deleter
    # def salary(self):
    #    del self._salary


se = SoftwareEngineer()

se.salary = 6000
print(se.salary)
del se._salary
print(se.salary)
