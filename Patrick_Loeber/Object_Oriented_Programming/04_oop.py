class SoftwareEngineer:

    def __init__(self, name, age):
        # Public attribute
        self.name = name
        self.age = age
        # _ x Protected attribute, accessable, often used
        # __ x Private attribute, not accessable
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1

    # Getter
    # Should be only way to access protected attributes
    def get_salary(self):
        return self._salary

    # Setter
    # Should be only way to access protected attributes
    def set_salary(self, base_value):
        # Check value, enforece constraints
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("Max", 25)

for i in range(70):
    se.code()

# Apply abstraction principle
# no knowledge about the internal implementation of set_salary is needed
se.set_salary(6000)
print(se.get_salary())


"""
Abstraction
Natural extention of encapsulation
Each object should only expose a high level mechanism
- internal implementation details: only relevent for the other objects
"""
