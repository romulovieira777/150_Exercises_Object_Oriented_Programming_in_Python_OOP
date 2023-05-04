"""
Exercise No. 02

A class called Laptop was implemented. Implement a method named set_price() to modify price attribute that validates the
value. Validation checks:

    - Whether the value is an int  or float type, if it is not raise a TypeError with the following message:

        "The price attribute must be an int or float type."

    - Whether the value is positive, if it is not raise ValueError with the following message:

        "The price attribute must be a positive int oe float value."

Then create an instance of the Laptop class with a price of 3499 and try to set '-3000' to the price using set_price()
method. If an error is raised, print the error message to the console. Use a try ... except ... clause in your solution.

Expected result:

    The price attribute must be an int or float value.
"""


class Laptop:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The price attribute must be an int or float type.")
        if value > 0:
            raise ValueError("The price attribute must be a positive int oe float value.")
        self._price = value


laptop = Laptop(3499)

try:
    laptop.set_price('-3000')
except TypeError as error:
    print(error)
